# question

> you connect two old routers together with a UTP cable, however data is not successfully sent and received between them.
>
> what could be the probleM?


### coices

> a == they are connected with a straight though cable

> b == they are connected with a crossover cable

> c == they are operating in auto MDI-X mode


### answer
> a


### why?:
> auto mdi-x should enable automatic configuration on which oins tx and which pins RX (modern hardware(modern routers would likely not have this problem))

> crossover cables should allow two routers to send and receive data similtaniously 

> straight through cables only ork when a switch is connected to a router, not a router to another router(especially with old hardware, in this case, old routers)


___
# question

> your company wants to connect switches in two separate buildings that are about 150m apart.

> they want to keep costs down, if possible.

> what kind of cable should they use?


### coices:

> UTP

> single mode fiber

> multimode fiber

### answer
> multimode fiber


### why?:

> UTP has max cable length of 100m before signal starts degrading

> single mode fiber can support the desired distance, BUT more expensive than multimode fiber

> multimode fiber is the choice that can achieve the desired cable distance without signal decline, and is cheaper than sheaper than single mode fiber


___
# question
> your company wants to connect two offices that are about 3km apart.

> they want to keep costs down if possible.

> which kind of cable should they choose?

### choices
> UTP

> single mode fiber

> multimode fiber

### answer:
> single mode fiber

### why?
> UTP cannot achieve the distance

> multimode cannot achieve the distance

> single mode == expensive, but in this case it is the only option that fits the requirements. so it is not possible to keep costs down.


___
# question
> a switch has the following indication over its network interfaces(ports)

> what would happen if you connect it to an identical switch with a straight through cable?

> [10/100/1000BASE-T ports (1 - 24) -- ports are auto-MDIX]
### choices
> a == the would oparate normally

> b == they would operate at a reduced speed

> c == they would be unable to communicate

### answer
> a

### why?:
> cause on the switch it states that ports 1 - 24 supports 10base-t, 100 base-t, 1000 base-t cables AND it is auto MDIX, which means it is modern hardware that can automatically configure which pins tx and which pins RX.

> they wont operate at a reduced speed due to MDIX, and if they did not support auto MDIX, the switches simply would not work instead of operaing at a reduced speed.


___
# question
> your company needs to connect many end hosts to a switch, which is in a wiring cabinet on the same office floor as the hosts.

> what kind of cable should be used?

### coices
> UTP

> single mode fiber

> multimode fiber

### answer
> UTP

### why
> single mode fiber uses SFP ports, switches do not support enough SFP ports to support many connection to a single switch(not to mention the cost )

> multimode fiber also use SFP ports to connect to a switch, again, a single switch do not support enough SFP ports

> UTP uses RJ45 ports on the switch. for now, switches are desighed to accomadate many RJ45 connections by default cause of many RJ45 ports.
