inux]]
sudo == super user do

	- can run cmd as admin

cli == cmd line interface

gui == graphical user interface

pw cracking:

	art == finding the right wordlist
	
	science == software or tools used

(-) for letters

(--) for words

| whoami                                                                              | username                                                                                            |     |
| ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --- |
| hostname                                                                            | hostname                                                                                            |     |
| clear                                                                               | clear terminal                                                                                      |     |
| sudo whoami                                                                         | root(name of sudo account)                                                                          |     |
| sudo apt update                          \|                                         | update sys                                                                                          |     |
| sudo apt upgrade                        \|                                          | upgrade sys                                                                                         |     |
| sudo apt update && sudo apt    \|    upgrade                                      < | update and upgrade at once                                                                          |     |
| cd                                                                                  | change dir (relative or full path)                                                                  |     |
| pwd                                                                                 | print current dir                                                                                   |     |
| ls                                                                                  | list current dir contents                                                                           |     |
| ls -l                                                                               | same as ls but can see more info like permissions                                                   |     |
| ls -la                                                                              | show hidden dirs also                                                                               |     |
| cd ..                                                                               | take a step back to previous dir(do this enough and youll end up at /)                              |     |
| aircrack-ng --help                                                                  | help using flags                                                                                    |     |
| nmap -h                                                                             | help using nmap                                                                                     |     |
| man nmap                                                                            | user manual (more depth)                                                                            |     |
| locate aircrack-ng                                                                  | locate str by filtering through entire sys                                                          |     |
| whereis aircrack-ng                                                                 | use binaries to locate and not str matching                                                         |     |
| echo $PATH                                                                          | show all dirs sys filters through                                                                   |     |
| which aircrack-ng                                                                   | show dir to locate tool among PATH variable                                                         |     |
| locate wordlists                                                                    | ocate wordlists on your  sys                                                                        |     |
| find / -type f -name apache2                                                        | find all filetypes related to apache2                                                               |     |
| sudo find / -type f -name apache2                                                   | same but allows more permission                                                                     |     |
| man find                                                                            | user ,anual for find                                                                                |     |
| ps aux \| grep burp                                                                 | (ps aux)= locate all processes, (\|)= pipe to grep followed by keyword. [like past parsing scripts] |     |
|                                                                                     |                                                                                                     |     |

