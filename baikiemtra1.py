# Nhập tên (không dấu): (Bình)
name = input('Nhập tên (Ex: binh):')
print(name)


# Nhập n là số lượng kí tự của tên (binh = 4)
n = input('Nhập độ dài tên của mình:')
n = int(n)
for i in range(n):
    myDict = {i+1:(i+1)*(i+1)}
    print(myDict)


