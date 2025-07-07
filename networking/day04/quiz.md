
# question

> what type of cable is used to connect to a cisco device via the RJ45 console port?

### choices
> rollover cable

> crossover cable

> USB cable

### answer
> a

### why
> although USB can be used can be used to connect different devices together, it is more to do with computers. also, the console port has a usb port as weel, however, this is for a specific usb called the USB mini-B 

> a crossover cable is used to connect many different end hosts of the same type. (router to router, pc to pc... but not switch to switch). it has an RJ45 connecter on each end of the cable and is used for ethernet connection, not console connection. (used for data tx/RX)

> a rollover cable has an RJ45 connecter on one end, and a DB9 connecter on the other end. (modern cables use adapters due to limited DB9 ports on modern end hosts) this cable is used on the console port. for acces, not data tx/RX

---
# question
> you type "enable" to enter privileged exec mode on your cisco router, however the password you enter is not accepted.

> what could be the problem?

### choices
> a == "service password-encryption" is enabled

> b == "service password-encryption" is disabled

> c == caps lock is on

### answer
> c

### why
> if "service password-encryption" is enabled, it does not affect the the type errors that can occur. it only encrypts the password for security reasons (in "sh run conf")

> if "service password-encryption"  is disabled, it only prevents future password to be encrypted(leaving future passwords in plain txt) while viewing configuration(sh run conf)

> if caps lock is on, and the password has lowercase letters, the password will not be accepted due to cisco password being case-sensitive by default

---
# question

> what is the most secure method to protect acces to privileged exec mode?
### choices
> a == the "enable secret" cmd

> b == the "enable password" cmd

> c == the "enable password" cmd + "service password-encryption"

### answer
> a

### why
> "enable password" sets a password to access privileged exec mode but does not encrypt it, leaving it to be viewed in config as plain text

> "enable password" cmd + "service password-encryption" is a safer option but ("service password-encryption") uses MD7 encryption. this type of encryption is easily cracked by simply doing a quick search online. (maybe it is an old encryption type)

> "enable secret" sets up a password for acces, just like "enable password", but encrypts the password automatically. no need for additional security-based commands. it is also important to keep in mind that this cmd uses MD5 encryption method. possiby a newer type that MD7, and is harder to crack than MD7.



---
# question
> if both the "enable password" and the "enable secret" command are configured, what will happen when you use "enable" to enter privileged exec mode?

### choices
> a == you must enter the "enable password" pwd, followed by the "enable secret" pwd

> b == you must enter the "enable password" only

> c == you must enter the "enable secret" only
### answer
> c

### why
> "enable password" pwd must only be typed if secret is not configured

> entering both is not necissary (sys prioritize stronger protection and ignore weaker security)

> "enable secret" pwd must be typed regardless if other security commands are configured. maybe secret is the first line of defence cause the sys knows it is the strongest


---
# question
> you enter the "conf t" command to enter global configuration mode.

> what is the full length of the command?

### choices
> a == configuration time

> b == configure terminal

> c == configuration terminal

### answer
> c

### why
> "configuration time" does not exist

> "configure terminal" is the full len of "conf t" and will take you to global configuration mode. (it is a command)

> "configuration terminal" is not a command. configuration is a process.
