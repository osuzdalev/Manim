# %% manim Fraction


class Fraction(Scene):
    def construct(self):
        eq = MathTex("{\sqrt{4}", "+", "\ln{(1)}", "+", "2^2", "\\over", "\sum_{i=1} ^3 i}").scale(1.5)
        self.play(Write(eq), run_time=1)
        self.wait()
        self.play(eq.animate.to_edge(LEFT))
        self.wait()

        sqrt = MathTex("\sqrt{4}", "=", "2").to_edge(UP).shift(RIGHT * 2).scale(1.5)
        ln = MathTex("\ln{(1)}", "=", "0").next_to(sqrt, DOWN * 3).shift(RIGHT * 0.5).scale(1.5)
        sq = MathTex("2^2", "=", "2\cdot2", "=", "4").next_to(sqrt, DOWN * 8).scale(1.5)
        over = MathTex("\\over", "=>", "\div").next_to(sqrt, DOWN * 14).scale(1.5).shift(LEFT)
        sigma = MathTex("\sum_{i=1} ^3 i", "=", "1 + 2 + 3", "=", "6").next_to(sqrt, DOWN * 16).scale(1.5)

        # Symbole pour des valeurs
        self.play(ReplacementTransform(eq[4].copy(), sq[0]))
        self.wait()
        self.play(Write(sq[1:3]))
        self.wait()
        self.play(Write(sq[3:]))
        self.wait()

        self.play(ReplacementTransform(eq[0].copy(), sqrt[0]))
        self.wait()
        self.play(Write(sqrt[1:]))
        self.wait()

        self.play(ReplacementTransform(eq[2].copy(), ln[0]))
        self.wait()
        self.play(Write(ln[1:]))
        self.wait()

        # Symbole pour des opérations
        self.play(ReplacementTransform(eq[5].copy(), over[0]))
        self.wait()
        self.play(Write(over[1:].next_to(over[0], RIGHT)))
        self.wait()

        self.play(ReplacementTransform(eq[6].copy(), sigma[0]))
        self.wait()
        self.play(Write(sigma[1]),
                  Write(sigma[2][1::2]))
        self.wait()
        self.play(Write(sigma[2][0::2]))
        self.wait()
        self.play(Write(sigma[3:]))
        self.wait()

        # Placement de valeurs

        eq_copy = MathTex("{2", "+", "0", "+", "4", "\\over", "6}").move_to(eq).scale(1.5)

        self.play(Transform(eq[0], eq_copy[0]),
                  ReplacementTransform(sqrt[-1].copy(), eq_copy[0]),
                  Transform(eq[1], eq_copy[1]),
                  Transform(eq[2], eq_copy[2]),
                  ReplacementTransform(ln[-1].copy(), eq_copy[2]),
                  Transform(eq[3], eq_copy[3]),
                  Transform(eq[4], eq_copy[4]),
                  ReplacementTransform(sq[-1].copy(), eq_copy[4]),
                  Transform(eq[5], eq_copy[5]),
                  ReplacementTransform(over[0].copy(), eq_copy[5]),
                  Transform(eq[6], eq_copy[6]),
                  ReplacementTransform(sigma[-1].copy(), eq_copy[6])
                  )
        self.wait()

        self.play(FadeOut(sqrt),
                  FadeOut(ln),
                  FadeOut(sq),
                  FadeOut(over),
                  FadeOut(sigma))

        eq_1 = MathTex("=", "{6", "\\over", "6}", "=", "1").next_to(eq_copy, RIGHT * 2).scale(1.5)
        self.play(Write(eq_1[:4]))
        self.wait()
        self.play(Write(eq_1[4:]))