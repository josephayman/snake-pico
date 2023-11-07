from machine import Pin
from util import LCD, color_rgb
import random
import utime


# 1
# Set up button pins
btn_a = Pin(15, Pin.IN, Pin.PULL_UP)
btn_b = Pin(17, Pin.IN, Pin.PULL_UP)
btn_x = Pin(19, Pin.IN, Pin.PULL_UP)
btn_y = Pin(21, Pin.IN, Pin.PULL_UP)

# 2
# Set up joystick pins
joy_up = Pin(2, Pin.IN, Pin.PULL_UP)
joy_down = Pin(18, Pin.IN, Pin.PULL_UP)
joy_left = Pin(16, Pin.IN, Pin.PULL_UP)
joy_right = Pin(20, Pin.IN, Pin.PULL_UP)

# 3
# Initialise LCD
lcd = LCD()

# 4
# Create some colors
BLACK = color_rgb(0, 0, 0)
RED = color_rgb(255, 0, 0)
GREEN = color_rgb(0, 255, 0)
BLUE = color_rgb(0, 0, 255)
WHITE = color_rgb(255, 255, 255)

# 5
# Size of the display in pixels
WIDTH = 240
HEIGHT = 240

# Function to draw a square


def draw_square(x, y, size, color):
    for i in range(x, x + size):
        for j in range(y, y + size):
            lcd.pixel(i, j, color)

# Game loop


def main_game_loop():
    # Position of snake
    snake_x = 120
    snake_y = 120

    # Game objects
    snake = [(120, 120), (120, 130), (120, 140)]
    snake_direction = 'up'
    snake_speed = 5
    food = (100, 60)
    while True:
        # Clear screen and add banner
        lcd.fill(BLACK)
        lcd.text('JOSALA @ KANTEGA', 60, 60, BLUE)

        # Draw the snake
        for segment in snake:
            # Snake is 10x10 pixels
            draw_square(segment[0], segment[1], 10, WHITE)

        # Draw the food
        draw_square(food[0], food[1], 10, GREEN)  # Food is 10x10 pixels

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
        if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
            lcd.fill(BLACK)
            lcd.text('GAME OVER', 50, 120, RED)
            lcd.show()
            break

        # Check if snake has eaten the food
        if (snake_x in range(food[0], food[0] + 10)) and (snake_y in range(food[1], food[1] + 10)):
            # Extend the snake
            snake.insert(0, (snake_x, snake_y))

            # Generate new food location
            while True:
                new_food_x = random.randint(0, WIDTH - 10)
                new_food_y = random.randint(0, HEIGHT - 10)
                new_food = (new_food_x, new_food_y)
                if all((nx, ny) not in snake for nx in range(new_food_x, new_food_x + 10) for ny in range(new_food_y, new_food_y + 10)):
                    food = new_food
                    break
        else:
            # Move the snake
            snake.insert(0, (snake_x, snake_y))
            snake.pop()

        # Check for collisions with itself
        if (snake_x, snake_y) in snake[1:]:
            lcd.fill(BLACK)
            lcd.text('GAME OVER', 50, 120, RED)
            lcd.show()
            break

        # Render everything to screen
        lcd.show()

        # Delay to control game speed
        utime.sleep_ms(100)

        # Check for game over and prompt for restart
    if (snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT) or ((snake_x, snake_y) in snake[1:]):
        lcd.fill(BLACK)
        lcd.text('GAME OVER', 50, 120, RED)
        lcd.text('Press A to restart', 35, 140, WHITE)
        lcd.show()
        while True:
            # Wait for button A to be pressed to restart
            if not btn_a.value():
                main_game_loop()
            utime.sleep_ms(100)


print('Starting Snake game')
main_game_loop()

#
