from manim import *
from os import listdir
from os.path import join
import re

config.background_color = GREY_A

RHYTHMIC_VALUES = "./Rhythm/"

natsort = lambda s: [int(t) if t.isdigit() else t.lower() for t in re.split('(\d+)', s)]


class RythmicValues(Scene):
    def construct(self):
        number_plane = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            }
        )
        # self.add(number_plane)

        line_top = VGroup(
            *[Line(start=[-6, 1 + (0.25 * i), 0], end=[6, 1 + (0.25 * i), 0]).set_color(BLACK) for i in range(5)])
        line_bot = VGroup(
            *[Line(start=[-6, -2 + (0.25 * i), 0], end=[6, -2 + (0.25 * i), 0]).set_color(BLACK) for i in range(5)])
        self.play(DrawBorderThenFill(line_top), DrawBorderThenFill(line_bot), run_time=2)

        bar = SVGMobject("/Users/imac/Desktop/Manim/Music/Bar/Accolade.svg").scale(2).move_to([-6.2, 0, 0])
        bar_h = VGroup(
            *[Line(start=[-6 + 6 * i, 2.02, 0], end=[-6 + 6 * i, -2.02, 0]).set_color(BLACK).set_stroke(width=6.0) for i
              in range(3)])
        key_G = SVGMobject("/Users/imac/Desktop/Manim/Music/Keys/Sol.svg").move_to([-5.5, 1.5, 0])
        time_sig_top = SVGMobject("/Users/imac/Desktop/Manim/Music/Time_Signature/4_4.svg").scale(0.5).move_to(
            [[-4.5, 1.5, 0]])
        key_F = SVGMobject("/Users/imac/Desktop/Manim/Music/Keys/Fa.svg").scale(0.4).move_to([-5.5, -1.375, 0])
        time_sig_bot = SVGMobject("/Users/imac/Desktop/Manim/Music/Time_Signature/4_4.svg").scale(0.5).move_to(
            [[-4.5, -1.5, 0]])

        self.play(Write(bar), Write(bar_h),
                  DrawBorderThenFill(key_G), DrawBorderThenFill(key_F),
                  Write(time_sig_top), Write(time_sig_bot),
                  run_time=2)

        rhythmic_values = sorted([join(RHYTHMIC_VALUES, f) for f in listdir(RHYTHMIC_VALUES) if f != ".DS_Store"],
                                 key=natsort, reverse=False)

        note = VGroup(*[SVGMobject(rhythmic_values[i]).scale(0.5).move_to([-3.5 + 1 * i, 1.5, 0]) for i in
                        range(1, len(rhythmic_values))])
        self.play(Write(note), run_time=1)
