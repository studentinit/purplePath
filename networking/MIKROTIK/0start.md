## 4 Day Troubleshooting EXP

**Where to begin?**

As someone with no prior experience working with MikroTik or any physical networking devices, I was excited... maybe a bit too hasty to dive into the terminal and start configuring "stuff". I’ve been studying networking at a CCNA level, and until recently, I had only simulated environments to practice on. So, when I finally got my hands on a MikroTik router, I jumped straight into setup and exploration — aiming to understand firewall rules and configurations on a more advanced level.

But I made one classic mistake:  
I tried to span the wagon **in front of the cattle.**

I didn’t read the manual.  
I didn’t realize that the default username and **password were printed on the box/manual**. So when I couldn’t log in, I assumed the router needed to be reset — and did so **incorrectly**.

---

### **The Chaos Begins**

After that first improper reset, the router started behaving oddly. My computer’s Ethernet interface, which had previously shown as “Connected,” now displayed a **“Self-Assigned IP”** (on macOS) — a sure sign that DHCP failed and no communication was established.

Thus began a **4-day troubleshooting marathon**, including:

- Winbox on macOS (via Wine) → failed
    
- Manually setting up a Windows VM on UTM → too slow, messy bridging
    
- Switching to a pre-built UTM Windows image → faster but still complicated networking
    
- Netinstall in the Windows VM → unable to detect router
    
- Switched to a native Windows laptop
    
    - Installed Netinstall
        
    - Allowed through Windows Firewall
        
    - Tried multiple guides, videos, reset techniques
        
    - Router still didn’t show up in Netinstall
        
- Tried **static IPs** on both ends, played with **bridged** vs **shared networking**, disabled VPNs and proxies
    
- Ping sometimes worked, **but ARP showed incomplete entries or all-FF MAC addresses**
    
- Reset after reset, still nothing
    
- Even ChatGPT was trying to help me make sense of it all
    

---

### **The Reality Hits**

Eventually, I realized something important:

The router wasn’t “bricked”... it was just **never broken** in the first place.  
I had caused a network misconfiguration by resetting it when there was no need. The only real issue was **not knowing the login credentials**, which had been right there in the manual the whole time.

When I replaced the MikroTik with a new one, I did the smart thing:  
**I read the manual first.**  
Entered the default password.  
Logged in.  
Everything just worked.

No troubleshooting. No resets. No Netinstall. No headaches.

---

### **What I Learned (the Hard Way)**

- **Always check the manual** before doing anything drastic with new hardware.
    
- **Resetting isn't always the answer** — especially if you don't fully understand the consequences.
    
- **MAC address-based login (Layer 2)** in Winbox doesn’t work unless the router is properly broadcasting it and you're on the same Layer 2 segment.
    
- Netinstall is a useful recovery tool — but it's not magic. It only works in very specific conditions (correct architecture, correct interface, proper reset timing, etc.).
    
- Troubleshooting Layer 1 and 2 problems can be frustrating without tools and experience — but each failure teaches something new.
    

---

### Final Thoughts

This wasn’t just a technical hiccup — it was a deep learning experience about how physical networking works, how embedded devices behave, and how _overconfidence without preparation_ can cost you time.

If you’re ever setting up MikroTik (or any router) for the first time:  
**Read the manual.**  
**Save yourself 4 days.**


```
# Why self-assigned IPs happen

When your computer doesn’t get a valid IP from a DHCP server (like a router), it gives itself a **self-assigned IP** (usually in the `169.254.x.x` range).  
This is your machine saying:  
	“I asked for an IP, but no one answered. So I’ll just givE myself one.”

In this case, the Mikrotik either wasn’t acting as a DHCP server anymore (due to reset), or the Ethernet negotiation failed.
```


```
# How Netinstall actually works (PXE-style booting)

Netinstall doesn’t flash the router like a USB. It works by:

1. The router booting into **Ethernet listen mode** (after a reset with the reset button held).
    
2. Sending a **boot request** over the network.
    
3. Netinstall on your PC hears that request and **sends the OS image back**.
    

It’s similar to PXE booting (network boot). So:

- Your PC must have a bridged Ethernet connection
    
- Your firewall must not block UDP
    
- Your router must be properly reset and **powered while holding the button** until it shows up.

```


```
# Layer 2 vs Layer 3 troubleshooting

Think of it like this:

- **Layer 2 (Data Link)** = MAC addresses  
    Tools like `Winbox` (via MAC connection) or `ARP` operate here.
    
- **Layer 3 (Network)** = IP addresses  
    Tools like `ping`, `browser`, or IP-based Winbox access use this.
    

So:

- If Layer 3 (IP) fails but Layer 2 (MAC) works → Your router is alive, but networking config is broken.
    
- If Layer 2 fails too → Bad cable, wrong reset, dead router, or firewall issues.

```
