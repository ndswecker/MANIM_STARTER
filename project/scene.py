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

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(Create(square)) # Display the square
        self.play(square.animate.rotate(PI / 4)) # Rotate square as an animation
        self.play(ReplacementTransform(square,circle)) # transforms the square into the circle as an animation
        self.play(circle.animate.set_fill(PINK, opacity=0.5)) # Fills in the circle as an animation

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2*LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2*RIGHT)
        # self.play(left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2)
        self.play(Rotate(left_square, angle=(2*PI)), Rotate(right_square, angle=PI),run_time=2)
        self.wait()

class Movement(Scene):
    def construct(self):
        car = Square(color=TEAL, fill_opacity=0.8).shift(4*LEFT)
        self.play(Create(car), run_time=4)
        self.wait(2)
        self.play(car.animate.shift(4*RIGHT), run_time=4)
