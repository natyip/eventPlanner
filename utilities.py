
import pathlib, os

class utilities:
    def getAssetPath(relativePath):
        current_dir = pathlib.Path(__file__).parent.resolve() # current directory
        # print(os.path.join(current_dir, relativePath))
        return os.path.join(current_dir, relativePath) # join with your image's file name
