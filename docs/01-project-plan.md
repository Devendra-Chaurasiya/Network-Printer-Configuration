# 01 - Project Plan

## Objective
Configure one network printer with a static IP address and make it accessible from at least two client systems on the same LAN.

## Deliverables
- Documented network topology
- Documented IP addressing plan
- Printer configured on network
- Client-side setup completed
- Test evidence and checklist

## Requirements
- Router with LAN connectivity
- Switch (optional if router has enough LAN ports)
- Network printer (Ethernet or Wi-Fi)
- Two client machines (Windows/Linux/macOS)
- Correct printer drivers

## Assumptions
- LAN subnet: 192.168.10.0/24
- Default gateway: 192.168.10.1
- Printer static IP: 192.168.10.50
- DHCP pool excludes 192.168.10.50

## Success Criteria
1. Printer responds to ping from all required clients.
2. Printer can be added using IP address on each client.
3. Test print succeeds from each client.
4. All configuration details are documented.

## Risk Register
| Risk | Impact | Mitigation |
|------|--------|------------|
| IP conflict on printer IP | High | Reserve IP and keep printer outside DHCP pool |
| Incorrect driver | High | Download exact model driver from vendor |
| Firewall blocks print traffic | Medium | Allow printer ports (9100/IPP/LPD as needed) |
| Unstable network link | Medium | Check cable, switch port, and Wi-Fi signal |
