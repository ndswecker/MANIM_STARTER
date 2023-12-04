from manim import *

class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number, **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        #Set value of DecimalNumber according to alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)

class CountingScene(Scene):
    def construct(self):
        # Create the decimal number and add it to the scene
        number = DecimalNumber().set_color(WHITE).scale(5)
        # Add an updater to keep the decimal number centered as its value changes
        number.add_updater(lambda number: number.move_to(ORIGIN))

        self.add(number)
        self.wait() # Default 1 second I presume
        
        #Play the count animation to count from 0 to 100 in 4 seconds
        self.play(Count(number, 0, 100), run_time=4, rate_func=linear)

        self.wait()