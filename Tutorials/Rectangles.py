from manim import *
import math


class Rect(Scene):
    def construct(self):
        rect = Rectangle(height=0.5, width=0.5, fill_opacity=1)
        rect.set_color(color=[PINK,YELLOW])
        rect.set_stroke(width=3)

        group = VGroup(*[rect.copy() for i in range(5)])
        group.arrange(RIGHT)

        group_2 = VGroup(*[group.copy() for i in range(3)])
        group_2.arrange(DOWN).to_edge(UP)

        group_3 = group_2.copy().rotate(math.pi/2)

        self.play(Write(group_2), run_time=2)
        self.wait()
        self.play(TransformFromCopy(group_2, group_3))
        self.wait()
        self.play(ApplyMethod(group_3.rotate_about_origin, 110 * DEGREES, [0, 0, 0]))
