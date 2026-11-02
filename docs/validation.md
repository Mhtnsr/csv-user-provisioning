# Local validation record

Date: November 1, 2026 (America/New_York).

Environment: Windows authoring workspace; PowerShell 7 for PowerShell checks and Python 3.12 for Python checks. These are local test results, not a CI result or a completed production incident.

## Scope

The suite uses in-memory synthetic CSV fixtures, including malformed quoting and rejected-input cases. It does not connect to a directory.

## Observed output

```text
test_rejected_inputs (test_csv_plan.CsvPlanTests.test_rejected_inputs) ... ok
test_unclosed_quote_rejected (test_csv_plan.CsvPlanTests.test_unclosed_quote_rejected) ... ok
test_valid_and_normalized (test_csv_plan.CsvPlanTests.test_valid_and_normalized) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

## Reproduce

Run the test command in this repository's README. A passing suite establishes only the cases represented in the tests; add actual lab evidence before claiming end-to-end deployment or recovery.
