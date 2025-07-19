## MikroTik Mastery Quiz

Use this quiz to test your understanding and ability to redo the full MikroTik setup process without referring to your notes.

---

### Step 0: Factory Reset Router

- What method would you use to reset the MikroTik to factory defaults?

	> use winbox for convenience(if available via wine on mac)

		> with router connected,, open wine
		> select mikrotik MAC addr
		> enter correct credentials
		> "system" -> "reset configuration"
			> do not tick any boxes (unless you clearly understand what each does)
		> click "reset configuration" button

>	  if winbox not available, physical reset

		> unplug mikrotik
		> hold down power button (before reconnecting power cable)
		> keep holding down button and plug in power cable
		> hold button until LED stars flashing rapidly
		> when rapid flash, release power button

- What behavior signals the reset is working (LEDs, boot process, etc)?
    
		> if LED flashes rapid, and you release:
			> you can go to system settings -> network
			> see eth cnnection status as "connected"
			> further go to browser and seach 192.168.88.1
				> if default credentials work for login, reset == sucsess
---

### Step 1: Layer 1 Setup

- What cable connects which port on your Mac and MikroTik?

		> eth cable(RJ45 plug) -> eth port(RJ45 interface)
		> any port csn technically be connected

- What port number should you use on MikroTik for initial LAN access?

		> with no other internet access available, mikrotik port1 should be connected to laptop
		> with external wifi source, connecting mikrotik port2 is fine. just ensure system network settings are set to prioritize wifi over eth connection

---

### Step 2: macOS Network Configuration

- What network setting must your Mac use to receive an IP from the MikroTik router?

		> dynamic host connection protocol (DHCP)

- How do you verify your Mac has received the correct IP address?

		> sys settings -> network
			> eth status == connected
			> able to brows to 192.168.88.1

- How do you test if the connection to MikroTik is active?

		> head to laptop terminal
		> ping mikrotik ip addr
		> is packets tx + rx == sucsessfull, you are good
---

### Step 3: Access the MikroTik Web Interface

- What web address or IP do you enter to access WebFig?

		> 192.168.88.1

- What are the default login credentials for MikroTik?

		> username = admin
		> password = (blank) OR pw on sticker of mikrotik

---

### Step 4: WebFig Interface Navigation

- Where in WebFig can you:
    
    - View all physical and virtual interfaces?

		> head to "interfaces" tab (usually default screen)

    - Make a backup of your current configuration?

		> head to "files" tab

    - See current DHCP leases and assigned IP?

		> head to "IP" -> DHCP server -> "leases"

---

### Step 5: Safe Shutdown and Saving Config

- What command saves your current configuration to a backup file?

		> in terminal

			> /system backup save name=clean-state

- What command initiates a clean power-off from the terminal?

		> /system shutdown

- Why is it important to avoid unplugging the router before issuing these commands?

		> even though mikrotik hardware are generally resiliant to sudden power-loss(like you just unplugging the power cable), there are always the risk of corrupting configuration.
		> can cause file errors on next boot
		> can cause booting errors with next session

---

### Bonus: Troubleshooting

- Why might your Mac lose internet access after connecting to the MikroTik via Ethernet?

		> because modern systems typically prioritise eth connection over wifi. if the eth connection has no internet access, your laptop (now mainly eth connected) also does not have internet access

- How can you change interface priority so macOS prefers Wi-Fi over Ethernet?

		> in laptop
		
			> ssystem settings -> network
		
				> here you will see all connected interfaces
				> usualy at the bottom of the list, there will be a clickable bar that has 3 dots("...")
				> select it
				> you will se a "select service order" section. click it
				> drag wifi to the top
				
			> this prioritizes wifi to be the main internet methd that your laptop will use.
