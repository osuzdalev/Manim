from manim import *
import math
import numpy as np


class LinFunc(Scene):
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
        y_label = axes.get_y_axis_label("y").set_color(GREEN)

        # Function computation
        accelerator = ValueTracker(1)
        h_translator = ValueTracker(0)
        v_translator = ValueTracker(0)
        symmetry_y = ValueTracker(1)

        function_equation = axes.get_graph(
            lambda x: accelerator.get_value() * (
                    symmetry_y.get_value() * x + h_translator.get_value()) + v_translator.get_value(),
            color=BLUE)
        function_equation.add_updater(
            lambda m: m.become(
                axes.get_graph(
                    lambda x: accelerator.get_value() * (
                            symmetry_y.get_value() * x + h_translator.get_value()) + v_translator.get_value(),
                    color=BLUE
                )
            )
        )

        # Function Labels
        function_label_pos = [-3.75, 3.5, 0]
        transformation_label_pos = np.add(function_label_pos, [0, -1, 0])

        y_function_label = MathTex("y", "=", "\quad \enspace \enspace", "\\times", "{( \enspace", "x", "\qquad",
                                   ")").move_to(
            function_label_pos)
        y_idx = 0
        eq_idx = 1
        x_idx = 5
        y_function_label[y_idx].set_color(BLUE)
        y_function_label[x_idx].set_color(GREEN)

        function_equation_label = MathTex("f(x)").next_to(y_function_label[eq_idx], LEFT).set_color(BLUE)

        negative_x = MathTex("-x").set_color(GREEN).move_to(y_function_label[x_idx])

        accelerator_label = DecimalNumber().next_to(y_function_label[eq_idx], RIGHT).set_color(PURPLE).scale(0.85)
        accelerator_label.add_updater(
            lambda d: d.set_value(accelerator.get_value()).next_to(y_function_label[eq_idx], RIGHT)).set_color(
            PURPLE).scale(0.85)

        h_translator_label = DecimalNumber(include_sign=True).next_to(y_function_label[x_idx], RIGHT * 0.75).set_color(
            YELLOW).scale(0.85)
        h_translator_label.add_updater(
            lambda d: d.set_value(h_translator.get_value()).next_to(y_function_label[x_idx], RIGHT * 0.75)).set_color(
            YELLOW).scale(0.85)

        v_translator_label = DecimalNumber(include_sign=True).next_to(y_function_label[x_idx], RIGHT * 5.5).set_color(
            MAROON).scale(0.85)
        v_translator_label.add_updater(
            lambda d: d.set_value(v_translator.get_value()).next_to(y_function_label[x_idx], RIGHT * 5.5)).set_color(
            MAROON).scale(0.85)

        # Description labels
        transformation_label = MathTex("Transformations").scale(3)

        v_translation_label = MathTex("Translation \enspace", "Verticale").move_to(transformation_label_pos)
        v_translation_label[1].set_color(MAROON)

        h_translation_label = MathTex("Translation \enspace", "Horizontale").move_to(v_translation_label)
        h_translation_label[1].set_color(YELLOW)

        acceleration_label = MathTex("Accélération").move_to(h_translation_label)
        acceleration_label.set_color(PURPLE)
        deceleration_label = MathTex("Décélération").move_to(acceleration_label)
        deceleration_label.set_color(PURPLE)
        annulation_label = MathTex("Annulation").move_to(deceleration_label)
        annulation_label.set_color(PURPLE)
        symmetry_x_label = MathTex("Symmétrie \enspace", "X").move_to(h_translation_label)
        symmetry_x_label.set_color(PURPLE)

        symmetry_y_label = MathTex("Symmétrie \enspace", "Y").move_to(h_translation_label)
        symmetry_y_label.set_color(GREEN)

        # Init Plot
        self.play(Write(transformation_label))
        self.wait()
        self.play(Transform(transformation_label, axes), Create(x_label), Create(y_label))
        self.wait()
        self.play(Create(function_equation))
        self.wait()

        # Write Function
        self.play(ReplacementTransform(y_label.copy(), y_function_label[y_idx]), run_time=2)
        self.wait()
        self.play(Write(y_function_label[eq_idx]),
                  ReplacementTransform(x_label.copy(), y_function_label[x_idx]))
        self.play(Write(y_function_label[3]),
                  Write(y_function_label[4]),
                  Write(y_function_label[7]),
                  Write(accelerator_label),
                  Write(h_translator_label),
                  Write(v_translator_label),
                  run_time=2)
        self.wait()
        self.play(Transform(y_function_label[y_idx], function_equation_label))
        self.wait()

        # Vertical Translation
        self.play(Write(v_translation_label))
        self.play(ApplyMethod(v_translator.set_value, 3), run_time=2)
        self.wait()
        self.play(ApplyMethod(v_translator.set_value, -3), run_time=2)
        self.wait()
        self.play(ApplyMethod(v_translator.set_value, 0), run_time=2)
        self.wait()

        # Horizontal Translation
        self.play(Transform(v_translation_label, h_translation_label))
        self.play(ApplyMethod(h_translator.set_value, 3), run_time=2)
        self.wait()
        self.play(ApplyMethod(h_translator.set_value, -3), run_time=2)
        self.wait()
        self.play(ApplyMethod(h_translator.set_value, 0), run_time=2)
        self.wait()

        # Acceleration
        self.play(Transform(v_translation_label, acceleration_label))
        self.play(ApplyMethod(accelerator.set_value, 4), run_time=2)
        self.wait()
        self.play(ApplyMethod(accelerator.set_value, 1), run_time=2)
        self.wait()

        # Deceleration
        self.play(Transform(v_translation_label, deceleration_label))
        self.play(ApplyMethod(accelerator.set_value, 0.5), run_time=2)
        self.wait()

        # Nullifying
        self.play(Transform(v_translation_label, annulation_label))
        self.play(ApplyMethod(accelerator.set_value, 0), run_time=2)
        self.wait()

        # Negative Acceleration
        self.play(Transform(v_translation_label, acceleration_label))
        self.play(ApplyMethod(accelerator.set_value, -4), run_time=2)
        self.wait()
        self.play(ApplyMethod(accelerator.set_value, 1), run_time=2)
        self.wait()

        # X-axis Symmetry
        self.play(Transform(v_translation_label, symmetry_x_label))
        self.play(ApplyMethod(accelerator.set_value, -1), run_time=2)
        self.wait()
        self.play(ApplyMethod(accelerator.set_value, 1), run_time=2)
        self.wait()

        # Y-axis Symmetry
        self.play(Transform(v_translation_label, symmetry_y_label))
        self.play(FadeOut(y_function_label[x_idx]),
                  Write(negative_x))
        self.play(ApplyMethod(symmetry_y.set_value, -1), run_time=2)
        self.wait()

        # Back to Init
        self.play(FadeOut(v_translation_label),
                  Transform(negative_x, y_function_label[x_idx]))
        self.play(ApplyMethod(symmetry_y.set_value, 1), run_time=2)
        self.wait()


class Expo(Scene):
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
        y_label = axes.get_y_axis_label("y").set_color(GREEN)

        # Function computation
        accelerator = ValueTracker(1)
        h_translator = ValueTracker(0)
        v_translator = ValueTracker(0)
        symmetry_y = ValueTracker(1)

        function_equation = axes.get_graph(
            lambda x: accelerator.get_value() * (
                math.exp(symmetry_y.get_value() * x + h_translator.get_value())) + v_translator.get_value(),
            color=BLUE)
        function_equation.add_updater(
            lambda m: m.become(
                axes.get_graph(
                    lambda x: accelerator.get_value() * (
                        math.exp(symmetry_y.get_value() * x + h_translator.get_value())) + v_translator.get_value(),
                    color=BLUE
                )
            )
        )

        # Function Labels
        function_label_pos = [-3.75, -2.5, 0]
        transformation_label_pos = np.add(function_label_pos, [0, -1, 0])

        y_function_label = MathTex("y", "=", "\quad \enspace \enspace", "\\times", "e^{(", "x", "\quad \enspace",
                                   ")}").move_to(
            function_label_pos)
        y_idx = 0
        eq_idx = 1
        x_idx = 5
        y_function_label[y_idx].set_color(BLUE)
        y_function_label[x_idx].set_color(GREEN)

        function_equation_label = MathTex("f(x)").next_to(y_function_label[eq_idx], LEFT).set_color(BLUE)

        negative_x = MathTex("-x").scale(0.65).set_color(GREEN).move_to(y_function_label[x_idx])

        accelerator_label = DecimalNumber().next_to(y_function_label[eq_idx], RIGHT).set_color(PURPLE).scale(0.85)
        accelerator_label.add_updater(
            lambda d: d.set_value(accelerator.get_value()).next_to(y_function_label[eq_idx], RIGHT)).set_color(
            PURPLE).scale(0.85)

        h_translator_label = DecimalNumber(include_sign=True).next_to(y_function_label[x_idx], RIGHT * 0.75).set_color(
            YELLOW).scale(0.7)
        h_translator_label.add_updater(
            lambda d: d.set_value(h_translator.get_value()).next_to(y_function_label[x_idx], RIGHT * 0.75)).set_color(
            YELLOW).scale(0.7)

        v_translator_label = DecimalNumber(include_sign=True).next_to(y_function_label[eq_idx], RIGHT * 12.5).set_color(
            MAROON).scale(0.85)
        v_translator_label.add_updater(
            lambda d: d.set_value(v_translator.get_value()).next_to(y_function_label[eq_idx], RIGHT * 12.5)).set_color(
            MAROON).scale(0.85)

        # Description labels
        transformation_label = MathTex("Transformations").scale(3)

        v_translation_label = MathTex("Translation \enspace", "Verticale").move_to(transformation_label_pos)
        v_translation_label[1].set_color(MAROON)

        h_translation_label = MathTex("Translation \enspace", "Horizontale").move_to(v_translation_label)
        h_translation_label[1].set_color(YELLOW)

        acceleration_label = MathTex("Accélération").move_to(h_translation_label)
        acceleration_label.set_color(PURPLE)
        deceleration_label = MathTex("Décélération").move_to(acceleration_label)
        deceleration_label.set_color(PURPLE)
        annulation_label = MathTex("Annulation").move_to(deceleration_label)
        annulation_label.set_color(PURPLE)
        symmetry_x_label = MathTex("Symmétrie \enspace", "X").move_to(h_translation_label)
        symmetry_x_label.set_color(PURPLE)

        symmetry_y_label = MathTex("Symmétrie \enspace", "Y").move_to(h_translation_label)
        symmetry_y_label.set_color(GREEN)

        # Init Plot
        self.play(Write(transformation_label))
        self.wait()
        self.play(Transform(transformation_label, axes), Create(x_label), Create(y_label))
        self.wait()
        self.play(Create(function_equation))
        self.wait()

        # Write Function
        self.play(ReplacementTransform(y_label.copy(), y_function_label[y_idx]), run_time=2)
        self.wait()
        self.play(Write(y_function_label[eq_idx]),
                  ReplacementTransform(x_label.copy(), y_function_label[x_idx]))
        self.play(Write(y_function_label[3]),
                  Write(y_function_label[4]),
                  Write(y_function_label[7]),
                  Write(accelerator_label),
                  Write(h_translator_label),
                  Write(v_translator_label),
                  run_time=2)
        self.wait()
        self.play(Transform(y_function_label[y_idx], function_equation_label))
        self.wait()

        # Vertical Translation
        self.play(Write(v_translation_label))
        self.play(ApplyMethod(v_translator.set_value, 3), run_time=2)
        self.wait()
        self.play(ApplyMethod(v_translator.set_value, -3), run_time=2)
        self.wait()
        self.play(ApplyMethod(v_translator.set_value, 0), run_time=2)
        self.wait()

        # Horizontal Translation
        self.play(Transform(v_translation_label, h_translation_label))
        self.play(ApplyMethod(h_translator.set_value, 3), run_time=2)
        self.wait()
        self.play(ApplyMethod(h_translator.set_value, -3), run_time=2)
        self.wait()
        self.play(ApplyMethod(h_translator.set_value, 0), run_time=2)
        self.wait()

        # Acceleration
        self.play(Transform(v_translation_label, acceleration_label))
        self.play(ApplyMethod(accelerator.set_value, 4), run_time=2)
        self.wait()
        self.play(ApplyMethod(accelerator.set_value, 1), run_time=2)
        self.wait()

        # Deceleration
        self.play(Transform(v_translation_label, deceleration_label))
        self.play(ApplyMethod(accelerator.set_value, 0.5), run_time=2)
        self.wait()

        # Nullifying
        self.play(Transform(v_translation_label, annulation_label))
        self.play(ApplyMethod(accelerator.set_value, 0), run_time=2)
        self.wait()

        # Negative Acceleration
        self.play(Transform(v_translation_label, acceleration_label))
        self.play(ApplyMethod(accelerator.set_value, -4), run_time=2)
        self.wait()
        self.play(ApplyMethod(accelerator.set_value, 1), run_time=2)
        self.wait()

        # X-axis Symmetry
        self.play(Transform(v_translation_label, symmetry_x_label))
        self.play(ApplyMethod(accelerator.set_value, -1), run_time=2)
        self.wait()
        self.play(ApplyMethod(accelerator.set_value, 1), run_time=2)
        self.wait()

        # Y-axis Symmetry
        self.play(Transform(v_translation_label, symmetry_y_label))
        self.play(FadeOut(y_function_label[x_idx]),
                  Write(negative_x))
        self.play(ApplyMethod(symmetry_y.set_value, -1), run_time=2)
        self.wait()

        # Back to Init
        self.play(FadeOut(v_translation_label),
                  Transform(negative_x, y_function_label[x_idx]))
        self.play(ApplyMethod(symmetry_y.set_value, 1), run_time=2)
        self.wait()


class LogNat(Scene):
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
        y_label = axes.get_y_axis_label("y").set_color(GREEN)

        # Function computation
        accelerator = ValueTracker(1)
        h_translator = ValueTracker(0)
        v_translator = ValueTracker(0)
        symmetry_y = ValueTracker(-1)

        function_equation = axes.get_graph(
            lambda x: accelerator.get_value() * math.log(
                x + h_translator.get_value()) + v_translator.get_value(),
            x_range=[0.01, 5],
            color=BLUE)
        function_equation.add_updater(
            lambda m: m.become(
                axes.get_graph(
                    lambda x: accelerator.get_value() * math.log(x + h_translator.get_value())
                              + v_translator.get_value(),
                    x_range=[-h_translator.get_value() + 0.01, 5],
                    color=BLUE
                )
            )
        )

        function_equation_2 = axes.get_graph(
            lambda x: accelerator.get_value() * math.log(
                symmetry_y.get_value() * x + h_translator.get_value()) + v_translator.get_value(),
            x_range=[-5, -0.01],
            color=BLUE)

        function_equation_3 = axes.get_graph(
            lambda x: accelerator.get_value() * math.log(
                x + h_translator.get_value()) + v_translator.get_value(),
            x_range=[0.01, 5],
            color=BLUE)

        # Function Labels
        function_label_pos = [-3.75, -2.5, 0]
        transformation_label_pos = np.add(function_label_pos, [0, -1, 0])

        y_function_label = MathTex("y", "=", "\quad \enspace \enspace", "\\times", "(", "ln(", "x", "\quad \enspace",
                                   "\enspace ))").move_to(function_label_pos)
        y_idx = 0
        eq_idx = 1
        x_idx = 6
        y_function_label[y_idx].set_color(BLUE)
        y_function_label[x_idx].set_color(GREEN)

        function_equation_label = MathTex("f(x)").next_to(y_function_label[eq_idx], LEFT).set_color(BLUE)

        negative_x = MathTex("-x").set_color(GREEN).move_to(y_function_label[x_idx])

        accelerator_label = DecimalNumber().next_to(y_function_label[eq_idx], RIGHT).set_color(PURPLE).scale(0.85)
        accelerator_label.add_updater(
            lambda d: d.set_value(accelerator.get_value()).next_to(y_function_label[eq_idx], RIGHT)).set_color(
            PURPLE).scale(0.85)

        h_translator_label = DecimalNumber(include_sign=True).next_to(y_function_label[x_idx], RIGHT * 0.75).set_color(
            YELLOW).scale(0.85)
        h_translator_label.add_updater(
            lambda d: d.set_value(h_translator.get_value()).next_to(y_function_label[x_idx], RIGHT * 0.75)).set_color(
            YELLOW).scale(0.85)

        v_translator_label = DecimalNumber(include_sign=True).next_to(y_function_label[eq_idx], RIGHT * 16.5).set_color(
            MAROON).scale(0.85)
        v_translator_label.add_updater(
            lambda d: d.set_value(v_translator.get_value()).next_to(y_function_label[eq_idx], RIGHT * 16.5)).set_color(
            MAROON).scale(0.85)

        # Description labels
        transformation_label = MathTex("Transformations").scale(3)

        v_translation_label = MathTex("Translation \enspace", "Verticale").move_to(transformation_label_pos)
        v_translation_label[1].set_color(MAROON)

        h_translation_label = MathTex("Translation \enspace", "Horizontale").move_to(v_translation_label)
        h_translation_label[1].set_color(YELLOW)

        acceleration_label = MathTex("Accélération").move_to(h_translation_label)
        acceleration_label.set_color(PURPLE)
        deceleration_label = MathTex("Décélération").move_to(acceleration_label)
        deceleration_label.set_color(PURPLE)
        annulation_label = MathTex("Annulation").move_to(deceleration_label)
        annulation_label.set_color(PURPLE)
        symmetry_x_label = MathTex("Symmétrie \enspace", "X").move_to(h_translation_label)
        symmetry_x_label.set_color(PURPLE)

        symmetry_y_label = MathTex("Symmétrie \enspace", "Y").move_to(h_translation_label)
        symmetry_y_label.set_color(GREEN)

        # Init Plot
        self.play(Write(transformation_label))
        self.wait()
        self.play(Transform(transformation_label, axes), Create(x_label), Create(y_label))
        self.wait()
        self.play(Create(function_equation))
        self.wait()

        # Write Function
        self.play(ReplacementTransform(y_label.copy(), y_function_label[y_idx]), run_time=2)
        self.wait()
        self.play(Write(y_function_label[eq_idx]),
                  ReplacementTransform(x_label.copy(), y_function_label[x_idx]))
        self.play(Write(y_function_label[3:6]),
                  Write(y_function_label[8]),
                  Write(accelerator_label),
                  Write(h_translator_label),
                  Write(v_translator_label),
                  run_time=2)
        self.wait()
        self.play(Transform(y_function_label[y_idx], function_equation_label))
        self.wait()

        # Vertical Translation
        self.play(Write(v_translation_label))
        self.play(ApplyMethod(v_translator.set_value, 3), run_time=2)
        self.wait()
        self.play(ApplyMethod(v_translator.set_value, -3), run_time=2)
        self.wait()
        self.play(ApplyMethod(v_translator.set_value, 0), run_time=2)
        self.wait()

        # Horizontal Translation
        self.play(Transform(v_translation_label, h_translation_label))
        self.play(ApplyMethod(h_translator.set_value, 3), run_time=2)
        self.wait()
        self.play(ApplyMethod(h_translator.set_value, -3), run_time=2)
        self.wait()
        self.play(ApplyMethod(h_translator.set_value, 0), run_time=2)
        self.wait()

        # Acceleration
        self.play(Transform(v_translation_label, acceleration_label))
        self.play(ApplyMethod(accelerator.set_value, 4), run_time=2)
        self.wait()
        self.play(ApplyMethod(accelerator.set_value, 1), run_time=2)
        self.wait()

        # Deceleration
        self.play(Transform(v_translation_label, deceleration_label))
        self.play(ApplyMethod(accelerator.set_value, 0.5), run_time=2)
        self.wait()

        # Nullifying
        self.play(Transform(v_translation_label, annulation_label))
        self.play(ApplyMethod(accelerator.set_value, 0), run_time=2)
        self.wait()

        # Negative Acceleration
        self.play(Transform(v_translation_label, acceleration_label))
        self.play(ApplyMethod(accelerator.set_value, -4), run_time=2)
        self.wait()
        self.play(ApplyMethod(accelerator.set_value, 1), run_time=2)
        self.wait()

        # X-axis Symmetry
        self.play(Transform(v_translation_label, symmetry_x_label))
        self.play(ApplyMethod(accelerator.set_value, -1), run_time=2)
        self.wait()
        self.play(ApplyMethod(accelerator.set_value, 1), run_time=2)
        self.wait()

        # Y-axis Symmetry
        self.play(Transform(v_translation_label, symmetry_y_label))
        self.play(FadeOut(y_function_label[x_idx]),
                  Write(negative_x))
        function_equation.clear_updaters()
        self.play(Transform(function_equation, function_equation_2), run_time=2)
        self.wait()

        # Back to Init
        self.play(FadeOut(v_translation_label),
                  Transform(negative_x, y_function_label[x_idx]))
        self.play(Transform(function_equation, function_equation_3), run_time=2)
        self.wait()


class Sqrt(Scene):
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
        y_label = axes.get_y_axis_label("y").set_color(GREEN)

        accelerator = ValueTracker(1)
        h_translator = ValueTracker(0)
        v_translator = ValueTracker(0)

        function_equation = axes.get_graph(
            lambda x: accelerator.get_value() * math.sqrt(x + h_translator.get_value()) + v_translator.get_value(),
            x_range=[-h_translator.get_value() + 0.01, 5],
            color=BLUE)
        function_equation.add_updater(
            lambda m: m.become(
                axes.get_graph(
                    lambda x: accelerator.get_value() * math.sqrt(
                        x + h_translator.get_value()) + v_translator.get_value(),
                    x_range=[-h_translator.get_value() + 0.01, 5],
                    color=BLUE
                )
            )
        )

        y_function_label = MathTex("y", "=", "a", "\quad", "\\times", "(", "\sqrt{x", "+", "b}", "\enspace )", "+",
                                   "c").move_to([-3.5, 3, 0])
        y_function_label[0].set_color(BLUE)
        y_function_label[6][2].set_color(GREEN)

        function_equation_label = MathTex("f(x)").next_to(y_function_label[1], LEFT).set_color(BLUE)

        accelerator_label = DecimalNumber().next_to(y_function_label[1]).set_color(PURPLE).scale(0.85)
        accelerator_label.add_updater(
            lambda d: d.set_value(accelerator.get_value()).next_to(y_function_label[1])).set_color(PURPLE).scale(0.85)

        h_translator_label = DecimalNumber(include_sign=True).next_to(accelerator_label, RIGHT * 6.5).set_color(
            YELLOW).scale(0.85)
        h_translator_label.add_updater(
            lambda d: d.set_value(h_translator.get_value()).next_to(accelerator_label, RIGHT * 6.5)).set_color(
            YELLOW).scale(0.85)

        v_translator_label = DecimalNumber(include_sign=True).next_to(h_translator_label, RIGHT * 2).set_color(
            MAROON).scale(0.85)
        v_translator_label.add_updater(
            lambda d: d.set_value(v_translator.get_value()).next_to(h_translator_label, RIGHT * 2)).set_color(
            MAROON).scale(0.85)

        transformation_label = MathTex("Transformations").scale(3)
        v_translation_label = MathTex("Translation \enspace Verticale").move_to([-3.5, 2, 0])
        h_translation_label = MathTex("Translation \enspace Horizontale").move_to(v_translation_label)
        acceleration_label = MathTex("Accélération").move_to(h_translation_label)

        self.play(Write(transformation_label))
        self.wait()
        self.play(Transform(transformation_label, axes), Create(x_label), Create(y_label))
        self.wait()
        self.play(Create(function_equation))
        self.wait()

        self.play(ReplacementTransform(y_label.copy(), y_function_label[0]), run_time=2)
        self.wait()
        self.play(Write(y_function_label[1]),
                  Transform(x_label.copy(), y_function_label[6]))
        self.play(Write(y_function_label[4]),
                  Write(y_function_label[5]),
                  Write(y_function_label[9]),
                  Write(accelerator_label),
                  Write(h_translator_label),
                  Write(v_translator_label),
                  run_time=2)
        self.wait()
        self.play(Transform(y_function_label[0], function_equation_label))
        self.wait()

        self.play(Write(v_translation_label))
        self.play(ApplyMethod(v_translator.increment_value, 3), run_time=2)
        self.wait()
        self.play(ApplyMethod(v_translator.increment_value, -6), run_time=2)
        self.wait()
        self.play(ApplyMethod(v_translator.increment_value, 3), run_time=2)
        self.wait()

        self.play(Transform(v_translation_label, h_translation_label))
        self.play(ApplyMethod(h_translator.increment_value, 3), run_time=2)
        self.wait()
        self.play(ApplyMethod(h_translator.increment_value, -6), run_time=2)
        self.wait()
        self.play(ApplyMethod(h_translator.increment_value, 3), run_time=2)
        self.wait()

        self.play(Transform(v_translation_label, acceleration_label))
        self.play(ApplyMethod(accelerator.increment_value, 3), run_time=2)
        self.wait()
        self.play(ApplyMethod(accelerator.increment_value, -3), run_time=2)
        self.wait()
        self.play(ApplyMethod(accelerator.increment_value, -0.5), run_time=2)
        self.wait()
        self.play(ApplyMethod(accelerator.increment_value, -0.5), run_time=2)
        self.wait()
        self.play(ApplyMethod(accelerator.increment_value, -3), run_time=2)
        self.wait()
        self.play(ApplyMethod(accelerator.increment_value, 4), run_time=2)
        self.wait()


class Square(Scene):
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
        y_label = axes.get_y_axis_label("y").set_color(GREEN)

        # Function computation
        accelerator = ValueTracker(1)
        h_translator = ValueTracker(0)
        v_translator = ValueTracker(0)
        symmetry_y = ValueTracker(1)

        function_equation = axes.get_graph(
            lambda x: accelerator.get_value() * (
                        symmetry_y.get_value() * x + h_translator.get_value()) ** 2 + v_translator.get_value(),
            color=BLUE)
        function_equation.add_updater(
            lambda m: m.become(
                axes.get_graph(
                    lambda x: accelerator.get_value() * (
                                symmetry_y.get_value() * x + h_translator.get_value()) ** 2 + v_translator.get_value(),
                    color=BLUE
                )
            )
        )

        # Function Labels
        function_label_pos = [3.75, -2.5, 0]
        transformation_label_pos = np.add(function_label_pos, [0, -1, 0])

        y_function_label = MathTex("y", "=", "\quad \enspace \enspace", "\\times", "{(", "x", "\qquad", ")}^2").move_to(
            function_label_pos)
        y_idx = 0
        eq_idx = 1
        x_idx = 5
        y_function_label[y_idx].set_color(BLUE)
        y_function_label[x_idx].set_color(GREEN)

        function_equation_label = MathTex("f(x)").next_to(y_function_label[eq_idx], LEFT).set_color(BLUE)

        negative_x = MathTex("-x").set_color(GREEN).move_to(y_function_label[x_idx])

        accelerator_label = DecimalNumber().next_to(y_function_label[eq_idx], RIGHT).set_color(PURPLE).scale(0.85)
        accelerator_label.add_updater(
            lambda d: d.set_value(accelerator.get_value()).next_to(y_function_label[eq_idx], RIGHT)).set_color(
            PURPLE).scale(0.85)

        h_translator_label = DecimalNumber(include_sign=True).next_to(y_function_label[x_idx], RIGHT * 0.3).set_color(
            YELLOW).scale(0.85)
        h_translator_label.add_updater(
            lambda d: d.set_value(h_translator.get_value()).next_to(y_function_label[x_idx], RIGHT * 0.3)).set_color(
            YELLOW).scale(0.85)

        v_translator_label = DecimalNumber(include_sign=True).next_to(y_function_label[x_idx], RIGHT * 6).set_color(
            MAROON).scale(0.85)
        v_translator_label.add_updater(
            lambda d: d.set_value(v_translator.get_value()).next_to(y_function_label[x_idx], RIGHT * 6)).set_color(
            MAROON).scale(0.85)

        # Description labels
        transformation_label = MathTex("Transformations").scale(3)
        v_translation_label = MathTex("Translation \enspace", "Verticale").move_to(transformation_label_pos)
        v_translation_label[1].set_color(MAROON)
        h_translation_label = MathTex("Translation \enspace", "Horizontale").move_to(v_translation_label)
        h_translation_label[1].set_color(YELLOW)
        acceleration_label = MathTex("Accélération").move_to(h_translation_label)
        acceleration_label.set_color(PURPLE)
        symmetry_x_label = MathTex("Symmétrie \enspace X").move_to(h_translation_label)
        symmetry_x_label.set_color(PURPLE)
        symmetry_y_label = MathTex("Symmétrie \enspace Y").move_to(h_translation_label)
        symmetry_y_label.set_color(GREEN)

        # Init Plot
        self.play(Write(transformation_label))
        self.wait()
        self.play(Transform(transformation_label, axes), Create(x_label), Create(y_label))
        self.wait()
        self.play(Create(function_equation))
        self.wait()

        # Write Function
        self.play(ReplacementTransform(y_label.copy(), y_function_label[y_idx]), run_time=2)
        self.wait()
        self.play(Write(y_function_label[eq_idx]),
                  Transform(x_label.copy(), y_function_label[x_idx]))
        self.play(Write(y_function_label[3]),
                  Write(y_function_label[4]),
                  Write(y_function_label[7]),
                  Write(accelerator_label),
                  Write(h_translator_label),
                  Write(v_translator_label),
                  run_time=2)
        self.wait()
        self.play(Transform(y_function_label[y_idx], function_equation_label))
        self.wait()

        # Vertical Translation
        self.play(Write(v_translation_label))
        self.play(ApplyMethod(v_translator.set_value, 3), run_time=2)
        self.wait()
        self.play(ApplyMethod(v_translator.set_value, -3), run_time=2)
        self.wait()
        self.play(ApplyMethod(v_translator.set_value, 0), run_time=2)
        self.wait()

        # Horizontal Translation
        self.play(Transform(v_translation_label, h_translation_label))
        self.play(ApplyMethod(h_translator.set_value, 3), run_time=2)
        self.wait()
        self.play(ApplyMethod(h_translator.set_value, -3), run_time=2)
        self.wait()
        self.play(ApplyMethod(h_translator.set_value, 0), run_time=2)
        self.wait()

        # Acceleration
        self.play(Transform(v_translation_label, acceleration_label))
        self.play(ApplyMethod(accelerator.set_value, 4), run_time=2)
        self.wait()
        self.play(ApplyMethod(accelerator.set_value, 1), run_time=2)
        self.wait()

        # Deceleration
        self.play(ApplyMethod(accelerator.set_value, 0.5), run_time=2)
        self.wait()

        # Nullifying
        self.play(ApplyMethod(accelerator.set_value, 0), run_time=2)
        self.wait()

        # X-axis Symmetry
        self.play(Transform(v_translation_label, symmetry_x_label), run_time=2)
        self.wait()
        self.play(ApplyMethod(accelerator.set_value, -1), run_time=2)
        self.wait()

        # Negative Acceleration
        self.play(FadeOut(v_translation_label),
                  Write(acceleration_label),
                  run_time=2)
        self.wait()
        self.play(ApplyMethod(accelerator.set_value, -4), run_time=2)
        self.wait()

        # Back to Init
        self.play(ApplyMethod(accelerator.set_value, 1), run_time=2)
        self.wait()
