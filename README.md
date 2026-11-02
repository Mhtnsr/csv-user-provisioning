# Csv User Provisioning

Validate synthetic user CSVs and produce reviewable provisioning plans before directory changes.

**Owner:** [Mahamat Nassour Ahmat](https://github.com/Mhtnsr) · IT Support Specialist → Systems Administrator

## Problem

Bulk input errors propagate into identity changes.

## Solution

Validate an exact synthetic CSV schema, normalize usernames, reject duplicates/formula-like/control-character fields, and emit a JSON plan with disabled accounts. The plan is a review artifact; it does not create users.

## Usage

Run from the repository root. Use an isolated, authorized environment and inspect source before execution.

```bash
python scripts/csv_plan.py examples/users.csv
python -m unittest discover -s tests -v
```

## Validation and limits

Python standard library only. Fixture-based validation tests passed. Live provisioning is deliberately not implemented; an approved adapter with uniqueness checks, domain validation, error handling, and rollback would be required.

## Screenshots and evidence

[Evidence checklist](evidence/README.md). Placeholder: add a sanitized capture of the actual execution or lab result here after validation. No screenshots or outcomes are fabricated.

<!-- Example after creating the file: ![Sanitized lab result](evidence/lab-result.png) -->

## Repository map

Source belongs in `scripts/`, reproducible checks in `tests/`, synthetic inputs in `examples/`, design notes in `docs/`, reusable records in `templates/`, and sanitized proof in `evidence/`. Only directories relevant to this project are created.

## Next steps

- Capture a reproducible lab run with expected versus observed behavior.
- Document failure cases and recovery or escalation.
- Update validation status only after recording actual results.

## Security

See [SECURITY.md](SECURITY.md). No company data, credentials, internal topology, or live ticket details belong here.

## License

[MIT](LICENSE). A personal learning project; not affiliated with or endorsed by USEReady, Microsoft, CompTIA, or other vendors.
