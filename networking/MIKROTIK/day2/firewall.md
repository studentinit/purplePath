
# **7 firewall rules to practice (input chain)**
___
These go under:  
`IP > Firewall > Filter Rules > Input Chain`

| Priority                                   | Rule                                                         |
| ------------------------------------------ | ------------------------------------------------------------ |
|                                            |                                                              |
| 1                                          | **Accept Established/Related**                               |
| → Chain: `input`                           |                                                              |
| → Connection State: `established, related` | Keeps active and expected connections working                |
|                                            |                                                              |
| 2                                          | **Drop Invalid**                                             |
| → Chain: `input`                           |                                                              |
| → Connection State: `invalid`              |                                                              |
| → Action: `drop`                           | Stops corrupted or suspicious packets                        |
|                                            |                                                              |
| 3                                          | **Accept ICMP from LAN**                                     |
| → Chain: `input`                           |                                                              |
| → Protocol: `icmp`                         |                                                              |
| → Src. Address: `192.168.88.0/24`          |                                                              |
| → Action: `accept`                         | Allows ping/troubleshooting inside LAN                       |
|                                            |                                                              |
| 4                                          | **Drop ICMP from WAN**                                       |
| → Chain: `input`                           |                                                              |
| → Protocol: `icmp`                         |                                                              |
| → In Interface List: `WAN`                 |                                                              |
| → Action: `drop`                           | Prevents ping/scan from internet                             |
|                                            |                                                              |
| 5                                          | **Accept Config Access from LAN**                            |
| → Chain: `input`                           |                                                              |
| → Protocol: `tcp`                          |                                                              |
| → Port: `8291` (Winbox), `80` (WebFig)     |                                                              |
| → In Interface List: `LAN`                 |                                                              |
| → Action: `accept`                         | Allows router access only from trusted LAN                   |
|                                            |                                                              |
| 6                                          | **Log Dropped Attempts**                                     |
| → Chain: `input`                           |                                                              |
| → Action: `log`                            |                                                              |
| → Prefix: `"Blocked Input"`                |                                                              |
| → Place below Rule 6                       | Lets you _see_ what's being blocked (for training/debugging) |
|                                            |                                                              |
| 7                                          | **Drop All Other Input Traffic**                             |
| → Chain: `input`                           |                                                              |
| → Action: `drop`                           | Denies anything not explicitly allowed                       |

---
## important ! ! ! !
> keep in mind that firewall rules in mikrotik are followed from top to bottom, so your rule1 will be followed before rule2. so keep in mind that when doin specific tasks like voip where udp traffic is sent to specified ports and port ranges, or certain LAN devices are set for specific tasks, it should be placed above the catch-all.

> it is a good idea to have a catch all rule placed after specific drop/accept rules in general. like a final safety net

___
## why these are a good starting point

> 1 == allows expected connections to be established AND keep those connections open

> 2 == if an unwanted connection is requesting to be linked, it is blocked immediately(like an explicid rule that covers the "what if" condition opposite of rule 1)

> 3 == allow link between devices within the LAN that has been setup. easy to control LAN devices compared to WAN

> 4 == drop link requests from WAN(again, like the rule that covers the opposite situation of rule 3)

> 5 == allows configuration access from LAN. this is (again) simpler to control who can access the "back door" of the router

> 6 == its al logger. i personally like visibility and you should too. no one wants to run around in the dark

> 7 == this rule is designed/config as a "catch all" of sorts. a protection layer for the general "exceptions"

