let Bit = 0
input.onGesture(Gesture.Shake, function () {
    Bit = randint(0, 2)
    if (Bit == 0) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (Bit == 1) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
})
basic.forever(function () {
	
})
