[[network]]

Pre-made cables are convenient, but making your own is useful when: 

	You need a **custom length** (not too long, not too short)
	   
	A cable is **damaged and needs repair**
   
	You want to **build on-site**, especially in tight spaces or through walls


---

## Things You Need:

- Cat5e cable (UTP — unshielded twisted pair)
    
- RJ45 connectors (Ethernet plugs)
    
-  Crimping tool (crimper)
    
-  Cable tester (to confirm it works)
    
- (Optional) Wire stripper or scissors
    

---

## Step-by-Step:

### **Step 1: Cut the cable to your desired length.**

cut head off:

> If you're fixing or shortening a cable, cut off the existing connector(s) cleanly.

---

### **Step 2: Strip about 2 cm (0.8 in) of the outer jacket.**

This part is great and very safe:

> - **Scratch**, don’t slice — to avoid cutting inner wires
>     
> - **Bend back and forth** to snap the jacket cleanly
>     
>  - Remove any nylon string or "cable hair" if present.

---

### **Step 3: Identify the 4 twisted pairs:**

Perfect colours:

- Orange + White-Orange
    
- Green + White-Green
    
- Blue + White-Blue
    
- Brown + White-Brown
    

This is for **TIA/EIA-568B standard**, the most common.

---

### **Step 4: Untwist, straighten, and arrange the wires**

order for T568B:

> **WO, O, WG, BL, WBL, G, WBR, BR**

- Use your fingers or a straight edge (like a ruler) to flatten wires.
    
- Cut tips **evenly**, leave about **1.3–1.5 cm** length.
    
- Keep them flat and in the correct order before insertion.
    

---

### **Step 5: Insert wires into RJ45 plug**

- Hold the plug with **clip facing down**, **gold pins facing up**
    
- Make sure wires **reach the end** of the plug (you should see copper in front)
    
- Check the **wire order** again before crimping
    

Crimp firmly to:

- Push pins into wires for electrical contact
    
- Clamp the plug around the jacket for strain relief
    

---

##  BONUS Step 6: Test the cable

> Plug both ends into a **cable tester**. All lights should flash in order (1–8). If any number doesn’t light up, it may be a miswire or bad crimp.

---

## Summary:

> Making your own Ethernet cable allows for **custom lengths, repairs, and installations**.  
> Follow the **T568B** wire order, keep wires flat and aligned, and always **test your cable** before use.

---

purpose of the outer layer/jacket of the cable is to protect the wires on the inside.

EMI = electromagnetic interference

by twisting the pairs together also helps with EMI

cross talk = unwanted signal interference between wires, like when signals from one wire “leak” into another, causing noise or data errors. (caused by EMI)

This is why it's classified as a **UTP (Unshielded Twisted Pair(refer to note 2))** cable, the twists help reduce internal EMI without needing shielding.


###############################################
###############################################
###############################################
#### cat3 == category 3
10 base-T and 100 base-TX

##### straight through (endpoint to switch)
___
The other pins 4, 5, 7, 8 are unused in 10Base-T and 100Base-T.)
  
On both ends, the wire colors and pin numbers **match exactly** — this is why it’s a "straight-through" cable. Data goes out of pin 1 and 2 on the endpoint and goes into pin 1 and 2 on the switch.

| -------------------------- | ENDPOINT | -------------------------- |
| -------------------------- | -------- | -------------------------- |

| 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| --- | --- | --- | --- | --- | --- | --- | --- |


| Tx + | Tx - | Rx + |     |     | Rx - |     |     |
| ---- | ---- | ---- | --- | --- | ---- | --- | --- |
| VVVV | VVVV | ^^^^ |     |     | ^^^^ |     |     |
| VVVV | VVVV | ^^^^ |     |     | ^^^^ |     |     |
| WO   | O    | WG   |     |     | G    |     |     |
| WO   | O    | WG   |     |     | G    |     |     |
| VVVV | VVVV | ^^^^ |     |     | ^^^^ |     |     |
| VVVV | VVVV | ^^^^ |     |     | ^^^^ |     |     |
| Tx + | Tx - | Rx + |     |     | Rx - |     |     |

| 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| --- | --- | --- | --- | --- | --- | --- | --- |

| --------------------------- | SWITCH | --------------------------- |
| --------------------------- | ------ | --------------------------- |

##### crossover (endpoint to endpoint)
___
The **Transmit (Tx)** and **Receive (Rx)** wires are **swapped** between the two ends. This lets two similar devices talk to each other by matching output to input.

| -------------------------- | ENDPOINT | -------------------------- |
| -------------------------- | -------- | -------------------------- |

| 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| --- | --- | --- | --- | --- | --- | --- | --- |


| Tx + | Tx - | Rx + |     |     | Rx - |     |     |
| ---- | ---- | ---- | --- | --- | ---- | --- | --- |
| VVVV | VVVV | ^^^^ |     |     | ^^^^ |     |     |
| VVVV | VVVV | ^^^^ |     |     | ^^^^ |     |     |
| WO   | O    | WG   |     |     | G    |     |     |
| WG   | G    | WO   |     |     | O    |     |     |
| VVVV | VVVV | ^^^^ |     |     | ^^^^ |     |     |
| VVVV | VVVV | ^^^^ |     |     | ^^^^ |     |     |
| Rx + | Rx - | Tx + |     |     | Tx - |     |     |

| 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| --- | --- | --- | --- | --- | --- | --- | --- |

| --------------------------- | SWITCH | --------------------------- |
| --------------------------- | ------ | --------------------------- |


###############################################
###############################################
###############################################
#### cat5e == category 5 ethernet cable (1000 base-T)
___
##### crossover cable 
___
endpoint = 568 B
switch     = 568 A

| -------------------------- | ENDPOINT | -------------------------- |
| -------------------------- | -------- | -------------------------- |

| 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| --- | --- | --- | --- | --- | --- | --- | --- |


| ^^^^ | ^^^^ | ^^^^ | ^^^^ | ^^^^ | ^^^^ | ^^^^ | ^^^^ |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| ^^^^ | ^^^^ | ^^^^ | ^^^^ | ^^^^ | ^^^^ | ^^^^ | ^^^^ |
| WO   | O    | WG   | BL   | WBL  | G    | WBR  | BR   |
| WG   | G    | WO   | BL   | WBL  | O    | WBR  | BR   |
| VVVV | VVVV | VVVV | VVVV | VVVV | VVVV | VVVV | VVVV |
| VVVV | VVVV | VVVV | VVVV | VVVV | VVVV | VVVV | VVVV |

| 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| --- | --- | --- | --- | --- | --- | --- | --- |

| --------------------------- | SWITCH | --------------------------- |
| --------------------------- | ------ | --------------------------- |
##### straight-through cable 
___
endpoint = 568 B
switch     = 568 B

| -------------------------- | ENDPOINT | -------------------------- |
| -------------------------- | -------- | -------------------------- |

| 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| --- | --- | --- | --- | --- | --- | --- | --- |


| ^^^^ | ^^^^ | ^^^^ | ^^^^ | ^^^^ | ^^^^ | ^^^^ | ^^^^ |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| ^^^^ | ^^^^ | ^^^^ | ^^^^ | ^^^^ | ^^^^ | ^^^^ | ^^^^ |
| WO   | O    | WG   | BL   | WBL  | G    | WBR  | BR   |
| WO   | O    | WG   | BL   | WBL  | G    | WBR  | BR   |
| VVVV | VVVV | VVVV | VVVV | VVVV | VVVV | VVVV | VVVV |
| VVVV | VVVV | VVVV | VVVV | VVVV | VVVV | VVVV | VVVV |

| 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| --- | --- | --- | --- | --- | --- | --- | --- |

| --------------------------- | SWITCH | --------------------------- |
| --------------------------- | ------ | --------------------------- |
