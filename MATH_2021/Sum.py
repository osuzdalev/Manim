% % manim
Sum


class Sum(Scene):
    def construct(self):
        s = MathTex("\int", "xdx")
        self.play(Write(s))

        self.wait()

        self.add(s.set_color_by_tex("\int", YELLOW))

        self.wait()

        self.play(s[0].animate.shift(LEFT * 4))

        self.wait()

        somme = Text("Somme", t2c={'S': YELLOW})
        S = Text("S", color=YELLOW)
        S.move_to(s[0])

        self.play(Transform(s[0], S))

        self.wait()

        omme = Text("omme")
        omme.next_to(S)

        self.play(Write(omme))
        self.wait()

        la = Text("La")
        de = Text("de")

        la.next_to(S, LEFT)
        de.next_to(omme)

        self.play(
            Write(la),
            Write(de))

        self.wait()