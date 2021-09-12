from manim import *


class Coefs(Scene):
    def construct(self):
        #                      0     1   2   3
        equation = MathTex("---", "x", "---", "y", "=", "1")
        x_coef = DecimalNumber(1)
        y_coef = DecimalNumber(1,include_sign=True)
        for i,mob in zip([0,2],[x_coef,y_coef]):
            mob.move_to(equation[i])
            equation[i].fade(1)
        self.add(equation,x_coef,y_coef)
        self.play(
            ChangeDecimalToValue(x_coef,3),
        )
        self.wait()
        self.play(
            ChangeDecimalToValue(y_coef,6),
        )
        self.wait()
        self.play(
            ChangeDecimalToValue(x_coef,2),
            ChangeDecimalToValue(y_coef,-7),
        )
        self.wait()