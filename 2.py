def binary_to_decimal(binary_number):
    decimal_number = 0
    power = 0
    for digit in reversed(binary_number):
        decimal_number += int(digit) * (2 ** power)
        power += 1
    return decimal_number

binary_number = input("Enter the binary number :")
decimal_number = binary_to_decimal(binary_number)
print("Decimal number :" ,decimal_number)
