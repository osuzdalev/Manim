from manim import *


class Transform(Scene):
    def construct(self):
        a = MathTex("TEST")
        b = DecimalNumber(include_sign=True)

        self.play(Create(b))
        self.wait()
        self.play(Transform(b, a))
        self.wait()