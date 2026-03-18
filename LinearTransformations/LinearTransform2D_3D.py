from manim import *
import numpy as np
import sympy as sp
from fractions import Fraction


def load_matrix_symbolic(file_path="input.txt"):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    # Create a SymPy Matrix using Rational objects for exactness
    data = [[sp.Rational(x) for x in line.split()] for line in lines]
    return sp.Matrix(data)


class LinearTransformation(ThreeDScene):
    def construct(self):
        # 1. Symbolic Analysis
        M_sym = load_matrix_symbolic()
        dim = M_sym.shape[0]

        # Calculate Eigen-info analytically
        # eigenvects() returns list of (eigenvalue, multiplicity, [eigenvectors])
        eigen_info = M_sym.eigenvects()

        print(f"\n--- Analytical Matrix Analysis ({dim}x{dim}) ---")
        print("Matrix (Exact):")
        sp.pprint(M_sym)

        # Prepare lists for animation
        evals_float = []
        evecs_float = []

        print("\nEigen-structure:")
        for val, mult, vecs in eigen_info:
            evals_float.append(float(val.evalf()))
            for v in vecs:
                # Store numeric version for Manim
                evecs_float.append(np.array(v.tolist(), dtype=float).flatten())
                # Print exact version to console
                print(f"λ = {val}:")
                sp.pprint(v)

        # Convert matrix to numpy for Manim's apply_matrix
        matrix_np = np.array(M_sym.tolist(), dtype=float)

        if dim == 2:
            self.animate_2d(matrix_np, evals_float, evecs_float)
        elif dim == 3:
            self.animate_3d(matrix_np, evals_float, evecs_float)

    def animate_2d(self, matrix, evals, evecs):
        bg_plane = NumberPlane(x_range=[-20, 20], y_range=[-20, 20],
                               background_line_style={"stroke_color": YELLOW, "stroke_opacity": 0.2})
        moving_plane = NumberPlane(x_range=[-20, 20], y_range=[-20, 20],
                                   background_line_style={"stroke_color": BLUE, "stroke_opacity": 0.6})
        bg_plane.add_coordinates()

        unit_square = Square(side_length=1, fill_color=YELLOW, fill_opacity=0.3).move_to([0.5, 0.5, 0])
        i_hat = Vector([1, 0], color=YELLOW)
        j_hat = Vector([0, 1], color=PINK)

        eigenvectors_vg = VGroup()
        for vec in evecs:
            # Manim 2D vectors need 3 components [x, y, 0]
            v_obj = Vector([vec[0], vec[1], 0], color=PURPLE).set_stroke(width=10)
            eigenvectors_vg.add(v_obj)

        self.add(bg_plane, moving_plane, unit_square, i_hat, j_hat, eigenvectors_vg)
        self.play(
            *[m.animate.apply_matrix(matrix) for m in [moving_plane, unit_square, i_hat, j_hat, eigenvectors_vg]],
            run_time=4
        )
        self.wait(2)

    def animate_3d(self, matrix, evals, evecs):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        axes = ThreeDAxes()

        # Create a visual 3D grid
        grid = VGroup()
        for i in range(-5, 6):
            grid.add(Line3D(start=[-5, i, 0], end=[5, i, 0], color=BLUE ))
            grid.add(Line3D(start=[i, -5, 0], end=[i, 5, 0], color=BLUE))

        basis = VGroup(
            Vector([1, 0, 0], color=YELLOW),
            Vector([0, 1, 0], color=PINK),
            Vector([0, 0, 1], color=GREEN)
        )

        eigenvectors_vg = VGroup()
        for vec in evecs:
            v_obj = Vector(vec, color=GOLD).set_stroke(width=10)
            eigenvectors_vg.add(v_obj)

        self.add(axes, grid, basis, eigenvectors_vg)
        self.begin_ambient_camera_rotation(rate=0.1)

        self.play(
            grid.animate.apply_matrix(matrix),
            basis.animate.apply_matrix(matrix),
            eigenvectors_vg.animate.apply_matrix(matrix),
            axes.animate.apply_matrix(matrix),
            run_time=4
        )
        self.wait(2)