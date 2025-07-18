## MikroTik Day 1: Initial Setup and Configuration

### Layer 1 Setup (Physical)

**Devices used:**

* MikroTik hAP lite
* USB-C to Ethernet adapter
* Cat6 cable

```
          RJ45 plug    Ethernet cable     RJ45 plug
(Mikrotik) ----->     ----------->     ----------->  |
    ^                                               v
mikrotik power port                          adapter (RJ45)
    ^                                               |
    |                                               v
power cable                                   adapter cable
    ^                                               |
    |                                               v
home wall plug                                  laptop (USB-C)
```

---

### MikroTik Port Overview

| Port | Label    | Default Function                       |
| ---- | -------- | -------------------------------------- |
| 1    | ether1   | WAN port – connects to modem/uplink    |
| 2-4  | ether2-4 | LAN ports – local devices like laptops |

---

### Phase 1: Connect and Access Web Interface

#### 1. Connect Hardware

* Connect Ethernet adapter to MacBook
* Connect Cat6 cable from adapter to **ether2** on MikroTik
* Plug in MikroTik power and wait \~30 seconds for boot

#### 2. macOS: Enable DHCP

* System Settings → Network → \[Your Adapter Name]
* Set to **Using DHCP** (if set to Automatic, DHCP works by default)

**Verify with terminal:**

```bash
ifconfig | grep inet
ping 192.168.88.1
```

#### 3. Open MikroTik Web Interface

> Open Safari or Chrome

> Navigate to: `http://192.168.88.1`

* Login:

  > Username: admin
  
  > Password: *(leave blank OR type pw on sticker)*

If it doesn’t load:

> Confirm DHCP IP assignment
    > walkthrough further down

> Factory reset the MikroTik if needed
    > walkthrough further down


#### 4. Inside WebFig

* Navigate through:

  * **Interfaces** – eth1–4 and wlan1
  * **Bridge** – Virtual switch linking LAN ports and Wi-Fi
  * **Files** – Create and download backups

---

### Quick Features to Try

* **Backups**: Create via WebFig > Files > Backup
  > SEE backup.md

* **Set Username & Password**
  > SEE name.md

* **DHCP Server**: Enable or view on bridge or LAN
  > SEE dhcp.md

* **Static IPs**: Assign under IP → DHCP Leases
  > SEE ip.md

* **NAT masquerade rule**: Basic settings under IP → Firewall
  > SEE nat.md

* **shut down cleanly**:
  > SEE down.md

---

## Troubleshooting: No Internet While Connected to MikroTik

**Problem**: Mac connected via Ethernet to MikroTik, but can’t access internet.

**Cause**: Mac prioritizes Ethernet connection over Wi-Fi.

**Solution**:

1. Go to System Settings > Network
2. Click the 3 dots > Set Service Order
3. Drag Wi-Fi to top of list

---

### Resetting MikroTik to Factory Defaults

**Hold reset button** on MikroTik while powering on until LED blinks, then release.
This restores factory settings and allows fresh config.

---

### Summary

You now have:

> A functional Layer 1 setup

> DHCP-enabled link from MikroTik to your Mac

> Access to WebFig (GUI)

> Ability to make and download backups

> Verified interface and IP configuration


