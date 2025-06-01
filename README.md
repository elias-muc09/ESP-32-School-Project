**Simple ESP-32 House**
--

***Needed Hardware:***


- Esp-32
  Used item: [FREENOVE ESP32-S3 on Amazon](https://www.amazon.com/-/en/FREENOVE-ESP32-S3-WROOM-Dual-Core-Microcontroller-Wireless/dp/B0BMQ8F7FN/ref=sr_1_2?crid=2K8N31FTIQM51&dib=eyJ2IjoiMSJ9.6dly-XBkenELENJtlf6IL_dsDb1sdPIMRBuKHpMy8C0vL79UzmGGOg8FLqdC74pvfMxQNUs0xGfV2M0m6uv0KMwuCUg3ijQkuRNLtUOdlpVhQKxq_wkonPif4pkhh-nr9axBk8wAVe21zK3MXXkpgBi-2_8-EHd4gNfwC0ZPEmv04bem_oykeBXe6i_Ux3DH7oZUPr_z0rLTt4lWiIypZoYUyVCX3kEj5u4XOedfItk.RucVj4CapOBYHWMEn08RyFJ0ZgS-eX-_pZEsHhzgAzU&dib_tag=se&keywords=freenove%2Besp32-s3%2Bcam&qid=1748782374&sprefix=esp32%2Bcam%2Bfree%2Caps%2C92&sr=8-2&th=1)

- Wooden house
  used item: [Wooden House](https://www.amazon.com/-/en/gp/product/B074MB1QCY/ref=sw_img_1?smid=A2BZPTL9A42Y3O&psc=1)

- 2x RGB Led, 1x White Led
  used item: [Arduino RGBs](https://store.arduino.cc/products/set-of-70-assorted-color-5mm-leds?queryID=c2f9d4fca16aed5d29d7417c89561fd4)
  
- 1x red blinking Led (if its not blinking just modify the code to your needs)

- A buzzer
  
- 8x 220Ω resistor
  used item: [Arduino resistors](https://store.arduino.cc/products/box-525-1-precision-resistors-17-values?queryID=undefined)

- 25x male to female jumper cables (13 of them should be 20cm long or longer, the others can be shorter)
  used item: [Arduino Jumper](https://store.arduino.cc/collections/cables-wires/products/40-colored-male-female-jumper-wires)
  
- Small Breadboard
  [Arduino Breadboard](https://store.arduino.cc/products/mini-breadboard-white)

- Some Glue (I used a hot glue gun, that worked out pretty good)
- Something to prevent the cables from falling into the door (I used a zip tie glued to the celing and wall)

---


**Step 1:**

Download [Thonny](https://thonny.org/) and install it
Download the [CH343](https://www.wch-ic.com/products/CH343.html) driver and install it (idk if its diffrent on Linux or Mac)


**Sted 2:**

Open Thonny, plug the esp into your computer and flash [Micropython](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html) on the ESP-32.


**Step 3:**

Upload the Code

Big thanks to [Jonoack](https://github.com/jonoack) for coding my project


**Step 4:**

Build the house as described in the instructions.


**Step 5:**

Add the Electronics:

- The blinkin red led with the white led in the front
- One of the RGB led´s in the left room (with the chimney), the other one in the main room
- The buzzer in the chimney
- Run all the cables to the back (squeeze them trrou every space so they aren't noticable) 


**Step 6:**

Wire everything up:

Common Anode explaind [here](https://projecthub.arduino.cc/lewiskell/common-anode-rgb-led-f368dd)

RGBs:

First led:

- 16 = R
- 7 = G
- 15 = B
- plus = GND

Second led:

-  36 = R
-  35 = G
-  0 = B
-  plus = GND


Buzzer:

-  The longer end of the buzzer = 3.3 V
-  The shorter end of the buzzer = 47


Leds:

- white led the shorter end = 38
- red led the shorter end = 40
- the longer ones = GND


**Don't forget the resisters between every led (you only need them on those wires that dont go to GND, the buzzer dosen't need a resistor) and to secure all cables and other parts**

---

Pinout of the ESP I used:

![ESP32S3_Pinout](https://github.com/user-attachments/assets/ee496d8e-9ea8-47a7-aebf-25d86bdc8acb)

---

A few pictures of my house:

![Minimalist Photo Collage Instagram Post](https://github.com/user-attachments/assets/2345b567-777c-4c29-a234-fef87c19b5db)
