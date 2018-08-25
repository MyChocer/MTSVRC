from .dataset import VideoDataset, ProcessDesc, SingleVideoLoader
from .loader import VideoLoader

def video_size_from_file(filename):
    return lib.nvvl_video_size_from_file(str.encode(filename))
