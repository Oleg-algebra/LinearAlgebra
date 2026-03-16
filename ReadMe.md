

# Linear Algebra Visualizer: 2D Transformations

This repository is an **educational toolkit** designed to visualize the geometric meaning of linear transformations. By animating the transition from an identity grid to a transformed state, this project helps users develop an intuitive grasp of how matrices manipulate space.

## 🎯 Project Purpose

In textbooks, linear transformations are often shown as static "before and after" snapshots. This project fills the gap by animating the **interpolation** between those states. It is designed to demonstrate:

* **Basis Vector Mapping:** Watch $\hat{i}$ and $\hat{j}$ move to their new coordinates (the columns of the matrix).
* **Area Scaling:** Visualize the **Determinant** through the stretching or squishing of the unit square.
* **Orientation:** See how negative determinants "flip" the coordinate system.
* **Grid Preservation:** Observe how parallel lines remain parallel after a linear transformation.

---

## 💻 How to Run the Code

### 1. Prerequisites

Ensure you have Python installed. You will also need **FFmpeg** installed on your system if you intend to save animations as MP4 files.

### 2. Installation

Clone the repository and install the necessary dependencies using the provided `requirements.txt`:

```bash
git clone https://github.com/Oleg-algebra/LinearAlgebra.git
cd LinearAlgebra
pip install -r requirements.txt

```

### 3. Configuration

Both visualizers read the transformation matrix from a file named `input.txt`. Edit this file to define your $2 \times 2$ matrix row-by-row.

**Example (for a 45° rotation):**

```text
0.707 -0.707
0.707  0.707

```

### 4. Rendering the Animation

#### **Option A: Manim (Cinematic Quality)**

Best for creating polished educational videos with high-quality rendering and LaTeX labels.

```bash
manim -pql LinearTransformationManim.py LinearTransformation

```

**Flag Guide:**

* `-p`: **Preview** the video automatically once rendering is finished.
* `-ql`: **Quality Low** (480p) – Fast rendering for testing.
* `-qh`: **Quality High** (1080p) – Best for final exports.
* `--format=gif`: Add this flag if you want a **GIF** instead of an MP4.

#### **Option B: Matplotlib (Quick & Lightweight)**

Best for a fast interactive preview or generating a quick GIF without the overhead of a full animation engine.

```bash
python LinearTransformMatplotlib.py

```

---

## 🛠 Tech Stack

* **[Manim](https://www.manim.community/):** The mathematical animation engine.
* **NumPy:** Used for matrix operations and file parsing.
* **Matplotlib:** Used for lightweight, frame-by-frame plotting.

## 📜 License

This project is open-source and available under the MIT License. Feel free to use it for teaching or self-study!

