list_number = []
n = 1


def nhap(n, list_number):
    while True:
        try:
            n = int(input("Nhập vào số lượng phần tử: "))
        except:
            print("Vui lòng nhập n >= 1")
        if n >= 1:
            break
    for i in range(n):
        list_number.append(int(input(f"Nhập vào giá trị thứ {i + 1}: ")))


def calculate_sum(list_number):
    pass

if __name__ == "__main__":
    nhap(n, list_number)