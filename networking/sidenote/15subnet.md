
[[network]]

CIDR == classless inter-domain routing

could also be called cidr prefix or slash notation

(/24 , /26 . /27)

/24 == the first 24 bits is the network

/25 == the first 25 bits are the network

etc.

# 3 shop split
___

> split the network into 3 subnets to cover 3 locations

original decimal:

the network ---> 10.1.1.0 /24

netmask == 255.255.255.0

original binary:

netmask == 11111111 . 11111111 . 11111111 . 00000000

2 bits will give 4 more subnets (only 3 will be used).

new binary netmask:

11111111 . 11111111 . 11111111 . 11000000

new network:

10.1.1.0/26

10.1.1.0 - 10.1.1.63

10.1.1.64 - 10.1.1.127

10.1.1.128 - 10.1.1.191

| shop 1 | 10.1.1.0 - 10.1.1.63    |
| ------ | ----------------------- |
| shop 2 | 10.1.1.64 - 10.1.1.127  |
| shop 3 | 10.1.1.128 - 10.1.1.191 |

___

# 5 customer split
___
> you are an isp.

> you have 5 customers who need at least 20 static ip addresses(public).

> do not give too many addresses. the idea is to stay conservative
___

original decimal:
ip == 142.2.0.0/16

original netmask binary:
netmask == 11111111 . 11111111 . 00000000 . 00000000

original netmask decimal:
255.255.0.0
___
new netmask binary:
11111111 . 11111111 . 11111111 . 11100000

new netmask  decimal:
255.255.255.224

new network decimal:
142.2.32.0/27

| client     |                             |
| ---------- | --------------------------- |
| customer 1 | 142.2.32.0 - 142.2.32.31    |
| customer 2 | 142.2.32.32 - 142.2.32.63   |
| customer 3 | 142.2.32.64 - 142.2.32.95   |
| customer 4 | 142.2.32.96 - 142.2.32.127  |
| customer 5 | 142.2.32.128 - 142.2.32.159 |
