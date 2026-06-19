<div align="center">

<img src="toolkit_hero.svg" alt="Image Processing Toolkit Banner" width="600"/>

# 🖼️ Image Processing Toolkit

**A modern desktop app to Edit, Transform and Enhance images — built with Python & Tkinter**

![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-6366f1?style=for-the-badge)
![Pillow](https://img.shields.io/badge/Pillow-PIL-ff6b6b?style=for-the-badge)
![NumPy](https://img.shields.io/badge/NumPy-Matrix-013243?style=for-the-badge&logo=numpy&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22d3ee?style=for-the-badge)

[Features](#-features) · [Screenshots](#-screenshots) · [Demo](#-demo-video) · [Installation](#-installation) · [Usage](#-how-to-use) · [Tech Stack](#-tech-stack)

</div>

---

## 📌 About The Project

Image Processing Toolkit is a fully functional desktop application built from scratch using **Python**, **Tkinter**, **Pillow (PIL)**, and **NumPy**. It gives you a clean, modern dark-themed GUI to open any image and apply filters, effects, and transformations — all with **live preview** so you see changes instantly without opening a new window every time.

This project was built as a hands-on Python learning project by **Daksh Sharma** (Eagle Head) to understand image manipulation at the pixel/matrix level using NumPy arrays instead of just relying on library functions.

---

## ✨ Features

### 🎨 Filter & Effects
| Feature | Description |
|---|---|
| **Brightness** | Slide to increase or decrease brightness (-100 to +100) |
| **Contrast** | Adjust contrast factor from 0.1x to 4.0x |
| **Grayscale** | Convert image to grayscale using weighted RGB formula |
| **Invert** | Invert all pixel values (255 - pixel) |
| **Blur** | Apply box blur with radius 3 |
| **Sharpen** | Enhance sharpness using PIL ImageEnhance |

### 🔄 Transformations
| Feature | Description |
|---|---|
| **Resize** | Enter custom Width & Height and apply |
| **Crop** | Crop using x1, y1, x2, y2 coordinates |
| **Rotate** | Rotate image by 90°, 180°, or 270° |
| **Flip Horizontal** | Mirror image left to right |
| **Flip Vertical** | Flip image upside down |

### 💡 Extra
- **Live Preview** — every change shows instantly on screen
- **Save Image** — export as PNG or JPEG
- **Dark Modern UI** — indigo/navy theme, same across all windows
- **Two-window Flow** — Home screen → Editor window (home hides, not closes)
- **Status Bar** — always tells you what was last applied

---

## 📸 Screenshots

> **Home Screen**

![Home Screen](screenshots/home.png)

> **Editor Window — Filter & Effects**

![Editor Filters](screenshots/editor_filters.png)

> **Editor Window — Transformations**

![Editor Transforms](screenshots/editor_transform.png)

> **Before / After Preview**

![Before After](screenshots/before_after.png)

---

## 🎬 Demo Video

> Click the thumbnail below to watch the full demo on YouTube

[![Watch Demo](https://img.shields.io/badge/▶_Watch_Demo-YouTube-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/your-video-link)

<!-- Replace the link above with your actual YouTube video URL -->
<!-- To embed a video thumbnail directly:
[![Demo Video](https://img.youtube.com/vi/YOUR_VIDEO_ID/maxresdefault.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)
-->

---

## 🛠️ Tech Stack

| Technology | Role |
|---|---|
| **Python 3.7+** | Core language |
| **Tkinter** | GUI framework (built into Python) |
| **Pillow (PIL)** | Image open, save, filters, resize, crop |
| **NumPy** | Pixel-level matrix operations for brightness, contrast, grayscale, invert, flip, rotate |

### Why NumPy for image processing?
Most of the effects (Brightness, Contrast, Grayscale, Invert, Flip, Rotate) are done using **raw NumPy matrix operations** — not just calling a PIL function. This means the code is doing the actual math on pixel arrays, which is how real image processing works under the hood.

For example, grayscale uses the **luminosity formula**:
```
Gray = 0.299×R + 0.587×G + 0.114×B
```

---

## 📁 Project Structure

```
image-processing-toolkit/
│
├── image_toolkit.py       # Main file — home screen + editor GUI + all functions
├── toolkit_hero.svg       # Banner image for README
├── screenshots/           # App screenshots (add your own)
│   ├── home.png
│   ├── editor_filters.png
│   └── editor_transform.png
└── README.md              # This file
```

---

## ⚙️ Installation

### Prerequisites
Make sure you have **Python 3.7 or above** installed.

### Step 1 — Clone the repository
```bash
git clone https://github.com/your-username/image-processing-toolkit.git
cd image-processing-toolkit
```

### Step 2 — Install dependencies
```bash
pip install pillow numpy
```

> Tkinter comes pre-installed with Python on Windows. If you're on Linux:
> ```bash
> sudo apt-get install python3-tk
> ```

### Step 3 — Run the app
```bash
python image_toolkit.py
```

---

## 🚀 How To Use

1. **Launch** the app — the home screen appears
2. Click **Open Image** to load a PNG, JPG, JPEG, BMP, or WEBP file
3. The image thumbnail appears in the preview box
4. Click **Start Editing** — the editor window opens
5. Use the **sliders** for live brightness/contrast preview
6. Click any **effect button** (Grayscale, Invert, Blur, Sharpen) to apply instantly
7. Use **Resize / Crop / Rotate / Flip** in the Transformations section
8. Click **Save Image** to export your edited image
9. Click **Exit** to close the editor

---

## 🧠 How The Image Functions Work

```python
# Grayscale — weighted average of RGB channels
gray = np.dot(image_matrix[..., :3], [0.299, 0.587, 0.114])

# Brightness — add/subtract value to every pixel
result = np.clip(image_matrix + value, 0, 255)

# Contrast — stretch pixel values away from midpoint (128)
result = np.clip((image_matrix - 128) * factor + 128, 0, 255)

# Invert — flip every pixel value
result = 255 - image_matrix

# Flip Horizontal — mirror array left to right
result = np.fliplr(image_matrix)
```

These run directly on NumPy arrays, which makes them fast and easy to understand.

---

## 🔮 Future Plans

- [ ] Add **Undo / Redo** (history stack)
- [ ] **Batch processing** — apply effect to multiple images at once
- [ ] Add **color filters** (sepia, cool, warm tones)
- [ ] **Drag and drop** image loading
- [ ] Export with **custom quality** settings for JPEG
- [ ] Add **histogram view** showing RGB distribution

---

## 🤝 Contributing

Contributions are welcome! If you find a bug or want to add a feature:

1. Fork the repository
2. Create your branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — you are free to use, modify, and distribute it.

---

## 👨‍💻 Author

<div align="center">

**Daksh Sharma**

[![GitHub](https://img.shields.io/badge/GitHub-Eagle_Head-181717?style=for-the-badge&logo=github)](https://github.com/your-username)
[![YouTube](https://img.shields.io/badge/YouTube-Eagle_Head_YT-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/your-channel)

*Built with 💜 using Python*

© 2025 Eagle Head | Daksh Sharma

</div>
