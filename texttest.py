coin_array = {"XEC":[0,0], "FIT":[0,0], "AMO":[0,0], "BTT":[0,0], "HIBS":[0,0], "TMTG":[0,0], "OBSR":[0,0], "TEMCO":[0,0], "BASIC":[0,0], "MBL":[0,0], "EL":[0,0], "EGG":[0,0], "QTCON":[0,0]}

for coin in coin_array:
    coin_array[coin][0] = 3
    coin_array[coin][1] = 5

print(coin_array)

for coin in coin_array:
    print(coin_array[coin][0])

print(coin_array)