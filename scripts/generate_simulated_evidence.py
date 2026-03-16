#!/usr/bin/env python3
"""Generate simulation evidence files for the Network Printer Configuration project."""

from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_DIR = ROOT / "evidence"


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def ping_output(source: str, target_ip: str) -> str:
    return f"""Source Host: {source}
Command: ping -c 4 {target_ip}
Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

PING {target_ip} ({target_ip}) 56(84) bytes of data.
64 bytes from {target_ip}: icmp_seq=1 ttl=64 time=0.42 ms
64 bytes from {target_ip}: icmp_seq=2 ttl=64 time=0.39 ms
64 bytes from {target_ip}: icmp_seq=3 ttl=64 time=0.44 ms
64 bytes from {target_ip}: icmp_seq=4 ttl=64 time=0.41 ms

--- {target_ip} ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3006ms
rtt min/avg/max/mdev = 0.39/0.41/0.44/0.02 ms

Result: Simulated Pass
Note: Generated as simulated evidence for no-hardware mode.
"""


def build_topology_mermaid() -> str:
    return """flowchart TB
    internet([Internet]) --> router[Router\n192.168.10.1]
    router --> switch[Switch]
    switch --> pc1[PC-01\n192.168.10.101]
    switch --> pc2[PC-02\n192.168.10.102]
    switch --> printer[Printer\n192.168.10.50]
"""


def build_completed_results() -> str:
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""# Completed Test Results (Simulation Mode)

Generated At: {generated_at}

| Test ID | Test Description | Expected Result | Actual Result | Status |
|---------|------------------|-----------------|---------------|--------|
| T1 | Printer powered and connected to LAN | Link is up | Simulated link up in planned topology | Simulated |
| T2 | Ping from PC-01 to printer IP | Ping replies received | 4/4 replies from 192.168.10.50 | Simulated |
| T3 | Ping from PC-02 to printer IP | Ping replies received | 4/4 replies from 192.168.10.50 | Simulated |
| T4 | Add printer on PC-01 by TCP/IP | Printer added successfully | Simulated successful install | Simulated |
| T5 | Add printer on PC-02 by TCP/IP | Printer added successfully | Simulated successful install | Simulated |
| T6 | Test print from PC-01 | Print job completed | Simulated print queue success | Simulated |
| T7 | Test print from PC-02 | Print job completed | Simulated print queue success | Simulated |
| T8 | Printer survives restart with same IP | Same static IP retained | Simulated persistence of static config | Simulated |
"""


def build_installation_log() -> str:
    return """Simulated Printer Installation Log
================================

Windows Client (PC-01)
- Opened Settings > Bluetooth & devices > Printers & scanners
- Selected Add printer manually
- Added TCP/IP printer at 192.168.10.50
- Selected matching generic TCP/IP model in simulation
- Status: Simulated Pass

Linux Client (PC-02)
- Accessed CUPS at http://localhost:631
- Added printer using URI socket://192.168.10.50:9100
- Applied model profile in simulation
- Sent test job to queue
- Status: Simulated Pass
"""


def build_test_print_log() -> str:
    return """Simulated Test Print Log
========================

PC-01
- Job ID: SIM-PC01-001
- Printer IP: 192.168.10.50
- Result: Completed (Simulated)

PC-02
- Job ID: SIM-PC02-001
- Printer IP: 192.168.10.50
- Result: Completed (Simulated)

Overall Result: Simulated Pass
"""


def main() -> None:
    write_file(EVIDENCE_DIR / "ping-pc01-to-printer.txt", ping_output("PC-01", "192.168.10.50"))
    write_file(EVIDENCE_DIR / "ping-pc02-to-printer.txt", ping_output("PC-02", "192.168.10.50"))
    write_file(EVIDENCE_DIR / "topology-diagram.mmd", build_topology_mermaid())
    write_file(EVIDENCE_DIR / "completed-test-results.md", build_completed_results())
    write_file(EVIDENCE_DIR / "simulated-installation-log.txt", build_installation_log())
    write_file(EVIDENCE_DIR / "simulated-test-print-log.txt", build_test_print_log())

    print("Generated simulation evidence files in:", EVIDENCE_DIR)


if __name__ == "__main__":
    main()
