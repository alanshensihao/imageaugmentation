import os
from keras.preprocessing.image import ImageDataGenerator,load_img,img_to_array,array_to_img
 
class Augmentation(object):
    def __init__(self,img_type="png"):
        self.datagen=ImageDataGenerator(
            #rotation_range=1.2,
            #width_shift_range=0.05,
            height_shift_range=0.05,
            # shear_range=0.05,
            # zoom_range=0.05,
            # horizontal_flip=True,
            fill_mode='nearest')
 
    def augmentation(self):
        # 读入3通道的train和label, 分别转换成矩阵, 然后将label的第一个通道放在train的第2个通处, 做数据增强
        print("运行 Augmentation")
        # Start augmentation.....
        img_t = load_img("../one/img/0.png")  # 读入train
        img_l = load_img("../one/label/0.png")  # 读入label
 
        x_t = img_to_array(img_t)  # 转换成矩阵
        x_l = img_to_array(img_l)
        x_t[:, :, 2] = x_l[:, :, 0]  # 把label当做train的第三个通道
        #x_t = x_t[..., [2,0,1]]#image-102,120,210
        img_tmp = array_to_img(x_t)
        img_tmp.save("../one/merge/0.png")  # 保存合并后的图像
        img = x_t
        img = img.reshape((1,) + img.shape)  # 改变shape(1, 512, 512, 3)
        savedir = "../one/aug_merge"  # 存储合并增强后的图像
        if not os.path.lexists(savedir):
            os.mkdir(savedir)
        print("running %d doAugmenttaion" % 0)
        self.do_augmentate(img, savedir, str(0))  # 数据增强
 
    def do_augmentate(self, img, save_to_dir, save_prefix, batch_size=1, save_format='png', imgnum=30):
        # augmentate one image
        datagen = self.datagen
        i = 0
        for _ in datagen.flow(
                img,
                batch_size=batch_size,
                save_to_dir=save_to_dir,
                save_prefix=save_prefix,
                save_format=save_format):
            i += 1
            if i > imgnum:
                break
if __name__=="__main__":
    aug=Augmentation()
    aug.augmentation()