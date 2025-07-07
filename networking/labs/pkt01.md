
cisco lab with 2 routers. below are steps to follow to setup.

1. Connect R1 and R2 by their GigabitEthernet0/0 interfaces
___
	- use copper staight through connection and connect both routers on "GigabitEthernet0/0"
  

2. Set the hostnames according to the network diagram (R1 and R2)
___
	  this can be done via config GUI or the CLI
	  - open CLI tab
	  - type "enable" to enter previledge exec mode
	  - "exit" == cd ..
	  - "config t" to enter global config mode
	  - "hostname R1" for router 1 and "hostname R2" for router 2
	  - 

3. Set the enable password on each router to 'cisco'
___
  while in global config mode:
  
  	- "enable password cisco" to set the password on each router
  to test:
  
  	- "exit" * 2 (* 1 back to previladge exec mode(* 1 back to exec mode))
  	- "enable"(pw must be entered)
    -
  
4. View the password in the running configuration. Is it encrypted?
___
	  - "show running config" or "sh run" to view running config
	  - pw not encrypted

5. Enable password encryption on each router
___
	   - "service password-encryption" encrypt password

6. View the password in the running configuration. Is it encrypted?
___
previledge exec mode, else use "do" (like sudo)

	  - "do show running config" password == enrypted

7. Disable password encryption on each router.
___
	  - "no service password encryption"

8. View the password in the running configuration. Is it encrypted?
___
	- "show running config"
	- password still encrypted but step 7 ensure future passwords will not be encrypted.
