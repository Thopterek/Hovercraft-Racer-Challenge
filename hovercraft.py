from microbit import *
import radio
import sys

# --------------------------------------------------------------
# Microbit Python, webversion is stable and was used in hackaton
# Warning pure python might need some adjustmens, look at webv.
# --------------------------------------------------------------
def Motor_A(on: bool, cw: bool, speed: int):
    if on:
        if cw:
           pin12.write_digital(0)
           pin13.write_digital(1)
        else:
            pin12.write_digital(1)
            pin13.write_digital(0)
    else:
        pin12.write_digital(0)
        pin13.write_digital(0)
    pin1.write_analog(max(0, min(1023, int(speed))))

def Motor_B(on: bool, cw: bool, speed: int):
    if on:
        if cw:
            pin15.write_digital(0)
            pin16.write_digital(1)
        else:
            pin15.write_digital(1)
            pint16.write_digital(0)
    else:
        pin15.write_digital(0)
        pin16.write_digital(0)
    pin2.write_analog(max(0, min(1023, int(speed))))

def servo_write(pin_obj, angle: int):
    if angle < 0:
        angle = 0
    if angle > 180:
        angle = 180
    pin_obj.set_analog_period(20)
    min_pulse_ms = 1.0
    max_pulse_ms = 2.0
    period_ms = 20.0
    min_duty = (min_pulse_ms / period_ms) * 1023.0
    max_duty = (max_pulse_ms / period_ms) * 1023.0
    duty = int(min_duty + (angle / 180.0) * (max_duty - min_duty))
    duty = max(0, min(1023, duty))
    pin_obj.write_analog(duty)

radio.on()
radio.config(group=10)
pin14.write_digital(1)
pin0.write_analog(1023)
display.show(Image.YES)

while True:
    msg = radio.receive()
    if msg:
        if "START" in msg:
            Motor_A(True, False, 1023)
            Motor_B(True, False, 1023)
            servo_write(pin3, 45)
            display.show(Image.TARGET)
        if "RIGHT" in msg:
            servo_write(pin3, 180)
        if "LEFT" in msg:
            servo_write(pin3, 0)
        if "UP" in msg:
            servo_write(pin3, 90)
        if "STOP" in msg:
            Motor_B(False, False, 0)
            Motor_A(False, False, 0)
    sleep(10)

# -------------------------
# Below microbit webversion
# -------------------------
#def Motor_A(AnAus: bool, CWCCW: bool, Speed: number):
#    if AnAus:
#        if CWCCW:
#            pins.digital_write_pin(DigitalPin.P12, 0)
#            pins.digital_write_pin(DigitalPin.P13, 1)
#        else:
#            pins.digital_write_pin(DigitalPin.P12, 1)
#            pins.digital_write_pin(DigitalPin.P13, 0)
#    else:
#        pins.digital_write_pin(DigitalPin.P12, 0)
#        pins.digital_write_pin(DigitalPin.P13, 0)
#    pins.analog_write_pin(AnalogPin.P1, Speed)
#
#def Motor_B(AnAus2: bool, CWCW2: bool, Speed2: number):
#    if AnAus2:
#        if CWCW2:
#            pins.digital_write_pin(DigitalPin.P15, 0)
#            pins.digital_write_pin(DigitalPin.P16, 1)
#        else:
#            pins.digital_write_pin(DigitalPin.P15, 1)
#            pins.digital_write_pin(DigitalPin.P16, 0)
#    else:
#        pins.digital_write_pin(DigitalPin.P15, 0)
#        pins.digital_write_pin(DigitalPin.P16, 0)
#    pins.analog_write_pin(AnalogPin.P2, Speed2)
#
#def on_received_string(receivedString):
#    if receivedString.includes("START"):
#        Motor_A(True, False, 1023)
#        Motor_B(True, False, 1023)
#        pins.servo_write_pin(AnalogPin.P3, 45)
#        basic.show_icon(IconNames.TARGET)
#    if receivedString.includes("RIGHT"):
#        pins.servo_write_pin(AnalogPin.P3, 180)
#    if receivedString.includes("LEFT"):
#        pins.servo_write_pin(AnalogPin.P3, 0)
#    if receivedString.includes("UP"):
#        pins.servo_write_pin(AnalogPin.P3, 90)
#    if receivedString.includes("STOP"):
#        Motor_B(False, False, 0)
#        Motor_A(False, False, 0)
#radio.on_received_string(on_received_string)

#radio.set_group(10)
#pins.digital_write_pin(DigitalPin.P14, 1)
#pins.analog_write_pin(AnalogPin.P0, 1023)
#basic.show_icon(IconNames.YES)

