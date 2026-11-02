"""Validate a synthetic CSV and emit a disabled-account plan; never writes to AD."""
import argparse
import csv
import json
import re
import sys

FIELDS = ['username', 'given_name', 'surname', 'department']

def build_plan(stream):
    reader = csv.DictReader(stream)
    if reader.fieldnames != FIELDS:
        raise ValueError('Expected exact header: ' + ','.join(FIELDS))
    seen, users = set(), []
    for row_number, row in enumerate(reader, 2):
        if None in row or any(row.get(k) is None for k in FIELDS):
            raise ValueError(f'Row {row_number}: incorrect column count')
        row = {k: v.strip() for k, v in row.items()}
        if any(not v or len(v) > 80 or any(ord(c) < 32 for c in v) or v[0] in '=+-@' for v in row.values()):
            raise ValueError(f'Row {row_number}: invalid field')
        username = row['username'].lower()
        if not re.fullmatch(r'[a-z][a-z0-9._-]{0,19}', username):
            raise ValueError(f'Row {row_number}: invalid username')
        if username in seen:
            raise ValueError(f'Row {row_number}: duplicate username')
        seen.add(username)
        users.append(dict(row, username=username, enabled=False))
    if not users:
        raise ValueError('CSV contains no user rows')
    return {'schema_version': 1, 'mode': 'plan-only', 'users': users}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv_path')
    args = parser.parse_args()
    try:
        with open(args.csv_path, encoding='utf-8-sig', newline='') as source:
            plan = build_plan(source)
        print(json.dumps(plan, indent=2, ensure_ascii=False))
        return 0
    except (OSError, UnicodeError, ValueError, csv.Error) as exc:
        # Do not print file paths, row contents, or exception data that may be private.
        print('Input rejected; check file access, encoding, header, and field validation.', file=sys.stderr)
        return 2

if __name__ == '__main__':
    raise SystemExit(main())
