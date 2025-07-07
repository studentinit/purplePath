1. Connect the two routers by their GigabitEthernet0/0 interfaces
___
    again ill use copper straight-through and connect on above interface
  

2. Set the hostname of each router according to the network diagram (R1 and R2)
___
	  - "enable"
	  - "conf t" mave from :> to :#
	  - "hostname R1"

3. Set the enable password of each router to 'cisco'
___
	  - "enable password cisco" add pw(cisco)
	  - "do sh run" check running configuration session

4. Set the enable secret of each router to 'ccna'
___
	more secure than enable password cause its encrypted by default
	
	  - "enable secret ccna"

5. Exit back to exec mode and try to enter privileged exec mode. Which password do you have to use?
___
	  - "exit " * 2
	  - "enable"
	  - "ccna" secret must be typed in(secret) and not pw(cisco)

6. View the running configuration. Which of the passwords is encrypted?
___
	  - secret is encrypted and pw is plain text

7. Enable password encryption on the router, and view the running configuration. What has changed?
___
	  - "conf t"
	  - "service password-encryption"
	  - "do sh run"
	  - secret + pw == encrypted

8. Save the configuration and reload the router to confirm.
___
	- "startup-config" check current
	- "copy run start"
	- "sh start" confirm startup-config is same as running config
- a shorter way is simply "write" to copy running-config (confirm with sh start)
	- "exit" * 2 
	- "enable"
	- if user is R1 then config copy == sucsess
