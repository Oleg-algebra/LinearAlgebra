import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter, FFMpegWriter
import os


def generate_transformation_gif(file_path='input.txt', grid_range=5):
    # Load Matrix
    try:
        A = np.loadtxt(file_path)
    except:
        A = np.array([[2, 1], [0.5, 1]])  # Fallback

    # --- 1. Timing Logic ---
    moving_frames = 40  # Frames for the actual transformation
    padding_frames = 20  # Frames to "freeze" at the end result

    # Create the timeline: 0 -> 1, then a bunch of 1s
    t_move = np.linspace(0, 1, moving_frames)
    t_pause_end = np.ones(padding_frames)
    t_pause_start = np.zeros(padding_frames)
    all_t = np.concatenate([t_pause_start,t_move, t_pause_end])

    fig, ax = plt.subplots(figsize=(6, 6))

    def update(t):
        ax.clear()
        M = (1 - t) * np.eye(2) + t * A

        # Grid boundaries
        limit = grid_range * 1.5
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_aspect('equal')
        ax.grid(True, linestyle=':', alpha=0.4)

        # Drawing Logic
        ticks = np.linspace(-grid_range, grid_range, 11)
        for val in ticks:
            # Vertical lines
            v = M @ np.array([[val, val], [-grid_range, grid_range]])
            ax.plot(v[0], v[1], color='blue', lw=0.8, alpha=0.5)
            # Horizontal lines
            h = M @ np.array([[-grid_range, grid_range], [val, val]])
            ax.plot(h[0], h[1], color='red', lw=0.8, alpha=0.5)

        # Basis Vectors
        i_hat = M @ np.array([1, 0])
        j_hat = M @ np.array([0, 1])
        ax.quiver(0, 0, i_hat[0], i_hat[1], color='blue', angles='xy', scale_units='xy', scale=1)
        ax.quiver(0, 0, j_hat[0], j_hat[1], color='red', angles='xy', scale_units='xy', scale=1)
        ax.set_title(f"t = {t:.2f}")

    # --- 2. Save as GIF ---
    ani = FuncAnimation(fig, update, frames=all_t, interval=50)

    # Using PillowWriter for GIF export
    writer = PillowWriter(fps=20)
    print("Saving to transformation.gif...")
    ani.save("transformation.gif", writer=writer)
    print("Done!")

    # 3. Create and Save Animation
    ani = FuncAnimation(fig, update, frames=all_t, interval=50)

    # Define the writer (codec, bitrate, and fps)
    writer = FFMpegWriter(fps=30, metadata=dict(artist='Me'), bitrate=1800)

    # Save the file
    print("Saving animation to transformation.mp4...")
    ani.save("transformation.mp4", writer=writer)
    print("Done!")

    # Optional: Still show it if you want
    # plt.show()


if __name__ == "__main__":
    generate_transformation_gif()