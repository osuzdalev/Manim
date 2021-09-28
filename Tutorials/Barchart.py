from manim import *
import random
import math

NUM = 50

class Bars(Scene):
    def construct(self):
        vals = [1 for i in range(NUM)]
        colors = ["#003f5c", "#58508d", "#bc5090", "#ff6361", YELLOW, GREEN, TEAL, BLUE]
        bar = BarChart(
            vals,
            max_value=1,
            bar_colors=colors,
            bar_label_scale_val=1,
            width=12,
            bar_fill_opacity=1.0,
            label_y_axis=False,
        )
        self.add(bar)

        x = 0
        for i in range(1000):
            new_vals = [0.01 + abs(math.sin(x + math.pi / NUM * j)) for j in range(NUM)]
            print("VALS: ", new_vals)
            print("x: ", x)
            self.play(ApplyMethod(bar.change_bar_values, new_vals), run_time=0.2, rate_func=linear)
            x += math.pi / NUM
