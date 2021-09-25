from manim import *


class Phi(Scene):
    def construct(self):
        phi = MathTex("\Phi").set_color(GOLD).scale(8)
        circle = Circle().scale(3.5)

        dot = Dot(color=GOLD).move_to(circle.get_start())
        trace = TracedPath(dot.get_center, dissipating_time=1, stroke_opacity=[0, 1]).set_color(GOLD).set_stroke(width=3)

        rotations = []
        for i in range(30):
            rotations.append(MoveAlongPath(dot, circle))

        self.add(trace)
        self.play(Write(phi), run_time=2)
        for i in range(len(rotations)):
            self.play(rotations[i], run_time=2, rate_func=linear)