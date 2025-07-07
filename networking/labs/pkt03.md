1. Connect PC1's RS-232 port to R1's console port.
___
	  - go to connections tab and select the console connection(blue wire in pkt)
	  - clicks pc and select RS-232 port
	  - click and connect router on console port
	  - 

2. Use the console connection to configure the router from PC1. Change the hostname to R1.
___
	  - select pc -> desktop -> terminal
	  - clicks ok button to accept default config settings of terminal
	  - now we can use router CLI through pc
	  - "enable"
	  - "conf t"
	  -  "hostname R1"
	  - 

3. Set the enable secret of R1 to 'cisco'.
___
	  - "enable secret cisco"

4. Set the console password of R1 to 'ccna', and make it required to connect to R1 by the console port. Check the runing configuration. Is the password encrypted?
___
	  - "line console 0" -> line config mode for port 0. since there is only 1 connection, there is only connection 0
	  - "password ccna" -> set pw for connection line
	  - "login" -> tell sys that pw must be used when logging in
	  - "end" -> return to privelege exec mode
	  - "exit" -> quit connection
	  - press enter
	  - now pw(ccna) must be entered
	  - "enable"
	  - pw (cisco) must be entered
	  - "do sh run"
	  - secret == enrypted
	  - password == plain txt
	  - hit space until at bottom of running config
	  - (line con 0)
	    (password ccna)
	    (login)
		line con pw not encrypted
		
5. Enable password encryption on R1. Verify by checking the running configuration, and then save your configurations.
___
	- "conf t"
	- "service password-encryption"
	- "do sh run"
		(line con 0)
		(password 7 08224F4008)
		(login)
	- "do copy run start" save running config
	- "do sh start" make sure start config is same as running config
