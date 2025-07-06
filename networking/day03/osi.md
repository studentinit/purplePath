
### layer 7 - application
---
receptionist.

encapsulation (dispatch):

.......“I have this thing that needs to be sent. I know what to do — let me give it to the translator.”

de-encapsulation (receiving):

.......“Ah, I just received this thing from the translator. It tells me exactly what to do.”

> this layer is closest to the end user

> interacts with software applications, like your webb browser(safari, chrome, firefox etc.).

> HTTP and HTTPS are layer 7 protocols ([https]://www.cisco.com)

> functions include:
> 		identify communication partners
> 		synchronizing communication

___
### layer 6 - presentation
___
translator.

encapsulation (dispatch):

“Hmm, I just got this thing that needs to be sent, but the receiving department might not understand this gibberish… Let me make sure the language is clear.”

"Ah, it’s **HTTPS**? Then we better wrap this message in a sturdy, locked cloth bag... so no thieves can peek inside while it’s traveling.”

de-encapsulation (receiving):

“This message is locked up tight… no problem. I’ll decrypt it, unpack it, and translate it into something the receptionist can read.”

> data in the application layer is in 'application format'

> it needs to be translated to a different format t be sent over the network

> presentation layer's job is to translate between application and network formats.

> for example, encryption of data as it is sent, and decryption of data as it is received

> also translates between different application layer formats


### layer 5 - session
___
mr doorman.

encapsulation (dispatch):

“I’ll open the door because we want to send this thing... and I’ll keep it open until it’s sent.”

de-encapsulation (receiving):

“Yo, that thing is part of an ongoing delivery... you can come in.”

> controls dialogues(sessions) between communicating hosts

> establish, manage and terminate connections between the local application( for example, your web browser) and the remote application(for example, youtube)



### layer 4 transport
___
delivery man.

encapsulation (dispatch):

"I got this thing in my truck that needs to be delivered — let’s get moving!”

de-encapsulation (receiving):

"The thing has survived the travel — time to drop it off!”

> segments and reassembles data for comms between hosts

> break large data pieces into smaller segments that can be sent more easily or the network(less likely to cause tansmission problem if error == true)

> provide host to host comms (end to end communication)



### layer 3 - network
___
map man.

encapsulation (dispatch):

“Alright, I know where this thing needs to go — let me figure out the best path and write the address on it.”

de-encapsulation (receiving):

“This thing just arrived at my stop — time to pass the bucket toward its final destination.”

> provide cennectivity between end hosts on differen networks(outside LAN)

> provide logical addressing(IP address)

> provide path selection between source and destination

> routers are on layer 3

> packet == |DATA |L4 header |L3 header |

### layer 2 - data link
___
quality checker & coordinator.

encapsulation (dispatch):

“Let me wrap this data into a neat package, slap on the local address label, and check it’s all in order before it leaves.”

de-encapsulation (receiving):

“Package received!... label looks good and no damage detected, I’ll pass it up to the map man.”

> provide node-to-node connectivity and data transfer(pc to switch, switch to router, router to router)

> defines how data is formatted for transmission over a physical medium(copper UTP)

> detect and (possibly) corrects physical layer errors

> uses layer 2 addressing(MAC address)

> switches operate on layer 2

> frame == |L2 trailer |DATA |L4 header |L3 header |L2 header |


### layer 1 - physical
___
electrician.

encapsulation (dispatch):

“I’ll turn these bits into electrical signals (or light pulses, radio waves), and send them down the wire or through the air.”

de-encapsulation (receiving):

“got a signal!... I’ll convert the electrical pulses back into bits and pass them up to the quality checker & coordinator.”

> defines physical characteristics of the medium used to transfer data between devices

> for example, voltage levels, max transmission distance, physical connectors, cable specs etc etc

> wired connection == digital bits are converted into electrical signals

> wireless connection == digital bits are converted into radio signals

___
here we have 2 pcs interacting with eachother. the software app, maybe a webb app, interacts with all the layers

this is called same-layer interaction

| layer name     | encapsulation                                                  | de-encapsulation                                               | layer name     |
| -------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------- |
|                |                                                                |                                                                |                |
| 7 application  | v \|DATA \| v                                                  | ^ \|DATA \| ^                                                  | 7 application  |
| 6 presentation | v \|DATA \| v                                                  | ^ \|DATA \| ^                                                  | 6 presentation |
| 5 session      | v \|DATA \| v                                                  | ^ \|DATA \| ^                                                  | 5 session      |
| 4 transport    | v \|DATA \|L4 header \| v                                      | ^ \|DATA \|L4 header \| ^                                      | 4 transport    |
| 3 network      | v \|DATA \|L4 header \|L3 header \| v                          | ^ \|DATA \|L4 header \|L3 header \| ^                          | 3 network      |
| 2 data link    | v \|L2 trailer \|DATA \|L4 header \|L3 header \|L2 header \| v | ^ \|L2 trailer \|DATA \|L4 header \|L3 header \|L2 header \| ^ | 2 data link    |
| 1 physical     | ->->->->->->                                                   | ->->->->->->                                                   | 1 physical     |


---
# PDUs

---
protocol data units

\|DATA \| == data (layer 5 PDU)

\|DATA \|L4 header \| == segment (layer 4 PDU)

\|DATA \|L4 header \|L3 header \| == packet (layer 3 PDU)

\|L2 trailer \|DATA \|L4 header \|L3 header \|L2 header \| == frame (layer 2 PDU)

BIT == layer 1 PDU)
