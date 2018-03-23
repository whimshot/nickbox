'''A simple program to drive buttons to hire and fire Nick'''
import socket
import time

import requests
import urllib3

import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
from lxml import html

hire_btn = 12
fire_btn = 26

green_is_down = False
red_is_down = False

hire_down = False
fire_down = False


GPIO.setmode(GPIO.BCM)
GPIO.setup(hire_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(fire_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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
            urllib3.exceptions.MaxRetryError,
            socket.timeout):
        message = 'Connect Failed'
    finally:
        return message


def update_display(message):
    '''update the lcd display with message'''
    lcd.clear()
    lcd.message(message)


def hire_button_pressed(channel):
    try:
        if (!(GPIO.input(fire_btn) and GPIO.input(hire_btn))):
            update_display('Stop being a\nSMARTASS!')
            sleep(30)
        else:
            try:
                requests.post('http://isnickfired.com/status/notfired')
                sleep(1)
                message = 'Nick is\n' + is_nick_fired()
            except (requests.exceptions.ConnectionError,
                    urllib3.exceptions.NewConnectionError,
                    urllib3.exceptions.MaxRetryError,
                    socket.timeout):
                message = 'Connection\nFailed'
            finally:
                update_display(message)
    except Exception:
        raise
    finally:
        pass


def fire_button_pressed(channel):
    try:
        if (!(GPIO.input(fire_btn) and GPIO.input(hire_btn))):
            update_display('Stop being a\nSMARTASS!')
            sleep(30)
        else:
            try:
                requests.post('http://isnickfired.com/status/fired/nickbox')
                sleep(1)
                message = 'Nick is\n' + is_nick_fired()
            except (requests.exceptions.ConnectionError,
                    urllib3.exceptions.NewConnectionError,
                    urllib3.exceptions.MaxRetryError,
                    socket.timeout):
                message = 'Connection\nFailed'
            finally:
                update_display(message)
    except Exception:
        raise
    finally:
        pass


GPIO.add_event_detect(hire_btn, GPIO.BOTH,
                      callback=hire_button_pressed, bouncetime=300)
GPIO.add_event_detect(fire_btn, GPIO.RISING,
                      callback=fire_button_pressed, bouncetime=300)
update_display('Checking Status')

while True:
    message = 'Nick is\n' + is_nick_fired()
    update_display(message)
    time.sleep(900)
