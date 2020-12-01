import os
import argparse
from PIL import Image


# Replace these paths as you see fit.
MINECRAFT_PATH = "YOUR PATH HERE/.../.minecraft"
OUT_FOLDER = os.path.join(os.getcwd(), "named_screenshots")


def rename_file(args):
    """
    Rename and move the latest screenshot according to the provided pitch, yaw, and tick values in the arguments.
    :param args:
    :return: None
    """
    source_dir = os.path.join(MINECRAFT_PATH, "screenshots")
    source_file = os.path.join(source_dir, os.listdir(source_dir)[0])

    # ensure Minecraft finished writing the PNG file
    cont = True
    while cont:
        try:
            im = Image.open(source_file)
            im.verify()
            cont = False
        except Exception:
            pass

    file_name = f"y{args.yaw}_p{args.pitch}_t{args.ticks}.png"
    os.rename(source_file, os.path.join(OUT_FOLDER, file_name))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Names a Minecraft screenshot according to the specified yaw, pitch, and tick values.")
    parser.add_argument('--pitch', help="Pitch, the vertical viewing angle.")
    parser.add_argument('--yaw', help="Yaw, the horizontal viewing angle.")
    parser.add_argument('--ticks', help="Ticks, the number of Minecraft ticks in the day at which the screenshot was taken")
    rename_file(parser.parse_args())
