from bot import Bot

if __name__ == '__main__':
    adress = 'https://forms.gle/MkX1C5WE4R3qSh6F6'
    bot = Bot(adress, 2)
    bot.fill_forms()