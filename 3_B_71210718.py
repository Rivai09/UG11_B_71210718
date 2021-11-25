
def sisip():
    input1 = (input("Masukkan kalimat awal :"))
    input2 = input("Masukkan kata untuk disisipkan :")
    input3 = int(input("Masukkan index :"))
    output = (input1[:input3]) + input2 +input1[input3:]
    print (output)





sisip()