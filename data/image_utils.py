# Various helper functions for data collection.
import os
from PIL import Image


# Replace this as you see fit.
MINECRAFT_PATH = "YOUR PATH HERE/.../.minecraft"


def compress_images(in_path, out_path):
    """
    Function for compressing the collected images. This saved us gigabytes of space.

    :param in_path: path to Minecraft PNG
    :param out_path: path to save compressed image to
    :return: None
    """
    files = os.listdir(in_path)
    for image in files:
        i = Image.open(os.path.join(in_path, image))
        i = i.convert('RGB')
        i.save(os.path.join(out_path, image[:-4] + '.jpg'), quality=20, optimize=True)


def move_subset_images(in_path, out_path,
                       yaw_start=-180, yaw_end=170, yaw_int=20,
                       pitch_start=-90, pitch_end=30, pitch_int=15,
                       tick_start=0, tick_end=24000, tick_int=240):
    """
    If you only want to move a certain subset of images from somewhere to another
    based on yaw, pitch, and tick values.

    :param in_path: path to source file
    :param out_path: destination path
    :return: None
    """
    for yaw in range(-yaw_start, yaw_end, yaw_int):
        for pitch in range(pitch_start, pitch_end, pitch_int):
            for tick in range(tick_start, tick_end, tick_int):
                os.rename(os.path.join(in_path, f'p{pitch}_y{yaw}_t{tick}.jpg'),
                          os.path.join(out_path, f'p{pitch}_y{yaw}_t{tick}.jpg'))
