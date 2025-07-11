eth LAN switching

involves layer 1(physical and layer 2(data link) of the osi model




| LAN1    |        |         |        |        |          |     |
| ------- | ------ | ------- | ------ | ------ | -------- | --- |
| PC1     | ->->-> | SWITCH1 | ->->-> | ROUTER |          |     |
|         |        | ^       |        | v      |          |     |
| PC2     | ->->-> | ^       |        | v      |          |     |
|         |        |         |        | ->->-> | V        |     |
|         |        |         |        |        | V        |     |
| LAN2    |        |         |        |        |          |     |
| pc1     | ->->-> | v       |        |        | INTERNET |     |
|         |        | v       |        |        | ^        |     |
| PC2     | ->->-> | SWITCH1 |        | ->->-> | ^        |     |
|         |        | v^      |        | ^      |          |     |
|         |        | v^      |        | ^      |          |     |
| PRINTER | ->->-> | SWITCH2 | ->->-> | ROUTER |          |     |
|         |        | ^       |        |        |          |     |
| PC3     | ->->-> | ^       |        |        |          |     |

---
# PDU REVISION

DATA == DATA

SEGMENT == DATA + L4 HEADER

PACKET == DATA + L4 HEADER + L3 HEADER

FRAME == L2 TRAILER + DATA + L4 HEADER + L3 HEADER + L2 HEADER

---
 
 the following will focus on how switches tx and RX frames (specific to eth)
 ----
structure


| eth header  | byte amnt | packet | eth trailer | byte amnt |
| ----------- | --------- | ------ | ----------- | --------- |
| v           |           |        | v           |           |
| preamble    | 7         |        | fcs         | 4         |
| v           |           |        |             |           |
| sfd         | 1         |        |             |           |
| v           |           |        |             |           |
| destination | 6         |        |             |           |
| v           |           |        |             |           |
| source      | 6         |        |             |           |
| v           |           |        |             |           |
| type        | 2         |        |             |           |


#### eth header

preamble == used (together with SFD) for synchronization and prepare the RX device to receive the rest of the data within the frame

SFD(start frame delimiter) == used (together with preamble) for synchronization and prepare the RX device to receive the rest of the data within the frame

destination == the layer 2 address of the RX device

source == the layer 2 address of the tx device

type == indicates the layer 3 protocol used in the encapsulated packet(almost always ipv4/ipv6). BUT sometimes it is a length field of the encapsulated data, depending on the version of eth being used.

		f it's **small** → it's probably **Length** 
		 
		If it's **hex** and **starts with 08 or 86** → it's probably a **Type**  
		
		Ethernet II is what you’ll see **99% of the time today**


#### eth trailer

FCS (Frame Check Sequence) == used by RX device to detect any errors that might have occurred in transmission

---
# more on header
---
### preamble

| 7 bytes                             | (56 bits) |
| ----------------------------------- | --------- |

| pattern == alternating 1s and 0s    | (101010)  |
| ----------------------------------- | --------- |

> allows devices to synchronize their receiver clocks, to ensure they're ready to receive the rest of the frame and the data inside the frame

---
### SFD (start frame delimiter)

| 1 byte               | (8 bits) |
| -------------------- | -------- |

| pattern ==           | 10101011 |
| -------------------- | -------- |

> markss the end of the preamble and the beginning of the rest of the frame

---
### destination + source

> indicate the devices sending and receiving the frame

> consist of the destination and source MAC addr

> MAC == media access control

> MAC == 6 byte (48 bit) address of the physical device

> mac addr is like the device's id number and the ip addr is like a driver licence number

### type OR length

> 2 byte (16 bits) field

> a value of 1500 or less in this field indicates the LENGTH of the encapsulated packet (in bytes)

> a value of 1536 or more in this field indicates the TYPE of the encapsulated packet(ipv4/ipv6) and the length is determined via other methods


---
# more on trailer
---

### FCS (frame check sequence)

> 4 bytes (32 bits) in length

> purpose:

			detect corrupt data by running "CRC" algorithm over the received data

> CRC == cyclic redundency check

	> cyclic refers to cyclic codes (to learn more)
	> redundancy refers these 4 bytes at the end of the msg enlarge the msg without adding new data/info.
	> check refers to checking/verify data for errors
