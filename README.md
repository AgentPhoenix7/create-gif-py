<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=32&duration=3000&pause=1000&color=FF6B6B&center=true&vCenter=true&width=600&lines=create-gif-py;Turn+Images+into+Animated+GIFs;Simple+%E2%80%A2+Lightweight+%E2%80%A2+Pythonic" alt="Animated header" />

<br/>

<img src="nyan-cat.gif" alt="Demo — nyan cat animated GIF created with this project" width="420" />

<br/><br/>

[![Python](https://img.shields.io/badge/Python-3.13%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![imageio](https://img.shields.io/badge/imageio-%3E%3D2.37.3-FF6B6B?style=for-the-badge)](https://imageio.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![uv](https://img.shields.io/badge/managed%20with-uv-7C3AED?style=for-the-badge)](https://github.com/astral-sh/uv)

**Convert a sequence of images into a smooth, looping animated GIF — in a single Python file.**

</div>

---

## What It Does

`create-gif-py` reads a list of image frames (PNG, JPEG, or any format supported by Pillow) and stitches them into a single animated GIF with configurable frame timing and loop behavior. The entire implementation fits in one file with no boilerplate.

---

## Demo

The GIF at the top of this page was produced by running the script against three PNG frames:

```
nyan-cat1.png  →
nyan-cat2.png  →  nyan-cat.gif  (250 ms/frame, loops forever)
nyan-cat3.png  →
```

---

## Requirements

| Dependency | Version |
|------------|---------|
| Python     | ≥ 3.13 |
| imageio    | ≥ 2.37.3 |

`imageio` installs its required dependencies (including Pillow and NumPy) automatically.

---

## Installation

### Using uv (recommended)

```bash
# Clone the repository
git clone https://github.com/AgentPhoenix7/create-gif-py.git
cd create-gif-py

# Create a virtual environment and install dependencies
uv sync
```

### Using pip

```bash
# Clone the repository
git clone https://github.com/AgentPhoenix7/create-gif-py.git
cd create-gif-py

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install .
```

---

## Usage

### Run as-is

Drop your image frames into the project folder, update the `filenames` list in `create_gif.py`, then run:

```bash
# With uv
uv run create_gif.py

# With an activated virtual environment
python create_gif.py
```

The output GIF is written to the same directory.

### Customise

Open `create_gif.py` — there are three values you might want to change:

```python
import imageio.v3 as iio

# 1. The input frames, in order
filenames = ['frame1.png', 'frame2.png', 'frame3.png']

# 2. Load all frames into memory
images = [iio.imread(filename) for filename in filenames]

# 3. Write the GIF
iio.imwrite(
    'output.gif',   # output path
    images,
    duration=250,   # milliseconds each frame is displayed
    loop=0,         # 0 = loop forever; 1+ = loop N times then stop
)
```

#### Key parameters

| Parameter  | Type  | Default | Description |
|------------|-------|---------|-------------|
| `duration` | `int` | `250`   | How long each frame is shown, in milliseconds. Lower = faster animation. |
| `loop`     | `int` | `0`     | Number of times the GIF loops. `0` means infinite. |

---

## Project Structure

```
create-gif-py/
├── create_gif.py      # Main script — the entire implementation
├── nyan-cat1.png      # Input frame 1
├── nyan-cat2.png      # Input frame 2
├── nyan-cat3.png      # Input frame 3
├── nyan-cat.gif       # Generated output
├── pyproject.toml     # Project metadata and dependencies
├── uv.lock            # Locked dependency versions
└── LICENSE            # MIT
```

---

## How It Works

```
┌──────────────┐     iio.imread()     ┌──────────────────────┐
│  frame1.png  │ ──────────────────►  │                      │
│  frame2.png  │ ──────────────────►  │  In-memory frame list│
│  frame3.png  │ ──────────────────►  │                      │
└──────────────┘                      └──────────┬───────────┘
                                                 │
                                        iio.imwrite()
                                                 │
                                                 ▼
                                       ┌──────────────────┐
                                       │   output.gif     │
                                       │  (animated GIF)  │
                                       └──────────────────┘
```

1. `iio.imread()` decodes each image file into a NumPy array using Pillow under the hood.
2. `iio.imwrite()` encodes the list of arrays as a multi-frame GIF, writing the `duration` metadata into each frame's delay field.

---

## License

Distributed under the [MIT License](LICENSE). Copyright © 2026 Anis Mandal.
