from watchdog.events import FileSystemEventHandler
import os.path
from PIL import Image

from config import OUTPUT_FOLDER

#Handler for working with image on creation:
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        img_path = event.src_path.strip()
        img = Image.open(img_path)

        #Stub image handling logic:
        r_img = img.rotate(90)
        #Saving to output folder 
        r_img.save(os.path.join(OUTPUT_FOLDER, 'output_' + img.filename.split('/')[-1]))