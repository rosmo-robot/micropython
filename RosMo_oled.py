#https://docs.micropython.org/en/latest/esp8266/tutorial/ssd1306.html
#https://github.com/dmccreary/robot-faces/tree/master/src



from machine import Pin, I2C
import ssd1306

# using default address 0x3C
i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
