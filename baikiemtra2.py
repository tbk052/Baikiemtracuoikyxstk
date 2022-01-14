# Nhập tên đệm: (Thanh)
subName = input('Nhập tên đệm (Ex: thanh):')
print(subName)


# Nhập tổng số kí tự của tên đệm và tên
print("Nhập số lượng kí tự của tên đệm và tên của bạn (ex: Thanh Bình = 9):",end='')
n=input()
n_len=len(n)
tong=0
for i in range(n_len):
    n_val=n[i]
    tong=tong+int(n_val)
print("Tổng các ký tự của tên đệm và tên vừa nhập là: ",tong)
