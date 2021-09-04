import PIL.Image
import os
import numpy as np
from .mono_dataset import MonoDataset


class ETS2Dataset(MonoDataset):
    """ Superclass for ETS2 Datasets
    """
    def __init__(self, *args, **kwargs):
        super(ETS2Dataset, self).__init__(*args, **kwargs)

        # NOTE: Make sure your intrinsics matrix is *normalized* by the original image size.
        # To normalize you need to scale the first row by 1 / image_width and the second row
        # by 1 / image_height. Monodepth2 assumes a principal point to be exactly centered.
        # If your principal point is far from the center you might need to disable the horizontal
        # flip augmentation.
        self.K = np.array([[990.9949 / 1440, 0, 0.5, 0],
                           [0, 561.5638 / 816, 0.5, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]], dtype=np.float32)

        self.full_res_shape = (1440, 816)
        self.img_ext = '.jpg'

    def get_color(self, folder, frame_index, side, do_flip):
        try:
            file = self.get_image_path(folder, frame_index)
            color = self.loader(file)
        except FileNotFoundError as err:
            print("File not found {0} for frame {1}".format(file, frame_index))
            raise

        if do_flip:
            color = color.transpose(PIL.Image.FLIP_LEFT_RIGHT)

        return color

    def get_image_path(self, folder, frame_index):
        f_str = "capture-{:010d}{}".format(frame_index, self.img_ext)

        image_path = os.path.join(
            self.data_path, folder, f_str
        )

        return image_path

    def check_depth(self):
        return False

    def get_depth(self, folder, frame_index, side, do_flip):
        pass
