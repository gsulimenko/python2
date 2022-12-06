percent = int(input('Введите число процентов: '))

if (percent % 10 == 1) or (percent == 1):
    word = 'процент'
elif 1 < percent <= 4:
    word = 'процента'
elif (12 <= percent <= 14) or (12 <= percent % 100 <= 14):
    word = 'процентов'
elif (1 < percent % 10 <= 4):
    word = 'процента'
else:
    word = 'процентов'

print(percent, word)