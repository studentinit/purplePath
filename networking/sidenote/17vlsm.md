[[network]]

# VLSM (variable length subnet masking)
___
# orgnl
___
decimal:

> ip = 172.21.42.0/24

> (172.21.42.0 - 172.21.42.255)

> netmask = 255.255.255.0

binary:

netmask = 11111111 . 11111111 . 11111111 . 00000000

## split into 4 networks

> guest = 10

> robots = 57

> servers = 26

> workers = 117

___

| bits |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- |
| 128  | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
| host |     |     |     |     |     |     |     |
| 256  | 128 | 64  | 32  | 16  | 8   | 4   | 2   |

> start from biggest to smallest
___
# new
___

workers ==

> 7 bits = 64

> 64 * 2 = 128 (can cover 117)

binary netmask: 

> 11111111 . 11111111 . 11111111 . 10000000

(7 bits still open)

ip for workers:

> 172.21.42.0/25

> (172.21.42.0 - 172.21.42.127)

robots

> 6 bits = 32

> 32 * 2 = 64 (can cover 57)

binary netmask:

> 11111111 . 11111111 . 11111111 . 11000000

ip for robots:

> 172.21.42.128/26

> (172.21.42.128 - 172.21.42.191)

servers

> 5 bits = 16

> 16 * 2 + 32 (can cover 26)

binary netmask:

> 11111111 . 11111111 . 11111111 . 11100000

ip for servers:

> 172.21.42.192/27

> (172.21.42.192 - 172.21.42.223)

guest

> 4 bits = 8

> 8 * 2 = 16 (can cover 10)

binary netmask:

> 11111111 . 11111111 . 11111111 . 11110000

ip for guest:

> 172.21.42.224/28

> (172.21.42.224 - 172.21.42.239)

# more stuff

“Divide a /24 into 8 equal subnets”

“Give each department just what it needs”
got it

“How many subnets can I make from a /26?”

“What subnet is 192.168.1.77/28 in?”

“Summarize 192.168.0.0 – 192.168.3.255”
