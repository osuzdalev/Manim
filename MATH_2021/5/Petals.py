from manim import *
import math

PHI = (1 + math.sqrt(5)) / 2

big_dimension = False
BIG = [250, 0.03, 0.75, 2.0]
SMALL = [20, 0.2, 1.75, 3.0]
ROWS = BIG[0] if big_dimension else SMALL[0]
CIRCLE_SPACE = BIG[1] if big_dimension else SMALL[1]
DOT_SCALE = BIG[2] if big_dimension else SMALL[2]
DOT_STROKE_WIDTH = BIG[3] if big_dimension else SMALL[3]


class Intro(Scene):
    def construct(self):
        phi = MathTex("\Phi", "=", PHI, "...").scale(2)
        phi[0].set_color(GOLD)
        self.play(Write(phi), run_time=2)


class Petals(Scene):
    def construct(self):
        circles = self.gen_circles()
        self.gen_rotations(circles, 0.2, 0.22, 1000)
        #self.gen_interest(circles)

    def gen_circles(self):
        circles = VGroup(
            *[Circle(fill_opacity=0.75).scale(0.75 + CIRCLE_SPACE * i).set_color(GREEN) for i in range(ROWS)])
        self.add(circles[0])
        print("CIRCLES GENERATED")
        return circles

    def gen_petals(self, circles, parts):
        arrangement = VGroup()

        theta = parts * 360
        counter = 0
        row = 0
        while row < ROWS:
            arrangement.add(Dot(circles[row].point_at_angle(counter * DEGREES),
                                stroke_color=WHITE, stroke_width=DOT_STROKE_WIDTH, color=GOLD).scale(DOT_SCALE))
            counter += theta
            if counter > 360:
                counter %= 360
                row += 1
        return arrangement

    def gen_arrangements(self, circles, start, stop, step):
        arrangements = []
        for i in range(step):
            arrangements.append(self.gen_petals(circles, start + (stop - start) / step * i))
        return arrangements

    def gen_rotations(self, circles, start, stop, step):
        arrangements = self.gen_arrangements(circles, start, stop, step)

        decimal = DecimalNumber(
            start,
            show_ellipsis=True,
            num_decimal_places=5,
            include_sign=True,
        ).to_corner(UR)

        self.play(Write(arrangements[0]),
                  Write(decimal),
                  run_time=1.0, rate_functions=linear)
        for i in range(1, len(arrangements)):
            decimal.set_value(start + (stop - start) / step * i)
            self.play(Transform(arrangements[0], arrangements[i]), run_time=0.1, rate_functions=linear)

    def gen_interest(self, circles):
        rationals = [1, 2, 3, 10, 20, 100]
        rational_arrangements = []
        irrationals = [math.pi, math.e, math.sqrt(5), math.sqrt(2) / 2, PHI]
        irrational_arrangements = []

        decimal = DecimalNumber(0, stroke_color=BLACK, stroke_opacity=1.0, stroke_width=1.0, color=BLUE,
                                show_ellipsis=True, num_decimal_places=5, include_sign=True).to_corner(UR)

        tex = MathTex("\pi", "e", "\sqrt{5}", "{ \sqrt{2} \over 2}", "\Phi",
                      stroke_color=BLACK, stroke_opacity=1.0, stroke_width=2.0, color=BLUE).scale(3)
        irr_tex = VGroup(*[tex[i].next_to(decimal, DOWN) for i in range(len(tex))])

        self.add(circles[0], decimal)

        basis = self.gen_petals(circles, 1 / irrationals[0])
        self.play(Write(basis))

        for i in range(len(rationals)):
            rational_arrangements.append(self.gen_petals(circles, 1 / rationals[i]))
            decimal.set_value(1 / rationals[i])
            self.play(Transform(basis, rational_arrangements[i]), run_time=2.0)
            self.wait()
        # for i in range(len(irrationals)):
        #     irrational_arrangements.append(self.gen_petals(circles, 1 / irrationals[i]))
        #     self.play(Transform(basis, irrational_arrangements[i]),
        #               Transform(irr_tex[0], irr_tex[i]))
        #     decimal.set_value(1 / irrationals[i])
        #     self.wait()


class Fraction(Scene):
    def construct(self):
        five = MathTex("5", "=", "{5 \over 1}").scale(2).to_edge(UP)
        fith = MathTex("{1 \over 5}", "=", "0.2", "=", "20\%").scale(2).next_to(five, DOWN)
        three_quaters = MathTex("{3 \over 4}", "=", "0.75", "=", "75\%").scale(2).next_to(fith, DOWN)

        self.play(Write(five))
        self.wait()
        self.play(ReplacementTransform(five.copy(), fith[:3]))
        self.wait()
        self.play(Write(fith[3:]))
        self.wait()
        self.play(ReplacementTransform(fith.copy(), three_quaters[:3]))
        self.wait()
        self.play(Write(three_quaters[3:]))
        self.wait()


class Irrationals(Scene):
    def construct(self):
        pi = MathTex("\pi", "=", math.pi, "...").scale(2).to_edge(UP)
        pi[0].set_color(BLUE)
        phi = MathTex("\Phi", "=", PHI, "...").scale(2)
        phi[0].set_color(GOLD)
        square_2 = MathTex("\sqrt{2}", "=", math.sqrt(2), "...").scale(2).to_edge(DOWN)
        square_2[0].set_color(GREEN)

        self.play(Write(pi))
        self.wait()
        self.play(Write(phi))
        self.wait()
        self.play(Write(square_2))
        self.wait()

        self.clear()

        fraction = MathTex("{X \over X}").scale(3)
        cross = Cross().scale(3)

        self.play(Write(fraction))
        self.wait()
        self.play(Write(cross))
        self.wait()
        

class IrrFractions(Scene):
    def construct(self):
        pi = MathTex("\pi", "=3+\\frac{1}{7+\\frac{1}{15+\\frac{1}{1+\\frac{1}{292+\\frac{1}{1+\\frac{1}{1+\\frac{1}{1+\ddots}}}}}}}").scale(2)
        pi[0].set_color(BLUE)
        sqrt_2 = MathTex("\sqrt{2}", "=1+\\frac{1}{2+\\frac{1}{2+\\frac{1}{2+\\frac{1}{2+\ddots}}}}").scale(2)
        sqrt_2[0].set_color(GREEN)
        phi = MathTex("\Phi", "=1+\\frac{1}{1+\\frac{1}{1+\\frac{1}{1+\ddots}}}").scale(2)
        phi[0].set_color(GOLD)

        self.play(Write(pi[0]))
        self.wait()
        self.play(Write(pi[1]))
        self.wait()
        self.clear()

        self.play(Write(sqrt_2[0]))
        self.wait()
        self.play(Write(sqrt_2[1]))
        self.wait()
        self.clear()

        self.play(Write(phi[0]))
        self.wait()
        self.play(Write(phi[1]))
        self.wait()
        self.clear()