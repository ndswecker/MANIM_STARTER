from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle() # Here we create the circle object
        circle.set_fill(PINK, opacity=0.5) # Set the inside of the object as pink and semi transparent

        square = Square() # I summon a square!
        square.rotate(PI / 4) # I think we rotate square a quarter turn...
        
        self.play(Create(square)) # This should animate the square creation
        self.play(Transform(square,circle)) # Magically transforms square to circle
        self.play(FadeOut(square)) # banish the square back to whence it came

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.set_fill(BLUE, opacity=0.5)
        square.next_to(circle, RIGHT, buff=0.5) # Setting the position of the square
        self.play(Create(circle), Create(square)) # Display the shapes