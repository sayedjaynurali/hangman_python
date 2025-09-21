import turtle
from game import HangmanGame

def main():
    screen = turtle.Screen()
    screen.title("Hangman Game")
    screen.setup(width=1000, height=700)
    screen.bgcolor("white")
    screen.tracer(0)

    game = HangmanGame(screen)
    game.start_game()

    screen.onclick(game.click_handler)
    turtle.done()

if __name__ == "__main__":
    main()
