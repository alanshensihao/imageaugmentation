# 把label.png改名为1.png
import os
from shutil import copyfile 

# mugs_json path
JSON_PATH = os.path.abspath('.\image\mugs_json')




i = 0

for root, dirs, names in os.walk(JSON_PATH): 
    for dr in dirs:

        new_name = dr.split('_')[0] + '.png'
        path = os.path.join(JSON_PATH,new_name)
        file_dir = os.path.join(root, dr)

        if os.path.exists(path):
            print(dr)
            file = os.path.join(file_dir,'label.png')
            print(file)
        
            new_file_name = os.path.join(file_dir, new_name)
            print(new_file_name)
        else:
            dr_str = str(dr)
            partitioned_dir = dr_str.split('_')

            #print(partitioned_dir[0])
            dir_num = str(partitioned_dir[0])

            new_name = dir_num+'.png'
            new_file_name = os.path.join(file_dir,new_name)
        
        TAR_PATH = os.path.abspath('.\image\mugs_data\cv2_mask')   
        tar_file = os.path.join(TAR_PATH, new_name)
        copyfile(new_file_name, tar_file)
        i = i + 1