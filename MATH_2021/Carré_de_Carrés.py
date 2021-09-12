% % manim
Carre


class Carre(Scene):
    def construct(self):
        model = MathTex("\sum_{i=1} i^{2}", "=", "1^{2}+2^{2}+3^{2}+\ldots+n^{2}")
        n = MathTex("n")
        n.next_to(model[0], UP)
        n.shift(LEFT * 0.2)

        self.play(Write(model[0]),
                  Write(n))
        self.wait()

        self.play(Write(model[1:]))
        self.wait()

        four = MathTex("4", color=YELLOW)
        four.move_to(n)
        self.play(Transform(n, four))
        self.wait()

        model_4 = MathTex("1^{2}+2^{2}+3^{2}+4^{2}", substrings_to_isolate="4")
        model_4.set_color_by_tex("4", YELLOW)
        model_4.move_to(model[2])
        self.play(Transform(model[2], model_4))
        self.wait()

        eq = MathTex('= ')
        eq.next_to(model_4)

        model_4_result = MathTex("30", color=GREEN)
        model_4_result.next_to(eq)
        self.play(Write(eq), Write(model_4_result))
        self.wait()

        hundred = MathTex("100", color=YELLOW)
        hundred.move_to(four)
        self.play(Transform(n, hundred))
        self.wait()

        model_100 = MathTex("1^{2}+2^{2}+3^{2}+\ldots+", "100^", "{2}")
        model_100[1].set_color(YELLOW)
        model_100.move_to(model_4)
        self.play(Transform(model[2], model_100),
                  FadeOut(eq, shift=RIGHT),
                  FadeOut(model_4_result, shift=RIGHT))
        self.wait()

        eq.next_to(model_100)
        model_100_result = MathTex("338350", color=GREEN)
        model_100_result.next_to(eq)
        self.play(Write(eq), Write(model_100_result))
        self.wait()