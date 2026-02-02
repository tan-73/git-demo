from PIL import Image 
 
img = Image.open("cat.jpg").convert("RGB") 
pixels = img.load() 
 
message = input("Enter the message to be hidden: ") 
msg = message + "#"   # delimiter 
 
bits = ''.join(format(ord(c), '08b') for c in msg) 
 
max_bits = img.width * img.height 
if len(bits) > max_bits: 
    raise ValueError("Message too long for this image") 
 
i = 0 
for y in range(img.height): 
    for x in range(img.width): 
        if i < len(bits): 
            r, g, b = pixels[x, y] 
            r = (r & ~1) | int(bits[i])   # modify LSB of red channel 
            pixels[x, y] = (r, g, b) 
            i += 1 
        else: 
        
            break 
 
img.save("stego.png") 
print("Message hidden successfully!") 