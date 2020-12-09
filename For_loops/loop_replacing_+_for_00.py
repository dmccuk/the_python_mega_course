phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for number in phone_numbers.values():
    number = number.replace('+', '00')
    print(number)