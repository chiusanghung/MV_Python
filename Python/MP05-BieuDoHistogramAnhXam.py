import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt #Thư viện vẽ biểu đồ pip install matplotlib


def ChuyenDoiAnhMauRGBSangAnhXamLuminance(imgPIL):
    #Tạo một ảnh có cùng kích thước và mode với ảnh imgPIL
    #Ảnh này dùng để chứa kết quả chuyển đổi RGB sang Grayscale
    average = Image.new(imgPIL.mode, imgPIL.size)
    width = average.size[0]
    height = average.size[1]

    #Mỗi ảnh là một ma trận 2 chiều nên sẽ dùng 2 vòng for để
    # để đọc hết các điểm ảnh (pixel) có trong hình
    for x in range(width):
        for y in range(height):
            #Lấy giá trị điểm ảnh tại vị trí (x,y)
            R,G,B = imgPIL.getpixel((x,y))

            #công thức chuyển đổi điểm ảnh màu RGB thành điểm anhrxams dùng phương pháp binary

            gray=np.uint8(0.2126*R + 0.7152*G + 0.0722*B)
            #Gán giá trị mức xám vừa tính cho ảnh xám
            average.putpixel((x,y),(gray,gray,gray))
    return average

def TinhHistogram(HinhXamPIL):
    #Mỗi pixel có giá trị từ 0-255, nên phải khai báo có một mảng có 256 phần tử để chứa số đếm của các pixel có cùng giá trị 
    his = np.zeros(256)
     #kích thước ảnh
    w=HinhXamPIL.size[0]
    h=HinhXamPIL.size[1]
    for x in range(w):
        for y in range(h):
            #Lấy giá trị xám tại điểm x,y
            gR, gG, gB = HinhXamPIL.getpixel((x,y))
            his[gR] += 1  
    return his

def VeBieuDoHistogram(his):
    w= 5
    h=4
    plt.figure('Biểu đồ Histogram ảnh xám',figsize=(((w,h))),dpi = 100)
    trucX=np.zeros(256)
    trucX=np.linspace(0,256,256)
    plt.plot(trucX,his, color ='orange')
    plt.title('Biểu đồ Histogram')
    plt.xlabel('Giá trị mức xám')
    plt.ylabel('Số điểm cùng giá trị mức xám')
    plt.show()

filehinh = r'bird_small.jpg'

imgPIL = Image.open(filehinh)

#chuyen anh PIL sang Opencv de hien thi bang thu vien cv2
HinhxamPIL = ChuyenDoiAnhMauRGBSangAnhXamLuminance(imgPIL)

his = TinhHistogram(HinhxamPIL)

HinhXamCV = np.array(HinhxamPIL)
cv2.imshow('Anh mmuc xam',HinhXamCV)

#Hien thi bieu do His
VeBieuDoHistogram(his)

#Bấm phím bất kì để đóng cửa sổ hiển thị hình
cv2.waitKey(0)

# Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiện thị hình
cv2.destroyAllWindows()




