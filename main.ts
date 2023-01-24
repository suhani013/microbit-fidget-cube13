let rock_paper_scissors = 0
let number1 = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showLeds(`
       . . . . .
               . # # # .
               . # . # .
               . # # # .
               . . . . .
   `)
    basic.showLeds(`
       # # # # #
               # . . . #
               # . # . #
               # . . . #
               # # # # #
   `)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    rock_paper_scissors = randint(1, 3)
    if (rock_paper_scissors == 1) {
        basic.showString("R")
    } else if (rock_paper_scissors == 2) {
        basic.showString("P")
    } else {
        basic.showString("S")
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    basic.clearScreen()
    number1 = randint(0, 100)
    basic.showNumber(number1)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showIcon(IconNames.SmallHeart)
    basic.showIcon(IconNames.Heart)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    basic.showLeds(`
       # # # # #
               # # # # #
               # # # # #
               # # # # #
               # # # # #
   `)
})
input.onLogoEvent(TouchButtonEvent.Released, function on_logo_released() {
    basic.showLeds(`
       . . . . .
               . . . . .
               . . . . .
               . . . . .
               . . . . .
   `)
})
