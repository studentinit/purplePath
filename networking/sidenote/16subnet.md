[[network]]

# test 1
given a host ip addr of 48.25.24.71/21, what is the broadcast addr for the subnetwork?

a = 48.25.25.254

b = 48.25.24.240

c = 48.25.31.254

d = 48.25.31.255

e = 48.25.24.255

f = 48.25.24.127

___
netmask binary:

11111111 . 11111111 . 11111000 . 00000000

netmask decimal:

255.255.248.0


# more
___
decimal:
 
 ipv4 = 172.17.16.255
 
 subnet mask = 255.255.240.0
 
 default gateway = 172.17.0.1

binary:
 
 subnet mask = 11111111 . 11111111 . 11110000
 
 ___

# reverse subnet challenge 1
___
You are given the following subnets:

- `192.168.4.0/24`
    
- `192.168.5.0/24`
    

### ❓ Can these be summarized?

- ✅ Yes or ❌ No?
    
- If yes: What is the summarized block?

> yes

binary:

    192.168.4.0/24 = 11000000 . 10101000 . 00000100 . 00000000

    192.168.5.0/24 = 11000000 . 10101000 . 00000101 . 00000000

192.168.4.0 - 192.168.5.255 = 192.168.4.0/25

/24 - 1 because the 3rd octet has an extra bit in the range of 4 and 5

    (/23 is bigger than /24)

# reverse subnet challenge 2
___
Can the following be summarized?

- `192.168.0.0/24`
    
- `192.168.1.0/24`
    
- `192.168.2.0/24`
    
- `192.168.3.0/24`
    

Give it a shot — and let me know:

1. ✅ Yes or ❌ No?
    
2. If yes, what is the summarized block?

> yes

binary:

    192.168.0.0/24 = 11000000 . 10101000 . 00000000 . 00000000

    192.168.1.0/24 =  11000000 . 10101000 . 00000001 . 00000000

    192.168.2.0/24 = 11000000 . 10101000 . 00000010 . 00000000

    192.168.3.0/24 = 11000000 . 10101000 . 00000011 . 00000000

192.168.0.0 - 192.168.3.255 = 192.168.0.0/20

/24 - 1 - 1 - 2 = /20

(/20 is bigger than /24)

