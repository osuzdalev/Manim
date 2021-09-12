# %% manim Normal

from manim import *


class Normal(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-6, 6.1, 1],
            y_range=[-1, 1, 1],
            x_length=10,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": np.arange(-4, 4.1, 2),
                "numbers_with_elongated_ticks": np.arange(-4, 4.1, 2),
            },
            tips=False,
        )

        axes_labels = axes.get_axis_labels()

        normal_graph = axes.get_graph(lambda x: (1 / (np.sqrt(2 * np.pi) * np.exp((-x / 2) ** 2))), color=BLUE)

        normal_area = axes.get_area(graph=normal_graph, x_range=[-4, 4], color=[YELLOW, BLUE])

        normal_area_label = axes.get_graph_label(
            normal_graph, "\sqrt{\pi}", x_val=1, direction=UP / 2, color=YELLOW
        )

        normal_label = axes.get_graph_label(
            normal_graph, "f(x)", x_val=-6, direction=UP / 2
        )

        plot = VGroup(axes, normal_graph)

        self.play(DrawBorderThenFill(axes))
        self.play(Create(normal_graph), run_time=3)
        self.play(Write(normal_label))
        self.wait()
        self.play(FadeIn(normal_area))
        self.wait()
        self.play(Write(normal_area_label))
        self.wait()