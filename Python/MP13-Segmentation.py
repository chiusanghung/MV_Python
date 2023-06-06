import cv2 #Xu li anh
from PIL import Image #Thu vien xu li anh ho tro nhieu loai anh
import numpy as np

#Tao duong dan
filehinh = r'lena_color.jpg'

#Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)

#Đọc ảnh màu dùng thư viện PIL
imgPIL = Image.open(filehinh)

#Tạo 1 ảnh cùng kích thước và mode với ảnh imgPIL
#Ảnh này chứa kết quả cuyển đổi RGB to Grayscale
SegImg = Image.new(imgPIL.mode, imgPIL.size)

#Lấy kích thước của ảnh từ imgPIL`
width = imgPIL.size[0]
height = imgPIL.size[1]

# Khai báo giá trị ngưỡng xy
X1 = 80
X2 = 150
Y1 = 400
Y2 = 500
nguong = 45

Gs = 0
Rs = 0
Bs = 0

for x in range (X1,Y1):
    for y in range (X2,Y2):
        R,G,B = imgPIL.getpixel((x,y))

        # Cộng dồn điểm ảnh cho mỗi kênh tương ứng
        Gs += G
        Rs += R
        Bs += B
    # Size = (X2-X1+1)*(Y2-Y1+1)
    Size = np.abs (X2-X1)*np.abs(Y2-Y1)
    Rs /= Size
    Gs /= Size
    Bs /= Size
        
    for x in range (width):
        for y in range (height):
            R1, B1, G1 =imgPIL.getpixel((x,y))

            # Công thức tính Euclidean Distance giữa 2 vector a và z như sau (ct 6.7-1)
            D = np.sqrt((R1-Rs)**2 + (G1-Gs)**2 + (B1-Bs)**2)

            # Sau khi tính được giá trị D(z,a), chúng ta so sanh vs giá trị ngưỡng (Threshold)
            # để xác định điểm z(x,y) đang x l backgruond hay object
            if D <= nguong:
                SegImg.putpixel((x,y),(255,255,255))
            else:
                SegImg.putpixel((x,y),(B1,G1,R1))

#Chuyển ảnh PIL sang OpenCv để hiển thị bằng thư viện OpenCv
imgSeg = np.array(SegImg)

#hiển thị ảnh bằng thư viện OpenCv
cv2.imshow('Hinh phan doan mau', imgSeg)
cv2.imshow('Anh goc RGB', img)

# Bấm phím bất kỳ để đóng cửa sổ hiển thị
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị hình
cv2.destroyAllWindows()

