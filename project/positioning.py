from manim import *
from manim.utils.unit import Percent, Pixels

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
        
        sq = Square(color=RED, fill_opacity=0.5)
        sq.move_to([1,1,0], aligned_edge=DOWN)
        self.add(sq)

class UsefulUnits(Scene):
    def construct(self):
        for perc in range(5, 51, 5):
            self.add(Circle(radius=perc*Percent(X_AXIS)))
            self.add(Square(side_length=2*perc*Percent(X_AXIS), color=YELLOW))
        
        dot = Dot().shift(100*Pixels*RIGHT)
        self.add(dot)

class Grouping(Scene):
    def construct(self):
        dot_red = Dot(color=RED)
        dot_green = Dot(color=GREEN).next_to(dot_red, RIGHT)
        dot_blue = Dot(color=BLUE).next_to(dot_red, UP)
        dot_group = VGroup(dot_red, dot_green, dot_blue)
        dot_group.to_edge(RIGHT)
        self.add(dot_group)

        circles = VGroup(*[Circle(radius=0.2) for _ in range(10)])
        circles.arrange(UP, buff=0.5)
        self.add(circles)

        stars = VGroup(*[Star(color=YELLOW, fill_opacity=0.9).scale(0.5) for _ in range(20)])
        stars.arrange_in_grid(4, 5, buff=0.2)
        self.add(stars)