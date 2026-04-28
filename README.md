# warehouse-management
# Hệ thống quản lý kho hàng

## 1. Giới thiệt dự án

+ Đây là một hệ thống quản lý kho hàng đơn giản được xây dựng bằng Python.
Chương trình cho phép người dùng quản lý các mặt hàng thông qua giao diện dòng lệnh (CLI).

Người dùng có thể thêm, xem, tìm kiếm, sắp xếp và lưu dữ liệu một cách dễ dàng.

+ Dự án được thực hiện nhằm vận dụng các kiến thức đã học trong học phần **Phương pháp lập trình**, bao gồm:

- Sử dụng hàm để chia nhỏ chương trình.
- Sử dụng vòng lặp để xây dựng menu tương tác.
- Sử dụng cấu trúc điều kiện để xử lý lựa chọn của người dùng.
- Sử dụng danh sách và từ điển để quản lý dữ liệu.
- Kiểm tra dữ liệu đầu vào.
- Đọc, ghi và xuất dữ liệu ra file.
- Trình bày dữ liệu dưới dạng bảng có định dạng.

**Hệ thống quản lý kho hàng**
+ Đề tài tập trung xây dựng một chương trình đơn giản để quản lý thông tin hàng hóa trong kho.
+ Mỗi mặt hàng được xem là một bản dữ liệu, bao gồm các thông tin cơ bản như:
- Mã hàng
- Tên hàng
- Số lượng
- Giá cả

## 2. Chức năng chính của chương trình 
+ 3.1. Thêm hàng hóa mới
- Nhập thông tin hàng hóa từ bàn phím
- Kiểm tra dữ liệu hợp lệ (không âm, đúng kiểu số)
- Lưu vào danh sách
+ 3.2. Hiển thị danh sách hàng
- In toàn bộ danh sách hàng hóa ra màn hình
- Hiển thị theo dạng bảng
+ 3.3. Tìm kiếm hàng hóa
- Tìm theo mã hoặc tên
- Không phân biệt chữ hoa/thường
+ 3.4. Sắp xếp hàng hóa
- Sắp xếp theo:
Tên
Số lượng
Giá
+ 3.5. Thống kê
- Tổng số mặt hàng
- Tổng số lượng hàng
+ 3.6. Lưu dữ liệu
- Ghi danh sách hàng vào file
+ 3.7. Đọc dữ liệu
- Đọc dữ liệu từ file và khôi phục danh sách

## 3. Mục tiêu của chương trình

Chương trình được xây dựng với các mục tiêu chính sau:

1. Giúp người dùng quản lý danh sách hàng hóa trong kho một cách đơn giản và hiệu quả.  
2. Cho phép thêm, xem, tìm kiếm, sắp xếp, thống kê thông tin hàng hóa và lưu danh sách  
3. Hỗ trợ theo dõi số lượng và giá trị của từng mặt hàng trong kho.  
4. Cung cấp chức năng thống kê tổng số lượng và tổng giá trị hàng hóa.  
5. Lưu trữ dữ liệu vào file để có thể sử dụng lại trong các lần chạy sau.  
6. Đảm bảo dữ liệu nhập vào hợp lệ (không âm, đúng kiểu dữ liệu).  
7. Rèn luyện kỹ năng lập trình Python, xử lý dữ liệu và tổ chức chương trình theo từng hàm.

## 4. Công nghệ và thư viện sử dụng

- Ngôn ngữ lập trình: Python  
- Môi trường phát triển: Visual Studio Code  

## 5. Cấu trúc dữ liệu

+ Trong chương trình, mỗi bệnh nhân được lưu dưới dạng một dictionary gồm các trường thông tin:

    {
        "id": "A1",
        "name": "Sách",
        "quantily": 10,
        "price": "20.0"
    }

+ Cách tổ chức này giúp chương trình dễ dàng thêm, tìm kiếm, sắp xếp và thống kê dữ liệu hàng hóa.

## 6. Các file trong dự án

| Tên file | Chức năng |
- | `main + menu.py` | File chứa mã nguồn chính của chương trình quản lý kho (menu, thêm, tìm kiếm, thống kê, lưu file, ...) |
- | `README.md` | File mô tả dự án, hướng dẫn sử dụng và thông tin chi tiết |
- | `.gitattributes` | File cấu hình cho Git (quản lý định dạng file và line ending) |

## 7. Menu của chương trình

========================================
   HỆ THỐNG QUẢN LÝ KHO HÀNG
========================================

1. Thêm hàng hóa mới
2. Hiển thị danh sách hàng hóa
3. Tìm kiếm hàng hóa (theo ID hoặc tên)
4. Sắp xếp danh sách hàng hóa
5. Thống kê & tính toán dữ liệu
6. Chỉnh sửa thông tin hàng hóa
7. Xóa hàng hóa
8. Lưu dữ liệu & xuất báo cáo (.txt)
9. Thoát chương trình

----------------------------------------
Chọn chức năng (1-9):

## 8. Thông tin sinh viên
 
Sinh viên thực hiện: **Lưu Thảo Ngân**
Môn học: **Phương pháp lập trình**
Giảng viên: **Trần Văng Long**
Khoa: **Tin học**

### TỔNG ĐIỂM TỰ ĐÁNH GIÁ: 9/10

