# Network Printer Configuration

Submission target: 17 March 2026

## Project Description
This project configures a network printer so that multiple users on the same LAN can print reliably using TCP/IP. It demonstrates practical knowledge of:

- Network device integration
- IPv4 addressing and subnet planning
- Static IP assignment for infrastructure devices
- Client-side printer setup on Windows and Linux
- Validation and troubleshooting

## Learning Outcomes
After completing this project, you will be able to:

1. Design a small office/home network printer topology.
2. Assign and document valid IPv4 addresses.
3. Configure a printer with static network settings.
4. Add the printer on different operating systems.
5. Diagnose common connectivity and print queue issues.

## Scope
Included:

- One router/switch network
- One network-capable printer
- Two or more client devices
- IP plan, implementation steps, and test evidence template

Not included:

- Enterprise print servers (Active Directory/GPO)
- VLAN segmentation and advanced firewalling

## Proposed Topology
```text
				 Internet
					|
				[Router]
					|
				 [Switch]
		  _________|___________
		 |         |           |
	 [PC-01]   [PC-02]   [Printer]
```

## IP Addressing Plan (Example)
| Device   | Role            | IP Address     | Subnet Mask     | Gateway       | DNS         |
|----------|-----------------|----------------|-----------------|---------------|-------------|
| Router   | Default Gateway | 192.168.10.1   | 255.255.255.0   | N/A           | N/A         |
| Printer  | Static Device   | 192.168.10.50  | 255.255.255.0   | 192.168.10.1  | 8.8.8.8     |
| PC-01    | Client          | 192.168.10.101 | 255.255.255.0   | 192.168.10.1  | 8.8.8.8     |
| PC-02    | Client          | 192.168.10.102 | 255.255.255.0   | 192.168.10.1  | 8.8.8.8     |

## Quick Implementation Steps
1. Connect printer to switch/router LAN port.
2. Assign a static IP to printer (outside DHCP dynamic range).
3. Verify printer is reachable with ping from client machine.
4. Install printer driver on each client.
5. Add printer by TCP/IP address.
6. Print test page from each client.

Detailed instructions are in the docs folder.

## Repository Structure
```text
.
|-- README.md
|-- docs
|   |-- 01-project-plan.md
|   |-- 02-implementation-steps.md
|   |-- 03-testing-checklist.md
|   `-- 04-troubleshooting.md
`-- configs
	|-- example-ip-plan.csv
	`-- example-printer-network-settings.txt
```

## Execution Workflow
1. Review project plan: `docs/01-project-plan.md`
2. Perform setup: `docs/02-implementation-steps.md`
3. Validate setup: `docs/03-testing-checklist.md`
4. Resolve issues (if any): `docs/04-troubleshooting.md`

## Evidence to Collect for Submission
- Screenshots of printer network settings page
- Ping success from at least two clients
- Printer installed on clients
- Successful test print page
- Completed testing checklist

## GitHub Upload Steps
Use these commands in terminal from project root:

```bash
git init
git add .
git commit -m "Complete Network Printer Configuration project"
git branch -M main
git remote add origin https://github.com/<your-username>/Network-Printer-Configuration.git
git push -u origin main
```

If the remote repository already exists and has content, run:

```bash
git pull --rebase origin main
git push -u origin main
```

## Final Submission Checklist
- [ ] All docs completed and reviewed
- [ ] IP plan matches real network
- [ ] Printer reachable from all required clients
- [ ] Test print succeeded on all required clients
- [ ] Project pushed to GitHub before 17 March 2026