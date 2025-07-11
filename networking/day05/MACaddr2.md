# 2 switch illustration
___

lets say you have 2 switches connected to eachother via eth

> switch1 has pc1 + pc2 connected via eth ports

> switch2 has pc3 + pc4 connected via eth ports


```
       (PC1)                        (PC3)
       MAC:                         MAC:
       AA.AA.AA.00.00.01            AA.AA.AA.00.00.02
          |                            |
          | FO/1                       | FO/1 
          v                            v
-------            F0/3         F0/3              -------
|LAN 1|   SWITCH <-------------------> SWITCH     |LAN 2|
-------                                           -------
          ^                            ^
          | FO/2                       | FO/2 
          |                            |
       AA.AA.AA.00.00.01            AA.AA.AA.00.00.02
       MAC:                         MAC:
       (PC2)                        (PC4)
 
```


### pc1 tx -> pc3 RX

pc1 send frame via FO/1

	> sw1 receive frame
		> associate pc1 MAC with FO/1 port (on sw1 MAC addr table)
		> does not know where destination is (unknown unicast frame)
		> floods frame through all ports (exl F0/1)
		> PC2 drops frame
			> BECAUSE MAC addr is different from frame destination addr

		> sw2 floods frame through all ports (exl F0/3) (unknown unicast frame)
		> PC4 drops frame
			> BECAUSE MAC addr is different from frame destination
			
		> PC 3 accepts frame
			> processes frame via OSI layers 2 - 7

### pc3 tx -> pc1 RX

pc3 send frame via FO/1

	
	> sw2 receive frame
		> associate pc3 MAC with FO/1 port (on sw2 MAC addr table)
		> knows destination is with sw1 (known unicast frame)
		> forwards frame through F0/3 to sw1
		> PC4 receives nothing
			> BECAUSE sw2 knows pc1 MAC addr is with sw1

		> sw1 forwards frame through port F0/1 (known unicast frame)
		> PC2 drops frame
			> BECAUSE sw1 knows pc1 MAC addr is with F0/1
			
		> PC1 accepts frame
			> processes frame via OSI layers 2 - 7

