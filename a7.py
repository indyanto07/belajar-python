# def fungsi(a, b):
#     if  a < b:
#         return a
#     elif b < a:
#         return b
#     elif a == b:
#         return a
    
# print(fungsi(10, 5))
def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info
 
print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))
