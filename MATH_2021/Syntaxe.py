% % manim
Syntaxe


class Syntaxe(Scene):
    def construct(self):
        garcon = Text('Le garçon s’est fait mordre par le chien après l’avoir provoqué.').scale(0.6)
        chien = Text('Le chien mordit le garçon après avoir été provoqué.').next_to(garcon, DOWN).scale(0.6)
        provoc = Text('Après l’avoir provoqué, le garçon s’est fait mordre par le chien.').next_to(chien, DOWN).scale(
            0.6)

        self.play(Write(garcon))
        self.wait()
        self.play(garcon[0:23].animate.set_color(BLUE))
        self.wait()

        self.play(Write(chien))
        self.wait()
        self.play(chien[0:21].animate.set_color(RED))
        self.wait()

        self.play(Write(provoc))
        self.wait()
        self.play(provoc[0:20].animate.set_color(YELLOW))
        self.wait()