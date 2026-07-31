def tinh_tien_thua(gia, tien_khach_dua):
    tien_thua = tien_khach_dua - gia
    menh_gia = [20, 10, 5, 2, 1]
    tong_so_to = 0
    for mg in menh_gia:
        so_to = tien_thua // mg
        if so_to > 0:
            print(f"{so_to} tờ {mg} nghìn đồng")
            tong_so_to += so_to
            tien_thua = tien_thua % mg
    return tong_so_to
gia = int(input("Nhập giá tiền:"))
tien_khach_dua = int(input("Nhập tiền khách đưa:"))
ket_qua = tinh_tien_thua(gia, tien_khach_dua)
print("Tổng số tờ tiền thừa:", ket_qua)