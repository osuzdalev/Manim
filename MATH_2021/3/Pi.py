# %% manim Pi


class Pi(Scene):
    def construct(self):
        police_num = MathTex("17").scale(10)
        self.play(Write(police_num))
        self.wait()

        police = Text("Police", color=BLUE).scale(3)
        self.play(Transform(police_num, police), run_time=2)
        self.wait()

        self.play(FadeOut(police_num))

        pompier_num = MathTex("18").scale(10)
        self.play(Write(pompier_num))
        self.wait()

        pompier = Text("Pompier", color=RED).scale(3)
        self.play(Transform(pompier_num, pompier), run_time=2)
        self.wait()

        self.play(FadeOut(pompier_num))

        pi_text = Text(
            "3.14159265358979 \n 323846264338327 \n 950288419716939 \n 937510582097494 \n 459230781640628 \n 620899862803482 ").scale(
            2).to_corner(LEFT, UP)
        self.play(Write(pi_text), run_time=3)
        self.wait()

        pi_sym = MathTex("\pi").scale(10)

        self.play(Transform(pi_text, pi_sym), run_time=2)
        self.wait()