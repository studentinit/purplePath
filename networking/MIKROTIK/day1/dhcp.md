# **View or Enable DHCP Server**

**Why:** DHCP automatically assigns IPs to connected devices, so you don’t have to do it manually.

**Steps:**

> go to `IP` → `DHCP Server`
    
> see a list of interfaces (like `bridge1`) where DHCP may be active
    
* Check:
    
    > Status = **Running**
        
    > Address Pool = shows which IPs it can assign
        
#### If no DHCP server exists:
    
    > Click **DHCP Setup**
        
    > Select interface (LIKE bridge1)
        
    > Follow prompts to configure address ranges, DNS, lease time
        

> the default config should already have DHCP active on the bridge interface.
