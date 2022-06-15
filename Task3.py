with open('RLE_decoded.txt', 'r') as data:
    my_text = data.read()

def encode_rle(ss):
    str_code = ''
    prev_char = ss[0]
    count = 0
    for i in range(len(ss)):
        # print(ss[i])
        
        if prev_char == ss[i]:
            count +=1
            # print(count)
        else:

            str_code +=str(count)+prev_char
            prev_char = ss[i]
            count=1
    str_code +=str(count)+prev_char       
    
    return str_code

            
str_code = encode_rle(my_text)

print(my_text)
print(str_code)
with open('RLE_encoded.txt', 'w') as data:
     my_text2 = data.write(str_code)

with open('RLE_encoded.txt', 'r') as data:
    my_text2 = data.read()

def decoding_rle(ss:str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char 
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

str_decode = decoding_rle(my_text2)
with open('RLE_encoded_prov.txt', 'w') as data:
     my_text2 = data.write(str_decode)
print(str_decode)