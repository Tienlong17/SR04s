import PCA_library
def xuat_ra_man_hinh(a):
    print('a = ',a)
    if a == 1 :
        PCA_library.main()
    if a == 2 :
        PCA_library.servo0.angle = 120
    if a == 3 :
        PCA_library.servo0.angle = 40
    if a == 4 :
        PCA_library.servo0.angle = 180