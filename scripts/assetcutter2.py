import cv2
from pathlib import Path
pic_pool = [
    Path(Path.cwd() / "orig assets/uniformblue.png"),
    Path(Path.cwd() / "orig assets/uniformgreen.png"),
    Path(Path.cwd() / "orig assets/uniformwhite.png"),
    Path(Path.cwd() / "orig assets/uniformyellow.png")
]
writepath = Path(Path.cwd() / "1.1"/"Textures"/"Things"/"Apparel"/"Clothing")

color_pool = [
    "blue",
    "green",
    "white",
    "yellow"
]

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
#print(path)
for k in range(0,4):
    orig_img = cv2.imread(str(pic_pool[k]), cv2.IMREAD_UNCHANGED)

    #coat icons
    for i in range(0,5):
        for j in range(0,3):

            crop_img = orig_img[128*i:128*(i+1), 128*(j):128*(j+1)]


            t_writepath = writepath/("redcoat_"+color_pool[k]+"_"+size_pool[i]+"_"+orient_pool[j%3]+".png")
            print(t_writepath)

            cv2.imshow("crop", crop_img)
            cv2.waitKey(0)

            cv2.imwrite(str(t_writepath), crop_img)
