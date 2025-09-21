import turtle

class UIManager:
    def __init__(self, screen):
        self.screen = screen
        self.hint_writer = self._make_writer()
        self.word_writer = self._make_writer()
        self.status_writer = self._make_writer()
        self.result_writer = self._make_writer()
        self.restart_writer = self._make_writer()

        self.letter_buttons = {}
        self.restart_box = None

    def _make_writer(self):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        return t

    def display_text(self, writer, message, x, y, size=18, color="black", align="center"):
        writer.clear()
        writer.goto(x, y)
        writer.color(color)
        writer.write(message, align=align, font=("Arial", size, "bold"))

    def draw_buttons(self, used_letters):
        """Draw clickable A-Z letter buttons."""
        for btn in self.letter_buttons.values():
            btn.clear() if isinstance(btn, turtle.Turtle) else None
        self.letter_buttons = {}

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
            btn.speed(0)
            btn.penup()
            btn.goto(x, y)

            btn.color("grey" if letter in used_letters else "red")
            btn.write(letter, align="center", font=("Arial", 18, "bold"))

            self.letter_buttons[letter] = (x, y)

        self.screen.update()

    def draw_restart_button(self, cx=0, cy=-250, width=140, height=50,
                            border_color="black", fill_color="lightgrey",
                            text="Restart", text_color="red",
                            font=("Arial", 20, "bold"),
                            vert_offset_factor=0.45):
        self.restart_writer.clear()
        self.restart_writer.penup()

        x1 = cx - width / 2
        y1 = cy - height / 2
        self.restart_writer.setheading(0)
        self.restart_writer.goto(x1, y1)
        self.restart_writer.pendown()
        self.restart_writer.color(border_color, fill_color)
        self.restart_writer.begin_fill()
        for _ in range(2):
            self.restart_writer.forward(width)
            self.restart_writer.left(90)
            self.restart_writer.forward(height)
            self.restart_writer.left(90)
        self.restart_writer.end_fill()
        self.restart_writer.penup()

        font_size = font[1] if isinstance(font, tuple) and len(font) >= 2 else 20
        y_text = cy - (font_size * vert_offset_factor)

        self.restart_writer.goto(cx, y_text)
        self.restart_writer.color(text_color)
        self.restart_writer.write(text, align="center", font=font)

        self.restart_box = (x1, y1, x1 + width, y1 + height)

    def hide_restart_button(self):
        self.restart_writer.clear()
        self.restart_box = None
