# Evidence Index

This folder contains completed simulation-mode evidence for the Network Printer Configuration project.

## Generated Evidence Files
- `completed-test-results.md`: filled test matrix with simulation outcomes
- `ip-plan-validation-report.txt`: automated IP plan validation (PASS)
- `ping-pc01-to-printer.txt`: simulated ping output from PC-01
- `ping-pc02-to-printer.txt`: simulated ping output from PC-02
- `simulated-installation-log.txt`: simulated Windows/Linux printer setup log
- `simulated-ping-results.txt`: summary ping evidence
- `simulated-test-print-log.txt`: simulated print job completion log
- `topology-diagram.mmd`: topology diagram in Mermaid format

## Notes
- All artifacts are explicitly simulation-based because physical hardware is unavailable.
- To regenerate evidence, run:

```bash
python3 scripts/generate_simulated_evidence.py
python3 scripts/validate_ip_plan.py
```
