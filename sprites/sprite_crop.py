from PIL import Image
# from os import mkdir

# mkdir("sprites/character/choice1/death")
sheet = Image.open("sprites/character/choice1/death/death.png")
count = 0

for x in range(6):
    for y in range(3):
        a = (x + 1) * 80
        b = (y + 1) * 80
        icon = sheet.crop((a - 80, b - 80, a, b))  # Problem here
        icon.save("sprites/character/choice1/death/{}.png".format(count))
        count += 1