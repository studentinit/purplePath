# below is a walkthrough of completing tasks in packet tracer using router and switch CLI


1. Change the hostnames of the router and switch to the appropriate names (R1, SW1)

##Use the 'hostname' command in global configuration mode##

	  > select router and select CLI
	  
		  > hit enter TO GO TO USER EXEC MODE (>)
		  > 
		  > "enable" to enter privileged exec mode (#)
		  > 
		  > "conf t" to enter global configuration mode ((config)#)
		  > 
		  > "hostname R1" to change name
	
	  > select switch and select CLI

		  > hit enter TO GO TO USER EXEC MODE (>)
		  > 
		  > "enable" to enter privileged exec mode (#)
		  > 
		  > "conf t" to enter global configuration mode ((config)#)
		  > 
		  > "hostname SW1" to change name

2. Configure an unencrypted enable password of 'CCNA' on both devices

	> WHILE IN GLOBAL CONFIGURATION MODE:

		> "enable password CCNA" on both devices
  

3. Exit back to user EXEC mode and test the password

	> IN GLOBAL CONFIGURATION MODE

		> "exit" == same as cd ..

	> IN PRIVILEGED EXEC MODE

		> "exit" == same as cd..

	> IN USER EXEC MODE

		> hit enter
		
		> "enable" to go back to prvileged exec mode
		
		> enter password: "CCNA"
  

4. View the password in the running configuration

	  > IN PRIVILEGED EXEC MODE

		> "sh run"

5. Ensure that the current password, and all future passwords, are encrypted

	  > IN PRIVILEGED EXEC MODE

		> "conf t" to go to global configuration mode
		
	IN GLOBAL CONFIGURATION MODE

		> "service password-encryption"

6. View the password in the running configuration

	  > IN GLOBAL CONFIGURATION MODE

		> "do sh run"

7. Configure a more secure, encrypted enable password of 'Cisco' on both devices

	  > IN GLOBAL CONFIGURATION MODE

		> "enable secret Cisco"

8. Exit back to user EXEC mode and then return to privileged EXEC mode.

Which password do you have to use?

	  > secret (Cisco)

9. View the passwords in the running configuration.

What encryption type number is used for the encrypted 'enable password'?

	> 7

What encryption type number is used for the encrypted 'enable secret'?

	  > 5

10. Save the running configuration to the startup configuration

	> IN PRIVILEGED EXEC MODE

		> "write"
