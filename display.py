# SPDX-FileCopyrightText: 2018 Mikey Sklar for Adafruit Industries
#
# SPDX-License-Identifier: MIT
# Modified by Jonathan Seyfert, 2022-01-22
# to keep code from crashing when WiFi or IP is unavailable
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2

# compatible with all versions of RPI as of Jan. 2019
# v1 - v3B+
lcd_rs = digitalio.DigitalInOut(board.D22)
lcd_en = digitalio.DigitalInOut(board.D17)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d6 = digitalio.DigitalInOut(board.D23)
lcd_d7 = digitalio.DigitalInOut(board.D18)

# Initialise the lcd class
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                      lcd_d7, lcd_columns, lcd_rows)

# Custom character byte array for degree symbol
degree_symbol = [
    0b00111,
    0b00101,
    0b00111,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000
]
# wipe LCD screen before we start
lcd.clear()
# Create the custom character
lcd.create_char(0, degree_symbol)

def display_message(temperature, humidity):
    # Temeprature
    lcd_line_1 = "Temperature: " + str(temperature) + "\x00" + "\n"
    # Humidity
    lcd_line_2 = "Humidity: " + str(humidity)
    # combine both lines into one update to the display
    lcd.message = lcd_line_1 + lcd_line_2

    

