from manim import *


class MObjectGradient(Scene):
    def construct(self):
        dots = VGroup(*[Dot(radius=0.1) for i in range(100)])
        dots.arrange_in_grid(rows=10, cols=10)
        dots.set_colors_by_radial_gradient(radius=2.0, inner_color=BLUE, outer_color=PINK)
        self.add(dots)

class TextGradient(Scene):
    def construct(self):
        text = Tex("Hello, World!").set_color_by_gradient(PINK, BLUE, PURPLE)
        self.add(text)