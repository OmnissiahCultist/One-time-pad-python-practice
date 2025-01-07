import secrets


plaintext = str('abc')
#Takes in the initial plaintext and ensures it is a string
print(plaintext, '= plaintext\n') #DEBUG DEBUG DEBUG

key_vals = [format(int(secrets.randbelow(128)), '07b') for char in plaintext]
#Key generation
#For each character in input, it produces a random 8bit based integer (from 0-127 for ASCII chars)
#Then generates the 7bit value for that integer (minus prefixes)
print(key_vals, '= key_vals\n') #DEBUG DEBUG DEBUG

ascii_vals = [format(ord(char), '07b') for char in plaintext]
#Produces ASCII values for each character in the string
#Then produces 7bit value for ASCII integer (minus prefixes)
print(ascii_vals, '= ascii_vals\n') #DEBUG DEBUG DEBUG

key_list = ''.join(key_vals)
ascii_list = ''.join(ascii_vals)
#Combines the list values created previously (for comparison)
print(key_list, ascii_list, '= key_list and ascii_list\n') #DEBUG DEBUG DEBUG

XOR_list = ''
#Starts the new string of values created by XOR statement below

if len(key_list) == len(ascii_list):
    for index in range(len(key_list)):
        if key_list[index] == ascii_list[index]:
            XOR_list += '0'
        else:
            XOR_list += '1'
else:
    raise ValueError('String length mismatch: key and ascii')
#Adds the values to the XOR list, this will be transformed into cypher text
print(XOR_list, '= XOR_list\n')#DEBUG DEBUG DEBUG

XOR_byte_list = [XOR_list[index:index+7] for index in range(0, len(XOR_list), 7)]
print(XOR_byte_list, '= XOR_byte_list\n')#DEBUG DEBUG DEBUG
if len(''.join(XOR_byte_list)) != len(XOR_list):
    raise ValueError('String length mismatch: XOR bytes bit count current != XOR total bit count prior')
#Seperates the values into bytes to convert from byte > int(ASCII) > char equivalent

cypher_str = ''
for byte in XOR_byte_list:
    cypher_str += chr(int(byte, 2))
print(cypher_str, '= full cypher text\n')#DEBUG DEBUG DEBUG
#Converts to cypher text and produces the final string

print(f'The plaintext "{plaintext}" is converted to "{cypher_str}" using the key "{key_list}".')
