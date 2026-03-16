# 04 - Troubleshooting Guide

## Common Issues and Fixes

### 1) Printer Not Reachable (Ping Fails)
Possible causes:
- Wrong IP/subnet/gateway
- Cable disconnected or weak Wi-Fi signal
- Client and printer in different subnet/VLAN

Fixes:
1. Verify printer IP settings.
2. Confirm client IP settings are in same subnet.
3. Check cable/switch port/Wi-Fi status.
4. Restart printer and router/switch if needed.

### 2) IP Conflict Detected
Symptoms:
- Intermittent printer availability
- ARP warnings or duplicate IP messages

Fixes:
1. Change printer IP to unused address.
2. Exclude static IP from DHCP pool.
3. Configure DHCP reservation by MAC address.

### 3) Printer Added But Cannot Print
Possible causes:
- Incorrect driver or wrong protocol/port
- Print spooler/CUPS service issues

Fixes:
1. Reinstall proper model-specific driver.
2. For raw printing, ensure port 9100 is used.
3. Restart print spooler service.
4. Clear stuck print queue.

### 4) Slow or Delayed Printing
Possible causes:
- Network congestion
- Duplex/high-resolution default settings

Fixes:
1. Use wired Ethernet when possible.
2. Reduce default print quality for testing.
3. Update printer firmware.

## Useful Commands
Check local IP:

```bash
ip a
```

Ping printer:

```bash
ping -c 4 192.168.10.50
```

Check CUPS service:

```bash
systemctl status cups
```
