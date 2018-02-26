'''A simple program to drive buttons to hire and fire Nick'''
import socket
import time

import requests
import urllib3

import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
from lxml import html

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Raspberry Pi pin configuration:
# LCD to RPI connections.
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


def is_nick_fired():
    '''query isnickfired.com'''
    try:
        page = requests.get('http://isnickfired.com')
        tree = html.fromstring(page.content)
        status = tree.xpath('//h1[@class="cover-heading"]/text()')
        message = status[0][8:]
    except (requests.exceptions.ConnectionError,
            urllib3.exceptions.NewConnectionError,
            urllib3.exceptions.MaxRetryError):
        message = 'Connection\nFailure'
    finally:
        return message


def update_display(message):
    '''update the lcd display with message'''
    lcd.clear()
    lcd.message(message)


def hire_nick(channel):
    '''Callback for button to hire Nick'''
    try:
        requests.post('http://isnickfired.com/status/notfired')
        message = is_nick_fired()
    except (requests.exceptions.ConnectionError,
            urllib3.exceptions.NewConnectionError,
            urllib3.exceptions.MaxRetryError):
        message = 'Connection\nFailure'
    finally:
        update_display(message)


def fire_nick(channel):
    '''Callback for buttonn to fire Nick'''
    try:
        requests.post('http://isnickfired.com/status/fired')
        message = is_nick_fired()
    except (requests.exceptions.ConnectionError,
            urllib3.exceptions.NewConnectionError,
            urllib3.exceptions.MaxRetryError):
        message = 'Connection\nFailure'
    finally:
        update_display(message)


GPIO.add_event_detect(12, GPIO.FALLING, callback=hire_nick, bouncetime=300)
GPIO.add_event_detect(13, GPIO.FALLING, callback=fire_nick, bouncetime=300)

while True:
    message = is_nick_fired()
    update_display(message)
    time.sleep(60)
