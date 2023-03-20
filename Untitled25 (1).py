#!/usr/bin/env python
# coding: utf-8

# In[2]:


#NAMA = Muhammad Abidin
#NIM  = V3922032
#KELAS= TI E

def hitung_fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def hitung_kpk(a, b):
    kpk = max(a, b)
    while True:
        if kpk % a == 0 and kpk % b == 0:
            return kpk
        kpk += 1

def tampilkan_menu():
    print("Pilihan menu:")
    print("1. Hitung FPB")
    print("2. Hitung KPK")
    print("3. Keluar")

def main():
    while True:
        tampilkan_menu()
        pilihan = int(input("Masukkan pilihan Anda: "))

        if pilihan == 1:
            a = int(input("Masukkan bilangan pertama: "))
            b = int(input("Masukkan bilangan kedua: "))
            fpb = hitung_fpb(a, b)
            print("FPB dari", a, "dan", b, "adalah", fpb)

        elif pilihan == 2:
            a = int(input("Masukkan bilangan pertama: "))
            b = int(input("Masukkan bilangan kedua: "))
            kpk = hitung_kpk(a, b)
            print("KPK dari", a, "dan", b, "adalah", kpk)

        elif pilihan == 3:
            print("Terima kasih telah menggunakan program ini!")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == '__main__':
    main()


# In[ ]:




