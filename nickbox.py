#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi
import time
import requests
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
from lxml import html

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Raspberry Pi pin configuration:
# Note this might need to be changed to 21 for older revision Pi's.
lcd_rs = 27
lcd_en = 22
lcd_d4 = 25
lcd_d5 = 24
lcd_d6 = 23
lcd_d7 = 18
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)


def hire_nick(channel):
    requests.post('http://isnickfired.com/status/notfired')


def fire_nick(channel):
    requests.post('http://isnickfired.com/status/fired')


GPIO.add_event_detect(12, GPIO.FALLING, callback=hire_nick, bouncetime=300)
GPIO.add_event_detect(13, GPIO.FALLING, callback=fire_nick, bouncetime=300)

while True:
    page = requests.get('http://isnickfired.com')
    tree = html.fromstring(page.content)

    status = tree.xpath('//h1[@class="cover-heading"]/text()')

    message = status[0][8:]
    lcd.message(message)
    time.sleep(60)
    lcd.clear()
