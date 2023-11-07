from machine import Pin
from util import LCD, color_rgb


# 1
# Set up button pins.
# These are all instances of machine.Pin.
# See docs at https://docs.micropython.org/en/latest/library/machine.Pin.html#machine.Pin
btn_a = Pin(15, Pin.IN, Pin.PULL_UP)
btn_b = Pin(17, Pin.IN, Pin.PULL_UP)
btn_x = Pin(19, Pin.IN, Pin.PULL_UP)
btn_y = Pin(21, Pin.IN, Pin.PULL_UP)

# 2
# Set up joystick pins.
# These are also machine.Pin instances.
joy_up = Pin(2, Pin.IN, Pin.PULL_UP)
joy_down = Pin(18, Pin.IN, Pin.PULL_UP)
joy_left = Pin(16, Pin.IN, Pin.PULL_UP)
joy_right = Pin(20, Pin.IN, Pin.PULL_UP)

# 3
# Initialise LCD.
# This is a framebuf.FrameBuffer instance. See docs at:
# https://docs.micropython.org/en/latest/library/framebuf.html
lcd = LCD()

# 4
# Create some colors.
# color_rgb is a function from our utility library.
BLACK = color_rgb(0, 0, 0)
RED   = color_rgb(255, 0, 0)
GREEN = color_rgb(0, 255, 0)
BLUE  = color_rgb(0, 0, 255)
YELLOW = color_rgb(255, 255, 0)
WHITE = color_rgb(255, 255, 255)


# 5
# Size of the display in pixels.
WIDTH = 240
HEIGHT = 240


# Position of snake
snake_x = 120
snake_y = 120

box = (10, 10)


# Game objects
snake = [(120, 120), (120, 130), (120, 140)]
snake_direction = 'up'
snake_speed = 5
food = (100, 60)



while True:
    #
    # CLEAR SCREEN AND ADD BANNER
    #

    # Fill the screen with black color.
    lcd.fill(BLACK)

    # Display a nice banner.
    lcd.text('JOSALA @ KANTEGA', 60, 60, BLUE)
    # TODO 0:
    # Change the banner so it includes your name!


    # Draw the snake
    for x, y in snake:
        lcd.pixel(x, y, WHITE)

    # Draw the food
    lcd.pixel(food[0], food[1], GREEN)

    # Get the joystick input
    if not joy_up.value():
        snake_direction = 'up'
    elif not joy_down.value():
        snake_direction = 'down'
    elif not joy_left.value():
        snake_direction = 'left'
    elif not joy_right.value():
        snake_direction = 'right'
    
    # Move the snake
    if snake_direction == 'up':
        snake_y -= snake_speed
    elif snake_direction == 'down':
        snake_y += snake_speed
    elif snake_direction == 'left':
        snake_x -= snake_speed
    elif snake_direction == 'right':
        snake_x += snake_speed

    # Check if snake is outside the screen
    if snake_x < 0 or snake_x > WIDTH or snake_y < 0 or snake_y > HEIGHT:
        # TODO 1:
        # Add a game over message
        pass

    # Check if snake has eaten the food
    if snake_x == food[0] and snake_y == food[1]:
        # TODO 2:
        # Add a new food
        # Make the snake longer
        pass
    

    #
    # FINAL DRAWING
    #

    # Render everything to screen...
    lcd.show()
