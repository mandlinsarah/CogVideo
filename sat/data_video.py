import os
import shutil
import logging

class VideoManager:
    def __init__(self, video_folder):
        self.video_folder = video_folder
        self.logger = logging.getLogger(__name__)

    def delete_video(self, video_name):
        video_path = os.path.join(self.video_folder, video_name)
        if os.path.exists(video_path):
            os.remove(video_path)
            self.logger.info(f"{video_name} deleted successfully.")
            return f"{video_name} deleted successfully."
        else:
            self.logger.warning(f"{video_name} does not exist.")
            return f"{video_name} does not exist."

    def copy_video(self, src_video_name, dst_video_name):
        src_path = os.path.join(self.video_folder, src_video_name)
        dst_path = os.path.join(self.video_folder, dst_video_name)
        if os.path.exists(src_path):
            shutil.copyfile(src_path, dst_path)
            self.logger.info(f"{src_video_name} copied to {dst_video_name}.")
            return f"{src_video_name} copied to {dst_video_name}."
        else:
            self.logger.warning(f"{src_video_name} does not exist.")
            return f"{src_video_name} does not exist."

# Optional: Configure logging globally, could be done outside this script
logging.basicConfig(level=logging.INFO)
