"""
Utility for creating animated GIFs from image files.
"""

from collections.abc import Sequence
from pathlib import Path
import imageio.v3 as iio

def create_gif(
    image_paths: Sequence[str | Path],
    output: str | Path,
    *,
    duration: int = 500,
    loop: int = 0,
) -> None:
    """
    Create an animated GIF from a sequence of image files.

    Parameters
    ----------
    image_paths
        Sequence of image file paths.
    output
        Output GIF filename.
    duration
        Duration of each frame in milliseconds.
    loop
        Number of animation loops.

        0 means loop forever.
    """

    if len(image_paths) < 2:
        raise ValueError("At least two images are required.")
    
    paths = [Path(path) for path in image_paths]

    missing = [path for path in paths if not path.is_file()]
    if missing:
        raise FileNotFoundError(
            f"Image not found: {missing[0]}"
        )
    
    images = [iio.imread(path) for path in paths]

    iio.imwrite(
        Path(output),
        images,
        duration=duration,
        loop=loop
    )