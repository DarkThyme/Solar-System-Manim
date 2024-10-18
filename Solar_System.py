from manim import *

class SolarSystem(ThreeDScene):
    def construct(self):
        #Set up 3D camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        #Create 3D axes
        axes = ThreeDAxes()
        self.add(axes)

        #Create the sun
        sun = Sphere(radius=0.5).move_to(ORIGIN)
        sun.set_color(YELLOW)

        #Create planets with different sizes and colors
        mercury = Sphere(radius=0.1).move_to(RIGHT * 1.5)
        mercury.set_color(LIGHT_GRAY)

        venus = Sphere(radius=0.15).move_to(RIGHT * 2)
        venus.set_color(GOLD)

        earth = Sphere(radius=0.2).move_to(RIGHT * 2.5)
        earth.set_color(BLUE)

        mars = Sphere(radius=0.15).move_to(RIGHT * 3)
        mars.set_color(RED)

        jupiter = Sphere(radius=0.3).move_to(RIGHT * 3.5)
        jupiter.set_color(ORANGE)

        saturn = Sphere(radius=0.25).move_to(RIGHT * 4)
        saturn.set_color(YELLOW_E)

        uranus = Sphere(radius=0.2).move_to(RIGHT * 4.5)
        uranus.set_color(GREEN)

        neptune = Sphere(radius=0.2).move_to(RIGHT * 5)
        neptune.set_color(BLUE_E)

        #Add sun and planets to the scene
        self.add(sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune)

        #Create orbit paths
        def create_orbit(radius):
            return Circle(radius=radius).rotate(PI/2, RIGHT).move_to(ORIGIN)

        orbits = VGroup(*[create_orbit(p.get_center()[0]) for p in [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]])
        orbits.set_color(GRAY).set_opacity(0.5)
        self.add(orbits)

        #Create asteroid belt
        asteroid_belt = VGroup()
        for _ in range(200):
            radius = np.random.uniform(2.75, 3.25)
            angle = np.random.uniform(0, TAU)
            asteroid = Dot3D(point=np.array([
                radius * np.cos(angle),
                radius * np.sin(angle),
                np.random.uniform(-0.1, 0.1)
            ]), radius=0.01)
            asteroid.set_color(GRAY)
            asteroid_belt.add(asteroid)
        self.add(asteroid_belt)

        #Animate the rotation of the planets and asteroid belt around the sun
        self.begin_ambient_camera_rotation(rate=0.2)
        self.play(
            *[Rotate(planet, angle=TAU, about_point=ORIGIN, rate_func=linear) 
              for planet in [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]],
            Rotate(asteroid_belt, angle=TAU, about_point=ORIGIN, rate_func=linear),
            run_time=10
        )
        self.wait(2)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera.frame_width = 12  #Adjust this value to zoom out and show more of the scene