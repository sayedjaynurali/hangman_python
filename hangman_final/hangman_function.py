from turtle import Turtle

class Hangman_Drawing:

    def __init__(self):
        self.tim = Turtle()
        self.tim.shape("turtle")
        self.tim.shapesize(1.5)  
    
    def draw_gallows(self):
        self.tim.reset()   # Reset heading and clear everything from this turtle only
        self.tim.hideturtle()
        self.tim.speed(0)

        self.tim.penup()
        self.tim.goto(-100, -150)
        self.tim.pendown()
        self.tim.forward(200)     
        self.tim.back(100)
        self.tim.left(90)
        self.tim.forward(300)     
        self.tim.right(90)
        self.tim.forward(100)     
        self.tim.right(90)
        self.tim.forward(50)
     
    
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
        self.tim.back(40)
        self.tim.left(45)
        self.tim.forward(50)
        self.tim.back(50)
        self.tim.right(45)

    def draw_right_arm(self):
        self.tim.right(45)
        self.tim.forward(50)
        self.tim.back(50)
        self.tim.left(45)

    def draw_left_leg(self):
        self.tim.forward(40)
        self.tim.left(30)
        self.tim.forward(60)
        self.tim.back(60)
        self.tim.right(30)

    def draw_right_leg(self):
        self.tim.right(30)
        self.tim.forward(60)
        self.tim.back(60)
        self.tim.left(30)


words = {
    'algebra': "I speak with letters, but I always mean numbers. Who am I?",
    'algorithm': "I'm a recipe, not for food but for solutions.",
    'angle': "I measure the turn when two lines decide to meet.",
    'area': "I tell you how much paint you need to cover the floor.",
    'asymptote': "Get close to me forever, but touch me never.",
    'axiom': "I'm accepted without question, the foundation of proofs.",
    'binomial': "I come in twos, always side by side with a plus or minus.",
    'calculus': "I watch things change, faster and slower, smaller and bigger.",
    'circle': "I'm round and endless, with no beginning or end.",
    'coefficient': "I stand in front of the variable, silent but powerful.",
    'combinatorics': "I count without numbers — arrangements, choices, possibilities.",
    'complex': "I'm part real, part imaginary, and fully mysterious.",
    'cone': "I'm pointed at the top and round at the bottom, like an ice-cream.",
    'congruence': "I mirror another shape perfectly — twins in geometry.",
    'cosine': "I hide beside the hypotenuse, always adjacent.",
    'cylinder': "I'm like a soda can — circles on top and bottom, smooth in between.",
    'denominator': "I always sit at the bottom of the fraction throne.",
    'derivative': "I'm the slope's shadow, the instant change at a point.",
    'determinant': "A square holds me, but I reduce it to one secret number.",
    'diameter': "Stretch me across the circle, through the very heart.",
    'dimension': "You feel me in 3D, but math can imagine many more.",
    'distribution': "I scatter values across a range — sometimes normal, sometimes not.",
    'divisor': "I divide without leaving a trace.",
    'eigenvalue': "Vectors listen to me: I tell them how much to stretch.",
    'ellipse': "I'm not quite a circle — two foci keep me balanced.",
    'equation': "Two sides of me must always agree.",
    'exponent': "I sit high and make numbers explode or shrink.",
    'factorial': "I multiply down to 1, leaving huge numbers behind.",
    'fibonacci': "I grow by remembering my last two steps.",
    'fraction': "I'm not whole — just a piece of the pie.",
    'function': "Feed me input, and I'll always spit out output.",
    'geometry': "I'm the art of shapes and the logic of space.",
    'gradient': "I tilt the line and show its steepness.",
    'graph': "Draw me and you'll see the math come alive.",
    'hypotenuse': "I'm the proudest, longest side in a right triangle.",
    'identity': "I hold true no matter the number — always loyal.",
    'imaginary': "I'm unreal, but without me, math feels incomplete.",
    'inequality': "I never settle for equal — I prefer greater or less.",
    'infinity': "No end, no limit, just forever.",
    'integral': "I gather tiny pieces into a whole — the area beneath curves.",
    'intersection': "I'm where two sets shake hands.",
    'inverse': "I undo what's been done — the great reverser.",
    'irrational': "I never repeat, I never end, but I'm very real.",
    'isosceles': "Two sides of me can't help but be equal.",
    'limit': "I'm what you approach but might never reach.",
    'line': "I stretch forever but never bend.",
    'logarithm': "I ask: 'Power, what number raised to you gives me this?'",
    'logic': "I'm reason's language: true or false, nothing in between.",
    'manifold': "Locally flat, globally strange — I'm the stage of modern geometry.",
    'matrix': "Rows and columns lock me up, but I hold infinite power.",
    'mean': "I balance numbers by being their average.",
    'median': "I'm the middle child of the data family.",
    'mode': "I love popularity — I appear the most.",
    'modulus': "I don't care about direction — only size matters to me.",
    'multiple': "I'm born when numbers repeat themselves by multiplication.",
    'negative': "I live below zero, always opposite of positive.",
    'normal': "I'm perpendicular to surfaces, always standing tall.",
    'numerator': "I sit on top of the fraction, proud and visible.",
    'octagon': "I wear eight sides like a crown.",
    'parallel': "We walk side by side but never meet.",
    'parabola': "Throw a ball, and I'll show you its path.",
    'parameter': "I'm the secret setting that changes everything in a formula.",
    'perimeter': "I measure how far it is to walk around me.",
    'permutation': "I care about order — who sits where matters to me.",
    'pi': "I'm endless, irrational, and the circle is my playground.",
    'plane': "I'm flat and endless — like an invisible sheet of paper.",
    'point': "I have no size, yet I exist.",
    'polygon': "I'm many-sided, from triangles to decagons.",
    'polynomial': "I'm a sum of powers, always loyal to my variables.",
    'prime': "I'm indivisible, except by 1 and myself.",
    'probability': "I whisper the odds of what might happen.",
    'product': "I'm born when numbers are multiplied.",
    'proof': "I convince the world with logic, no doubts allowed.",
    'proportion': "I keep two ratios in perfect harmony.",
    'pyramid': "I point to the sky, resting on a polygon base.",
    'quadratic': "I'm always squared, and I curve into a U-shape.",
    'quartile': "I slice data into four equal pieces.",
    'quotient': "I'm the answer you seek when you divide.",
    'radical': "I'm the root of all problems — literally.",
    'radius': "From the circle's heart to its edge, that's me.",
    'random': "Predict me if you can — you can't!",
    'range': "I measure the spread between high and low.",
    'ratio': "I compare two numbers in simplest form.",
    'rectangle': "I'm a quadrilateral with right angles everywhere.",
    'rhombus': "All my sides agree — equal in length.",
    'scalar': "I'm just a number, no direction attached.",
    'sequence': "I'm numbers in a line, each following the rules.",
    'set': "I gather distinct objects into one family.",
    'sigma': "The Greek who loves summing everything up.",
    'sine': "I rise opposite to the angle, loyal to right triangles.",
    'sphere': "I'm a ball, perfectly round in 3D space.",
    'square': "All my sides are equal, all my corners right.",
    'statistics': "I give meaning to data and numbers in the real world.",
    'subtraction': "I take away and leave what's left.",
    'sum': "I'm the total you get after adding up.",
    'symmetry': "Flip me, turn me, reflect me — I still look the same.",
    'tangent': "I touch the curve at one single, perfect point.",
    'theorem': "I'm a truth proven by reason, not assumption.",
    'topology': "I care about holes, not shapes — a donut is my favorite.",
    'triangle': "With three sides, I'm the simplest polygon.",
    'vector': "I march with both size and direction.",
    'vertex': "I'm where edges meet, sharp and clear.",
    'volume': "I tell you how much space a 3D object takes."
}

