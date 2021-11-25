def check_data_type(data , type) :
    if data == str and type == str :
        print ("Jawaban anda benar")
        print ("True")
        
        
    elif data == int and type == str :
         print ("Jawaban Anda salah, seharusnya adalah :", "int")
         print ("False")
         return data

    elif data == int and type == int :
         print ("Jawaban Anda salah, seharusnya adalah :", "str")
         print ("False")
         return data


check_data_type(str , str)
check_data_type(str , str)
check_data_type(int , str)
check_data_type(int , int)
check_data_type(str , str)

print(check_data_type("Kevin","STr"))
print(check_data_type("Kevin","str"))
print(check_data_type(12345,"str"))
print(check_data_type("9347","int"))
print(check_data_type(9876,"int"))
