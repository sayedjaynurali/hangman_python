import turtle
import random
from hangman_function import Hangman_Drawing, words

# -----------------------------
# Setup screen
# -----------------------------
screen = turtle.Screen()
screen.title("Hangman Game")
screen.setup(width=1000, height=700)
screen.bgcolor("white")
screen.tracer(0)   # speed up drawing

# -----------------------------
# Hangman Drawer
# -----------------------------
drawer = Hangman_Drawing()

# -----------------------------
# Writers
# -----------------------------
hint_writer = turtle.Turtle(); hint_writer.hideturtle(); hint_writer.penup()
word_writer = turtle.Turtle(); word_writer.hideturtle(); word_writer.penup()
status_writer = turtle.Turtle(); status_writer.hideturtle(); status_writer.penup()
result_writer = turtle.Turtle(); result_writer.hideturtle(); result_writer.penup()
restart_writer = turtle.Turtle(); restart_writer.hideturtle(); restart_writer.penup()

def display_text(writer, message, x, y, size=18, color="black", align="center"):
    writer.clear()
    writer.goto(x, y)
    writer.color(color)
    writer.write(message, align=align, font=("Arial", size, "bold"))

# -----------------------------
# Global state
# -----------------------------
chosen_word = ""
chosen_word_list = []
word_to_guess = []
l = 0
parts = []
letter_buttons = {}
used_letters = set()
game_over = False
restart_box = None  # bounding box of restart button

# -----------------------------
# Functions
# -----------------------------
def draw_buttons():
    """Draw clickable letter buttons A–Z on the screen."""
    global letter_buttons
    for btn in letter_buttons.values():
        btn.clear() if isinstance(btn, turtle.Turtle) else None
    letter_buttons = {}

    x_start, y_start = 200, 200
    spacing = 40
    row_length = 7
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for idx, letter in enumerate(letters):
        row = idx // row_length
        col = idx % row_length
        x = x_start + col * spacing
        y = y_start - row * spacing

        btn = turtle.Turtle()
        btn.hideturtle()
        btn.speed(0)   # draw instantly
        btn.penup()
        btn.goto(x, y)

        # Grey out used letters
        if letter in used_letters:
            btn.color("grey")
        else:
            btn.color("red")

        btn.write(letter, align="center", font=("Arial", 18, "bold"))

        # Save button position
        letter_buttons[letter] = (x, y)

    screen.update()   # redraw all at once

def draw_restart_button(cx=0, cy=-250, width=140, height=50,
                        border_color="black", fill_color="lightgrey",
                        text="Restart", text_color="red",
                        font=("Arial", 20, "bold"),
                        vert_offset_factor=0.45):
    """
    Draw a centered restart button and compute a bounding box for clicks.
    cx, cy = center coordinates of the button.
    vert_offset_factor = fraction of the font size to move text DOWN (tweak if needed).
    """
    global restart_box
    restart_writer.clear()
    restart_writer.penup()

    # Compute top-left corner from center
    x1 = cx - width / 2
    y1 = cy - height / 2

    # Ensure heading is standard so rectangle draws predictably
    restart_writer.setheading(0)
    restart_writer.goto(x1, y1)
    restart_writer.pendown()
    restart_writer.color(border_color, fill_color)
    restart_writer.begin_fill()
    for _ in range(2):
        restart_writer.forward(width)
        restart_writer.left(90)
        restart_writer.forward(height)
        restart_writer.left(90)
    restart_writer.end_fill()
    restart_writer.penup()

    # compute text vertical position: horizontally centered; vertically adjusted down
    font_size = font[1] if isinstance(font, tuple) and len(font) >= 2 else 20
    y_text = cy - (font_size * vert_offset_factor)

    restart_writer.goto(cx, y_text)
    restart_writer.color(text_color)
    restart_writer.write(text, align="center", font=font)

    # save bounding box for click detection (x1, y1, x2, y2)
    restart_box = (x1, y1, x1 + width, y1 + height)


def hide_restart_button():
    """Clear restart button."""
    global restart_box
    restart_writer.clear()
    restart_box = None

def start_game():
    """Initialize a new game."""
    global chosen_word, chosen_word_list, word_to_guess, l, parts, game_over, used_letters
    hint_writer.clear()
    word_writer.clear()
    status_writer.clear()
    result_writer.clear()
    restart_writer.clear()

    game_over = False
    used_letters = set()
    drawer.draw_gallows()

    # Pick a random word and hint from the dictionary; normalize to UPPERCASE
    chosen_word, hint = random.choice(list(words.items()))
    chosen_word = str(chosen_word).strip().upper()
    chosen_word_list = list(chosen_word)

    # Show underscores for letters, but keep spaces/punctuation visible
    word_to_guess = [ch if not ch.isalpha() else "_" for ch in chosen_word_list]

    # Display hint and word
    display_text(hint_writer, f"Hint: {hint}", 0, 280, 20, "blue")
    display_text(word_writer, " ".join(word_to_guess), 0, 200, 30, "black")

    # Parts of hangman (order)
    parts = [
        drawer.draw_head,
        drawer.draw_body,
        drawer.draw_left_arm,
        drawer.draw_right_arm,
        drawer.draw_left_leg,
        drawer.draw_right_leg,
    ]
    l = 0

    # Draw buttons
    draw_buttons()

def check_guess(letter):
    """Handle a guessed letter."""
    global l, game_over
    if game_over:
        return

    letter = letter.upper()  # ensure consistency

    if letter not in chosen_word_list:
        display_text(status_writer, "Wrong Guess!", 0, 150, 18, "red")
        if l < len(parts):
            parts[l]()
        l += 1
    else:
        for pos, char in enumerate(chosen_word_list):
            if char == letter:
                word_to_guess[pos] = letter
        display_text(status_writer, "Correct Guess!", 0, 150, 18, "green")

    # Update word display
    display_text(word_writer, " ".join(word_to_guess), 0, 200, 30, "black")

    # Win/Loss conditions
    if "_" not in word_to_guess:
        display_text(result_writer, f"🎉 You Win! Word: {chosen_word}", 0, -200, 24, "green")
        draw_restart_button()
        game_over = True
    elif l >= len(parts):
        display_text(result_writer, f"💀 You Lose! Word: {chosen_word}", 0, -200, 24, "red")
        draw_restart_button()
        game_over = True

def click_handler(x, y):
    global used_letters

    # Restart button click
    if game_over and restart_box:
        x1, y1, x2, y2 = restart_box
        if x1 <= x <= x2 and y1 <= y <= y2:
            hide_restart_button()
            start_game()
            return

    # Letter buttons click
    for letter, (bx, by) in letter_buttons.items():
        if abs(x - bx) < 20 and abs(y - by) < 20:
            if letter in used_letters:
                return
            used_letters.add(letter)
            check_guess(letter)
            draw_buttons()  # redraw buttons after guess
            return

# -----------------------------
# Main
# -----------------------------
start_game()
screen.onclick(click_handler)
turtle.done()
