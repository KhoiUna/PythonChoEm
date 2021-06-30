ten = input("Bạn tên gì? ")
so_luong = int(input("Bạn mua bao nhiêu quyển? "))

tien = 15000
tong = tien * so_luong

print("\nQuý khách ", ten.upper(), " mua ", so_luong, " quyển với tổng số tiền: ", tong, "VND", sep="")

if tong > 200000:
    print("\nChúc mừng! Quý khách được giảm giá. Tổng tiền: ", tong - 20000, "VND", sep="")
else:
    print("\nQuý khách không được giảm giá.")