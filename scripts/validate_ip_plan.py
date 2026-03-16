#!/usr/bin/env python3
"""Validate IP addressing plan consistency for the project."""

import csv
import ipaddress
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
INPUT_CSV = ROOT / "configs" / "example-ip-plan.csv"
OUTPUT_REPORT = ROOT / "evidence" / "ip-plan-validation-report.txt"


def parse_rows(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def network_of(ip_str: str, mask_str: str) -> ipaddress.IPv4Network:
    iface = ipaddress.ip_interface(f"{ip_str}/{mask_str}")
    return iface.network


def validate(rows: List[Dict[str, str]]) -> Tuple[bool, List[str]]:
    messages: List[str] = []
    ok = True

    seen_ips = set()

    for row in rows:
        device = row["Device"].strip()
        ip_text = row["IP Address"].strip()
        mask_text = row["Subnet Mask"].strip()
        gateway_text = row["Gateway"].strip()

        try:
            ip_obj = ipaddress.IPv4Address(ip_text)
            network = network_of(ip_text, mask_text)
        except ValueError as exc:
            ok = False
            messages.append(f"[ERROR] {device}: invalid IP or mask ({exc})")
            continue

        if ip_obj in seen_ips:
            ok = False
            messages.append(f"[ERROR] {device}: duplicate IP address {ip_obj}")
        seen_ips.add(ip_obj)

        if gateway_text.upper() != "N/A":
            try:
                gw_obj = ipaddress.IPv4Address(gateway_text)
                if gw_obj not in network:
                    ok = False
                    messages.append(
                        f"[ERROR] {device}: gateway {gw_obj} is outside network {network}"
                    )
            except ValueError:
                ok = False
                messages.append(f"[ERROR] {device}: invalid gateway {gateway_text}")

        messages.append(f"[OK] {device}: {ip_obj}/{mask_text} in network {network}")

    return ok, messages


def main() -> int:
    rows = parse_rows(INPUT_CSV)
    ok, messages = validate(rows)

    OUTPUT_REPORT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_REPORT.open("w", encoding="utf-8") as f:
        f.write("IP Plan Validation Report\n")
        f.write("=========================\n\n")
        f.write(f"Input file: {INPUT_CSV}\n\n")
        for line in messages:
            f.write(line + "\n")
        f.write("\nFinal status: " + ("PASS" if ok else "FAIL") + "\n")

    print("Validation report written to", OUTPUT_REPORT)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
