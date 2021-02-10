def on_button_pressed_a():
    radio.send_number(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string("" + str((countdown)))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global countdown
    countdown = 60
    radio.send_number(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

fade = 0
white = 0
countdown = 0
radio.set_group(1)
countdown = -1
strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
strip.range(0, 24).show_color(white)
strip.set_brightness(200)
white = 255

def on_forever():
    global white, fade
    while countdown < 0:
        strip.show_color(neopixel.rgb(white, white, 255))
        if fade == 0:
            white += -8
            if white == 47:
                fade = 1
                basic.pause(400)
        else:
            white += 8
            if white == 255:
                fade = 0
                basic.pause(400)
        basic.pause(100)
basic.forever(on_forever)
