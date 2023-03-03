

# class test:
#     def __init__(self, dataval=None):
#         self.dataval = dataval
#         self.nextval = None
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.headval = None

#     def listprint(self):
#         printval = self.headval
#         while printval is not None:
#             print(printval.dataval)
#             printval = printval.nextval

#     # chèn đầu
#     def etfirstly(self, newnode):
#         NewNode = test(newnode)
#         NewNode.nextval = self.headval
#         self.headval = NewNode


#     # chèn cuối
#     def AtEnd(self, newdata):
#         NewNode = test(newdata)
#         if self.headval is None:
#             self.headval = NewNode
#             return
#         laste = self.headval
#         while(laste.nextval):
#             laste = laste.nextval
#         laste.nextval=NewNode


# list_1 = LinkedList()
# list_1.headval = test("Mon")
# e2 = test('tue')
# e3 = test('wed')
# e4 = test('hame')
# # nút thứ nhất liên kết vs nút thứ 2 (0-1)
# list_1.headval.nextval = e2
# # nút thứ hai liên kết vs nút thứ 3 (1-2)
# e2.nextval = e3
# # nút thứ 3 liên kết vs nút thứ 4 (2-3)
# e3.nextval = e4

# list_1.AtEnd('the')
# list_1.etfirstly('seo')
# list_1.listprint()


from Method import *

ds = Method()

print('''
0. Thoát
1. Thêm hàng
2. Thêm đầu danh sách
3. Tìm hàng
4. Xóa hàng
5. Xóa tất cả hàng trong danh sách 
6. Hiển thị danh sách
''')


class test:
    def main():
        a = 'QUẢN LÝ KHO HÀNG'
        b = a.center(20, "*")
        print(b)

    def themHang():
        while True:
            a = input('Them hang (y/n): ')
            if a == "y":
                ds.add()
                ds.in_ds()
            elif a == "n":
                break

    def xuat_ds():
        ds.in_ds()
    
    def them_dau_ds():
        ds.addHead(chi_muc=0)
        ds.in_ds()

    def tim():
        ds.search(tenHang='tenHang')

    def remove():
        ds.xoa(tenHang='tenHang')
        ds.in_ds()

    def removefull():
        ds.xoa_het()
        ds.in_ds()
        
    if __name__ == '__main__':
        while True:
            main()
            select = input("")
            if select == "1":
                themHang()
            elif select == "2":
                them_dau_ds()
            elif select == "3":
                tim()
            elif select == "4":
                remove()
            elif select == "5":
                removefull()
            elif select == "6":
                xuat_ds()
            elif select == "0":
                break
        