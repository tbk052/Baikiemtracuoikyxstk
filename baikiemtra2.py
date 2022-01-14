    # Nhập tên đệm: (Thanh)
subName = input('Nhập tên đệm (Ex: thanh):')
print(subName)


# Nhập tên đệm và tên
print
subName=str(input("Nhập tên đệm (ex: thanh): "));
name=str(input("Nhập tên (ex:binh): "));
n=str(len(subName))+str(len(name));
n_len=len(n)
sum=0
for i in range(n_len):
    n_val=n[i]
    sum=sum+int(n_val)
print("Tổng các ký tự của tên đệm và tên vừa nhập là: ",sum)
