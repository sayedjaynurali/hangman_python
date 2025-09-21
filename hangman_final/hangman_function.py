from turtle import Turtle

class Hangman_Drawing:

    def __init__(self):
        self.tim = Turtle()
        self.tim.shape("turtle")
        self.tim.shapesize(1.5)  # make turtle bigger (5 was too large)
    
    # Function to draw base structure
    def draw_gallows(self):
        self.tim.penup()
        self.tim.goto(-100, -150)
        self.tim.pendown()
        self.tim.forward(200)     # Base
        self.tim.backward(100)
        self.tim.left(90)
        self.tim.forward(300)     # Pole
        self.tim.right(90)
        self.tim.forward(100)     # Beam
        self.tim.right(90)
        self.tim.forward(50)      # Rope
    
    # Functions for each hangman part
    def draw_head(self):
        self.tim.right(90)
        self.tim.circle(25)

    def draw_body(self):
        self.tim.left(90)
        self.tim.penup()
        self.tim.forward(50)
        self.tim.pendown()
        self.tim.forward(80)

    def draw_left_arm(self):
        self.tim.backward(40)
        self.tim.left(45)
        self.tim.forward(50)
        self.tim.backward(50)
        self.tim.right(45)

    def draw_right_arm(self):
        self.tim.right(45)
        self.tim.forward(50)
        self.tim.backward(50)
        self.tim.left(45)

    def draw_left_leg(self):
        self.tim.forward(40)
        self.tim.left(30)
        self.tim.forward(60)
        self.tim.backward(60)
        self.tim.right(30)

    def draw_right_leg(self):
        self.tim.right(30)
        self.tim.forward(60)
        self.tim.backward(60)
        self.tim.left(30)


words = ["apple", "banana", "cherry", "grape", "orange", "peach", "pear", "plum", "kiwi", "melon", "avocado", "apricot", "mango", "papaya", "pineapple", "strawberry", "blueberry", "raspberry", "blackberry", "watermelon", "coconut", "lemon", "lime", "tangerine", "nectarine", "dog", "cat", "mouse", "rat", "rabbit", "hamster", "horse", "cow", "goat", "sheep", "pig", "lion", "tiger", "bear", "elephant", "giraffe", "zebra", "monkey", "kangaroo", "koala", "self.timguin", "dolphin", "shark", "whale", "octopus", "crab", "lobster", "seal", "wolf", "fox", "car", "truck", "bus", "bicycle", "motorcycle", "train", "airplane", "helicopter", "boat", "submarine", "scooter", "skateboard", "van", "jeep", "tram", "ferry", "yacht", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white", "gray", "violet", "indigo", "turquoise", "magenta", "beige", "python", "java", "ruby", "javascript", "html", "css", "kotlin", "swift", "golang", "typescript", "react", "flask", "django", "angular", "node", "express", "sql", "mongodb", "cloud", "storm", "rain", "snow", "hail", "thunder", "lightning", "sunshine", "fog", "mist", "breeze", "tornado", "hurricane", "blizzard", "wind", "mountain", "valley", "river", "ocean", "lake", "desert", "forest", "jungle", "island", "beach", "volcano", "cave", "glacier", "hill", "plain", "cliff", "school", "teacher", "student", "classroom", "homework", "exam", "library", "notebook", "self.timcil", "eraser", "chalk", "ruler", "backpack", "desk", "blackboard", "music", "guitar", "piano", "violin", "drums", "trumpet", "flute", "saxophone", "cello", "clarinet", "microphone", "speaker", "headphones", "song", "melody", "rhythm", "lyrics", "football", "basketball", "baseball", "soccer", "tennis", "hockey", "cricket", "golf", "swimming", "running", "cycling", "boxing", "wrestling", "skiing", "snowboarding", "surfing", "science", "physics", "chemistry", "biology", "geology", "astronomy", "zoology", "botany", "ecology", "genetics", "robotics", "computer", "quantum", "energy", "gravity", "space", "planet", "earth", "mars", "venus", "jupiter", "saturn", "uranus", "neptune", "galaxy", "comet", "asteroid", "meteor", "universe", "rocket", "spaceship", "satellite", "happy", "sad", "angry", "excited", "bored", "tired", "scared", "brave", "curious", "nervous", "joyful", "hopeful", "proud", "grateful", "calm", "relaxed", "castle", "knight", "dragon", "sword", "wizard", "magic", "princess", "kingdom", "throne", "crown", "shield", "battle", "treasure", "dungeon", "giant", "goblin", "witch", "potion"]

hangman_ascii = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\\  |   
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |  
      |
=========''']
