from microbit import *
import radio

radio.on()
radio.config(group=10)

while True:
    if button_a.is_pressed():
        radio.send("LEFT")
    elif button_b.is_pressed():
        radio.send("RIGHT")
    elif pin_logo.is_touched():
        radio.send("UP")
    elif accelerometer.current_gesture() == "face down":
        radio.send("STOP")
    elif button_a.is_pressed() and button_b.is_pressed():
        radio.send("START")
    sleep(100)

# ---------------------------------
# Below Microbit webversion of code
# ---------------------------------
#def on_logo_pressed():
#    radio.send_string("UP")
#input.on_logo_pressed(TouchButtonEvent.PRESSED, on_logo_pressed)

#def on_gesture_screen_down():
#    radio.send_string("STOP")
#input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

#def on_button_pressed_a():
#    radio.send_string("LEFT")
#input.on_button_pressed_a(Button.A, on_button_pressed_a)

#def on_button_pressed_ab():
#    radio.send_string("START")
#input.on_button_pressed(Button.AB, on_button_pressed_ab)

#def on_button_pressed_b():
#    radio.send_string("RIGHT")
#input.on_button_pressed(Button.B, on_button_pressed_b)

#radio.set_group(10)

#def on_forever():
#    pass
#basic.forever(on_forever)
