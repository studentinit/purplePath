# MAC addresses
___

> 6 bute (48 bit) physical address assigned to a device at the factory

> AKA BIA (burned-in address)

> globally unique

> OUI (organizationally unique identifier) == first 3 bytes

> OUI is used to identify manufacturers

> last 3 bytes are used to uniquely identify the device itself

> MAC addresses are written in 12 hexadecimal chars

		> decimal == 0 1 2 3 4 5 6 7 8 9 (10 possible chars)
		
		> hexadecimal == 0 1 2 3 4 5 6 7 8 9 A B C D E F (16 possible chars)
		

---

| dec | hex |     | dec | hex | etc |
| --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | v   |
| 0   | 0   |     | 17  | 11  |     |
| 1   | 1   |     | 18  | 12  |     |
| 2   | 2   |     | 19  | 13  |     |
| 3   | 3   |     | 20  | 14  |     |
| 4   | 4   |     | 21  | 15  |     |
| 5   | 5   |     | 22  | 16  |     |
| 6   | 6   |     | 23  | 17  |     |
| 7   | 7   |     | 24  | 18  |     |
| 8   | 8   |     | 25  | 19  |     |
| 9   | 9   |     | 26  | 1A  |     |
| 10  | A   |     | 27  | 1B  |     |
| 11  | B   |     | 28  | 1C  |     |
| 12  | C   |     | 29  | 1D  |     |
| 13  | D   |     | 30  | 1E  |     |
| 14  | E   |     | 31  | 1F  |     |
| 15  | F   |     | 32  | 20  |     |
| 16  | 10  |     | 33  | 21  |     |

---
## UNICAST FRAME

a frame destined for a single target

below is an illustration of a LAN consisting of 3 computers and a switch


```
(PC1)                        (PC2)
MAC:                         MAC:
AA.AA.AA.00.00.01            AA.AA.AA.00.00.02
	|                            |
	|                            |
	----->      SWITCH      <-----
	FO/1                        FO/2
	              ^
	              |  FO/3
	              |  
	            (PC3)
	            MAC:
	            AA.AA.AA.00.00.03    

```

### MAC STRUCTURE
---

> AA.AA.AA == OUI (organizationally unique identifier)

 	> we can see all 3 PCs are made by same company

> 00.00.01 == PC1 global unique identifier

> 00.00.02 == PC2 global unique identifier

> 00.00.03 == PC3 global unique identifier

---

### cables and interfaces(ports)
---

> FO/1 == PC1 (via fastETH cable) connected on switch port 1

> F0/2 = PC2 (via fastETH cable) connected on switch port 2

> F0/3 = PC3 (via fastETH cable) connected on switch port 3

#### pc1 send -> pc2

> source: pc1  
> tx via F0/1  
> frame first stop: switch

	> switch RX (receives frame)  
	> learns pc1's MAC address  
	> associates pc1's MAC with F0/1 port  
 
		> stored as a dynamic MAC address  
  
	> switch checks the destination MAC address in the frame  
 
		> destination still unknown at this point  
		> this is known as an "unknown unicast frame"  
  
	> switch floods the frame out of all ports **except** the one it was received on  
 
		> uses standard Ethernet flooding (not ARP)  
		> host with matching MAC receives the frame  
		> hosts with different MACs drop the frame silently  

destination: pc2  
> RX via F0/2  
> processes the frame, following the OSI model (L2 → L7)  
> switch does not receive a frame *back* from pc2 at this point  
> therefore, switch has not yet learned pc2's MAC

	> if pc2 wants to transmit:  
 
		> pc2 TX → F0/2 → switch RX  
		> switch learns pc2's MAC and associates it with F0/2  
		> if destination = pc1  
  
			> this is a **known unicast frame**  
			> no flood needed  
			> switch forwards only to F0/1  
   
		> elif destination = pc3  
  
			> pc3’s MAC is still unknown to the switch  
			> switch floods the frame (unknown unicast again)

### Unknown Unicast Frame 
___
    > The switch doesn't yet know the destination MAC address  
    > **Action:** **Flood** the frame out of all ports except the one it was received on
    
### Known Unicast Frame
___
    > The switch has a MAC address table entry for the destination  
    > **Action:** **Forward** the frame only out of the correct port (no flooding)
    
### Dynamic MAC Address Aging (Cisco default)
___
    > **"DYNAMIC MAC ADDRESSES ARE REMOVED FROM THE MAC ADDRESS TABLE AFTER 5 MINUTES OF INACTIVITY"**  
    > This prevents the table from filling up with stale entries  
    > You can verify or change this with:

    
    Switch# show mac address-table aging-time 
    
    Switch(config)# mac address-table aging-time 600`
