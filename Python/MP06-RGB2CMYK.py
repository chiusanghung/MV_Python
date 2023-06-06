import cv2 
from PIL import Image
import numpy as np

# Khai báo đường dẫn file hình
filehinh = r'lena_color.jpg'

# Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)

# Đọc ảnh màu dùng thư viện PIL. Ảnh PIL này dùng để thực hiện các tác vụ xử lý & tính toán thay vì dùng OpenCV
imgPIL = Image.open(filehinh)

# Tạo 1 ảnh có cùng Mode và kích thước với ảnh imgPIL, dùng để chứa kết quả chuyển đổi RGB sang grayScale
Cyan = Image.new(imgPIL.mode, imgPIL.size)
Magenta = Image.new(imgPIL.mode, imgPIL.size)
Yellow = Image.new(imgPIL.mode, imgPIL.size)
Black = Image.new(imgPIL.mode, imgPIL.size)

# Lấy kích thước ảnh
width = imgPIL.size[0]
height = imgPIL.size[1]

#Mỗi ảnh là một ma trận 2 chiều nên sẽ dùng 2 vòng for để
# để đọc hết các điểm ảnh (pixel) có trong hình
for x in range(width):
    for y in range(height):

        #Lấy giá trị điểm ảnh tại vị trí (x,y)
        R,G,B = imgPIL.getpixel((x,y))

        # Tiến hành trộn các kênh màu cho ra các màu C-Y-M-K
        Cyan.putpixel((x,y),(B,G,0))
        Magenta.putpixel((x,y),(B,0,R))
        Yellow.putpixel((x,y),(0,G,R))
        
        Min = min(R,G,B)
        K = Min
        Black.putpixel((x,y),(K,K,K))

# Chuyển ảnh từ PIL sang OpenCV để hiện thị bằng OpenCV
ImgC = np.array(Cyan)
ImgM = np.array(Magenta)
ImgY = np.array(Yellow)
ImgK = np.array(Black)

# Hiện thị ảnh dùng thư viện OpenCV
cv2.imshow('Anh mau RGB goc', img)
cv2.imshow('Kenh Cyan', ImgC)
cv2.imshow('Kenh Magenta', ImgM)
cv2.imshow('Kenh Yellow', ImgY)
cv2.imshow('Kenh Black', ImgK)

# Bấm phím bất kì để đóng cửa sổ hiện thị hình
cv2.waitKey(0)

# Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiện thị hình
cv2.destroyAllWindows()