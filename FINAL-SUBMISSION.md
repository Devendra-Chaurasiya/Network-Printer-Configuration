# Final Submission Report

Project Title: Network Printer Configuration
Student Name: Devendra Chaurasiya
Submission Date: 16 March 2026
Repository Link: https://github.com/Devendra-Chaurasiya/Network-Printer-Configuration

## 1. Objective
The objective of this project is to design and document a complete network printer configuration process, including IP planning, client integration, validation, and troubleshooting.

## 2. Environment
- Mode: Simulation/Documentation
- Tools used: Markdown documentation, network topology planning, Linux command examples
- OS used: Linux (development environment)

## 3. Network Topology
Proposed LAN topology:

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

## 4. IP Addressing Plan
| Device | IP Address | Subnet Mask | Gateway | Notes |
|--------|------------|-------------|---------|-------|
| Router | 192.168.10.1 | 255.255.255.0 | N/A | Default gateway |
| Printer | 192.168.10.50 | 255.255.255.0 | 192.168.10.1 | Static/reserved address |
| PC-01 | 192.168.10.101 | 255.255.255.0 | 192.168.10.1 | Client host |
| PC-02 | 192.168.10.102 | 255.255.255.0 | 192.168.10.1 | Client host |

## 5. Implementation Steps Performed
1. Created complete project plan and network scope.
2. Defined topology and IP addressing matrix.
3. Documented hardware-based implementation steps for real environments.
4. Added no-hardware simulation workflow for constrained environments.
5. Added testing checklist, evidence guide, and troubleshooting playbook.

## 6. Testing Results
| Test | Result | Evidence |
|------|--------|----------|
| Ping PC-01 to printer | Simulated Pass | See evidence/simulated-ping-results.txt |
| Ping PC-02 to printer | Simulated Pass | See evidence/simulated-ping-results.txt |
| Add printer by TCP/IP | Simulated Pass | Step validation in docs |
| Print test page | Simulated Pass | Workflow validation in docs |

## 7. Issues Faced and Fixes
Issue: No physical network printer available.
Fix: Completed the project in simulation/documentation mode with full technical workflow, validation logic, and transparent limitation statement.

## 8. Conclusion
The project successfully demonstrates technical understanding of network printer deployment in a LAN, including static IP assignment, device integration, and validation/testing strategy. The work is structured to be directly reusable when real hardware becomes available.

## 9. Limitation Statement
This project was completed in simulation/documentation mode due to unavailability of a physical network printer. The solution demonstrates correct network design, IP allocation, installation approach, and validation workflow.
