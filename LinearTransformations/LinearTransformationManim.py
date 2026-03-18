from manim import *
import numpy as np
import random

class LinearTransformation(Scene):
    def construct(self):
        # 1. Load Matrix
        try:
            matrix = np.loadtxt("input.txt")
        except:
            # A shear + scale that would usually show edges
            matrix = [[2, 1], [0.5, 1]]

        # 2. Create an Oversized Background Grid (Static)
        background_plane = NumberPlane(
            x_range=[-20, 20, 1],  # Much wider than the screen
            y_range=[-20, 20, 1],  # Much taller than the screen
            background_line_style={
                "stroke_color": YELLOW,
                "stroke_width": 6,
                "stroke_opacity": 0.2
            }
        )

        # 3. Create an Oversized Moving Grid (High Visibility)
        moving_plane = NumberPlane(
            x_range=[-20, 20, 1],
            y_range=[-20, 20, 1],
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 6,
                "stroke_opacity": 0.6
            }
        )

        # Add coordinates only to the center area so they don't clutter
        background_plane.add_coordinates(range(-10, 11),range(-10, 11))

        # 4. The "Unit Square" (To show Area Change)
        # This square will transform along with the grid
        unit_square = Square(side_length=1, fill_color=YELLOW, fill_opacity=0.3, stroke_width=2)
        unit_square.move_to(moving_plane.coords_to_point(0.5, 0.5))

        # 4. Basis Vectors
        i_hat = Vector([1, 0], color=YELLOW).set_stroke(width=8)
        j_hat = Vector([0, 1], color=PINK).set_stroke(width=8)
        vector1 = Vector([0,0], color=RED).set_stroke(width=8)
        vector2 = Vector([1,-3], color=GREEN).set_stroke(width=8)

        # 3. Generate Random Vectors
        num_random_vectors = 0
        vectors = VGroup()
        N = 3
        for _ in range(num_random_vectors):
            # Generate random x, y between -4 and 4
            x, y = random.uniform(-N,N), random.uniform(-N,N)
            # Create a vector with a random bright color
            v = Vector([x, y], color=random_bright_color())
            vectors.add(v)
        # 5. Animation
        # 6. Animation Logic
        self.add(background_plane, moving_plane, unit_square, i_hat, j_hat,vector1,vector2)

        # We use a slightly zoomed out camera or just keep the default
        # The 'fading' edges effect can be ignored because the grid is so large
        self.play(
            moving_plane.animate.apply_matrix(matrix),
            i_hat.animate.apply_matrix(matrix),
            j_hat.animate.apply_matrix(matrix),
            vector1.animate.apply_matrix(matrix),
            vector2.animate.apply_matrix(matrix),
            unit_square.animate.apply_matrix(matrix),
            vectors.animate.apply_matrix(matrix),
            run_time=4,
            rate_func=smooth
        )
        self.wait(2)