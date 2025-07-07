[[network]]


split below in 4 subnets

| bits     |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- |
| 128      | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
| networks |     |     |     |     |     |     |     |
| 256      | 128 | 64  | 32  | 16  | 8   | 4   | 2   |

#### original in decimal
___
ip == 192.168.1.0/24
netmask == 255.255.255.0
#### orgnl in binary
___
netmask
11111111 . 11111111 . 11111111 . 00000000

to split it into 4:
we need 2 bits as shown in table above.
2 bits will give 4 more networks

new netmask binary:
11111111 . 11111111 . 11111111 . 11000000
___
new netmask decimal:
255.255.255.192
___
1st decimal ip network:
192.168.1.0/26
range (192.168.1.0 - 192.168.1.63)

2nd decimal ip network:
range (192.168.1.64 - 192.168.1.127)

3rd decimal ip network:
range (192.168.1.128 - 192.168.1.191)

4th decimal ip network:
range (192.168.1.192 - 192.168.1.254)

# split in 5
___
ip == 192.168.1.0/24
netmask == 255.255.255.0
___
netmask
11111111 . 11111111 . 11111111 . 00000000

to split it into 5:
we need 4 bits as shown in table above.
4 bits will give 5 more networks
___

new netmask binary:
11111111 . 11111111 . 11111111 . 11100000

new decimal nemask:
255.255.255.224

block size = 256 - 224 = 32
___
 new decimal ip:
 192.168.1.0/27
 
1st range:
192.168.1.0 - 192.168.1.31

2nd range:
192.168.1.32 - 192.168.1.63

3rd range:
192.168.1.64 - 192.168.1.95

4th range:
192.168.1.96 - 192.168.1.127

5th range:
192.168.1.128 - 192.168.1.159
___
