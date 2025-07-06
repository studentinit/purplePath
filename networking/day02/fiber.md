instead of RJ45 ports that is used with eth, we use sfp ports.

SFP == small form-factor pluggable

sfp tranceiver in plugged in an sfp port. some sfp tranceivers support fiver cables. (think of it as an adaptor of sorts that can be used on switches, router etc etc).


fiber's connection in terms of wiring seems a bit more straight forward.

instead of using copper wires to transmit data via electical currents like with eth, fiber uses glas and plastic to reflect light withing the cable.

it is with this light, that data is being transferred via reflection.







# fibet optic connection
___


| host | connector | direction | connector | host |
| ---- | --------- | --------- | --------- | ---- |
| tx   | 1         | >->->->-  | 1         | RX   |
| RX   | 2         | -<-<-<-<  | 2         | tx   |


### cable structure:
___

4 layers ==
> 1 == smalles / centre
>
>     fiberglass core
> 
>     light is transmitted down the core to transmit data from device to device
>
> 2 == cladding (wrapped around core)
>
>     reflects light
> 
> 3 == protective buffer
>
>     protect fibreglass from breaking
> 
> 4 == outer jacket of cable
>
>     further protection


## multimode fiber
___
> core diameter is wider than single mode fiber
> 
> allows multiple angles(modes) of light to enter the fiberglass core
> 
> allows longer cable length than UTP(eth), but still ahorter cables than single mode fiber
>
> cheaper than single mode fiber cables (due to cheaper LED-based SFP transmitters).

in short.
> it costs less to make these cables than to make single mode fiber cables cause the core is not as thin as single mode.

---

## single mode fiber
___
>core diameter is narrower than multimode fiber 
>
>light enters at a single angle(mode) from a laser-based transmiter
>
> allows longer cables than both UTP and multimode fiber cables
>
> more expensive than multimode (due to more expensive laser-based SFP transmitters)

---

## fiber-optic cable standards
___



| INFORMAL NAME | IEEE STANDARD | SPEED   | CABLE TYPE               | MAX CABLE LENGTH  |
| ------------- | ------------- | ------- | ------------------------ | ----------------- |
| 1000 BASE-LX  | 802.3z        | 1 gbps  | multimode or single mode | 550m(MM), 5km(SM) |
| 10G BASE-SR   | 802.3ae       | 10 gbps | multimode                | 400m              |
| 10G BASE-LR   | 802.3ae       | 10 gbps | single mode              | 10km              |
| 10G BASE-ER   | 802.3ae       | 10 gbps | single mode              | 30km              |

---


# utp vs fiber cables
___


| UTP                                                                               | FIBER                                                                                      |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| lower cost                                                                        | expensive                                                                                  |
| shorter distance cabling(100m max)                                                | longer max distance                                                                        |
| vuln to electromagnetic interference(EMI)                                         | no EMI vuln                                                                                |
| RJ45 ports used with UTP are cheaper than SFP ports                               | SFP ports are more expensive than RJ45 ports. multimode == more expensive than single mode |
| emit/leak a faint signal outside of the cable, which can be copied(security risk) | no leak outside cable. no known security risk                                              |
| still more accessable on hardware(more built-in ports) than fiber?... for now     |                                                                                            |

