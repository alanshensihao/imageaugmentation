import os

JASON_PATH = os.path.abspath('.\image\mugs_json')

json_file = os.listdir(JASON_PATH)

os.system("activate MaskRCNN") 
for file in json_file: 
    os.system("labelme_json_to_dataset.exe %s"%(JASON_PATH + '/' + file))