# %%manim Shapes

class Shapes(Scene):
  def construct(self):

    cylinder_svg = SVGMobject('/content/sample_data/cylinder.svg', color=WHITE).scale(3).to_edge(LEFT)
    self.play(Write(cylinder_svg), run_time=2)
    self.wait()

    cylinder_area = MathTex("A = ", "2 \pi r h + 2 \pi r^2").scale(2).to_corner(UR)
    cylinder_area[0][0].set_color(BLUE)
    cylinder_area[1][1:7:5].set_color(YELLOW)

    cylinder_volume = MathTex("V = ", "\pi r^2 h").scale(2).to_edge(RIGHT)
    cylinder_volume[0][0].set_color(GREEN)
    cylinder_volume[1][0].set_color(YELLOW)

    self.play(Write(cylinder_area),
              Write(cylinder_volume))
    self.wait()

    cone_svg = SVGMobject('/content/sample_data/cone.svg', color=WHITE).scale(3).to_edge(LEFT)
    self.play(Transform(cylinder_svg, cone_svg))

    cone_area = MathTex("A = ", "\pi r^{2}+\pi r \sqrt{r^{2}+h^{2}}").scale(2).to_corner(UR)
    cone_area[0][0].set_color(BLUE)
    cone_area[1][0].set_color(YELLOW)
    cone_area[1][4].set_color(YELLOW)

    cone_volume = MathTex("V = ", "{1 \over 3} \pi r^2 h").scale(2).to_edge(RIGHT)
    cone_volume[0][0].set_color(GREEN)
    cone_volume[1][3].set_color(YELLOW)

    self.play(Transform(cylinder_area, cone_area),
              Transform(cylinder_volume, cone_volume))
    self.wait()

    sphere_svg = SVGMobject('/content/sample_data/Sphere.svg', color=WHITE).scale(3).to_edge(LEFT)
    self.play(Transform(cylinder_svg, sphere_svg))

    sphere_area = MathTex("A = ", "4 \pi r^2").scale(2).to_corner(UR)
    sphere_area[0][0].set_color(BLUE)
    sphere_area[1][1].set_color(YELLOW)

    sphere_volume = MathTex("V = ", "{4 \over 3} \pi r^3").scale(2).to_edge(RIGHT)
    sphere_volume[0][0].set_color(GREEN)
    sphere_volume[1][3].set_color(YELLOW)

    self.play(Transform(cylinder_area, sphere_area),
              Transform(cylinder_volume, sphere_volume))
    self.wait()

    torus_svg = SVGMobject('/content/sample_data/3D-Torus.svg', color=WHITE).scale(3).to_edge(LEFT)
    self.play(Transform(cylinder_svg, torus_svg))

    torus_area = MathTex("A = ", "4 \pi^2 r a").scale(2).to_corner(UR)
    torus_area[0][0].set_color(BLUE)
    torus_area[1][1].set_color(YELLOW)

    torus_volume = MathTex("V = ", "2 \pi^2 r^2 a").scale(2).to_edge(RIGHT)
    torus_volume[0][0].set_color(GREEN)
    torus_volume[1][1].set_color(YELLOW)

    self.play(Transform(cylinder_area, torus_area),
              Transform(cylinder_volume, torus_volume))
    self.wait()