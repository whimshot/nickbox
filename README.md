# The NickBox

A box for nick

![A box for Nick](/nickbox.jpg "A box for Nick")

## The Hardware

### Parts list



| Trinket Schematic Label | Pi Zero W Schematic Label | Description |
| ------------- | ------------- | ------------- |
| Part 1 || Adafruit Trinket 5v  |
| LED1, R1, &  S1 || Illuminated Toggle Switch with Cover  |
| LED2, R2  | S1 | Large Arcade Button with LED - 60mm   |
| LED3, R3  | S2 | Large Arcade Button with LED - 60mm   |
| Q1  || NPN-Transistor 2N-3904  |
| Q2  || NPN-Transistor 2N-3904  |
| | MCU1 | Raspberry Pi Zero W  |
| | U1 | LCD 16x2  |
| | U2 | 10K Potentiometer  |


### Wiring

#### Adafruit Trinket, Power/Arming Switch and Pulsating LEDs for Buttons

This controls the power/arming switch and the pulsing LEDs in the
hired/fired buttons.

##### Breadboard Layout

![Adafruit Trinket with Switch and LEDs Breadboard](/hardware/trinket_fader_bb.png "Adafruit Trinket with Switch and LEDs Breadboard")

##### Schematic

![Adafruit Trinket with Switch and LEDs Schematic](/hardware/trinket_fader_schem.png "Adafruit Trinket with Switch and LEDs Schematic")

#### Raspberry Pi Zero W, LCD and Button Switches

This uses the buttons to trigger a call to isnickfired.com

##### Breadboard

![Raspberry Pi Zero W with LCD Display and Buttons Schematic](/hardware/rpi_lcd_bb.png?raw=true "Raspberry Pi Zero W with LCD Display and Buttons Breadboard")

##### Schematic

![Raspberry Pi Zero W with LCD Display and Buttons Schematic](/hardware/rpi_lcd_schem.png?raw=true "Raspberry Pi Zero W with LCD Display and Buttons Schematic")
