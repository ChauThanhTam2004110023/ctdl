from Class import *

class Method:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def them_hang(self):
        tenHang = input('Tên hàng: ')
        giaNhap = input("Giá nhập: ")
        soLuong = input("số lượng: ")
        ngayNhap = input('ngày nhập: ')
        return Class(tenHang, giaNhap, soLuong, ngayNhap)

    def add(self):
        ds = self.them_hang()
        if self.head == None:
            self.head = ds
            self.tail = ds
        else:
            self.tail.next = ds
            self.tail = ds

    def in_ds(self):
        ds = self.head
        if self.head == None:
            print("ko tìm thấy.")
            return
        while(ds != None):
            ds.show_info()
            ds = ds.next
        return ds

    def addHead(self, chi_muc):
        ds = self.them_hang()
        truoc = None
        hien_tai = self.head
        i = 0
        while i < chi_muc and hien_tai != None:
            i = i + 1
            truoc = hien_tai
            hien_tai = hien_tai.next
        if truoc == None:
            ds.next = self.head
            self.head = ds
            if self.tail == None:
                self.tail = ds

    def search(self, tenHang):
        tenHang = input("Enter name find: ")
        hien_tai = self.head
        vi_tri = 0
        while hien_tai != None and hien_tai.tenHang != tenHang:
            if self.head != len(tenHang):
                hien_tai = hien_tai.next
                vi_tri = vi_tri + 1
        if hien_tai == None:
            return print("ko tìm thấy.")
        else:
            print(vi_tri)
            return print(hien_tai.show_info())



    def xoa(self, tenHang):
        tenHang = input("enter remove name: ")
        hien_tai = self.head
        truoc = None
        while hien_tai != None and hien_tai.tenHang != tenHang:
            truoc = hien_tai
            hien_tai = hien_tai.next
        if hien_tai != None:
            # tìm thấy
            if hien_tai == self.head and hien_tai == self.tail:
                # xóa phần tử duy nhất
                self.head = self.tail = None
            elif hien_tai == self.head:
                # xóa phần tử đầu ko duy nhât
                self.head = self.head.next
            elif hien_tai == self.tail:
                # xóa đuôi
                truoc.next = None
                self.tail = truoc
            else:
                # ở giữa
                truoc.next = hien_tai.next
        del hien_tai


    def xoa_het(self):
        hien_tai = self.head
        self.head = self.tail = None
        while hien_tai != None:
            tam = hien_tai
            hien_tai = hien_tai.next
            if hien_tai != None:
                print("Đã xóa hết tất cả.")
            del tam
        

            



        
            
    

        
        
    
