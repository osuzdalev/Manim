from manim import *


class MovingDot(Scene):
    def construct(self):
        axes = Axes(x_range=[-10,10], y_range=[-20, 20])
        axes_labels = axes.get_axis_labels()

        graph = axes.get_graph(lambda x: 0.1 * (x + 7) * (x - 2) * (x - 7))

        start_x = -10
        end_x = 10
        tracker = ValueTracker(start_x)  # starting point of x

        ctp = axes.coords_to_point
        dot_x = tracker.get_value
        func = graph.underlying_function
        moving_dot = always_redraw(lambda: Dot(ctp(dot_x(), func(dot_x())), radius=0.1, color=RED))

        self.add(axes, axes_labels, graph, moving_dot)
        self.play(ApplyMethod(tracker.set_value, end_x), run_time=5)
        self.wait()
