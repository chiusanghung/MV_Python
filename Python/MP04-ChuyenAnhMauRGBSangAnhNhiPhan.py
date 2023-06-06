import cv2              # sử dụng thư viện xử lý ảnh
from PIL import Image   # thư viện xử lý ảnh PILLOW hỗ trợ nhiều định dạng ảnh
import numpy as np      # thư viện toán học, đặc biệt là các tính toán ma trận

# Khai báo đường dẫn file hình
filehinh = r'lena_color.jpg'

# Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread('lena_color.jpg', cv2.IMREAD_COLOR)

# Đọc ảnh màu dùng thư viện PIL. Ảnh PIL này dùng để thực hiện các tác vụ xử lý & tính toán thay vì dùng OpenCV
imgPIL = Image.open(filehinh)

# Tạo 1 ảnh có cùng kích thước và mode với ảnh imgPIL dùng để chứa kết quả chuyển đổi RGB sang Binary
binary = Image.new(imgPIL.mode, imgPIL.size)

# Lấy kích của ảnh từ imgPIL
width = binary.size[0]
height = binary.size[0]

# Thiết lập 1 giá trị ngưỡng để tính điểm ảnh nhị phân
nguong = 130

# Mỗi ảnh là 1 ma trận 2 chiều => 2 vòng for để đọc hết các điểm ảnh (pixel) trong ảnh
for x in range(width):
    for y in range(height):
        
        R, G, B = imgPIL.getpixel((x, y))     # Lấy giá trị điểm ảnh tại vị trí (x, y)

        # Công thức chuyển đổi điểm ảnh màu RGB thành điểm ảnh mức xám dùng pp Average
        gray = np.uint8(0.2126*R + 0.7152*G + 0.0722*B)

        # Xác định giá trị điểm nhị phân
        if (gray < nguong):
            binary.putpixel((x, y), (0, 0, 0))
        else:
            binary.putpixel((x, y), (255, 255, 255))

# Chuyển ảnh từ PIL sang OpenCV để hiện thị bằng OpenCV
nhiphan = np.array(binary)

# Hiện thị hình dùng thư viện OpenCV 
cv2.imshow('Anh mau RGB goc co gai Lena', img)
cv2.imshow('Anh nhi phan (Binary)', nhiphan)

# Bấm phím bất kì để đóng cửa sổ hiện thị hình
cv2.waitKey(0)

# Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiện thị hình
cv2.destroyAllWindows()