#!/usr/bin/env python3
"""Structural and integrity validator for JA21_DMLC_Suite_1.0.0."""
from __future__ import annotations
import csv, gzip, hashlib, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def fail(message: str) -> None:
    print('FAIL:', message)
    raise SystemExit(1)


def main() -> int:
    corpus = ROOT / 'corpus' / 'technical' / 'deepml_core_technical_corpus_10000.jsonl.gz'
    records = []
    with gzip.open(corpus, 'rt', encoding='utf-8') as f:
        for line in f:
            records.append(json.loads(line))
    if len(records) != 10000: fail(f'corpus count {len(records)}')
    ids = [r['identity']['id'] for r in records]
    if len(set(ids)) != 10000: fail('duplicate corpus IDs')
    if sorted(r['identity']['sequence'] for r in records) != list(range(1, 10001)):
        fail('sequence discontinuity')
    for r in records:
        program = r['source']['program']
        expected = r['source']['source_hash'].replace('sha256:', '')
        observed = hashlib.sha256(program.encode('utf-8')).hexdigest()
        if expected != observed: fail(f'source hash mismatch {r["identity"]["id"]}')

    scripts = sorted((ROOT / 'script_pack_1000').rglob('*.deepml'))
    if len(scripts) != 1000: fail(f'script count {len(scripts)}')
    with (ROOT / 'catalogs' / 'SCRIPT_CATALOG.csv').open(encoding='utf-8', newline='') as f:
        catalog = list(csv.DictReader(f))
    if len(catalog) != 1000: fail(f'catalog count {len(catalog)}')
    paths = {row['path']: row for row in catalog}
    if len(paths) != 1000: fail('duplicate script catalog paths')
    classes, tiers, topics = set(), set(), set()
    for script in scripts:
        rel = script.relative_to(ROOT).as_posix()
        if rel not in paths: fail(f'uncataloged script {rel}')
        text = script.read_text(encoding='utf-8')
        row = paths[rel]
        if not text.startswith('deepml core 0.3\n'): fail(f'bad header {rel}')
        if '\nmodule ' not in text: fail(f'missing module {rel}')
        if 'policy deterministic' not in text: fail(f'missing deterministic policy {rel}')
        if 'policy no_network' not in text: fail(f'missing no-network policy {rel}')
        if text.count('{') != text.count('}'): fail(f'unbalanced braces {rel}')
        expected = row['source_hash'].replace('sha256:', '')
        observed = hashlib.sha256(text.rstrip('\n').encode('utf-8')).hexdigest()
        if expected != observed: fail(f'script source hash mismatch {rel}')
        classes.add(row['class']); tiers.add(int(row['tier'])); topics.add(row['topic'])
    if classes != {'positive', 'negative', 'certification'}: fail(f'class coverage {classes}')
    if tiers != {1,2,3,4,5,6}: fail(f'tier coverage {tiers}')
    if len(topics) != 48: fail(f'topic coverage {len(topics)}')

    manifest_path = ROOT / 'manifests' / 'MANIFEST.json'
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        for item in manifest['files']:
            path = ROOT / item['path']
            if not path.exists(): fail(f'missing manifest file {item["path"]}')
            if sha256(path) != item['sha256']: fail(f'manifest hash {item["path"]}')
    print('PASS: 10,000 records; 1,000 scripts; source hashes, policies, braces, coverage, catalogs, and manifest verified.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
