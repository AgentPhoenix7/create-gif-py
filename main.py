from pathlib import Path
from create_gif import create_gif

def main() -> None:
    images = [
        Path("images/nyan-cat1.png"),
        Path("images/nyan-cat2.png"),
        Path("images/nyan-cat3.png")
    ]

    create_gif(
        images,
        "images/nyan-cat.gif",
        duration=250,
        loop=0
    )

if __name__ == "__main__":
    main()