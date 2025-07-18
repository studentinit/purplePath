# to shut down cleanly.
___
MikroTik devices are **generally very resilient**, even if you just yank the power.  
But if it’s **saving a config or updating packages** when you do that, there's a **risk** of:

	 **File system errors**
    
	**Corrupted configuration**
    
	**Router failing to boot cleanly next time**

first, we write changes to disk before power off.
to backup current configurations. basically saving properly, then shutting down in a safe way.

	> head to terminal
	
	> "/system backup save name=clean-state" = save
		> you should get a message like: saving system configuration
	
	> "/system shutdown" = shut down safely
		> you should get a message like: shutdown, yes? [y/N]:
			> type "y"
				> you should get a message like: system will shutdown promptly
		> now safe to unplug the router
