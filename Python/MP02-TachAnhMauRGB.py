import cv2              #Sử dụng thư viện xử lí ảnh OpenCV cho Python
import numpy as np      #Thư viện toán học, đặc biệt là các tính toán ma trận

# Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread('lena_color.jpg', cv2.IMREAD_COLOR)

# Lấy kích thước của ảnh
height = len(img[0])
width = len(img[1])

# Khai báo 3 biến để chứa hình 3 kênh RGB
red = np.zeros((width, height, 3), np.uint8)        # Số 3 là ba kênh RGB, mỗi kênh chứa 8bit (0-255)
green = np.zeros((width, height, 3), np.uint8)  
blue = np.zeros((width, height, 3), np.uint8)  

# Ban đầu set zero cho tất cả điểm ảnh có trong cả 3 kênh trong mỗi hình
red[:] = [0,0,0]
green[:] = [0,0,0]
blue[:] = [0,0,0]

# Mỗi hình là 1 ma trận 2 chiều nên sẽ dùng 2 vòng for để đọc hết các điểm ảnh (pixel) có trong hình
for x in range(width):
    for y in range(height):
        # Lấy giá trị điểm ảnh tại vị trí (x,y)
        R = img[x,y,2]
        G = img[x,y,1]
        B = img[x,y,0]

        # Thiết lập màu cho các kênh 
        red [x,y,2] = R
        green [x,y,1] = G
        blue [x,y,0] = B

# Hiện thị hình dùng thư viện OpenCV 
cv2.imshow('Hinh mau RGB goc', img)
cv2.imshow('Kenh red', red)
cv2.imshow('Kenh green', green)
cv2.imshow('Kenh blue', blue)

# Bấm phím bất kì để đóng cửa sổ hiện thị hình
cv2.waitKey(0)

# Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiện thị hình
cv2.destroyAllWindows()