# %% manim Syntaxe

class Syntaxe(Scene):
    def construct(self):

      eq_1 = MathTex("A", "=", "B", "+", "C").scale(1.5)
      eq_2 = MathTex("B", "=", "A", "-", "C").scale(1.5)
      eq_2[0].set_color(YELLOW)
      eq_3 = MathTex("C", "=", "A", "-", "B").scale(1.5)
      eq_3[0].set_color(YELLOW)

      # First equation
      self.play(Write(eq_1))
      self.wait()
      self.play(eq_1[0].animate.set_color(YELLOW))
      self.wait()
      self.play(eq_1.animate.to_edge(UP))
      self.wait()

      # Second equation
      self.play(ReplacementTransform(eq_1[2].copy(), eq_2[0]))
      self.wait()

      self.play(ReplacementTransform(eq_1[0].copy(), eq_2[2]),
                ReplacementTransform(eq_1[1].copy(), eq_2[1]),
                ReplacementTransform(eq_1[3].copy(), eq_2[3]),
                ReplacementTransform(eq_1[4].copy(), eq_2[4]))
      self.wait()

      self.play(eq_2.animate.shift(UP * 2.2))
      self.wait()

      # Third equation
      self.play(ReplacementTransform(eq_2[-1].copy(), eq_3[0]))
      self.wait()

      self.play(ReplacementTransform(eq_2[0].copy(), eq_3[-1]),
                ReplacementTransform(eq_2[1].copy(), eq_3[1]),
                ReplacementTransform(eq_2[2].copy(), eq_3[2]),
                ReplacementTransform(eq_2[3].copy(), eq_3[3]))
      self.wait()

      self.play(eq_3.animate.shift(UP * 1.2))
      self.wait()

      # + => -
      self.play(eq_1[3].animate.set_color(BLUE),
                eq_2[3].animate.set_color(BLUE),
                eq_3[3].animate.set_color(BLUE))
      self.wait()
