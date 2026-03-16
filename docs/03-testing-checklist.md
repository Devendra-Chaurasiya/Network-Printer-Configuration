# 03 - Testing Checklist

Use this checklist for both hardware and no-hardware simulation modes.
If you are using simulation mode, write `Simulated` in the `Actual Result` column and briefly describe expected behavior.

## Test Matrix
| Test ID | Test Description | Expected Result | Actual Result | Status |
|---------|------------------|-----------------|---------------|--------|
| T1 | Printer powered and connected to LAN | Link is up | | |
| T2 | Ping from PC-01 to printer IP | Ping replies received | | |
| T3 | Ping from PC-02 to printer IP | Ping replies received | | |
| T4 | Add printer on PC-01 by TCP/IP | Printer added successfully | | |
| T5 | Add printer on PC-02 by TCP/IP | Printer added successfully | | |
| T6 | Test print from PC-01 | Print job completed | | |
| T7 | Test print from PC-02 | Print job completed | | |
| T8 | Printer survives restart with same IP | Same static IP retained | | |

## Status Legend
- Pass: requirement achieved
- Fail: requirement not achieved
- Simulated: validated logically/documented without physical hardware

## Acceptance Criteria
- All mandatory tests (T1 to T7) pass.
- No unresolved connectivity errors.
- Printer is available to required users.

For simulation mode:
- All mandatory tests should be marked `Pass` or `Simulated` with clear remarks.
- The limitation (no physical printer) must be explicitly documented.

## Evidence Checklist
- [ ] Screenshot of printer network settings (or simulated equivalent)
- [ ] Ping output from each client (or simulated equivalent)
- [ ] Screenshot of printer installation on each client (or documented simulation step)
- [ ] Test print confirmation page/photo (or simulation statement)
- [ ] Final report includes hardware/simulation declaration
