def on_button_pressed_a():
    music._play_default_background(music.built_in_playable_melody(Melodies.WEDDING),
        music.PlaybackMode.IN_BACKGROUND)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music._play_default_background(music.built_in_playable_melody(Melodies.BIRTHDAY),
        music.PlaybackMode.IN_BACKGROUND)
input.on_button_pressed(Button.B, on_button_pressed_b)

music._play_default_background(music.built_in_playable_melody(Melodies.POWER_UP),
    music.PlaybackMode.UNTIL_DONE)

def on_forever():
    pass
basic.forever(on_forever)
