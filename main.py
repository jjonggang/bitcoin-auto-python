import datetime

import pybithumb
import time

con_key = ""
sec_key = ""

bit = pybithumb.Bithumb(con_key, sec_key)


# balance = bit.get_balance("DOT")
# print(balance)

# 1. get_balance : 현재 잔고를 보여준다. 0번 index에 코인 개수 표시.

# for ticker in pybithumb.get_tickers() :
#     balance = bit.get_balance(ticker)
#     if balance[0]:
#         print(ticker, ":", balance[0])

# 2. 지정가매수(limit order), 시장가매수(market order)
# 최소주문수량/ 유효자릿수/ 호가단위 주의
# buy_limit_order, buy_market_order

# order = bit.buy_limit_order("BTC", 4000100, 0.001)
# order = bit.buy_market_order("BTC", 1)

# 3. 매수, 매도 호가 확인하기
# orderbook = bit.get_orderbook("BTC")
# orderbook['asks']

# krw = bit.get_balance("BTC")[2]
# krw = 500000 # 내 잔고 확인하기
# orderbook = bit.get_orderbook("BTC")
# asks = orderbook['asks']
# sell_price = asks[0]['price']
# unit = krw/sell_price
# print(unit)
#
# order = bit.buy_market_order("BTC", unit)
# print(order)

# 4. 매도하기
# sell_limit_order("BTC", price, unit)
# sell_market_order("BTC", unit)

# 5. 주문 취소
# cancel_order(order)

# df = bit.get_ohlc("BTC")
# get_ohlc("BTC")
# 0: 시가 1: 고가 2: 저가 3: 종가
# 변동성 돌파 전략
# 변동폭 = 전일 고가 - 전일 저가
# 매수타겟 = 전일종가 + 변동폭 * 0.5
# 매도타겟 = 당일 종가 매도



def get_yesterday_ma5(ticker):
    df = bit.get_candlestick(ticker)
    close = df['close']
    ma = close.rolling(window=5).mean()
    return ma[-2]


def get_target_price(ticker):
    price_arr = bit.get_ohlc(ticker)
    # print(price_arr['BTC'])
    today_open = price_arr[ticker][3]
    yest_high = price_arr[ticker][1]
    yest_low = price_arr[ticker][2]
    target = today_open + (yest_high - yest_low) * 0.5
    return target


def sell(ticker):
    unit = bit.get_balance(ticker)[0]
    order = bit.sell_market_order(ticker, unit)
    f.write("-------------------------------------------")
    f.write(f'{datetime.datetime.now()} {ticker}판매 성공!!\n {order}')
    f.write("-------------------------------------------")


def buy(ticker):
    krw = bit.get_balance(ticker)[2]
    orderbook = bit.get_orderbook(ticker)
    sell_price = orderbook['asks'][0]['price']
    unit = 100000 / float(sell_price)
    order = bit.buy_market_order(ticker, unit)
    f.write("-------------------------------------------")
    f.write(f'{datetime.datetime.now()} {ticker}구매 성공!!\n {order}')
    f.write(f'target price: {coin_dict[ticker][0]} ma5: {coin_dict[ticker][1]}')
    f.write("-------------------------------------------")


def ma5_set(coin_dict):
    for coin in coin_dict:
        coin_dict[coin][1] = get_yesterday_ma5(coin)

def target_set(coin_dict):
    for coin in coin_dict:
        coin_dict[coin][0] = get_target_price(coin)


f = open('./record.txt', 'w')

now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
# target_price = get_target_price("BTC")
coin_array = ["XEC", "FIT", "AMO", "OBSR", "TEMCO", "BASIC", "EL", "EGG", "QTCON", "WIKEN", "MIX", "TRV", "CKB", "COS", "MVC", "FLETA", "MAP", "BLY", "RSR", "APM", "ANW", "ADP", "GOM2", "LINA", "ATOLO"]
coin_dict = {"XEC":[0,0], "FIT":[0,0], "AMO":[0,0], "OBSR":[0,0], "TEMCO":[0,0], "BASIC":[0,0], "EL":[0,0], "EGG":[0,0], "QTCON":[0,0], "WIKEN":[0,0], "MIX":[0,0], "TRV":[0,0], "CKB":[0,0], "COS":[0,0], "MVC":[0,0], "FLETA":[0,0], "MAP":[0,0], "BLY":[0,0], "RSR":[0,0],"APM":[0,0], "ANW":[0,0], "ADP":[0,0], "GOM2":[0,0], "LINA":[0,0], "ATOLO":[0,0], "RINGX":[0,0], "IPX":[0,0], "TRX":[0,0], "ZIL":[0,0], "GHX":[0,0], "EVZ":[0,0], "VET":[0,0], "LOOM":[0,0], "XNO":[0,0], "ASM":[0,0], "BIOT":[0,0], "CYCLUB":[0,0], "CENNZ":[0,0], "DOGE":[0,0], "DAD":[0,0], "XYM":[0,0], "XLM":[0,0], "LF":[0,0], "CHZ":[0,0], "CTXC":[0,0], "SOFI":[0,0], "ORC":[0,0], "CRO":[0,0], "GRT":[0,0], "CHR":[0,0], "ANV":[0,0], "XRP":[0,0], "BORA":[0,0], "PUNDIX":[0,0], "BAT":[0,0], "KLAY":[0,0], "MLK":[0,0], "ADA":[0,0], "ALGO":[0,0], "HIVE":[0,0], "UOS":[0,0], "GXC":[0,0], "MATIC":[0,0], "ENJ":[0,0], "EOS":[0,0], "MANA":[0,0], "XTZ":[0,0], "SAND":[0,0], "WEMIX":[0,0], "ALICE":[0,0], "XVS":[0,0], "LINK":[0,0], "ATOM":[0,0], "DOT":[0,0], "ETC":[0,0]}
buy_array = []

ma5_set(coin_dict)
target_set(coin_dict)





while True:
    for coin in coin_dict:
        if coin in buy_array:
            continue
        now = datetime.datetime.now()
        print(now)
        if mid < now < mid + datetime.delta(seconds=10):
            now = datetime.datetime.now()
            mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
            ma5_set(coin_dict)
            target_set(coin_dict)
            for coinbuy in buy_array:
                sell(coinbuy)
        target_price = coin_dict[coin][0]
        print(coin, "목표가", target_price)
        ma5 = coin_dict[coin][1]
        print(coin, "ma5", ma5)
        current_price = bit.get_current_price(coin)
        print(coin, "현재가", current_price)
        if current_price > target_price and current_price > ma5:
            buy(coin)
            buy_array.append(coin)
        print()
