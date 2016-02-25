import os, internetarchive, time, shutil
from internetarchive.api import upload
item = internetarchive.item('video_aljazeera_com')
md = dict(mediatype='video', creator='Al Jazeera', title='Al Jazeera Videos')
while True:
    for root, dirs, files in os.listdir("/home/video_aljazeera/"):
        for file in files:
            if file.endswith(".warc.gz"):
                fileage = os.path.getmtime(file)
                now = time.time()
                olderthan = 14400
                diff = now - fileage
                if diff > olderthan:
                   path = os.path.realpath(file)
                   item.upload(path, metadata=md, queue_derive=True, delete=True)
    time.sleep(600)
