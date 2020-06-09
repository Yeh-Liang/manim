from scipy.constants import zero_Celsius

from manim import *


class Heat(Scene):
    def construct(self):
        Tmax = zero_Celsius+150
        Tmin = zero_Celsius+20
        R = 8.314
        kappa = 5/3
        V1= 1
        V2= 2

        p1 = R*Tmax/V1
        p2 = p1*V1/V2

        V3 = (Tmax/Tmin * V2**(kappa-1))**(1/(kappa-1))
        p3 = p2* V2**kappa / V3**kappa

        V4 = (Tmax/Tmin * V1**(kappa-1))**(1/(kappa-1))
        p4 = p3*V3/V4


        def make_box():
            p1 = [0,1,0]
            p2 = [0,0,0]
            p3= [0.75,0,0]
            p4 = [0.75,1,0]
            l1 = Line(p1,p2).set_color(BLACK)
            l2 = Line(p2,p3).set_color(BLACK)
            l3 = Line(p3,p4).set_color(BLACK)
            obj = VGroup(l1,l2,l3)
            return obj
        def make_box_high():
            p1 = [0,4,0]
            p2 = [0,0,0]
            p3= [0.75,0,0]
            p4 = [0.75,4,0]
            l1 = Line(p1,p2).set_color(BLACK)
            l2 = Line(p2,p3).set_color(BLACK)
            l3 = Line(p3,p4).set_color(BLACK)
            obj = VGroup(l1,l2,l3)
            return obj
        DISTANCELEFTRIGHT= 0.8
        cold = make_box().shift(DOWN+DISTANCELEFTRIGHT*LEFT)
        cold.add_background_rectangle(color=BLUE)
        cold.text = TexMobject(r" \text{T}_{\text{min}}").scale(0.6).set_color(BLACK)
        cold.text.move_to(cold.get_center())
        hot = make_box().shift(DOWN+DISTANCELEFTRIGHT*RIGHT)
        hot.text = TexMobject(r" \text{T}_{\text{max}}").scale(0.6).set_color(BLACK)
        hot.text.move_to(hot.get_center())

        hot.add_background_rectangle(color= RED)
        obj = make_box_high()
        baths= VGroup(obj,cold, hot, cold.text, hot.text).to_edge(UR).shift(2*DOWN+LEFT*DISTANCELEFTRIGHT)
        self.add(baths)
        baths_hotcold = VGroup(cold, hot, cold.text, hot.text)
        #self.play(baths_hotcold.shift, LEFT*DISTANCELEFTRIGHT)
        #self.add(baths_hotcold.copy().shift(RIGHT*DISTANCELEFTRIGHT*2))
        #self.wait()
        path_weight = Path().home()/"Documents/manim_resources/weight.svg"
        weight_light = SVGMobject(str(path_weight)).set_stroke(width=0).scale(0.4)
        weight_light.set_color(interpolate_color(GREY,WHITE,0.2))
        weight_light.scale(0.829)
        weight_heavy = SVGMobject(str(path_weight)).set_stroke(width=0).scale(0.4)
        weight_heavy.set_color(interpolate_color(GREY,BLACK,0.2))

        weight_light.set_z_index(2)
        weight_heavy.set_z_index(2)
        stamp_thickness  = 0.1
        def make_stemp():
            stemp  = Rectangle()
            p1 = [0,stamp_thickness,0]
            p2 = [0,0,0]
            p3= [0.75,0,0]
            p4 = [0.75,stamp_thickness,0]
            lines = []
            lines.append(Line(p2,p3).set_color(BLACK))
            lines.append(Line(p4,p1).set_color(BLACK))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.1*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.2*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.3*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.4*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.5*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.6*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.7*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.8*0.75))
            lines.append(Line(p1,p2).set_color(BLACK).shift(RIGHT*0.9*0.75))
            obj = VGroup(*lines)
            return obj
        stemp= make_stemp()
        stemp.set_x(obj.get_center()[0])
        center= obj.get_center()
        dot_1 = Dot(center).shift(DOWN*0.2).set_color(BLUE_A)
        dot_2 = Dot(point=[center[0],((V2-V1) /(V3-V1)) *2+dot_1.get_y() ,0])
        dot_3 = Dot(point=[center[0],((V3-V1) /(V3-V1)) *2+dot_1.get_y() ,0])
        dot_4 = Dot(point=[center[0],((V4-V1) /(V3-V1)) *2+dot_1.get_y() ,0])


        line_1 = Line(dot_1.copy().shift(RIGHT*(0.75/2-0.01)).get_center(), dot_1.copy().shift(RIGHT*(0.75/2+0.01)).get_center()).set_color(GREEN).set_opacity(1).set_z_index(1)
        line_2 = Line(dot_2.copy().shift(RIGHT*(0.75/2-0.01)).get_center(), dot_2.copy().shift(RIGHT*(0.75/2+0.01)).get_center()).set_color(GREEN).set_opacity(1).set_z_index(1)
        line_3 = Line(dot_3.copy().shift(RIGHT*(0.75/2-0.01)).get_center(), dot_3.copy().shift(RIGHT*(0.75/2+0.01)).get_center()).set_color(GREEN).set_opacity(1).set_z_index(1)
        line_4 = Line(dot_4.copy().shift(RIGHT*(0.75/2-0.01)).get_center(), dot_4.copy().shift(RIGHT*(0.75/2+0.01)).get_center()).set_color(GREEN).set_opacity(1).set_z_index(1)
        self.add(line_1,line_2,line_3,line_4)
        line_1b = Line(dot_1.copy().shift(LEFT*(0.75/2-0.01)).get_center(), dot_1.copy().shift(LEFT*(0.75/2+0.01)).get_center()).set_color(GREEN).set_opacity(1).set_z_index(1)
        line_2b = Line(dot_2.copy().shift(LEFT*(0.75/2-0.01)).get_center(), dot_2.copy().shift(LEFT*(0.75/2+0.01)).get_center()).set_color(GREEN).set_opacity(1).set_z_index(1)
        line_3b = Line(dot_3.copy().shift(LEFT*(0.75/2-0.01)).get_center(), dot_3.copy().shift(LEFT*(0.75/2+0.01)).get_center()).set_color(GREEN).set_opacity(1).set_z_index(1)
        line_4b = Line(dot_4.copy().shift(LEFT*(0.75/2-0.01)).get_center(), dot_4.copy().shift(LEFT*(0.75/2+0.01)).get_center()).set_color(GREEN).set_opacity(1).set_z_index(1)
        self.add(line_1b,line_2b,line_3b,line_4b)


        plat1A = Dot(dot_1.get_center()+UP*stamp_thickness+LEFT).set_color(LIGHT_BROWN).set_opacity(0.4)
        lin_plat1A  = Line(plat1A.copy().shift(LEFT*0.4),plat1A.copy().shift(RIGHT*0.4)).set_color(LIGHT_BROWN).set_opacity(0.4)
        plat1B = Dot(dot_1.get_center()+UP*stamp_thickness+RIGHT).set_color(LIGHT_BROWN).set_opacity(0.4)
        lin_plat1B  = Line(plat1B.copy().shift(LEFT*0.4),plat1B.copy().shift(RIGHT*0.4)).set_color(LIGHT_BROWN).set_opacity(0.4)

        plat2A = Dot(dot_3.get_center()+UP*stamp_thickness+LEFT).set_color(LIGHT_BROWN).set_opacity(0.4)
        lin_plat2A  = Line(plat2A.copy().shift(LEFT*0.4),plat2A.copy().shift(RIGHT*0.4)).set_color(LIGHT_BROWN).set_opacity(0.4)
        plat2B = Dot(dot_3.get_center()+UP*stamp_thickness+RIGHT).set_color(LIGHT_BROWN).set_opacity(0.4)
        lin_plat2B  = Line(plat2B.copy().shift(LEFT*0.4),plat2B.copy().shift(RIGHT*0.4)).set_color(LIGHT_BROWN).set_opacity(0.4)


        self.add(plat1A,lin_plat1A,lin_plat1B,lin_plat2A,lin_plat2B)
        self.add(weight_heavy,weight_light)

        weight_heavy.move_to(plat1A.get_center(),aligned_edge=DOWN)
        height_of_weight_heavy =  weight_heavy.get_center()[1]-plat1A.get_center()[1]
        weight_light.move_to(plat2A.get_center(),aligned_edge=DOWN)
        height_of_weight_light = weight_light.get_center()[1]-plat2A.get_center()[1]
        val_tracker= ValueTracker(V1)
        def update_y_coordinate_of_stemp(mob):
            mob.set_y((val_tracker.get_value()-V1) /(V3-V1) *2 +dot_1.get_y()+stamp_thickness/2)
            return mob
        def update_y_coordinate_of_weight_heavy(mob):
            mob.set_y((val_tracker.get_value()-V1) /(V3-V1) *2 +dot_1.get_y()+stamp_thickness+height_of_weight_heavy)
            return mob
        def update_y_coordinate_of_weight_light(mob):
            mob.set_y((val_tracker.get_value()-V1) /(V3-V1) *2 +dot_1.get_y()+stamp_thickness+height_of_weight_light)

        stemp.add_updater(update_y_coordinate_of_stemp)
        self.add(stemp)

        baths_hotcold.shift(LEFT*DISTANCELEFTRIGHT)

        square= Rectangle(fill_opacity=1).set_stroke(width=0).set_color(RED)
        square.set_width(0.75)
        square.set_z_index(-1)
        square.set_x(center[0])
        square.set_height((stemp.get_center()-obj.get_bottom())[1]-stamp_thickness/2,stretch=True)
        square.align_to(obj,DOWN)

        def update_gas_square(square):
            square.set_height((stemp.get_center()-obj.get_bottom())[1]-stamp_thickness/2,stretch=True)
            square.align_to(obj,DOWN)
            return square
        num_colors= 1000
        cols =  color_gradient([RED,WHITE,BLUE], num_colors)
        def update_gas_square_turn_blue(square):
            square.set_height((stemp.get_center()-obj.get_bottom())[1]-stamp_thickness/2,stretch=True)
            square.align_to(obj,DOWN)
            integ = int((val_tracker.get_value()-V2)/(V3-V2)*(num_colors-1))
            square.set_color(cols[integ])
            return square
        def update_gas_square_turn_red(square):
            square.set_height((stemp.get_center()-obj.get_bottom())[1]-stamp_thickness/2,stretch=True)
            square.align_to(obj,DOWN)
            integ = int((val_tracker.get_value()-V1)/(V4-V1)*(num_colors-1))
            print(integ)
            square.set_color(cols[integ])
            return square

        self.add(square)

        #### START
        square.add_updater(update_gas_square)
        self.play(weight_heavy.shift, RIGHT)
        self.wait()
        weight_heavy.add_updater(update_y_coordinate_of_weight_heavy)

        #1-2
        self.play(val_tracker.set_value, V2, rate_func= linear)
        self.play(baths_hotcold.shift, RIGHT*DISTANCELEFTRIGHT)
        #2-3
        square.add_updater(update_gas_square_turn_blue)
        self.play(val_tracker.set_value, V3, rate_func= linear)
        weight_heavy.remove_updater(update_y_coordinate_of_weight_heavy)
        self.play(weight_heavy.shift, RIGHT)
        self.play(baths_hotcold.shift, RIGHT*DISTANCELEFTRIGHT)
        self.play(weight_light.shift, RIGHT)
        weight_light.add_updater(update_y_coordinate_of_weight_light)
        square.remove_updater(update_gas_square_turn_blue)

        #3-4
        self.play(val_tracker.set_value, V4, rate_func= linear)
        self.play(baths_hotcold.shift, LEFT*DISTANCELEFTRIGHT)

        #4-1
        square.add_updater(update_gas_square_turn_red)
        self.play(val_tracker.set_value, V1, rate_func= linear)
        self.play(weight_light.shift, RIGHT)
        self.wait()

from pathlib import Path

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim   -m  -p -c 'WHITE' --video_dir ~/Downloads/ " + script)
