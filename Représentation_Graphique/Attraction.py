from manim import *
from random import randint, uniform

NUMBER_OF_DOTS = 10000

class TwoPoints(Scene):
    def construct(self):

        anims = []

        colors = [['#%02X%02X%02X' % (randint(0,255), randint(0,255), randint(0,255))] for _ in range(NUMBER_OF_DOTS)]

        dots = VGroup(*[Dot([uniform(-6, 6), uniform(-4, 4), 0]).set_color(colors[i])
                        for i in range(NUMBER_OF_DOTS)])
        self.add(dots)

        x = 0
        y = 0

        for i in range(len(dots)):
            vector = dots[i].get_center() - dots[0].get_center()
            x += vector[0]
            y += vector[1]

        x = x / (len(dots) - 0)
        y = y / (len(dots) - 0)

        meeting_point = Dot([dots[0].get_x() + x, dots[0].get_y() + y, 0])

        for i in range(len(dots)):
            anims.append(dots[i].animate.move_to(meeting_point))
        self.play(*anims)