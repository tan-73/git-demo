from PIL import Image
img = Image.open("stego.png")
pixels = img.load()

bits = ""
for y in range(img.height):
    for x in range(img.width):
        bits += str(pixels[x, y][0] & 1)

msg = ""
for i in range(0, len(bits), 8):
    msg += chr(int(bits[i:i+8], 2))
    if msg.endswith("#"):
        break

print("Hidden message:", msg[:-1])  # remove delimiter