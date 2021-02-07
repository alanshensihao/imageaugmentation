# import libraries
import os

class RenameImage():

    def renameImage():

          # root directory
        ROOT_DIR = os.path.abspath(".")
        # image directory
        IMAGE_PATH = os.path.join(ROOT_DIR,"image")

        for dirname in os.listdir(IMAGE_PATH):

            # print(os.listdir(IMAGE_PATH))
            # print(os.path.isdir(dirname))

            MUG_PATH = os.path.join(IMAGE_PATH,dirname)

            # print(os.path.exists(MUG_PATH+"/"+"0"+".jpg"))
            # print(os.path.isdir(MUG_PATH))

            if os.path.isdir(MUG_PATH) and not os.path.exists(MUG_PATH+"/"+"0"+".jpg"):
                for i, filename in enumerate(os.listdir(MUG_PATH)):
                    print(i,filename)
                    os.rename(MUG_PATH+"/"+filename,MUG_PATH+"/"+str(i)+".jpg")
                return False
            else:
                return True
        

print(RenameImage.renameImage())


