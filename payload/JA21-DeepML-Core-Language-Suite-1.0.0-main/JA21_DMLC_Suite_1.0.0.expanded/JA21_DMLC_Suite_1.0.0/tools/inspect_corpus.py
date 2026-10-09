#!/usr/bin/env python3
"""Offline inspector for the normalized JA21 DeepML Core corpus."""
from __future__ import annotations
import argparse, gzip, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / 'corpus' / 'technical' / 'deepml_core_technical_corpus_10000.jsonl.gz'


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--corpus', type=Path, default=DEFAULT)
    parser.add_argument('--topic')
    parser.add_argument('--class-name', choices=['positive', 'negative', 'certification'])
    parser.add_argument('--tier', type=int, choices=range(1, 7))
    parser.add_argument('--id')
    parser.add_argument('--limit', type=int, default=20)
    args = parser.parse_args()
    shown = 0
    with gzip.open(args.corpus, 'rt', encoding='utf-8') as f:
        for line in f:
            rec = json.loads(line)
            ident, ped = rec['identity'], rec['pedagogy']
            if args.id and ident['id'] != args.id: continue
            if args.topic and ped['topic'] != args.topic: continue
            if args.class_name and ped['class'] != args.class_name: continue
            if args.tier and ped['tier'] != args.tier: continue
            print(json.dumps(rec, indent=2, ensure_ascii=False))
            shown += 1
            if shown >= args.limit: break
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
