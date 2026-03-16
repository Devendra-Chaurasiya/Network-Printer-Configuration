# 03 - Testing Checklist

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

## Acceptance Criteria
- All mandatory tests (T1 to T7) pass.
- No unresolved connectivity errors.
- Printer is available to required users.

## Evidence Checklist
- [ ] Screenshot of printer network settings
- [ ] Ping output from each client
- [ ] Screenshot of printer installation on each client
- [ ] Test print confirmation page/photo
