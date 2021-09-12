from manim import *


class Decimals(Scene):
    def construct(self):
        decimal_1 = MathTex("{5 \over 3}", "=", "1.", "66666666666666666", "...")
        self.play(Write(decimal_1))
        self.wait()

        self.play(decimal_1[:3].animate.shift(LEFT),
                  FadeOut(decimal_1[-1]))
        self.wait()

        self.play(decimal_1[3][0].animate.set_color(YELLOW))
        self.wait()

        self.play(decimal_1[3][1].animate.set_color(YELLOW))
        self.wait()

        self.play(decimal_1[3][2].animate.set_color(YELLOW))
        self.wait()

        self.play(decimal_1[3][3:].animate.set_color(YELLOW))
        self.wait()

        self.play(decimal_1[:-1].animate.shift(UP * 3))
        self.wait()

        decimal_2 = MathTex("{23 \over 11}", "=", "2.", "0909090909090909", "...")
        self.play(Write(decimal_2))
        self.wait()

        self.play(decimal_2[:3].animate.shift(LEFT),
                  FadeOut(decimal_2[-1]))
        self.wait()

        self.play(decimal_2[3][:2].animate.set_color(YELLOW))
        self.wait()

        self.play(decimal_2[3][2:4].animate.set_color(YELLOW))
        self.wait()

        self.play(decimal_2[3][4:6].animate.set_color(YELLOW))
        self.wait()

        self.play(decimal_2[3][3:].animate.set_color(YELLOW))
        self.wait()

        self.play(decimal_2[:-1].animate.shift(UP * 1.5))
        self.wait()

        decimal_3 = MathTex("{22 \over 7}", " = ", "3.", "142857", "142857", "142857", "...")
        self.play(Write(decimal_3))
        self.wait()

        self.play(decimal_3[:3].animate.shift(LEFT),
                  FadeOut(decimal_3[-1]))
        self.wait()

        self.play(decimal_3[4].animate.shift(RIGHT),
                  decimal_3[5].animate.shift(RIGHT * 2))
        self.wait()

        self.play(decimal_3[3].animate.set_color(YELLOW))
        self.wait()
        self.play(decimal_3[4].animate.set_color(YELLOW))
        self.wait()
        self.play(decimal_3[5].animate.set_color(YELLOW))
        self.wait()

        self.play(decimal_3[:-1].animate.shift(DOWN * 3))
        self.wait()

        pi = MathTex("\pi", "=", "3.", "141592653589793", "...")
        self.play(Write(pi))
        self.wait()

        self.play(pi[:3].animate.shift(LEFT),
                  FadeOut(pi[-1]))
        self.wait()

        self.play(pi[3].animate.set_color(RED))
        self.wait()
