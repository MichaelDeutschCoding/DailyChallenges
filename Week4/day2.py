from datetime import date
current = int(date.today().strftime("%Y"))

birth_year = int(input("What year were you born? "))

num_candles = int(str(current - birth_year)[-1])
candles = 'i' * num_candles
candle_row = candles.center(13, '_')

print()
print(candle_row.center(20))
print('|:H:A:P:P:Y:|'.center(20))
print(' __|___________|__ ')
print('|^^^^^^^^^^^^^^^^^|')
print('|:B:i:r:t:h:d:a:y:|')
print('|                 |')
print('~' * 20)
