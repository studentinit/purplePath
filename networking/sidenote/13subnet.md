[[network]]
octet == 8 bits
so an ipv4 addr == 32 bits (4 octets)
1 == on
0 == off

calculator for converting ip decimal into ip binary:
128   64.  32.  16.  8.  4.  2.  1   

decimal ip == 172.16.34.3
binary ip == 10101100. 00010000. 00100010. 00000011
# CALCULATE
## 1ST OCTET (172)
___

| DECIMAL IP | CALCULATION     | BINARY CODE | BINARY IP |
| ---------- | --------------- | ----------- | --------- |
| 172        | 172 -128 = 44   | 1           |           |
|            | 44 - 64 = ERROR | 0           |           |
|            | 44 - 32 = 12    | 1           |           |
|            | 12 - 16 = ERROR | 0           |           |
|            | 2 - 8 = 4       | 1           |           |
|            | 4 - 4 = 0       | 1           |           |
|            | 0 - 2 = ERROR   | 0           |           |
|            | 0 - 1 = ERROR   | 0           |           |
|            |                 |             | 10101100  |
___
## 2ND OCTET (16)
___

| DECIMAL IP | CALCULATION      | BINARY CODE | BINARY IP |
| ---------- | ---------------- | ----------- | --------- |
| 16         | 16 - 128 = ERROR | 0           |           |
|            | 16 - 64 = ERROR  | 0           |           |
|            | 16 - 32 = ERROR  | 0           |           |
|            | 16 - 16 = 0      | 1           |           |
|            | 0 - 8 = ERROR    | 0           |           |
|            | 0 - 4 = ERROR    | 0           |           |
|            | 0 - 2 =ERROR     | 0           |           |
|            | 0 - 1 = ERROR    | 0           |           |
|            |                  |             | 00010000  |
___
## 3RD OCTET (34)
___

| DECIMAL IP | CALCULATION      | BINARY CODE | BINARY IP |
| ---------- | ---------------- | ----------- | --------- |
| 34         | 34 - 128 = ERROR | 0           |           |
|            | 34 - 64 = ERROR  | 0           |           |
|            | 34 - 32 = 2      | 1           |           |
|            | 2 - 16 = ERROR   | 0           |           |
|            | 2 - 8 = ERROR    | 0           |           |
|            | 2 - 4 = ERROR    | 0           |           |
|            | 2 - 2 = 0        | 1           |           |
|            | 0 - 1 = ERROR    | 0           |           |
|            |                  |             | 00100010  |
___
## 4TH OCTET (3)

| DECIMAL IP | CALCULATION     | BINARY CODE | BINARY IP |
| ---------- | --------------- | ----------- | --------- |
| 3          | 3 - 128 = ERROR | 0           |           |
|            | 3 - 64 = ERROR  | 0           |           |
|            | 3 - 32 = ERROR  | 0           |           |
|            | 3 - 16 = ERRPR  | 0           |           |
|            | 3 - 8 = ERROR   | 0           |           |
|            | 3 - 4 = ERROR   | 0           |           |
|            | 3 - 2 = 1       | 1           |           |
|            | 1 - 1 = 0       | 1           |           |
|            |                 |             | 00000011  |

# more stuff
___

decimal ip == 192.168.32.5
binary ip == 11000000 . 10101100 . 00100000 . 00000101

decimal subnet mask = 255.255.255.0
binary subnet mask = 11111111 . 11111111 . 11111111 . 00000000

