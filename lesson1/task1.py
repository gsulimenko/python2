duration = int(input('Введите продолжительность в секундах: '))
seconds = 0
minutes = 0
hours = 0
days = 0

if duration // (60 * 60 * 24) > 0:
    days = duration // (60 * 60 * 24)
    duration = duration - (days * 60 * 60 * 24)
if duration // (60 * 60) > 0:
    hours = duration // (60 * 60)
    duration = duration - (hours * 60 * 60)
if duration // 60 > 0:
    minutes = duration // 60
    duration = duration - minutes * 60
if duration // 60 == 0:
    seconds = duration

print(f'{days} дней {hours} часов {minutes} мин {seconds} сек')
