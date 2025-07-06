
# question
> http data sent from a youtube web server is displayed via yor web browser.

> this is an example of what?

### choices:
> a == adjacent-layer ineraction

> b == same-layer interaction

> c == encapsulation

> d == de-encapsulation

### answer
> b

### why?:
> adjacent-layer interaction happens ONLY inside one device, between layers directly **above or below** each other (like Layer 7 -> Layer 6 -> Layer 5). DOES NOT INVOLVE 2 DEVICES ALKING TO EACHOTHER

> encapsulation is the process of a sender packaging data to send to a receiver, (describes only the 1st half of the communication process(dispatch))

> de-encapsulation is the process of "unpacking" the data, for an end host to understand the data it has received, (describes only the 2nd half of the communication process(receiving))

> same-layer interaction is when 2 devices "talk" to eachother on the same layer(in this case it is application via web browser)

___
# question

> http data has been encapsulated with three separate headers and one trailer.

> what is the appropriate name for the PDU?

### coices:
> a == packet

> b == segment

> c == frame

> D == data

### answer
> c

### why?

> packet == L4 header + L3 header

> segment == L4 header + data

> data == not yet encapsulated

> frame == L2 trailer, data, L4 header, L3 header, L2 header. this is then passed to layer 1(physical), where the frame is converted into bits, which can be transferred.

---
# question
> which layers of the osi model are most relevent to a network engineer?

### choices
> a == transport - network - data link - physical

> b == transport - network - data link

> c == network only

> application - presentation - session
### answer
> a


### why?:
> b (layers 2 - 4 of the osi model) are relevent to network engineers byt layer 1(physical) is missing. thats 25% of the job missing... not ideal.

> c (layer 3 of osi model) is relevent to network engineers but this only covers navigation(internet addressing)

> d (layers 5 - 7 of osi) covers software functions, internal data translation, and communication time. this will typically be decided/designed by software developers via scripts. (what does my computer do with something that is received and how do i send it.) it is not the send and receive process itself
> 
> a (layer 1-4 for the osi model) refers to the transmition and reception of data(communication between devices)

---

# question
> the link layer of the tcp/ip model is equal to what layer/s of the osi model?

### choices
> a == transport - network

> b == network - data link

> c == data link

> d == data link - physical

### answer
> d


### why?:
> a == internet and transport layers on tcp/ip model(separately)

> b == internet and half of link on the tcp/ip model(separately)

> c == half of link on the tcp/ip model

> d == the correct combo

---
# question
> which layer of the osi model provides host-to-host communications?

(to review again)
### choices
> application

> network

> transport

> data link

### answer 
> transport

### why
> application is for process to process comms. its about what does the data man and do, what is the process of the data(not how the data is transported between hosts)... [what process does the data follow/do]

> network refers to navigation to internet addresses (like pointing in the direction that the connection should be established and not connecting itself)... [where is the host that needs the data or where is the data coming from]

> data link serves as a "packager" of data and a package reviewer of data. (check if data is correct that is being communicated, not functioning as a communicator)... [is data in correct order/packaging to send and receive?]

> transport layer is the one that ships data from device to device... [i know where, the host is, lets send the data]
