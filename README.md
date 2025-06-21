# 🧊 Rubik’s Cube Solver – Python + OpenCV

A computer vision–based Rubik’s Cube solver built using Python, OpenCV, and the Kociemba algorithm. This project captures the cube faces via webcam, detects colors using HSV thresholding, and computes the optimal solution using the `kociemba` library.

---

## 📌 Features

- Uses OpenCV to capture cube face colors via webcam.
- Detects sticker colors using HSV values and maps them to standard cube notations.
- Computes an optimal solving sequence using the Kociemba 2-phase algorithm.
- Includes visual reference for cube notations (`cube notations.jpg`).

---

## 🔧 Technologies Used

- **Python 3.x**
- **OpenCV (`cv2`)** – for camera feed and color detection
- **kociemba** – for solving the cube algorithmically

---

## 🚀 How It Works

1. **Capture**:
   - The script uses your webcam to scan each face of the cube.
   - Captures are processed to read the center pixel of each sticker area.

2. **Detect Colors**:
   - Colors are detected using HSV thresholding.
   - Each color is mapped to a cube face letter (e.g., R, G, B, W, O, Y).

3. **Solve**:
   - Once all 6 faces are scanned, the sticker string is passed to the `kociemba.solve()` function.
   - It returns an optimal solution in standard Rubik's notation.

---

## 📷 Webcam Setup

Make sure your webcam is working. If you have multiple webcams, you can modify the index here:

```python
cap = cv2.VideoCapture(0)  # Change 0 to 1 or 2 if needed
