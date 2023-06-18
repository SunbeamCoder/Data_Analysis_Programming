# DangQuocToan_20051051_51
n = int(input("Nhap n: "))
List = []
for i in range(0,n+1):
	if i %2==0:
		List.append(i)
print(List)
file = open('D:\GT\DangQuocToan_20051051\out.txt','w')
for i in List:
  file.write(str(i) + "\n")
file.close()