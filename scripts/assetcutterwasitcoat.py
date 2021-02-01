import cv2
from pathlib import Path
pic_pool = [
    Path(Path.cwd()/".."/ "orig assets/release2/coatf.png")
]
writepath = Path(Path.cwd() /".."/ "1.2"/"Textures"/"Things"/"Apparel"/"Clothing"/"coatf")

# color_pool = [
#     "blue",
#     "green",
#     "white",
#     "yellow"
# ]

size_pool = [
    "Fat",
    "Hulk",
    "Male",
    "Female",
    "Thin"
]

orient_pool = [
    "south",
    "north",
    "east"

]

orig_img = cv2.imread(str(pic_pool[0]), cv2.IMREAD_UNCHANGED)
for i in range(0,5):
        for j in range(0,3):

            crop_img = orig_img[256*i:256*(i+1), 256*(j):256*(j+1)]


            t_writepath = writepath/("coatf"+"_"+size_pool[i]+"_"+orient_pool[j%3]+".png")
            print(t_writepath)

            cv2.imshow("crop", crop_img)
            cv2.waitKey(0)

            cv2.imwrite(str(t_writepath), crop_img)
