input.onButtonPressed(Button.A, function () {
    radio.sendNumber(0)
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("" + countdown)
})
input.onButtonPressed(Button.B, function () {
    countdown = 60
    radio.sendNumber(1)
})
let fade = 0
let white = 0
let countdown = 0
radio.setGroup(1)
countdown = -1
let strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
strip.range(0, 24).showColor(white)
strip.setBrightness(200)
white = 255
basic.forever(function () {
    while (countdown < 0) {
        strip.showColor(neopixel.rgb(white, white, 255))
        if (fade == 0) {
            white += -8
            if (white == 47) {
                fade = 1
                basic.pause(400)
            }
        } else {
            white += 8
            if (white == 255) {
                fade = 0
                basic.pause(400)
            }
        }
        basic.pause(100)
    }
})
