/*
  This is part of the nickbox project. This is written for an
  Adafruit Trinket which controls the arming switch and the 
  pulsing lights on the hire/fire buttons.
*/

int green_button_led = 1;         // the PWM pin the green button LED is attached to
int green_button_brightness = 0;  // how bright the green button LED is
int red_button_led = 0;           // the PWM pin the red button LED is attached to
int red_button_brightness = 255;  // how bright the blue button LED is
int fadeAmount = 5;               // how many points to fade the LED by

// the setup routine runs once when you press reset:
void setup() {
  // set up the pins as output:
  pinMode(green_button_led, OUTPUT);
  pinMode(red_button_led, OUTPUT);
}

void loop() {
  // set the brightness of the buttons:
  analogWrite(red_button_led, red_button_brightness);
  analogWrite(green_button_led, green_button_brightness);

  // change the brightness for next time through the loop:
  green_button_brightness = green_button_brightness + fadeAmount;
  red_button_brightness = red_button_brightness - fadeAmount;

  // reverse the direction of the fading at the ends of the fade:
  if (green_button_brightness <= 0 || green_button_brightness >= 255) {
    fadeAmount = -fadeAmount;
  }
  // wait for 30 milliseconds to see the dimming effect
  delay(30);
}
