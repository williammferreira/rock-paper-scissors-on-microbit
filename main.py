Bit = 0

def on_gesture_shake():
    global Bit
    Bit = randint(0, 2)
    if Bit == 0:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif Bit == 1:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
