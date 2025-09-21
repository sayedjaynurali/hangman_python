import random
from drawing import HangmanDrawing
from words import words
from ui import UIManager

class HangmanGame:
    def __init__(self, screen):
        self.screen = screen
        self.drawer = HangmanDrawing()
        self.ui = UIManager(screen)

        self.chosen_word = ""
        self.chosen_word_list = []
        self.word_to_guess = []
        self.parts = []
        self.l = 0
        self.used_letters = set()
        self.game_over = False

    def start_game(self):
        """Initialize new game"""
        self.ui.hint_writer.clear()
        self.ui.word_writer.clear()
        self.ui.status_writer.clear()
        self.ui.result_writer.clear()
        self.ui.restart_writer.clear()

        self.game_over = False
        self.used_letters = set()
        self.drawer.draw_gallows()

        self.chosen_word, hint = random.choice(list(words.items()))
        self.chosen_word = str(self.chosen_word).strip().upper()
        self.chosen_word_list = list(self.chosen_word)
        self.word_to_guess = [ch if not ch.isalpha() else "_" for ch in self.chosen_word_list]

        self.ui.display_text(self.ui.hint_writer, f"Hint: {hint}", 0, 280, 20, "blue")
        self.ui.display_text(self.ui.word_writer, " ".join(self.word_to_guess), 0, 200, 30, "black")

        self.parts = [
            self.drawer.draw_head,
            self.drawer.draw_body,
            self.drawer.draw_left_arm,
            self.drawer.draw_right_arm,
            self.drawer.draw_left_leg,
            self.drawer.draw_right_leg,
        ]
        self.l = 0
        self.ui.draw_buttons(self.used_letters)

    def check_guess(self, letter):
        """Handle a guessed letter"""
        if self.game_over:
            return

        letter = letter.upper()
        if letter not in self.chosen_word_list:
            self.ui.display_text(self.ui.status_writer, "Wrong Guess!", 0, 150, 18, "red")
            if self.l < len(self.parts):
                self.parts[self.l]()
            self.l += 1
        else:
            for pos, char in enumerate(self.chosen_word_list):
                if char == letter:
                    self.word_to_guess[pos] = letter
            self.ui.display_text(self.ui.status_writer, "Correct Guess!", 0, 150, 18, "green")

        self.ui.display_text(self.ui.word_writer, " ".join(self.word_to_guess), 0, 200, 30, "black")

        if "_" not in self.word_to_guess:
            self.ui.display_text(self.ui.result_writer, f"🎉 You Win! Word: {self.chosen_word}", 0, -200, 24, "green")
            self.ui.draw_restart_button()
            self.game_over = True
        elif self.l >= len(self.parts):
            self.ui.display_text(self.ui.result_writer, f"💀 You Lose! Word: {self.chosen_word}", 0, -200, 24, "red")
            self.ui.draw_restart_button()
            self.game_over = True

    def click_handler(self, x, y):
        if self.game_over and self.ui.restart_box:
            x1, y1, x2, y2 = self.ui.restart_box
            if x1 <= x <= x2 and y1 <= y <= y2:
                self.ui.hide_restart_button()
                self.start_game()
                return

        for letter, (bx, by) in self.ui.letter_buttons.items():
            if abs(x - bx) < 20 and abs(y - by) < 20:
                if letter in self.used_letters:
                    return
                self.used_letters.add(letter)
                self.check_guess(letter)
                self.ui.draw_buttons(self.used_letters)
                return
