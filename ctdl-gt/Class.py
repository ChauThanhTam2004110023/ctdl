class Class:
    def __init__(self, tenHang, giaNhap, soLuong, ngayNhap):
        self.tenHang = tenHang
        self.giaNhap = giaNhap
        self.soLuong = soLuong
        self.ngayNhap = ngayNhap
        self.next = None
        self.gia_tri = None

    def show_info(self):
        # print("Tên: ", self.tenHang)
        # print("Giá nhập: ", self.giaNhap)
        # print("Số lượng: ", self.soLuong)
        print('Tên: {}| giá nhập: {}| số lượng:  {}| ngày nhập: {}' .format(self.tenHang.center(15), self.giaNhap.center(20), self.soLuong.center(10), self.ngayNhap.center(20)))
