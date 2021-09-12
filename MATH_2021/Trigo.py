from manim import *
import math


class Trigo(Scene):
    def construct(self):
        circle = Circle(radius=3, color=BLACK)

        # Points every 90 degrees around the circle
        circle_right = circle.point_at_angle(0)
        circle_top = circle.point_at_angle(PI / 2)
        circle_left = circle.point_at_angle(PI)
        circle_bot = circle.point_at_angle(3 * PI / 2)

        # Horizontal and Vertical radii
        radius_v = Line(circle_right, circle_left).set_color(BLACK)
        radius_h = Line(circle_top, circle_bot).set_color(BLACK)

        dot = Dot(color=BLACK).scale(2).move_to(circle_right)

        # sin dot
        dot_v = Dot(color=YELLOW).scale(2).move_to([0, dot.get_y(), 1])
        dot_v.add_updater(lambda x: x.move_to([0, dot.get_y(), 1]))

        # cos dot
        dot_h = Dot(color=YELLOW).scale(2).move_to([dot.get_x(), 0, 1])
        dot_h.add_updater(lambda x: x.move_to([dot.get_x(), 0, 1]))

        # Projections
        radius_v_projection = Line(dot_v, dot, color=YELLOW)
        radius_v_projection.add_updater(lambda m: m.put_start_and_end_on(dot_v.get_center(), dot.get_center()))

        radius_h_projection = Line(dot_h, dot, color=YELLOW)
        radius_h_projection.add_updater(lambda m: m.put_start_and_end_on(dot_h.get_center(), dot.get_center()))

        # Segment
        segment = Line(dot_h, dot_v, color=WHITE)
        segment.add_updater(lambda m: m.put_start_and_end_on(dot_h.get_center(), dot_v.get_center()))

        dot_segment_center = Dot(color=GREEN).scale(2).move_to(segment.get_center())
        dot_segment_center.add_updater(lambda x: x.move_to(segment.get_center()))

        path = VMobject().set_color(GREEN)
        path.set_points_as_corners([dot_segment_center.get_center(), dot_segment_center.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot_segment_center.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)

        self.add(radius_v, radius_h, circle, dot, dot_v, dot_h)

        self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)
        self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)

        self.play(ApplyMethod(radius_v.set_color, WHITE),
                  ApplyMethod(radius_h.set_color, WHITE),
                  run_time=0.01)

        self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)
        self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)

        self.play(ApplyMethod(dot.set_color, BLUE),
                  ApplyMethod(circle.set_color, WHITE),
                  run_time=0.01)

        self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)
        self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)

        self.add(radius_v_projection)

        self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)
        self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)

        self.remove(radius_v_projection)
        self.add(radius_h_projection)

        self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)
        self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)

        self.remove(radius_h_projection, radius_h, radius_v, circle)

        self.play(ApplyMethod(dot.set_color, BLACK), run_time=0.01)
        self.add(segment)

        self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)
        self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)

        self.add(dot_segment_center, path)

        self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)
        self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)

        self.remove(segment, path, dot_segment_center, dot_h)

        self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)
        self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)


class SinWave(Scene):
    def construct(self):
        circle = Circle(radius=3, color=BLACK)

        # Points every 90 degrees around the circle
        circle_right = circle.point_at_angle(0)
        circle_top = circle.point_at_angle(PI / 2)
        circle_left = circle.point_at_angle(PI)
        circle_bot = circle.point_at_angle(3 * PI / 2)

        # Horizontal and Vertical radii
        radius_v = Line(circle_right, circle_left).set_color(BLACK)
        radius_h = Line(circle_top, circle_bot).set_color(BLACK)

        dot = Dot(color=BLACK).scale(2).move_to(circle_right)

        # sin dot
        dot_v = Dot(color=YELLOW).scale(2).move_to([circle.get_x(), dot.get_y(), 1])
        dot_v.add_updater(lambda x: x.move_to([circle.get_x(), dot.get_y(), 1]))

        start_x = -6
        dot_sin_tracker = ValueTracker(start_x)
        dot_sin = always_redraw(lambda: Dot([dot_sin_tracker.get_value(), dot_v.get_y(), 0], color=BLUE))

        # Projections
        dot_sin_projection = Line(dot_sin, dot_v, color=BLUE)
        dot_sin_projection.add_updater(lambda m: m.put_start_and_end_on(dot_sin.get_center(), dot_v.get_center()))

        # Ligne
        line = NumberLine(
            x_range=[-6, 12],
            length=12,
            include_ticks=False,
            include_tip=True
        ).to_edge(DOWN).shift(UP * 1)

        temps = Text("Temps").to_corner(DR)

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot_sin.get_center()])
            path.become(previous_path)

        path = VMobject().set_color(BLUE)
        path.set_points_as_corners([dot_sin.get_center(), dot_sin.get_center()])
        path.add_updater(update_path)

        self.add(dot, dot_v)

        self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)
        self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)

        self.play(ApplyMethod(circle.set_color, WHITE), run_time=0.1)
        self.play(circle.animate.scale(1 / 3),
                  dot_v.animate.scale(0.5))
        self.play(circle.animate.shift([-6, 0, 0] - circle.get_center()))
        self.play(ApplyMethod(dot.set_color, BLUE), run_time=0.1)

        self.add(dot_sin, path, dot_sin_projection)
        self.play(Write(line), Write(temps))

        self.play(MoveAlongPath(dot, circle),
                  ApplyMethod(dot_sin_tracker.increment_value, 4),
                  run_time=4, rate_func=linear)
        self.play(MoveAlongPath(dot, circle),
                  ApplyMethod(dot_sin_tracker.increment_value, 4),
                  run_time=4, rate_func=linear)
        self.play(MoveAlongPath(dot, circle),
                  ApplyMethod(dot_sin_tracker.increment_value, 4),
                  run_time=4, rate_func=linear)


class Basic(Scene):
    def construct(self):
        mul = Tex("X2").scale(5).to_edge(LEFT).shift(RIGHT * 2)
        add = Tex("+3").scale(5).to_edge(RIGHT).shift(LEFT * 2)

        equation = MathTex("2x", "+3").to_edge(DOWN).shift(UP).scale(2)
        equation[0][1].set_color(GREEN)

        self.play(Write(mul))
        self.wait()
        self.play(Write(add))
        self.wait()

        self.play(ReplacementTransform(mul.copy(), equation[0]), ReplacementTransform(add.copy(), equation[1]))
        self.wait()


class Complex(Scene):
    def construct(self):

        brake = MathTex("f(x)=", "{x \over 10}", "\\times", "{x \over 10}", "+", "{x \over 10} \\times 3").scale(2)
        brake[0][:2].set_color(BLUE)
        brake[0][2].set_color(GREEN)
        brake[0][3].set_color(BLUE)
        brake[1][0].set_color(GREEN)
        brake[3][0].set_color(GREEN)
        brake[5][0].set_color(GREEN)

        equation = MathTex("f(x)=\int_{-\infty}^{\infty} \hat{f}(\\xi) e^{2 \pi i x \\xi} d \\xi").scale(2)
        equation[0][:2].set_color(BLUE)
        equation[0][2].set_color(GREEN)
        equation[0][3].set_color(BLUE)
        equation[0][18].set_color(GREEN)

        self.play(Write(brake))
        self.wait()
        self.play(Transform(brake, equation))
        self.wait()


class BlackBox(Scene):
    def construct(self):
        box = Rectangle(color=BLUE).scale(1.5)

        equation = MathTex("y", "=", "f", "(", "x", ")").to_edge(UP).scale(2)
        equation[0].set_color(RED)
        equation[2:4].set_color(BLUE)
        equation[4].set_color(GREEN)
        equation[5].set_color(BLUE)

        function = MathTex("f", color=BLUE).scale(2)

        input = Circle(color=GREEN).to_edge(LEFT).scale(0.5)
        output = Circle(color=RED).to_edge(RIGHT).scale(0.5)

        x = MathTex("x", color=GREEN)
        x.add_updater(lambda m: m.move_to([input.get_x(), input.get_y(), 0]))

        y = MathTex("y", color=RED)
        y.add_updater(lambda m: m.move_to([output.get_x(), output.get_y(), 0]))

        self.play(Write(box), run_time=2)
        self.play(FadeIn(input, shift=RIGHT))
        self.play(FadeOut(input, shift=RIGHT * 2))
        self.play(FadeIn(output, shift=RIGHT * 2))
        self.play(FadeOut(output, shift=RIGHT))
        self.remove()

        self.play(Write(function))
        self.play(Indicate(function))
        self.play(AddTextLetterByLetter(x), FadeIn(input, shift=RIGHT))
        self.play(FadeOut(input, shift=RIGHT * 2), FadeOut(x))
        self.play(AddTextLetterByLetter(y), FadeIn(output, shift=RIGHT * 2))
        self.play(FadeOut(output, shift=RIGHT), FadeOut(y))

        self.play(Write(input),
                  Write(x),
                  Write(output),
                  Write(y))
        self.play(ReplacementTransform(y.copy(), equation[0]))
        self.play(Write(equation[1]))
        self.play(ReplacementTransform(x.copy(), equation[4]))
        self.play(ReplacementTransform(function.copy(), equation[2]))
        self.play(Write(equation[3]),
                  Write(equation[5]))


class Values(Scene):
    def construct(self):
        equation = MathTex("y", "=", "f", "( \enspace", "x", "\enspace\enspace)").scale(2)
        y_idx, eq_idx, x_idx = 0, 1, 4

        equation[y_idx].set_color(RED)
        equation[2:4].set_color(BLUE)
        equation[x_idx].set_color(GREEN)
        equation[5].set_color(BLUE)

        input = ValueTracker(0)
        input_label = DecimalNumber().next_to(equation[eq_idx], RIGHT * 6).set_color(GREEN).scale(1.5)
        input_label.add_updater(
            lambda d: d.set_value(input.get_value()).next_to(equation[eq_idx], RIGHT * 6).set_color(GREEN))

        output = ValueTracker(0)
        output_label = DecimalNumber().next_to(equation[eq_idx], LEFT * 3).set_color(RED).scale(1.5)
        output_label.add_updater(
            lambda d: d.set_value(output.get_value()).next_to(equation[eq_idx], LEFT * 3).set_color(RED))

        self.play(Write(equation))
        self.wait()
        self.play(FadeOut(equation[y_idx]), FadeOut(equation[x_idx]))
        self.play(Write(input_label),
                  Write(output_label))
        self.play(ApplyMethod(input.set_value, 3),
                  ApplyMethod(output.set_value, 3), run_time=2)
        self.wait()
        self.play(ApplyMethod(input.set_value, -3),
                  ApplyMethod(output.set_value, -3), run_time=2)
        self.wait()
        self.play(ApplyMethod(input.set_value, 0),
                  ApplyMethod(output.set_value, 0), run_time=2)
        self.wait()


class TableValues(Scene):
    def construct(self):
        box = Rectangle(color=BLUE).scale(1.5)

        equation = MathTex("y", "=", "f", "(", "x", ")").to_edge(UP).scale(2)
        equation[0].set_color(RED)
        equation[2:4].set_color(BLUE)
        equation[4].set_color(GREEN)
        equation[5].set_color(BLUE)

        function = MathTex("f", color=BLUE).scale(2)

        input = Circle(color=GREEN).to_edge(LEFT).scale(0.5)
        output = Circle(color=RED).to_edge(RIGHT).scale(0.5)

        x = MathTex("x", color=GREEN)
        x.add_updater(lambda m: m.move_to([input.get_x(), input.get_y(), 0]))

        y = MathTex("y", color=RED)
        y.add_updater(lambda m: m.move_to([output.get_x(), output.get_y(), 0]))

        x0 = MathTex("x", color=GREEN)
        y0 = MathTex("y", color=RED)
        x1 = MathTex("x1", color=GREEN)
        y1 = MathTex("y1", color=RED)
        x2 = MathTex("x2", color=GREEN)
        y2 = MathTex("y2", color=RED)
        x3 = MathTex("x3", color=GREEN)
        y3 = MathTex("y3", color=RED)
        x4 = MathTex("x4", color=GREEN)
        y4 = MathTex("y4", color=RED)

        table = MobjectTable(
            [[x0.copy(), x1.copy(), x2.copy(), x3.copy(), x4.copy()],
             [y0.copy(), y1.copy(), y2.copy(), y3.copy(), y4.copy()]],
            include_outer_lines=True).to_edge(DOWN).shift(DOWN).scale(0.5)

        self.play(Create(table[1:]), Create(table[0][0]), Create(table[0][5]), Write(box), Write(function),
                  Write(equation))

        self.play(FadeIn(input, shift=RIGHT))
        self.play(ReplacementTransform(x.copy(), table[0][1]))
        self.play(FadeOut(input, shift=RIGHT * 2))
        self.play(FadeIn(output, shift=RIGHT * 2))
        self.play(ReplacementTransform(y.copy(), table[0][6]))
        self.play(FadeOut(output, shift=RIGHT))

        self.play(FadeIn(input, shift=RIGHT))
        self.play(ReplacementTransform(x.copy(), table[0][2]))
        self.play(FadeOut(input, shift=RIGHT * 2))
        self.play(FadeIn(output, shift=RIGHT * 2))
        self.play(ReplacementTransform(y.copy(), table[0][7]))
        self.play(FadeOut(output, shift=RIGHT))

        self.play(FadeIn(input, shift=RIGHT))
        self.play(ReplacementTransform(x.copy(), table[0][3]))
        self.play(FadeOut(input, shift=RIGHT * 2))
        self.play(FadeIn(output, shift=RIGHT * 2))
        self.play(ReplacementTransform(y.copy(), table[0][8]))
        self.play(FadeOut(output, shift=RIGHT))

        self.play(FadeIn(input, shift=RIGHT))
        self.play(ReplacementTransform(x.copy(), table[0][4]))
        self.play(FadeOut(input, shift=RIGHT * 2))
        self.play(FadeIn(output, shift=RIGHT * 2))
        self.play(ReplacementTransform(y.copy(), table[0][9]))
        self.play(FadeOut(output, shift=RIGHT))


class LinFunc(Scene):
    def construct(self):
        box = Rectangle(color=BLUE).scale(1.5)

        equation = MathTex("y", "=", "f", "(", "x", ")", "=", "x", "+1").to_edge(UP).scale(2)
        equation[0].set_color(RED)
        equation[2:4].set_color(BLUE)
        equation[4].set_color(GREEN)
        equation[5].set_color(BLUE)
        equation[7].set_color(GREEN)

        function = MathTex("f", ":", "x", "\mapsto", "x", "+1").scale(2)
        function[0].set_color(BLUE)
        function[2].set_color(GREEN)
        function[4].set_color(GREEN)

        input = Circle(color=GREEN).to_edge(LEFT).scale(0.5)
        output = Circle(color=RED).to_edge(RIGHT).scale(0.5)

        x = MathTex("x", color=GREEN)
        x.add_updater(lambda m: m.move_to([input.get_x(), input.get_y(), 0]))

        y = MathTex("y", color=RED)
        y.add_updater(lambda m: m.move_to([output.get_x(), output.get_y(), 0]))

        x1 = MathTex("x1", color=GREEN)
        y1 = MathTex("y1", color=RED)
        x2 = MathTex("x2", color=GREEN)
        y2 = MathTex("y2", color=RED)
        x3 = MathTex("x3", color=GREEN)
        y3 = MathTex("y3", color=RED)

        table = IntegerTable(
            [[0, 1, 2],
             [1, 2, 3]],
            row_labels=[MathTex("x", color=GREEN), MathTex("y", color=RED)],
            h_buff=1).to_edge(DOWN).shift(DOWN).scale(0.5)

        self.play(Create(table[1:]), Create(table[0][0]), Create(table[0][4]), Write(box), Write(function),
                  Write(equation[:6]))
        self.play(Indicate(function[1]))
        self.wait()

        self.play(FadeIn(input, shift=RIGHT))
        self.play(ReplacementTransform(x.copy(), table[0][1]))
        self.play(FadeOut(input, shift=RIGHT * 2))
        self.play(FadeIn(output, shift=RIGHT * 2))
        self.play(ReplacementTransform(y.copy(), table[0][5]))
        self.play(FadeOut(output, shift=RIGHT))

        self.play(FadeIn(input, shift=RIGHT))
        self.play(ReplacementTransform(x.copy(), table[0][2]))
        self.play(FadeOut(input, shift=RIGHT * 2))
        self.play(FadeIn(output, shift=RIGHT * 2))
        self.play(ReplacementTransform(y.copy(), table[0][6]))
        self.play(FadeOut(output, shift=RIGHT))

        self.play(FadeIn(input, shift=RIGHT))
        self.play(ReplacementTransform(x.copy(), table[0][3]))
        self.play(FadeOut(input, shift=RIGHT * 2))
        self.play(FadeIn(output, shift=RIGHT * 2))
        self.play(ReplacementTransform(y.copy(), table[0][7]))
        self.play(FadeOut(output, shift=RIGHT))

        self.play(Write(equation[6]), ReplacementTransform(function[-2:].copy(), equation[7:]))


class Square(Scene):
    def construct(self):
        box = Rectangle(color=BLUE).scale(1.5)

        equation = MathTex("y", "=", "f", "(", "x", ")", "=", "x^{", "2}").to_edge(UP).scale(2)
        equation[0].set_color(RED)
        equation[2:4].set_color(BLUE)
        equation[4].set_color(GREEN)
        equation[5].set_color(BLUE)
        equation[7].set_color(GREEN)

        function = MathTex("f", ":", "x", "\mapsto", "x^{", "2}").scale(2)
        function[0].set_color(BLUE)
        function[2].set_color(GREEN)
        function[4].set_color(GREEN)

        input = Circle(color=GREEN).to_edge(LEFT).scale(0.5)
        output = Circle(color=RED).to_edge(RIGHT).scale(0.5)

        x = MathTex("x", color=GREEN)
        x.add_updater(lambda m: m.move_to([input.get_x(), input.get_y(), 0]))

        y = MathTex("y", color=RED)
        y.add_updater(lambda m: m.move_to([output.get_x(), output.get_y(), 0]))

        x1 = MathTex("x1", color=GREEN)
        y1 = MathTex("y1", color=RED)
        x2 = MathTex("x2", color=GREEN)
        y2 = MathTex("y2", color=RED)
        x3 = MathTex("x3", color=GREEN)
        y3 = MathTex("y3", color=RED)

        table = IntegerTable(
            [[0, 1, 2],
             [0, 1, 4]],
            row_labels=[MathTex("x", color=GREEN), MathTex("y", color=RED)],
            h_buff=1).to_edge(DOWN).shift(DOWN).scale(0.5)

        self.play(Create(table[1:]), Create(table[0][0]), Create(table[0][4]), Write(box), Write(function),
                  Write(equation[:6]))
        self.play(Indicate(function[1]))
        self.wait()

        self.play(FadeIn(input, shift=RIGHT))
        self.play(ReplacementTransform(x.copy(), table[0][1]))
        self.play(FadeOut(input, shift=RIGHT * 2))
        self.play(FadeIn(output, shift=RIGHT * 2))
        self.play(ReplacementTransform(y.copy(), table[0][5]))
        self.play(FadeOut(output, shift=RIGHT))

        self.play(FadeIn(input, shift=RIGHT))
        self.play(ReplacementTransform(x.copy(), table[0][2]))
        self.play(FadeOut(input, shift=RIGHT * 2))
        self.play(FadeIn(output, shift=RIGHT * 2))
        self.play(ReplacementTransform(y.copy(), table[0][6]))
        self.play(FadeOut(output, shift=RIGHT))

        self.play(FadeIn(input, shift=RIGHT))
        self.play(ReplacementTransform(x.copy(), table[0][3]))
        self.play(FadeOut(input, shift=RIGHT * 2))
        self.play(FadeIn(output, shift=RIGHT * 2))
        self.play(ReplacementTransform(y.copy(), table[0][7]))
        self.play(FadeOut(output, shift=RIGHT))

        self.play(Write(equation[6]), ReplacementTransform(function[-2:].copy(), equation[7:]))


class FourTimes(Scene):
    def construct(self):
        equation = MathTex("f", "(", "x", ")", "=", "4", "x").to_edge(UP).scale(2)
        equation[:2].set_color(BLUE)
        equation[2].set_color(GREEN)
        equation[3].set_color(BLUE)
        equation[-1].set_color(GREEN)

        square = Rectangle(width=5, height=5)

        brace = Brace(square[0])
        brace_text = brace.get_tex("x").set_color(GREEN)

        self.play(Write(equation))
        self.play(Write(square))
        self.play(Write(brace), Write(brace_text), run_time=2)


class Tables(Scene):
    def construct(self):
        table_1 = Rectangle(width=3, height=3)

        table_2 = VGroup(*[Rectangle(width=3, height=3) for i in range(2)])
        table_2.arrange(RIGHT, buff=0.0)

        table_3 = VGroup(*[Rectangle(width=3, height=3) for i in range(3)])
        table_3.arrange(RIGHT, buff=0.0)

        equation = MathTex("4 + 2(", "x", "-1)")
        equation[1].set_color(GREEN)

        self.play(Write(table_1))
        self.wait()
        self.play(Transform(table_1, table_2))
        self.wait()
        self.play(Transform(table_1, table_3))
        self.wait()
        self.play(Transform(table_1, equation))


class Graph(Scene):
    def construct(self):
        # Plot basis (axis)
        axes = Axes(
            x_range=[-5.1, 5, 1],
            y_range=[-4.1, 4, 1],
            x_length=10,
            y_length=6,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": np.arange(-5.1, 5, 1)
            },
            y_axis_config={
                "include_numbers": True
            },
            tips=True,
        )
        x_label = axes.get_x_axis_label("x").set_color(GREEN)
        y_label = axes.get_y_axis_label("y").set_color(RED)

        function_label_pos = [-3.75, 3, 0]
        function_equation_label = MathTex("f", "(", "x", ")", "=", color=BLUE).move_to(function_label_pos)
        function_equation_label[2].set_color(GREEN)

        table_pos = [-3.75, 1, 0]
        table_x = [0, 1, 2, 3]

        #  ------------------------------------- Linear Function -------------------------------------------------------
        table_reciproc_y = [0, 1, 2, 3]
        table_reciproc = IntegerTable(
            [table_x,
             table_reciproc_y],
            row_labels=[MathTex("x", color=GREEN), MathTex("y", color=RED)],
            h_buff=1).to_edge(DOWN).shift(RIGHT * 4).scale(0.5).move_to(table_pos)

        equation_reciproc = axes.get_graph(
            lambda x: x,
            color=BLUE)
        equation_reciproc.add_updater(
            lambda m: m.become(
                axes.get_graph(
                    lambda x: x,
                    color=BLUE
                )
            )
        )

        dots_reciproc = []
        for i in range(len(table_x)):
            dots_reciproc.append(Dot(point=axes.c2p(table_x[i], table_reciproc_y[i], 0), color=YELLOW))

        dots_reciproc_coords = []
        for i in range(len(table_x)):
            dots_reciproc_coords.append(Tex("({0},{1})".format(table_x[i], table_reciproc_y[i])).scale(0.75)
                                        .next_to(axes.c2p(table_x[i], table_reciproc_y[i], 0)))

        line_h = []
        for i in range(len(table_x)):
            line_h.append(axes.get_horizontal_line(axes.c2p(table_x[i], table_reciproc_y[i], 0), color=BLUE))
        line_v = []
        for i in range(len(table_x)):
            line_v.append(axes.get_vertical_line(axes.c2p(table_x[i], table_reciproc_y[i], 0), color=BLUE))

        reciproc_label = MathTex("x").next_to(function_equation_label[-1])
        reciproc_label[0].set_color(GREEN)

        t_label_lin_start = axes.get_T_label(x_val=-5, graph=equation_reciproc, label=MathTex("x"), label_color=GREEN, triangle_color=BLUE)
        t_label_lin_end = axes.get_T_label(x_val=5, graph=equation_reciproc, label=MathTex("x"), label_color=GREEN, triangle_color=BLUE)

        # ------------------------------------------- Video -----------------------------------------------------------
        # Basis
        self.play(Create(axes[0]), run_time=3)
        self.wait()
        self.play(Write(x_label))
        self.play(Create(axes[1]), run_time=3)
        self.play(Write(y_label))
        self.play(Write(function_equation_label))

        # Lin
        self.play(Write(reciproc_label))
        self.play(Create(table_reciproc))
        for i in range(len(table_x)):
            self.play(Indicate(table_reciproc[0][i + 1]), Indicate(table_reciproc[0][i + 6]), run_time=2)
            self.play(Create(line_h[i]), Create(line_v[i]))
            self.play(Create(dots_reciproc[i]), Write(dots_reciproc_coords[i]))
        self.play(Create(equation_reciproc))

        self.play(Create(t_label_lin_start))
        self.play(Transform(t_label_lin_start, t_label_lin_end), run_time=3)


class Functions(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5.1, 5, 1],
            y_range=[-4.1, 4, 1],
            x_length=10,
            y_length=6,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": np.arange(-5.1, 5, 1)
            },
            y_axis_config={
                "include_numbers": True
            },
            tips=True,
        )
        x_label = axes.get_x_axis_label("x").set_color(GREEN)
        y_label = axes.get_y_axis_label("y").set_color(RED)

        # Function Labels
        function_label_pos = [-3.75, 3.5, 0]

        function_equation_label = MathTex("f", "(", "x", ")", "=", color=BLUE).move_to(function_label_pos)
        function_equation_label[2].set_color(GREEN)

        #  ------------------------------------- Linear Function -------------------------------------------------------
        function_reciproc = axes.get_graph(lambda x: x, color=BLUE)
        function_reciproc.add_updater(lambda m: m.become(axes.get_graph(lambda x: x, color=BLUE)))
        function_reciproc_label = MathTex("x", color=GREEN).next_to(function_equation_label[-1])

        #  ------------------------------------- Square ----------------------------------------------------------------
        function_square = axes.get_graph(lambda x: x ** 2, color=BLUE)
        function_square.add_updater(lambda m: m.become(axes.get_graph(lambda x: x ** 2, color=BLUE)))
        function_square_label = MathTex("x^{", "2}").next_to(function_equation_label[-1])
        function_square_label[0].set_color(GREEN)

        #  ------------------------------------- LogNat ----------------------------------------------------------------
        function_lognat = axes.get_graph(lambda x: math.log(x), x_range=[0.01, 5], color=BLUE)
        function_lognat.add_updater(lambda m: m.become(axes.get_graph(lambda x: math.log(x), x_range=[0.01, 5], color=BLUE)))
        function_lognat_label = MathTex("ln(", "x", ")").next_to(function_equation_label[-1])
        function_lognat_label[1].set_color(GREEN)

        #  ------------------------------------- Expo ------------------------------------------------------------------
        function_exp = axes.get_graph(lambda x: math.exp(x), color=BLUE)
        function_exp.add_updater(lambda m: m.become(axes.get_graph(lambda x: math.exp(x), color=BLUE)))
        function_exp_label = MathTex("e^{", "x}").next_to(function_equation_label[-1])
        function_exp_label[1].set_color(GREEN)

        #  ------------------------------------- Polynome --------------------------------------------------------------
        function_polynome = axes.get_graph(lambda x: (2 * x ** 3) - (3 * x ** 2), color=BLUE)
        function_polynome.add_updater(lambda m: m.become(axes.get_graph(lambda x: (2 * x ** 3) - (3 * x ** 2), color=BLUE)))
        function_polynome_label = MathTex("2", "x^{", "3}", "-", "3", "x^{", "2}").next_to(function_equation_label[-1])
        function_polynome_label[1:6:4].set_color(GREEN)

        function_reciproc.clear_updaters()
        function_square.clear_updaters()
        function_lognat.clear_updaters()
        function_exp.clear_updaters()
        function_polynome.clear_updaters()
        #  ###################################### VIDEO ################################################################
        self.play(Write(axes), Write(x_label), Write(y_label))
        self.play(Write(function_equation_label))
        self.wait()

        self.play(Write(function_reciproc_label))
        self.play(Create(function_reciproc))
        self.wait()

        self.play(Transform(function_reciproc_label, function_square_label))
        self.play(Transform(function_reciproc, function_square))
        self.wait()

        self.play(Transform(function_reciproc_label, function_lognat_label))
        self.play(Transform(function_reciproc, function_lognat))
        self.wait()

        self.play(Transform(function_reciproc_label, function_exp_label))
        self.play(Transform(function_reciproc, function_exp))
        self.wait()

        self.play(Transform(function_reciproc_label, function_polynome_label))
        self.play(Transform(function_reciproc, function_polynome))
        self.wait()


class SinGraph(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5.1, 5, 1],
            y_range=[-4.1, 4, 1],
            x_length=10,
            y_length=6,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": np.arange(-5.1, 5, 1)
            },
            y_axis_config={
                "include_numbers": True
            },
            tips=True,
        )
        x_label = axes.get_x_axis_label("x").set_color(GREEN)
        y_label = axes.get_y_axis_label("y").set_color(RED)

        # Function Labels
        function_label_pos = [-3.75, 3.5, 0]

        function_equation_label = MathTex("f", "(", "x", ")", "=", color=BLUE).move_to(function_label_pos)
        function_equation_label[2].set_color(GREEN)

        #  ------------------------------------- Linear Function -------------------------------------------------------
        function_reciproc = axes.get_graph(lambda x: math.sin(x), color=BLUE)
        function_reciproc.add_updater(lambda m: m.become(axes.get_graph(lambda x: math.sin(x), color=BLUE)))
        function_reciproc_label = MathTex("\sin{(", "x", ")}").next_to(function_equation_label[-1])
        function_reciproc_label[1].set_color(GREEN)

        #  ###################################### VIDEO ################################################################
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Write(function_equation_label))
        self.wait()

        self.play(Write(function_reciproc_label))
        self.play(Create(function_reciproc))
        self.wait()


