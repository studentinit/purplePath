
# assigning a static IP via DHCP lease (without touching default config)

If you just want to **practice using the MikroTik interface** without modifying the default configuration (`defconf`), you can **add a static lease manually**:

#### in webfig or winbox:

> Navigate to:
    
    IP > DHCP Server > Leases
    
> Click:
    
    Add New
    
> Fill in the required fields:
    
    - **MAC address**: get this from your device (Mac: `System settings > network > ethernet > details`)
        
    - **address**: choose a static IP (192.168.88.100)... make sure the addr is within the subnet but outside the DHCP pool range (to avoid conflicts).
        
    - **Comment** (optional): Add a label like `"MacBook static lease"`
        
> Click **OK** or **Apply**.

### Notes

> this doesn't remove or change anything in the default config.
    
> router will now reserve the IP for that device every time it connects.
    
> you won’t break anything — it’s a safe and reversible way to explore.
    
> if the device is already connected and you want to skip typing, you can use the **“Make Static”** button instead.


# editing default config to get static (alternative/optional)

let’s say your Mac gets `192.168.88.254` via DHCP. In WebFig:

> Navigate to:
    
    IP > DHCP Server > Leases
    
> wait for your Mac to appear and select it

> Click:
    
    make static

> Optionally click **Edit** to assign a new IP (192.168.88.10) and name it `my-Mac`
    
> hit ok

		> Next time you connect, the router will **always assign that IP to your MAC address** — even though DHCP is still doing the work.

### Notes

> this **does** modify the default config (`defconf`).
    
> router will now **persistently assign the same IP** to your MAC address.
    
> it is still reversible, but mistakes could cause issues... be prepared to reset if needed.
