# CSV user provisioning plans

Validate a user CSV before it becomes a directory change. This Python tool produces a JSON plan; it does **not** create accounts or connect to AD/Entra ID.

## Input contract

The exact header is:

```csv
username,given_name,surname,department
lab.user01,Alex,Example,Lab
```

Usernames are normalized to lowercase. The validator rejects duplicate usernames, missing/extra columns, malformed CSV quoting, empty fields, control characters, oversized fields, and formula-like prefixes. The synthetic input is in [examples/users.csv](examples/users.csv).

## Run

Python 3.10+; no third-party dependencies. From the repository root:

```bash
python scripts/csv_plan.py examples/users.csv
python -m unittest discover -s tests -v
```

A valid input produces `mode: plan-only` and `enabled: false` for each proposed account. An invalid input exits with code 2 and a generic error; raw input rows and local file paths are not printed. [Synthetic output](examples/plan.synthetic.json).

## Why stop at a plan?

Input validation can be tested without granting directory access. A future provisioning adapter would still need server-side uniqueness checks, approved OU/domain targeting, authorization, per-account results, and recovery handling. A valid CSV alone is not approval to create an account.

## What was checked

[Validation record](docs/validation.md) includes deterministic fixtures and an actual CLI run using the synthetic CSV. No live users or employee exports were used. The current tool does not check whether an account already exists in a directory.

[Evidence index](evidence/README.md) · [MIT license](LICENSE) · [Security](SECURITY.md)
