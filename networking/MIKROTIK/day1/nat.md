# **Check or Add a NAT Masquerade Rule**

**Why:** NAT masquerading lets multiple local devices share one public IP — essential for internet access.

**Steps:**

1. Go to `IP` → `Firewall`
    
2. Select the `NAT` tab
    
3. Check if this rule exists:
    
    - **Chain**: `srcnat`
        
    - **Out Interface**: `ether1`
        
    - **Action**: `masquerade`
        
4. If missing:
    
    - Click **Add New**
        
    - Set:
        
        - **Chain**: `srcnat`
            
        - **Out Interface**: `ether1`
            
        - **Action**: `masquerade`
            
    - Click **OK**
        

> This rule enables internet sharing from LAN -> WAN via the MikroTik.
