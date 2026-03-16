# 02 - Implementation Steps

If you do not have a physical printer, follow `docs/05-no-hardware-simulation.md` instead of hardware steps.

## Step 1: Physical and Network Connection
1. Power on the printer.
2. Connect printer to LAN using Ethernet (recommended) or configure Wi-Fi.
3. Confirm link/activity LED on printer port (if Ethernet).

## Step 2: Configure Printer Network Settings
From printer control panel or web interface:

- Network mode: Static IP
- IP address: 192.168.10.50
- Subnet mask: 255.255.255.0
- Default gateway: 192.168.10.1
- DNS server: 8.8.8.8 or local DNS

Save and restart printer if required.

## Step 3: Verify Connectivity
From each client:

```bash
ping -c 4 192.168.10.50
```

Expected result: replies received with low latency and no packet loss.

## Step 4: Install Printer on Windows
1. Open Settings > Bluetooth & devices > Printers & scanners.
2. Select Add device.
3. Choose Add manually.
4. Select Add a printer using a TCP/IP address.
5. Enter hostname/IP: 192.168.10.50.
6. Install correct vendor driver.
7. Set as default printer if required.
8. Print a test page.

## Step 5: Install Printer on Linux (CUPS)
Install CUPS tools if needed:

```bash
sudo apt update
sudo apt install -y cups cups-client
sudo systemctl enable --now cups
```

Add printer from CUPS web UI:

1. Open http://localhost:631
2. Administration > Add Printer
3. Select protocol (AppSocket/JetDirect or IPP)
4. Enter device URI, for example:

```text
socket://192.168.10.50:9100
```

5. Select printer model/PPD.
6. Print test page.

## Step 6: Optional Router DHCP Reservation
Reserve 192.168.10.50 to printer MAC address in router DHCP settings to prevent conflicts.

## Step 7: Document Configuration
Record:
- Printer model and serial
- MAC address
- Final IP settings
- Driver version
- Client test results
