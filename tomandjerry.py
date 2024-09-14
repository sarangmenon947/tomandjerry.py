import pgzrun
import random

WIDTH = 600
HEIGHT = 500

tom = Actor("tom")
tom.pos = 300, 250

jerry = Actor("jerry")
jerry.pos = random.randint(70, WIDTH - 70), random.randint(70, HEIGHT - 70)

score = 0
game_over = False

def draw():
    screen.blit("backgroundtomandjerry", (0, 0))
    tom.draw()
    jerry.draw()
    screen.draw.text("Score: " + str(score), color="blue", topleft=(10, 20))
    
    if game_over:
        screen.draw.text("Game Over!", midtop=(WIDTH // 2, HEIGHT // 2), fontsize=50, color="red")

def place_jerry():
    """Randomly places Jerry on the screen."""
    jerry.pos = random.randint(70, WIDTH - 70), random.randint(70, HEIGHT - 70)

def on_mouse_down(pos):
    """Handles mouse click events."""
    global score
    if jerry.collidepoint(pos):
        score += 10
        place_jerry()

def update():
    global game_over
    if game_over:
        return  # Stop updating if the game is over
    
    # Controls for moving Tom
    if keyboard.left:
        tom.x -= 2
    if keyboard.right:
        tom.x += 2
    if keyboard.up:
        tom.y -= 2
    if keyboard.down:
        tom.y += 2

    # Check if the score has reached or exceeded 500
    if score >= 500:
        print("Score reached 500. Game over!")
        game_over = True  # Set the flag to stop the game

pgzrun.go()
