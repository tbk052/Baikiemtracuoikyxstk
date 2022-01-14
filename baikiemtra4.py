# Nhập vào chuỗi là tên và mã sv
fullName = input('Nhập họ tên (viết liền không dấu) (ex: phamdinhthanhbinh):')
id = input('Nhập idsv (kiểu số): ')
print(fullName + id)


# In ra màn hình từ chuỗi ở câu a
def split(fullName):
    return [char for char in fullName]
print(split(fullName))

print(tuple(id))