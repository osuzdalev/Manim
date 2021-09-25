# %% manim Pi


class Pi(Scene):
    def construct(self):
        circle = Circle(radius=2, color=BLUE, fill_opacity=0)
        dot = Dot()

        perimeter = MathTex("2 \pi r").next_to(circle, UP * 2).scale(2)

        area = MathTex("\pi r^2", color=BLACK).scale(2)

        self.play(Create(circle))
        self.play(Write(perimeter))
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.play(FadeOut(dot))

        self.play(circle.animate.set_fill(color=BLUE, opacity=1))

        self.play(Write(area))
        self.wait()