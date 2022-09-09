from manim import *
class q_equation(Scene):
    def construct(self):

        t1 = MathTex("2x^2", "-7x", "+3", "=0")
        tf = MathTex("(a-b)^2=","a^2","+b^2","-2ab").scale(1.5).set_color(BLUE)
        eg = VGroup(
            MathTex("2x^2", "-7x", "+3", "=0"),
            MathTex("\\frac{2}{2}x^2", "-\\frac{7}{2}x", "+\\frac{3}{2}", "=\\frac{0}{2}"),
            MathTex("x^2", "-\\frac{7}{2}x", "+\\frac{3}{2}", "=0"),
            MathTex("x^2", "-\\frac{7}{2}x","+\\frac{3}{2}", "+\\left(\\frac{7}{4}\\right)^2", "=\\left(\\frac{7}{4}\\right)^2"),
            MathTex("x^2", "-\\frac{7}{2}x", "+\\left(\\frac{7}{4}\\right)^2", "=\\frac{49}{16}", "-\\frac{3}{2}"),
            MathTex("\\left(x-\\frac{7}{4}\\right)^2", "=\\frac{49-24}{16}"),
            MathTex("\\left(x-\\frac{7}{4}\\right)^2","=\\frac{25}{16}"),
            MathTex("x-\\frac{7}{4}","=\\sqrt{\\frac{25}{16}}"),
            MathTex("x-\\frac{7}{4}", "=\\pm\\frac{5}{4}"),
            MathTex("x", "=\\frac{7\\pm 5}{4}")
            ).scale(1.5)
        dg = VGroup(
            MathTex("x=\\frac{7+5}{4}","\\quad \\quad", "x=\\frac{7-5}{4}"),
            MathTex("x=\\frac{12}{4}","\\quad  \\quad", "x=\\frac{2}{4}"),
            MathTex("x=3","\\quad  \\quad", "x=\\frac{1}{2}"),
            ).scale(1.5)
        eg.shift(UP)
        eg[1].next_to(eg[0], DOWN, buff=0.75)
        eg[3].shift(DOWN*0.5)
        eg[4].shift(DOWN*0.5)
        eg[5].shift(DOWN*0.75)
        eg[6].shift(DOWN*0.75)
        eg[7].shift(DOWN*0.75)
        eg[8].shift(DOWN*0.5)
        eg[9].shift(DOWN*0.5)
        eg[0].set_color(YELLOW)

        ea1 = MathTex("\\frac{7}{2}","\\frac{7}{4}","\\left(\\frac{7}{4}\\right)^2").scale(1.5).next_to(eg[3][3], DOWN, buff=1)
        
        te = MathTex(
            r"2x^2-7x+3 &=0\\",
            r"\frac{2}{2}x^2-\frac{7}{2} x+\frac{3}{2} &=\frac{0}{2}\\",
            r"x^2-\frac{7}{2} x+\frac{3}{2} &=0\\",
            r"x^2 -\frac{7}{2}x+\frac{3}{2}x +\left(\frac{7}{4}\right)^2 &=\left(\frac{7}{4}\right)^2\\",
            r"x^2 -\frac{7}{2}x +\left(\frac{7}{4}\right)^2 &=\frac{49}{16} -\frac{3}{2}\\",
            r"\left(x-\frac{7}{4}\right)^2 &=\frac{49-24}{16}\\",
            r"\left(x-\frac{7}{4}\right)^2 &=\frac{25}{16}\\",
            r"x-\frac{7}{4} &=\sqrt{\frac{25}{16}}\\",
            r"x-\frac{7}{4} &=\pm\frac{5}{4}\\",
            r"x &=\frac{7\pm 5}{4}",
            ).scale(1.5)
        te.shift(LEFT*0.75)
        for i in range(10):
            eg[i].set_x(te[i].get_x())
        ea1.set_color(BLUE).align_to(eg[3][3], RIGHT)
        tf.move_to(ea1).align_to(eg[4][:3])
        #Here we have the equation 2x squared minus 7x plus 3
        self.play(Write(eg[0]), run_time=2)
        self.wait()
        #divide the equation by 2
        self.play(
            AnimationGroup(*[TransformFromCopy(eg[0][i], eg[1][i]) for i in range(4)], lag_ratio=1)
            )
        self.play(eg[:2].animate.shift(UP*1.75))
        self.play(
            AnimationGroup(*[TransformMatchingShapes(eg[1][i], eg[2][i]) for i in range(4)], lag_ratio=1)
            )
        self.play(VGroup(eg[0],eg[2]).animate.shift(UP*1.75))
        #Now complete the square, to complete the square add the square of half the co-effiecient of x
        self.play(TransformFromCopy(eg[2][1][1:-1],ea1[0]))
        #Here in our case coefficient of x is 7 over 2, half the co-effiecient 
        #of x is 7 over 4 and its square is 7 over 4 whole square.
        self.play(TransformMatchingShapes(ea1[0],ea1[1]))
        self.play(TransformMatchingShapes(ea1[1],ea1[2]))
        self.wait()
        self.play(
            AnimationGroup(
                TransformFromCopy(eg[2][:3], eg[3][:3]),
                TransformFromCopy(eg[2][-1][0], eg[3][-1][0])
                )
            )
        #so adding 7 over 4 whole square on both the sides of equation. 
        self.play(AnimationGroup(
            TransformFromCopy(ea1[2], eg[3][3]),
            TransformFromCopy(ea1[2], eg[3][-1][1:]),
            ))
        #lets arrange them in a way so that we can simplify further.
        self.play(AnimationGroup(
            TransformMatchingShapes(eg[3][-1],eg[4][-2]),
            TransformMatchingShapes(eg[3][2], eg[4][-1]),
            TransformMatchingShapes(eg[3][3],eg[4][2]),
            TransformMatchingShapes(eg[3][:2], eg[4][:2]),
            lag_ratio=1
            ))
        self.wait()
        self.play(FadeOut(ea1[2]))
        self.play(VGroup(eg[0],eg[2],eg[4]).animate.shift(UP*2.15))
        self.wait()
        #Now this is of the form a minus b whole square, where a is x and b is 
        #7 over 4, which we can further rewrite as x minus 7 over 4 whole square is equal to 25 over 16
        self.play(Write(tf))
        self.play(
            eg[4][1].animate.align_to(eg[4][2], RIGHT),
            eg[4][2].animate.align_to(eg[4][1], LEFT)
            )
        self.play(AnimationGroup(*[
            AnimationGroup(Indicate(eg[4][i], color=BLUE), Indicate(tf[j+1], color=BLUE)) for i,j in zip([0,2,1],range(3))
            ], lag_ratio=1, rate_func=linear, run_time=3))
        self.play(AnimationGroup(
            Write(eg[5][0][0]),
            TransformFromCopy(VGroup(eg[4][0],eg[4][1][-1]), eg[5][0][1]),
            Write(eg[5][0][2]),
            TransformFromCopy(VGroup(eg[4][1][1:-1], eg[4][2][1:-2]), eg[5][0][3:-2]),
            Write(eg[5][0][-2:]),
            lag_ratio=0.8, rate_func=linear, run_time=4
            ))
        self.play(Indicate(eg[5][0], color=BLUE), Indicate(tf[0][:-1], color=BLUE))
        self.play(FadeIn(eg[5][1][0]))
        self.play(AnimationGroup(
            TransformFromCopy(VGroup(eg[4][-1][3], eg[4][-2][-2:]), eg[5][1][-2:]),
            Write(eg[5][1][-3]),
            TransformFromCopy(eg[4][-2][1:3], eg[5][1][1:3]),
            TransformFromCopy(eg[4][-1][0], eg[5][1][3]),
            TransformFromCopy(eg[4][-1][1], eg[5][1][4:6]),
            lag_ratio=1, run_time=4
            ))
        self.wait()
        self.play(AnimationGroup(
            ReplacementTransform(eg[5][1][1:-3], eg[6][1][1:-3]),
            TransformMatchingShapes(eg[5][1][-3:], eg[6][1][-3:]),
            lag_ratio=1, run_time=2
            ))
        self.play(FadeOut(tf))
        self.play(
            ReplacementTransform(eg[5][0],eg[6][0]),
            ReplacementTransform(eg[5][1][0],eg[6][1][0]),
            )
        #Now taking square roots on both the sides, well the square and its root 
        #gets cancelled here and square root of 25 over 16 is plus or minus 5 over 4
        self.play(AnimationGroup(
            TransformMatchingShapes(eg[6][1][-5:], eg[7][1][-5:]),
            ReplacementTransform(VGroup(eg[6][0][0], eg[6][0][-2:]), eg[7][1][1:3]),
            TransformMatchingShapes(VGroup(eg[6][0][1:-2], eg[6][1][0]), VGroup(eg[7][0], eg[7][1][0])),
            lag_ratio=1, run_time=3
            ))
        self.play(VGroup(eg[0],eg[2],eg[4],eg[7]).animate.shift(UP*2.5))
        self.remove(eg[8][1][1])
        self.play(AnimationGroup(
            TransformFromCopy(eg[7][0], eg[8][0]),
            TransformFromCopy(eg[7][1][0], eg[8][1][0]),
            TransformFromCopy(eg[7][1][2:6], eg[8][1][-3]),
            TransformFromCopy(eg[7][1][-3], eg[8][1][-2]),
            TransformFromCopy(VGroup(eg[7][1][2:4], eg[7][1][-2:]), eg[8][1][-1]),
            #Indicate(eg[8][1][1], color=WHITE),
            lag_ratio=1, run_time=5
            ))
        self.play(Indicate(eg[8][1][1], color=WHITE))
        #solving for x
        self.wait()
        self.play(AnimationGroup(
            AnimationGroup(
                TransformMatchingShapes(VGroup(eg[8][0][-2:], eg[8][1][-1]), eg[9][1][-2:]),
                TransformMatchingShapes(eg[8][1][1:4], eg[9][1][-4:-1]),
                TransformMatchingShapes(eg[8][1][0], eg[9][1][0]),
                TransformMatchingShapes(eg[8][0][2], eg[9][1][1]),
                FadeOut(eg[8][0][1], shift=RIGHT),
                lag_ratio=0
                ),
            TransformMatchingShapes(eg[8][0][0], eg[9][0]),
            lag_ratio=1, run_time=5
            ))
        #In case 7 over 4 plus 5 over 4 the value of x is 3
        #In case 7 over 4 minus 5 over 4 the value of x is 1 over 2
        self.play(Indicate(eg[9][1][2], color=RED), run_time=2)
        self.play(TransformFromCopy(eg[9], dg[0][0]))
        self.play(TransformMatchingShapes(eg[9],dg[0][2]))
        self.wait()
        self.play(
            TransformMatchingShapes(dg[0][0], dg[1][0]),
            TransformMatchingShapes(dg[0][2], dg[1][2]),
            )
        self.wait()
        self.play(
            TransformMatchingShapes(dg[1][0], dg[2][0]),
            TransformMatchingShapes(dg[1][2], dg[2][2]),
            )
        self.play(
            Indicate(dg[2][0], color=RED),
            Indicate(dg[2][2], color=RED),
            )
        self.wait()
        self.play(VGroup(eg[0],eg[2],eg[4],eg[7], dg[2]).animate(run_time=3, rate_func=linear).scale(0.65).to_edge(UP))
        self.wait(4)
