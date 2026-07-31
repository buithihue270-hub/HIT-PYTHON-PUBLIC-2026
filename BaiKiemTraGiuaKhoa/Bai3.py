def tim_vi_tri_tu(chuoi, tu_muc_tieu):
    danh_sach_tu = chuoi.split()
    ket_qua = []
    for vi_tri in range(len(danh_sach_tu)):
        if danh_sach_tu[vi_tri] == tu_muc_tieu:
            ket_qua.append(vi_tri)
    if len(ket_qua) == 0:
        return -1
    else:
        return ket_qua
chuoi = input("Nhập chuỗi:")
tu_muc_tieu = input("Nhập từ mục tiêu:")
ket_qua = tim_vi_tri_tu(chuoi, tu_muc_tieu)
print(ket_qua)