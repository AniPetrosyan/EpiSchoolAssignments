#Task 1: convert a decimal number to hexidecimal

def to_hex(dec):
    digits = "0123456789ABCDEF"
    x = (dec % 16)
    rest = dec // 16
    if (rest == 0):
        return digits[x]
    return to_hex(rest) + digits[x]

#print(to_hex(255))



#Task 2: function takes numbers from 0 to 255 for the amounts of red, green, and blue light that make up a color, and return the corresponding hex code

def hex_color(red,green,blue):
    temp = '#'
    for item in [red,green,blue]:
        if item < 0:
            item = 0
        elif item > 255:
            item = 255
        temp += str(to_hex(item)).replace('0x','').upper().zfill(2)
    return temp

print(hex_color(10,32,255))