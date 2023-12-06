from manim import *

class Positioning(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)

        # next to
        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN)
        green_dot.next_to(red_dot, RIGHT)

        self.add( red_dot, green_dot)

        # shift
        sq = Square(color=ORANGE)
        sq.shift(2*UP + 4*RIGHT)
        self.add(sq)

        # move to default anchor point center of object
        circle = Circle(color=PURPLE)
        circle.move_to([-3, -2, 0])
        self.add(circle)

        # align to
        circle2 = Circle(radius=0.5, color=RED, fill_opacity=0.5)
        circle3 = circle2.copy().set_color(YELLOW)
        circle4 = circle2.copy().set_color(ORANGE)
        circle2.align_to(sq, UP)
        circle3.align_to(sq, RIGHT)
        circle4.align_to(sq, UP + RIGHT)
        self.add(circle2, circle3, circle4)

class CriticalPoints(Scene):
    def construct(self):
        c = Circle(color=GREEN, fill_opacity=0.5)
        self.add(c)

        for d in [(0,0,0), UP, UR, RIGHT, DR, DOWN, DL ,LEFT, UL]:
            self.add(Cross(scale_factor=0.2).move_to(c.get_critical_point(d)))
