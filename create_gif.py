# Import ImageIO for reading and writing image files.
import imageio.v3 as iio

# List of image frames to include in the GIF.
filenames = ['nyan-cat1.png', 'nyan-cat2.png', 'nyan-cat3.png']

# Load all images into memory.
images = [iio.imread(filename) for filename in filenames]

# Save the images as an animated GIF.
# duration: Frame display time (milliseconds)
# loop=0: Repeat indefinitely
iio.imwrite('nyan-cat.gif', images, duration=250, loop=0)