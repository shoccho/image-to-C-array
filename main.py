#imports
import cv2
import numpy as np
import sys

def readingimg(img_path):
    img =  cv2.imread(img_path,0)
    dim=(64,32)
    img=cv2.resize(img,dim)

    _,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    data = []
    for row in img:
        for cell in row:
            if cell==0:
                data.append(0)
            else :
                data.append(1)
    return data


def write_to_file(data):
    with open("imgcode.txt","w")  as file:
        for i in range(0,len(data),8):
            bt = ""
            for j in range(0,8):
                if i+j <len(data) :
                    bt += str(data[i+j])
                else:
                    bt+=str(0)
            st = "B{0}, ".format(bt)
            file.write(st)
            if i%14==0:
                file.write("\n")
    

def main():
    if(len(sys.argv)==1):
        print("No imge was supplied :/ exiting")
        sys.exit()

    for arg in sys.argv[1:]:
        binary_data = readingimg(arg)
        write_to_file(binary_data)
    print("Done ")
if __name__ == "__main__":
    main()