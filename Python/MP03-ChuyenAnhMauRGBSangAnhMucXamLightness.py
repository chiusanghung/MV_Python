import cv2              # sử dụng thư viện xử lý ảnh
from PIL import Image   # thư viện xử lý ảnh PILLOW hỗ trợ nhiều định dạng ảnh
import numpy as np      # thư viện toán học, đặc biệt là các tính toán ma trận

# Khai báo đường dẫn file hình
filehinh = r'lena_color.jpg'

# Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread('lena_color.jpg', cv2.IMREAD_COLOR)

# Đọc ảnh màu dùng thư viện PIL. Ảnh PIL này dùng để thực hiện các tác vụ xử lý & tính toán thay vì dùng OpenCV
imgPIL = Image.open(filehinh)

# Tạo 1 ảnh có cùng kích thước và mode với ảnh imgPIL dùng để chứa kết quả chuyển đổi RGB sang Grayscale
average = Image.new(imgPIL.mode, imgPIL.size)

# Lấy kích của ảnh từ imgPIL
width = average.size[0]
height = average.size[0]

# Mỗi ảnh là 1 ma trận 2 chiều => 2 vòng for để đọc hết các điểm ảnh (pixel) trong ảnh
for x in range(width):
    for y in range(height):
        
        R, G, B = imgPIL.getpixel((x, y))     # Lấy giá trị điểm ảnh tại vị trí (x, y)

        # Công thức chuyển đổi điểm ảnh màu RGB thành điểm ảnh mức xám dùng pp Lightness
        MIN = min(R, G, B)
        MAX = max(R, G, B)
        gray = np.uint8((MIN + MAX) / 2)

        # Gán giá trị mức xám vừa tính cho ảnh
        average.putpixel((x, y), (gray, gray, gray))

# Chuyển ảnh từ PIL sang OpenCV để hiện thị bằng OpenCV
anhmucxam = np.array(average)

# Hiện thị hình dùng thư viện OpenCV 
cv2.imshow('Anh mau RGB goc co gai Lena', img)
cv2.imshow('Anh muc xam dung Lightness', anhmucxam)

# Bấm phím bất kì để đóng cửa sổ hiện thị hình
cv2.waitKey(0)

# Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiện thị hình
cv2.destroyAllWindows()