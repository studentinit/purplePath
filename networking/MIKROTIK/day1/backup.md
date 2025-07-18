# **Create a System Backup**

**Why:** A backup lets you quickly recover your current configuration if something goes wrong.

**Steps:**

> Log into WebFig (`http://192.168.88.1`)
    
> In the left menu, go to `Files`
    
> Click the **Backup** button at the top
    
> (Optional) Set:
    
    - **Name**: to identify this backup
        
    - **Password**: adds security to the file
        
5. Click **Backup**

	> A `.backup` file appears in the list — click on the filename to **download** it to your computer.
		
	> Tip: Keep your backups somewhere safe (e.g. cloud or external drive).

		> ## Backup Restore Warning(do not just press the "restore" button)

		> **Restoring `.backup` files from unknown sources (or old backups)** will replace **all router settings**, including WebFig access and interface modes.
		    
		> Always create a **current backup** first
		    
		> Be ready to perform a **factory reset** OR have winbox ready via wine, if the router becomes inaccessible. (see wine.md)
