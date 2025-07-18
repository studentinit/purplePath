# Step-by-Step Guide

---

#### 1. Install Homebrew (macOS Package Manager)

> Homebrew lets you install and manage software using the Terminal.

If you haven’t installed Homebrew yet, open the **Terminal** (press `Command + Space`, type “Terminal”, and hit Enter), then paste this command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- Follow the on-screen instructions — it will install and configure everything automatically.
    
- After installation, **close and reopen the Terminal** so it loads Homebrew correctly.
    

To test if Homebrew installed correctly:

```bash
brew --version
```

You should see a version number like `Homebrew 4.2.0` (or similar).

---

#### 2. Install Wine via Homebrew

> Wine allows you to run Windows `.exe` programs on your Mac.

In Terminal:

```bash
brew install --cask wine-stable
```

This might take a few minutes — wait for the install to complete.

---

#### 3. Download and Launch Winbox Using Wine

1. **Download Winbox** from the official MikroTik website
    
2. Locate the `winbox64.exe` (Downloads folder)
    
3. Run the `.exe` file using Wine:
    

```bash
wine ~/Downloads/winbox64.exe
```

> If your filename is different, replace `winbox64.exe` with the correct file name.

If this is your first time using Wine, it may take a few seconds to set up its environment.


with winbox ready:

	> open winbox app
	> at the top of winbox gui
		> select neigbours
		> a blank screen will appear
		> your app is now waiting for the mikrotik to connnect(if not already connected)
	> connect mikrotik
	> under MAC you will se sometext appear(this is your router's address via layer2)
	> click on the address
	> on the left side you will se the exact address pasted in automatically
	> username under MAC
	> password under username
	> type in the password(the one on your manual sticker)
	> you should now be able to log into the router with a similar gui as webfig.
	> click on system(left side bar)
	> select "reset configuration"
		> **DO NOT** check any boxes:
    
```
[x] keep user configuration      ❌ leave unchecked  
[x] CAPS                         ❌ leave unchecked  
[x] no default configuration     ❌ leave unchecked  
[x] do not backup                ❌ leave unchecked  
[x] run after reset              ❌ leave unchecked   
```
		
		Just hit the **"Reset Configuration"** button.
		
	> (optional) if you want to see more:
	
		> open mac system settings > network
		> you will see the ETH connection drop once reset has been selected in winbox.
		> just give it 30 - 40 sec to reconnect with default configurations again.
		
		> head back to winbox, you might see recconnection errors a few times, but once it sucsessfully reconnected, you will receive a notification in winbox stating "RouterOS Default Configuration"
		> this will list the config specs.
		> press "ok"
		
	> HEAD BACK TO BROWSER:
		> search 192.168.88.1 again.
		> enter sticker password
		> you should now be able to navigate through webfig again
	> OPTIONALLY
		> you can close winbox OR you can tweak setting in winbox as well(using it as an alternative to webfig).
