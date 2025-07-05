# ethernet standards (copper)
___
### defined in the IEEE 802.3 standard in 1983

#### IEEE == institute of electrical and electronics engineers
---
> 1 byte = 8 bits
>
>1 kilobit(kb) == 1000 bits
>
> 1 megabit(mb) == 1000 000 bits
>
> 1 gigabit(gb) == 1000 000 000 bits
>
> 1 terabit(tb) == 1000 000 000 000 bits
---


| speed    | common name | IEEE standard | informal name | max cable length |
| -------- | ----------- | ------------- | ------------- | ---------------- |
|          |             |               |               |                  |
| 10 mbps  | ethernet    | 802.3i        | 10 BASE-T     | 100m             |
| 100 mbps | fast eth    | 802.3u        | 100 BASE-T    | 100m             |
| 1 gbps   | gigabit eth | 802.3ab       | 1000 BASE-T   | 100m             |
| 10 gbps  | 10 gig eth  | 802.3an       | 10G BASE-T    | 100m             |

---
BASE == baseband signal

T == twisted pair

---

below is a table/diagram(unssure what to call it) of a pc on the left and a switch on the right.

showcase once again how wires are connected within a UTP



full duplex transmission == both endpoints can send and receive data without trouble.


# UTP cables (10 base t, 100 base t)
___
## straight through cabling

> pc to switch or,
> 
>
>  router to switch or,
>
> firewall to switch)

---

| pc  | pin nr | direction of comms | pin nr | switch |
| --- | ------ | ------------------ | ------ | ------ |
| tx  | 1      | >->->->->->->->->  | 1      | RX     |
| tx  | 2      | >->->->->->->->->  | 2      | RX     |
| RX  | 3      | -<-<-<-<-<-<-<-<-  | 3      | tx     |
|     | 4      |                    | 4      |        |
|     | 5      |                    | 5      |        |
| RX  | 6      | -<-<-<-<-<-<-<-<-  | 6      | tx     |
|     | 7      |                    | 7      |        |
|     | 8      |                    | 8      |        |

---

## crossover cabling

> switch to switch
> 
> pc to pc
>
> router to router
>
> firewall to firewall

---

| pc  | pin nr | cable nr | cable nr | pin nr | pc  |
| --- | ------ | -------- | -------- | ------ | --- |
| tx  | 1      | 1        | 3        | 1      | tx  |
| tx  | 2      | 2        | 4        | 2      | tx  |
| RX  | 3      | 3        | 1        | 3      | RX  |
|     | 4      |          |          | 4      |     |
|     | 5      |          |          | 5      |     |
| RX  | 6      | 4        | 2        | 6      | RX  |
|     | 7      |          |          | 7      |     |
|     | 8      |          |          | 8      |     |

---

# TO REMEMBER


| DEVICE TYPE | TRANSMIT (TX) PINS | RECEIVE (RX) PINS |
| ----------- | ------------------ | ----------------- |
| ROUTER      | 1 AND 2            | 3 AND 6           |
| FIREWALL    | 1 AND 2            | 3 AND 6           |
| PC          | 1 AND 2            | 3 AND 6           |
| SWITCH      | 3 AND 6            | 1 AND 2           |
