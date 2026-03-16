# Network Printer Configuration

## Implementation Mode
This repository is designed to be completed in either mode:

1. Real hardware mode (if printer is available)
2. Simulation/documentation mode (if printer is not available)

If you do not have a physical printer, use simulation mode and clearly mention this in your project report.

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
- One network-capable printer (real or simulated)
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

If no physical printer is available, use the simulation workflow in `docs/05-no-hardware-simulation.md`.

## Project Code (Automation)
This project includes runnable Python scripts so the repository is not only documentation.

- `scripts/generate_simulated_evidence.py`: generates simulation outputs in the `evidence` folder
- `scripts/validate_ip_plan.py`: validates `configs/example-ip-plan.csv` and writes a validation report

Run automation:

```bash
python3 scripts/generate_simulated_evidence.py
python3 scripts/validate_ip_plan.py
```

## Repository Structure
```text
.
|-- README.md
|-- scripts
|   |-- generate_simulated_evidence.py
|   `-- validate_ip_plan.py
|-- docs
|   |-- 01-project-plan.md
|   |-- 02-implementation-steps.md
|   |-- 03-testing-checklist.md
|   |-- 04-troubleshooting.md
|   |-- 05-no-hardware-simulation.md
|   `-- 06-final-report-template.md
|-- evidence
|   |-- README.md
|   |-- completed-test-results.md
|   |-- ip-plan-validation-report.txt
|   |-- ping-pc01-to-printer.txt
|   |-- ping-pc02-to-printer.txt
|   |-- simulated-installation-log.txt
|   |-- simulated-ping-results.txt
|   |-- simulated-test-print-log.txt
|   `-- topology-diagram.mmd
`-- configs
	|-- example-ip-plan.csv
	`-- example-printer-network-settings.txt
```

## Execution Workflow
1. Review project plan: `docs/01-project-plan.md`
2. Choose setup path:
	- Hardware path: `docs/02-implementation-steps.md`
	- No-hardware path: `docs/05-no-hardware-simulation.md`
3. Validate setup: `docs/03-testing-checklist.md`
4. Resolve issues (if any): `docs/04-troubleshooting.md`
5. Prepare project report: `docs/06-final-report-template.md`

## Project Evidence
- Topology diagram (drawn or simulated)
- IP plan table and chosen subnet
- Screenshots (or simulated outputs) for connectivity checks
- Printer installation steps and expected outcomes
- Completed testing checklist
- Project report

Current generated evidence is already available in `evidence/`.

## Repository Sync (Optional)
Use these commands in terminal from project root if you want to push updates:

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