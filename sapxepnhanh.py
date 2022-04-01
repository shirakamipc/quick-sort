import random

def san_sinh_so_ngau_nhien(n):
    mang=[]
    for i in range(n):
        so_ngau_nhien = random.randint(0,100)
        mang.append(so_ngau_nhien)

    return mang

def phan_vung(mang, duoi, tren):
    i = duoi - 1 # chi muc cua phan tu nho hon moc
    moc = mang[tren] # pivot
    # Dua lan luot cac phan tu nho hon moc ve tren
    for j in range(duoi, tren):
        if mang[j] < moc:
            i += 1
            mang[i], mang[j] = mang[j], mang[i]
        #End if 
    #End for   
    
    mang[i + 1], mang[tren] = mang[tren], mang[i+1]
    return i + 1

#End def

def sap_xep_nhanh(mang, duoi, tren):
    if duoi < tren:
        vitri = phan_vung(mang, duoi, tren)
        sap_xep_nhanh(mang, duoi, vitri - 1)
        sap_xep_nhanh(mang, vitri + 1, tren)
    #End if 
#End def

def main():
    mang = san_sinh_so_ngau_nhien(10)
    print("Mang ban dau la: \n", mang)
    sap_xep_nhanh(mang, 0, len(mang) - 1)
    print("Mang sau khi sap xep la: \n", mang)
#End def

if __name__ == '__main__':
    main()     
        
    