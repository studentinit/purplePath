this is complimentary to the hand-on notes via packet tracer


intro to cisco ios

cli == command line interface

the interface you use to config cisco devices

how to connect to a cisco device to config it with cli?

console port is an option

console port == RJ45 and/or usb mini-B ports. (depending on make and model of the hardware)

when you first configure a device, you have to connect via console port.

what cabble to use?

rollover cable == 1 end is RJ45 conneter and the other end is a DB9 connecter.

modern laptops need a adaptor for the db9 side

similar to a crossover cable, the rollover cable also does not connect same pins to eachother.


| DB9    | cable nr | cable nr | RJ45   |
| ------ | -------- | -------- | ------ |
| pin nr |          |          | pin nr |
|        |          |          |        |
| 1      | 1        | 8        | 1      |
| 2      | 2        | 7        | 2      |
| 3      | 3        | 6        | 3      |
| 4      | 4        | 5        | 4      |
| 5      | 5        | 4        | 5      |
| 6      | 6        | 3        | 6      |
| 7      | 7        | 2        | 7      |
| 8      | 8        | 1        | 8      |


as you can see, its a total oppesite connection of pins

---
once your computer is connected to the device via cable, you will need a terminal emulator like PuTTy (to actually access the CLI)

select serial, click open, and you should be connected to the CLI.

default settings should allow connection, but it is still wise to learn how to navigate the emulator settings

---
#### default settings 

baud == speed 9600

8 data bits == data

1 stop bit == 1 bit to mark the end of a transmission(like a pause between sentences)

none parity == used to detect errors

none flow control == control flow of data between tx and RX

---

once you connect, the shell will ask if you want to enter the initial config dialog

> answer no

> press enter to get started

> now you are free to enter commands

once you are granted access, the default mode is:

> user exec mode 
> 
> ">" next to hostname indicates user exec mode
> 
> user exec mode (aka user mode) is limited


| allowed cmd for exec mode ">" |                                     |
| ----------------------------- | ----------------------------------- |
| <1-99>                        | session number to resume            |
| connect                       | open a terminal connection          |
| disable                       | privileged commands = off           |
| disconnect                    | disconnect a existing connection    |
| enable                        | privileged commands = on            |
| exit                          | exit exec mode                      |
| logout                        | exit exec mode                      |
| ping                          | echo message = send                 |
| resume                        | resume active connection            |
| show                          | sh running sys info                 |
| ssh                           | open secure shell client connection |
| telnet                        | open telnet connection              |
| terminal                      | set terminal line parameters        |
| traceroute                    | trace route to destination          |

---
to move to a mode with more power/priveledges:

> "enable" will move you to privileged exec mode.

> here you can view with complete access the device configuration

> cannot make changes to configuration yet

> "#" next to hostname indicates privileged exec mode



| allowed cmd for privileged | exec mode "#"                                  |
| -------------------------- | ---------------------------------------------- |
|                            |                                                |
| <1-99>                     | session number to resume                       |
| connect                    | open a terminal connection                     |
| disable                    | privileged commands = off                      |
| disconnect                 | disconnect a existing connection               |
| enable                     | privileged commands = on                       |
| exit                       | exit exec mode                                 |
| logout                     | exit exec mode                                 |
| ping                       | echo message = send                            |
| resume                     | resume active connection                       |
| show                       | sh running sys info                            |
| ssh                        | open secure shell client connection            |
| telnet                     | open telnet connection                         |
| terminal                   | set terminal line parameters                   |
| traceroute                 | trace route to destination                     |
|                            |                                                |
| extra stuff                |                                                |
|                            |                                                |
| auto                       | exec level automation                          |
| clock                      | manage sys clock                               |
| **configure terminal**     | enter global configuration mode                |
| **copy**                   | copy files (e.g., running-config to startup)   |
| **debug**                  | show real-time system events (use carefully)   |
| **disable**                | exit privileged mode, return to user EXEC      |
| **enable**                 | re-enter privileged mode (if logged out)       |
| **erase**                  | erase saved configs or flash memory            |
| **reload**                 | reboot the device                              |
| **show**                   | view system, interface, and config details     |
| **write**                  | save current config to startup-config          |
| **ping / traceroute**      | test network reachability                      |
| **telnet / ssh**           | open remote CLI sessions                       |
| **terminal**               | change terminal settings (e.g., length, width) |
| **clear**                  | reset or clear statistics (like counters)      |
| **debug / undebug**        | start/stop real-time debugging output          |

---

to enter a mode with more privileges:
> configure terminal (conf t)

> "conf t" == global configuration mode

> here you have permission to make changes to the configuration itself

> "<hostname>(config)#" is the flags that show you are in this mode

