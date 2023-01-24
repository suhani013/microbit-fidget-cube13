rock_paper_scissors = 0
number1 = 0


def on_button_pressed_a():
   basic.show_leds("""
       . . . . .
               . # # # .
               . # . # .
               . # # # .
               . . . . .
   """)
   basic.show_leds("""
       # # # # #
               # . . . #
               # . # . #
               # . . . #
               # # # # #
   """)
input.on_button_pressed(Button.A, on_button_pressed_a)


def on_button_pressed_ab():
   global rock_paper_scissors
   rock_paper_scissors = randint(1, 3)
   if rock_paper_scissors == 1:
       basic.show_string("R")
   elif rock_paper_scissors == 2:
       basic.show_string("P")
   else:
       basic.show_string("S")
input.on_button_pressed(Button.AB, on_button_pressed_ab)


def on_button_pressed_b():
   global number1
   basic.clear_screen()
   number1 = randint(0, 100)
   basic.show_number(number1)
input.on_button_pressed(Button.B, on_button_pressed_b)


def on_gesture_shake():
   basic.show_icon(IconNames.SMALL_HEART)
   basic.show_icon(IconNames.HEART)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)


def on_logo_pressed():
   basic.show_leds("""
       # # # # #
               # # # # #
               # # # # #
               # # # # #
               # # # # #
   """)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)


def on_logo_released():
   basic.show_leds("""
       . . . . .
               . . . . .
               . . . . .
               . . . . .
               . . . . .
   """)
input.on_logo_event(TouchButtonEvent.RELEASED, on_logo_released)



