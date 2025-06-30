
[[tools]]

| flag | purpose         | description                                                                                                                               | sidenote                                                                    |
| ---- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
|      |                 |                                                                                                                                           |                                                                             |
| -sS  | SYN scan        | send syn pkgs without completing the tcp handshake.faster cause not fully connecting, stealthier cause ip not logged by internet provider | can still be seen by blue team if they use something as simple as wireshark |
| -sT  | tcp connect     | perform full tcp handshake. used if SYN not possible (eg. not raw socket access)                                                          | also one of the most basic and helpfull flags there is                      |
| -sU  | udp scan        | look for open udp ports                                                                                                                   | slow and noisy                                                              |
| -sV  | service version | probes ports to get service and version info of each                                                                                      |                                                                             |
| -O   | OS detect       | try identify oparating sys of target                                                                                                      |                                                                             |
| -A   | aggro           | combines -O, -sV + traceroute and script scanning                                                                                         | noisy but effective                                                         |
| -p   | specify ports   | use to specify specific port targets (eg. -p 22, 80) or range (eg. -p 1-100)                                                              | area specific(if you will)                                                  |
| -p-  | all ports       | scan all 65 535 ports                                                                                                                     | broad area                                                                  |
| -Pn  | no ping         | treat all hosts as online. used when ICMP(ping) is blocked by firewalls                                                                   | skip host discovery                                                         |
| -oX  | output to XML   | save scan report in a machine-readable XML format. (eg. -oX scan.xml)                                                                     | step 1 of parse pipe                                                        |

# typical commands
___
## --SYN SCAN--
### nmap -sS "target"
- yes it is stealthy in a way that your ip wont be logged by the service provider, but your ip is still visible with basic listening tools

## --AGGRESSIVE SCAN(os+version+script)--
### nmap -A "target"
- effective but noisy

## --SERVICE VERSION ON SPECIFIC PORTS--
### nmap -sV -p 21,80,102 "target"
- nmap will make a best guess on services.(can make mistakes)
- can put -p flag at end

## --SCAN ALL PORTS WITH NO PING--
### nmap -p- -Pn "target"
- will take long, also ignores "drop-ping" action if enabled on specific ports

## --EXPORT XML RESULT--
### nmap -sS -oX "file"xml "target"
