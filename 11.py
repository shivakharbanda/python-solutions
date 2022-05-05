from pyfiglet import Figlet
import sys
from random import choice


figlet = Figlet()

try:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        font = sys.argv[2]
    else:
        sys.exit("Invalid usage1")

except IndexError:
    pass

font_list = figlet.getFonts()

try:
    f = font
except NameError:
    f = choice(font_list)

if f in font_list:
    figlet.setFont(font=f)
else:
    print(f)
    sys.exit("invalid usage")



string = input("Input:")

print(figlet.renderText(string))
