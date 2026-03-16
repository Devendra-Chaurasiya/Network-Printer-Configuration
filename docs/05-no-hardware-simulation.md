# 05 - No Hardware Simulation Workflow

Use this workflow if you do not have a physical network printer.

## Goal
Demonstrate full understanding of network printer configuration using a simulated setup and documented validation.

## Option A: Packet Tracer / Network Simulator (Recommended)
1. Build topology:
   - 1 router
   - 1 switch
   - 2 PCs
   - 1 network printer device (simulated)
2. Configure subnet: 192.168.10.0/24
3. Assign addresses:
   - Router LAN: 192.168.10.1
   - Printer: 192.168.10.50
   - PC-01: 192.168.10.101
   - PC-02: 192.168.10.102
4. Test connectivity with ping from each PC to printer IP.
5. Capture screenshots of:
   - Topology view
   - Device IP configuration
   - Ping success output

## Option B: VM-Based Logical Simulation
If Packet Tracer is not available, use documentation-driven simulation:
1. Keep the same topology/IP plan in this repository.
2. Run connectivity commands and explain expected outcomes.
3. Provide command snippets and interpretation in report.
4. Mark all test entries as Simulated where physical proof is not possible.

## Required Submission Notes
Include this statement in your final report:

```text
This project was completed in simulation/documentation mode due to unavailability of a physical network printer. All network design, IP planning, installation logic, and testing workflow are documented according to standard network printer deployment practices.
```

## What Evaluators Usually Check
- Is the network design correct?
- Is IP addressing valid and conflict-free?
- Are setup steps technically accurate?
- Is testing methodology clear and complete?
- Is the limitation (no hardware) transparently explained?

## Minimum Evidence for No-Hardware Mode
- Topology diagram image (can be hand-drawn digitally)
- Filled IP plan table
- Simulated ping output or expected output table
- Completed testing checklist with comments
- Final report with limitation note
