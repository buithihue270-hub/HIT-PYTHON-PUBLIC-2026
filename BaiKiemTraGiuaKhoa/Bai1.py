x = int(input("Nhập số x:"))
if x == int(x):
    x = int(x)
he_so = list(map(int, input().split()))
n = len(he_so) - 1
ket_qua = 0
bac = n
for i in range(len(he_so)):
    a = he_so[i]
    ket_qua = ket_qua + a * (x ** bac)
    bac = bac - 1
print(int(ket_qua))