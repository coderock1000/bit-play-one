def find_rightmost_set_bit_position(num):
    if num == 0:
        return "No set bits found" 

    position = 1  
    while (num & 1) == 0:
        num >>= 1 
        position += 1

    return position

num = int(input("Enter a number: "))
print("The position of the rightmost set bit is:", find_rightmost_set_bit_position(num))
