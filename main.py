from bot import Bot
import sys

if __name__ == '__main__':
    forms_n = int(sys.argv[1])
    adress = ""
    with open("form_adress.txt", "r") as f:
        adress = f.read()
    
    bot = Bot(adress, forms_n)
    bot.fill_forms()