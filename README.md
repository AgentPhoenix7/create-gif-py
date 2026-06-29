<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=32&duration=3000&pause=1000&color=FF6B6B&center=true&vCenter=true&width=600&lines=create-gif-py;Turn+Images+into+Animated+GIFs;Simple+%E2%80%A2+Lightweight+%E2%80%A2+Pythonic" alt="Animated header" />

<br/>

<img src="images/nyan-cat.gif" alt="Demo — nyan cat animated GIF created with this project" width="420" />

<br/><br/>

[![Python](https://img.shields.io/badge/Python-3.13%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![imageio](https://img.shields.io/badge/imageio-%3E%3D2.37.3-FF6B6B?style=for-the-badge)](https://imageio.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![uv](https://img.shields.io/badge/managed%20with-uv-7C3AED?style=for-the-badge)](https://github.com/astral-sh/uv)

**Convert a sequence of images into a smooth, looping animated GIF — in a single importable function.**

</div>

---

## What It Does

`create-gif-py` reads a list of image frames (PNG, JPEG, or any format supported by Pillow) and stitches them into a single animated GIF with configurable frame timing and loop behavior.

---

## Demo

The GIF at the top of this page was produced by running `main.py` against three PNG frames:

```
images/nyan-cat1.png  →
images/nyan-cat2.png  →  images/nyan-cat.gif  (250 ms/frame, loops forever)
images/nyan-cat3.png  →
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

Place your image frames inside the `images/` folder, update the list in `main.py`, then run:

```bash
# With uv (no install needed)
uv run main.py

# After uv sync or pip install .
create-gif

# With an activated virtual environment
python main.py
```

The output GIF is written to the `images/` folder.

### Customise

Edit `main.py` to point at your own frames and tweak the parameters:

```python
from pathlib import Path
from create_gif import create_gif

create_gif(
    [
        Path("images/frame1.png"),
        Path("images/frame2.png"),
        Path("images/frame3.png"),
    ],
    "images/output.gif",
    duration=250,  # milliseconds each frame is displayed
    loop=0,        # 0 = loop forever; 1+ = loop N times then stop
)
```

You can also import `create_gif` directly in your own script:

```python
from create_gif import create_gif

create_gif(["a.png", "b.png", "c.png"], "out.gif", duration=100)
```

#### Key parameters

| Parameter  | Type  | Default | Description |
|------------|-------|---------|-------------|
| `duration` | `int` | `500`   | How long each frame is shown, in milliseconds. Lower = faster animation. |
| `loop`     | `int` | `0`     | Number of times the GIF loops. `0` means infinite. |

---

## Project Structure

```
create-gif-py/
├── create_gif.py      # Core utility — create_gif() function
├── main.py            # Entrypoint — runs the nyan-cat demo
├── images/
│   ├── nyan-cat1.png  # Input frame 1
│   ├── nyan-cat2.png  # Input frame 2
│   ├── nyan-cat3.png  # Input frame 3
│   └── nyan-cat.gif   # Generated output
├── pyproject.toml     # Project metadata and dependencies
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
