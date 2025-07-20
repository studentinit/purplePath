# question:

> which field of an ethernet frame provides receiver clock synchronization?

# choices:

> preamble

> SFD

> type

> FCS
# answer:

> preamble

# why?:

> FCS(frame check sequence) is the field of a frame that checks for errors

> SFD(start frame delimiter) is the field of a frame that marks the end of the preamble tx and the signals the start of another preamble field incoming

> type is the field of a frame that shows the "type" value of a frame, not the clock sync

> preamble provides clock sync. you can see this by the alternating binary pattern(10101010) that syncronizes rx clock


# question:

> how long is the physcal address of a network device?

# choices:

> a == 32 bytes

> b == 32 bits

> c == 48 bytes

> d == 48 bits
# answer:

> d == 48 bits

# why?:

> MAC addr is 48 bits(6 bytes)


# question:

> what is the OUI of this MAC addr? E8BA.7011.2874

# choices:

> A == E8BA

> B == E8BA.70

> C == 7011

> D == E8BA.7011
# answer:

> B

# why?:

> OUI(orginizationally unique identifier) is the first half of a MAC addr. used to identify the manufacturer of a device, so E8BA.70 is the OUI.


# question:

> which field of an ethernet frame does a switch use to populate its MAC address table?

# choices:

> a == preamble 

> b == length

> c == source MAC address

> d == destination MAC addrees
# answer:

> c

# why?:

> a preamble is a section of a frame that allows receiver clock synchronization, it does not contain MAC address credentials

> length is a section in the frame that relays communication of how big the frame is that is being sent.(length of frame)

> destination MAC address is only usefull when a switch already received an tx from a end host.(if pc1 sent a packet to the switch, the the switch added pc1 MAC to its source mac address table. destination address is updated through source address first)

> a switch receives a eth frame from an end host. the tx contains a clear message (n;. source) where the the address is listed from the sender. a switch is designed to interpret "source addr" details and the add it to its own source MAC address table.


# question

> what kind of frame does a switch flood out of all interfaces except the one it was received on?
# choices

> a == unknown unicast

> b == known unicast

> d == allcast
# answer

> a

# why/;

> known unicast is an action done by a switch if it already knows where the destination MAC addr is. (if destination MAC is alredey within its MAC address table)

> allcast im not familiar with this terminology

> unknown unicast is the flood frame. (happens if switch does not know which end device has the same MAC as that of the destination MAC addr)
