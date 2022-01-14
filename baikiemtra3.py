# Nhập họ tên: (Phạm Đình Thanh Bình)
fullName = input('Nhập tên đầy đủ (Ex: Phạm Đình Thanh Bình):')
print(fullName)


# Kiểm tra xem số nhập vào có là thuận nghịch hay không
def isThuanNghich(n):
    str1 = str(n); 
    str2 = str1[::-1];
    if (str1 == str2):
        print("Số vừa nhập là số thuận nghịch")
    else:
        print("Số vừa nhập không phải là số thuận nghịch")
 
name = int(input("Nhập số lượng các kí tự của tên (ex: Phạm Đình Thanh Bình = 4445): "));
isThuanNghich(name)