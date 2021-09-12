from manim import *
import numpy as np


class Series(Scene):
    def construct(self):
        fib_num = self.fibonacci(10)
        fib_0_1 = MathTex("0", "1").scale(1.5).to_corner(UL).set_color(RED)
        fib = self.build_VGroup(self.fibonacci(10)).scale(1.5).to_edge(UP)

        self.play(Write(fib), Write(fib_0_1))
        self.wait()
        self.play(FadeOut(fib_0_1))
        self.wait()
        for j in range(3):
            for i in range(j + (j * 3), j + (j * 3) + 3):
                eq = MathTex("{",  "{}".format(fib_num[i + 1]), "\over", "{}".format(fib_num[i]), "}", "=",
                             "{ratio:.5f}".format(ratio=fib_num[i + 1] / fib_num[i])).move_to([-5 + j * 4, 2 - (2 * (i - (j + (j * 3)))), 0])
                eq[-1].set_color(GOLD)

                self.play(ReplacementTransform(fib[i + 1].copy(), eq[1]),
                          Write(eq[2]),
                          ReplacementTransform(fib[i].copy(), eq[3]),
                          Write(eq[5]),
                          Write(eq[6]))
                self.wait()

        self.clear()

        phi = MathTex("=", "{1 + \sqrt{5}", "\over 2}", "=", "1.618033988749895", "...")
        phi_1 = MathTex("\Phi").set_color(GOLD).scale(4).next_to(phi, LEFT)
        phi[-2].set_color(GOLD)
        self.play(Write(phi_1), Write(phi))

    def build_VGroup(self, array):
        return VGroup(*[MathTex(array[i]) for i in range(len(array))]).arrange(RIGHT)

    def build_series(self, array):
        right_arrow = [MathTex("-") for i in range(len(array))]
        Marray = [MathTex(array[i]) for i in range(len(array))]
        series = []
        for elem in zip(Marray, right_arrow):
            series.extend(elem)

        series = VGroup(*[series[i] for i in range(len(series) - 1)])
        series.arrange(RIGHT)
        series[1::2].set_color(GREEN)
        return series

    def build_horizontal_labels(self, series, label):
        label.scale(0.5).set_color(GREEN)
        step = VGroup(*[label.copy() for i in range((len(series) - 1) // 2)])
        for i in range(len(step)):
            step[i].next_to(series[1 + 2 * i], UP)
        return step

    def build_vertical_labels(self, series, label):
        label.scale(0.5).set_color(GREEN)
        step = VGroup(*[label.copy() for i in range((len(series) - 1) // 2)])
        for i in range(len(step)):
            step[i].next_to(series[1 + 2 * i], UP)
        return step

    def basic_series(self):
        basic = self.build_VGroup([i for i in range(10)])
        basic_series = self.build_series([i for i in range(10)])
        basic_series_labels = self.build_horizontal_labels(basic_series, MathTex("+1"))

        self.play(Write(basic))
        self.wait()
        self.play(Transform(basic, basic_series[::2]))
        self.wait()
        self.play(DrawBorderThenFill(basic_series_labels[0]), DrawBorderThenFill(basic_series[1]))
        self.wait()
        self.play(DrawBorderThenFill(basic_series_labels[1]), DrawBorderThenFill(basic_series[3]))
        self.wait()
        self.play(DrawBorderThenFill(basic_series_labels[2:]), DrawBorderThenFill(basic_series[5::2]))
        self.wait()

    def series_ari_geo(self):
        series_1 = self.build_VGroup(list(range(1, 6))).scale(2).to_edge(UP)
        series_1_label = MathTex("+1").set_color(GREEN).next_to(series_1, RIGHT)
        series_2 = self.build_VGroup([5, 8, 11, 14, 17]).scale(2).next_to(series_1, DOWN * 3)
        series_2_label = MathTex("+3").set_color(GREEN).next_to(series_2, RIGHT)
        series_3 = self.build_VGroup([2 ** i for i in range(5)]).scale(2).next_to(series_2, DOWN * 3)
        series_3_label = MathTex("\\times 2").set_color(GREEN).next_to(series_3, RIGHT)

        series_4 = VGroup()
        series_4.add(MathTex("1"))
        series_4_array = [2 * i + 3 for i in [1, 5, 13, 29]]
        series_4.add(*[MathTex(series_4_array[i]) for i in range(len(series_4_array))]).arrange(RIGHT)
        series_4.scale(2).next_to(series_3, DOWN * 3)
        series_4_label = MathTex("2\\times x + 3").set_color(GREEN).next_to(series_4, RIGHT)

        self.play(Write(series_1))
        self.wait()
        self.play(Write(series_2))
        self.wait()
        self.play(Write(series_3))
        self.wait()
        self.play(Write(series_4))
        self.wait()
        self.play(Write(series_1_label))
        self.wait()
        self.play(Write(series_2_label))
        self.wait()
        self.play(Write(series_3_label))
        self.wait()
        self.play(Write(series_4_label))
        self.wait()

    def fibonacci(self, n):
        arr = [1, 2]
        i = 1
        j = 0
        for x in range(n):
            arr.append(arr[j] + arr[i])
            i += 1
            j += 1

        return arr

class Suites(Scene):
    def construct(self):
        suite_l = Text("Suite Littérale").move_to([0, 3, 0])
        name = Text("Суздалев").move_to([0, 1, 0])
        suite_n = Text("Suite Numérique").move_to([0, -1, 0])
        tel = MathTex("007 1234567789").move_to([0, -3, 0])

        self.play(Write(suite_l))
        self.wait()
        self.play(Write(name))
        self.wait()
        self.play(Write(suite_n))
        self.wait()
        self.play(Write(tel))
        self.wait()

        for i in range(len(name)):
            self.play(Indicate(name[i]), run_time=0.3)
        self.wait()
        for i in range(len(tel[0])):
            self.play(Indicate(tel[0][i]), run_time=0.3)
        self.wait()

class PI(Scene):
    def construct(self):
        circle = Circle().scale(2).set_color(WHITE).move_to([0, 1, 0])
        circle_2 = Circle().scale(2).set_color(RED).move_to([0, 1, 0])
        dot1 = circle.point_at_angle(0)
        dot2 = circle.point_at_angle(np.pi)
        diameter = Line(dot1, dot2).set_color(BLUE)

        circumference = diameter.copy().set_color(RED).scale(np.pi).move_to(DOWN * 3.5)


        eq = MathTex("{C", "\over", "D}", "=").move_to([3, 0, 0])
        eq[0].set_color(RED)
        eq[2].set_color(BLUE)
        pi = MathTex("\pi").scale(4).next_to(eq).set_color(GREEN)

        self.play(Create(circle))
        self.wait()
        self.play(Create(diameter))
        self.wait()
        self.play(diameter.animate.shift(DOWN * 3.5))
        diameter_label = MathTex("D").set_color(BLUE).next_to(diameter, UP)
        self.play(Write(diameter_label))
        self.wait()

        self.play(Create(circle_2))
        self.wait()
        self.play(Transform(circle_2, circumference))
        circumference_label = MathTex("C").set_color(RED).next_to(circumference, UP)
        self.play(Write(circumference_label))
        self.wait()

        self.play(ReplacementTransform(diameter_label.copy(), eq[2]), ReplacementTransform(circumference_label.copy(), eq[0]), Write(eq[1]))
        self.wait()
        self.play(Write(eq[-1]), Write(pi))
        self.wait()

class PHI(Scene):
    def construct(self):
        dot1 = Dot([-2, 0, 0])
        dot2 = Dot([0, 0, 0])
        dot3 = Dot([3, 0, 0])

        line_small = Line(dot1.get_center(), dot2.get_center()).set_color(BLUE)
        line_medium = Line(dot2.get_center(), dot3.get_center()).set_color(GREEN)
        line_large = Line(dot1.get_center(), dot3.get_center()).shift(DOWN * 0.5)

        bracket_small = Brace(line_small, direction=[0, 1, 0]).set_color(BLUE)
        bracket_medium = Brace(line_medium, direction=[0, 1, 0]).set_color(GREEN)
        bracket_large = Brace(line_large)

        line_small_label = Tex("A").next_to(bracket_small, UP).set_color(BLUE)
        line_medium_label = Tex("B").next_to(bracket_medium, UP).set_color(GREEN)
        line_large_label = Tex("C").next_to(bracket_large, DOWN)

        eq = MathTex("{C", "\over", "B}", "=", "{B", "\over", "A}", "=").move_to([-4, 2, 0])
        eq[2:5:2].set_color(GREEN)
        eq[6].set_color(BLUE)
        phi = MathTex("\Phi").scale(3).next_to(eq, RIGHT).set_color(GOLD)

        self.play(Create(line_small), Write(bracket_small), Write(line_small_label))
        self.wait()
        self.play(Create(line_medium), Write(bracket_medium), Write(line_medium_label))
        self.wait()
        self.play(Create(line_large), Write(bracket_large), Write(line_large_label))
        self.wait()

        self.play(ReplacementTransform(line_large_label.copy(), eq[0]), Write(eq[1]),
                  ReplacementTransform(line_medium_label.copy(), eq[2]))
        self.wait()
        self.play(Write(eq[3]), ReplacementTransform(line_medium_label.copy(), eq[4]), Write(eq[5]),
                  ReplacementTransform(line_small_label.copy(), eq[-2]))
        self.wait()
        self.play(Write(eq[-1]), Write(phi))
        self.wait()

