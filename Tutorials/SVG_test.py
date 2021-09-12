from manim import *


def get_colors_from_input(color1, color2, n):
    # Extract color coordinates
    r1, g1, b1 = [int('0x' + x, 16) for x in [color1[i:i + 2] for i in range(0, 6, 2)]]
    r2, g2, b2 = [int('0x' + x, 16) for x in [color2[i:i + 2] for i in range(0, 6, 2)]]

    # Build the coordinate-wise distribution
    # We could have used `range`, but using floats prevents some rounding errors
    r_values = [int(r1 + (r2 / n) * x) for x in range(1, n + 1)]
    g_values = [int(g1 + (g2 / n) * x) for x in range(1, n + 1)]
    b_values = [int(b1 + (b2 / n) * x) for x in range(1, n + 1)]
    dec_cols = zip(r_values, g_values, b_values)

    # Format back the coordinates to strings.
    generate = generate = ['#' + color1] + ['#' + ''.join(hex(x).replace('x', '')[-2:] for x in hex_num) for hex_num in
                                            dec_cols]

    return generate


class SVG(Scene):
    def construct(self):
        eat = SVGMobject('./SVG_media/roshan.svg').scale(3).set_color(WHITE)

        #svg.set_color(color=[PURPLE_E, BLUE,  GREEN, YELLOW, RED, MAROON_E])

        # brand = Text("Boroda Strats", font="Copperplate", weight="BOLD").shift(RIGHT)
        # gay.set_color(color=(PURPLE_E, BLUE, GREEN, YELLOW, RED, MAROON_E))

        # colors = get_colors_from_input("000000", "FFFFFF", len(svg))
        # for i in range(len(svg)):
        #     svg[i].set_color(colors[i])
        #svg[0].set_color(color=[TEAL, YELLOW_A])
        #svg[6:8].set_color(color=[WHITE, GOLD_A])

        #test = Tex("你好", tex_template=TexTemplateLibrary.ctex).to_edge(DOWN).scale(3)
        #for i in range(len(test)):
            #test[i].set_color(color=[YELLOW_A, TEAL])

        self.play(DrawBorderThenFill(eat))
