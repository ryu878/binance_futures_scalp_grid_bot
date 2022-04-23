from binance.client import Client
import config_xrp
import time
import ta
import pandas as pd
import numpy as np
from datetime import datetime


config = config_xrp
api_key = config.key
api_secret = config.secret
symbol = config.symbol
asset = config.asset
max_size = config.max_size
max_leverage = config.max_leverage
short_tp_static_deduct = config.short_tp_static_deduct

decimals = 0

if symbol == 'DOGEBUSD':
    decimals = 5
elif symbol == 'XRPBUSD':
    decimals = 4  
elif symbol == 'FTTBUSD':
    decimals = 3
elif symbol == 'BNBBUSD' or symbol == 'ETHBUSD' or symbol == 'SOLBUSD':    
    decimals = 2
elif symbol == 'BTCBUSD':    
    decimals = 1    
else:
    print('Wrong Symbol in Config')    

q0 = config.q0
q1 = config.q1
q2 = config.q2
q3 = config.q3
q4 = config.q4
q5 = config.q5

atr_mult1 = config.atr_mult1
atr_mult2 = config.atr_mult2
atr_mult3 = config.atr_mult3
atr_mult4 = config.atr_mult4
atr_mult5 = config.atr_mult5

mult1 = config.mult1
mult2 = config.mult2
mult3 = config.mult3
mult4 = config.mult4
mult5 = config.mult5

minD_mult = config.minD_mult
minYG_mult = config.minYG_mult

max_leverage = config.max_leverage

client = Client(api_key, api_secret)

def getOrderBook():
    global ask
    global bid
    orderBook = client.futures_order_book(symbol=symbol)
    bid = orderBook['bids'][0][0]
    ask = orderBook['asks'][0][0]
    #print(bid, ask)

def mybusdBalance():
    global balance
    getBusdBalance = client.futures_account_balance()
    balance = getBusdBalance[9]['balance']
    #print(balance)

def getMyPosition():
    global positionAmount
    global positionEntryPrice
    global positionLiqPrice
    global positionUnRealizedProfit
    myPosition = client.futures_position_information(symbol=symbol)
    positionAmount = myPosition[0]['positionAmt']
    positionEntryPrice = myPosition[0]['entryPrice']
    positionLiqPrice = myPosition[0]['liquidationPrice']
    positionUnRealizedProfit = myPosition[0]['unRealizedProfit']
    #print(positionAmount,positionUnRealizedProfit,positionEntryPrice,positionLiqPrice)
    #print(myPosition)

def getLimitEntryOrders(symbol):
    global leorders
    leorders = client.futures_get_open_orders(symbol=symbol)
    for order in leorders:
        if order['status'] == "NEW" and order['reduceOnly'] == False:
            print('Limit Entry Found', order['orderId'])
        else:
            pass
            print('No Limit Entry Orders Found')

def getLimitCloseOrders(symbol):
    global lcorders
    lcorders = client.futures_get_open_orders(symbol=symbol)
    for order in lcorders:
        if order['status'] == "NEW" and order['reduceOnly'] == True:
            print('Limit Close Entry Found', order['orderId'])
        else:
            pass
            print('No Close Orders Found')

def get_6ema():
    bars = client.futures_klines(symbol=symbol,interval='1m', limit=18)
    df = pd.DataFrame(bars, columns=['Time','Open','High','Low','Close','Vol','1','2','3','4','5','6'])
    df['EMA 6 High'] = ta.trend.EMAIndicator(df['High'], window=6).ema_indicator()
    df['EMA 6 Low'] = ta.trend.EMAIndicator(df['Low'], window=6).ema_indicator()
    global ema6high
    global ema6low
    ema6high = float(df['EMA 6 High'][17])
    ema6low = float(df['EMA 6 Low'][17])

def get_60ema():
    bars = client.futures_klines(symbol=symbol,interval='1m', limit=180)
    df = pd.DataFrame(bars, columns=['Time','Open','High','Low','Close','Vol','1','2','3','4','5','6'])
    df['EMA 60 Close'] = ta.trend.EMAIndicator(df['Close'], window=60).ema_indicator()
    global ema60
    ema60 = (df['EMA 60 Close'][179]).astype(float)

def get_120ema():
    bars = client.futures_klines(symbol=symbol,interval='1m', limit=360)
    df = pd.DataFrame(bars, columns=['Time','Open','High','Low','Close','Vol','1','2','3','4','5','6'])
    df['EMA 120 Close'] = ta.trend.EMAIndicator(df['Close'], window=120).ema_indicator()
    global ema120
    ema120 = (df['EMA 120 Close'][359]).astype(float)

def get_240ema():
    bars = client.futures_klines(symbol=symbol,interval='1m', limit=720)
    df = pd.DataFrame(bars, columns=['Time','Open','High','Low','Close','Vol','1','2','3','4','5','6'])
    df['EMA 240 Close'] = ta.trend.EMAIndicator(df['Close'], window=240).ema_indicator()
    global ema240
    ema240 = (df['EMA 240 Close'][719]).astype(float)

x = 1
while True:

    try:
        getLimitEntryOrders(symbol)
    except:
        print('Get Position Failed!')
    try:
        getLimitCloseOrders(symbol)
    except:
        print('Get Close orders Failed!')    
    
    get_6ema()
    get_60ema()
    get_120ema()
    get_240ema()

    real_6ema_high = round(ema6high,decimals)
    real_6ema_low = round(ema6low,decimals)
    real_60ema = round(ema60,decimals)
    real_120ema = round(ema120,decimals)
    real_240ema = round(ema240,decimals)
    # print('EMA 6 High', real_6ema_high)
    # print('EMA 6 Low', real_6ema_high)
    # print('EMA 60 Close', real_60ema)
    # print('EMA 120 Close', real_120ema)
    # print('EMA 240 Close', real_240ema)

    ema6hilo_distance = real_6ema_high - real_6ema_low
    real_ema6hilo_distance = round(ema6hilo_distance,decimals)
    
    ema6up = round(real_6ema_high + (real_ema6hilo_distance * mult3),decimals)
    ema6dn = round(real_6ema_low - (real_ema6hilo_distance * mult3),decimals)
    # print('EMA6 up',ema6up)
    # print('EMA6 dn',ema6dn)

    atr_bars = client.futures_klines(symbol=symbol,interval='1m', limit=720)
    df = pd.DataFrame(atr_bars, columns=['Time','Open','High','Low','Close','Vol','1','2','3','4','5','6'], dtype=np.single)
    df['ATR 240'] = ta.volatility.AverageTrueRange(df['High'], df['Low'], df['Close'], window=240).average_true_range()
    atr240 = float(df['ATR 240'][719])
    real_atr = round(atr240,decimals)
    # print('ATR',real_atr)

    getOrderBook()
    # print('Ask', ask)

    # If ATR calculations    
    short1 = round(float(ask) + (real_atr * 2),decimals) 
    short2 = round(float(ask) + (real_atr * 4),decimals) 
    short3 = round(float(ask) + (real_atr * 7),decimals) 
    short4 = round(float(ask) + (real_atr * 10),decimals) 
    short5 = round(float(ask) + (real_atr * 15),decimals)

    # print(short1)
    # print(short2)
    # print(short3)
    # print(short4)
    # print(short5)

    # If EMA60 - EMA 120 calculations
    ema_distance = real_60ema - real_240ema
    abs_ema_distance = abs(ema_distance)
    real_ema_distance = round(abs_ema_distance,decimals)
    # print('Ema6 dist', real_ema_distance)

    short_emad_1 = round(float(ask) + (real_ema_distance),decimals) 
    short_emad_2 = round(float(ask) + (real_ema_distance * 2),decimals) 
    short_emad_3 = round(float(ask) + (real_ema_distance * 3),decimals) 
    short_emad_4 = round(float(ask) + (real_ema_distance * 4),decimals) 
    short_emad_5 = round(float(ask) + (real_ema_distance * 5),decimals)

    # print(short_emad_1)
    # print(short_emad_2)
    # print(short_emad_3)
    # print(short_emad_4)
    # print(short_emad_5)

    long_trend = real_240ema < real_120ema and real_120ema < real_60ema and real_60ema > real_120ema and (real_60ema - real_120ema) > real_atr
    shrt_trend = real_240ema > real_120ema and real_120ema > real_60ema and real_60ema < real_120ema and (real_120ema - real_60ema) > real_atr

    ema_dist_shrt = ema6dn > real_60ema
    ema_dist_long = ema6up < real_60ema
    
    # time.sleep(333)

    getMyPosition()

    real_pos_size = abs(float(positionAmount))
    # print('Position size', real_pos_size)

    get_BUSD_balance = client.futures_account_balance()
    balance = get_BUSD_balance[9]['balance']
    calc_leverage = float(positionAmount) * 100 / (float(balance) * float(max_leverage)) * 100 / float(balance)
    # print('Balance BUSD', balance)
    # print('Current Leverage', calc_leverage)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    if float(positionAmount) < 0:
        print('Short Position Found', positionAmount)
        print('Current leverage:', abs(round(calc_leverage,2)),'x')        
    if float(positionAmount) > 0:
        print('Long Position Found', positionAmount)
        print('Current leverage:', abs(round(calc_leverage,2)),'x')
    else:
        pass     

    print('--💰-bȝstt--',symbol,'--',current_time)

    if float(ask) < real_6ema_high:
        print('1. Ask < EMA6 High')
    else:
        print('1. 🗹 Ask > EMA6 High')

    if long_trend == True:
        print('2. 🗹 Trend is Long ↑↑↑')
    elif shrt_trend == True:
        print('2. 🗹 Trend is Short ↓↓↓')
    elif shrt_trend != True and long_trend != True:
        print('2. Trend is Mixed ↺')
    else:
        pass

    if ema_dist_shrt == True:
        print('3. 🗹 Shftd Short')
    elif ema_dist_long:
        print('3. 🗹 Shftd Long')
    else:
        print('3. Shftd NoGood')   

    closePosQ = abs(float(positionAmount))
    # print('Close position Qty', closePosQ)

    short_tp_static = float(positionEntryPrice) - short_tp_static_deduct
    short_tp_static2 = float(positionEntryPrice) - real_atr

    lcorders = client.futures_get_open_orders(symbol=symbol)

    ### SHORT TP Block ###

    for order in lcorders:
        if order['status'] == "NEW" and order['reduceOnly'] == True and float(order['origQty']) < real_pos_size: # SHORT & LONG Cancel Close Order if size is different 
            try:
                #print('Limit Close Entry Found', order['orderId'])
                client.futures_cancel_order(symbol=symbol,orderId=order['orderId'])
                # print('Limit Close Entry Closed')
            except:
                pass
                # print('Something wrong with canceling Limit Entries')     
        else:
            pass
            # print('No Close Orders Found')  

    if real_pos_size != 0.0 and float(bid) > float(positionEntryPrice): # SHORT Take Profit at STATIC
        try:
            # print ('Placing Close BUY Order at Small Static Distance', round(short_tp_static,decimals))
            client.futures_create_order(side='BUY',price=round(short_tp_static,decimals),quantity=closePosQ,type='LIMIT',symbol=symbol,timeInForce='GTX',reduceOnly=True)
        except:
            pass
            # print('Something wrong with limit Close order')
    
    elif real_pos_size != 0.0 and float(bid) > float(positionEntryPrice) and real_pos_size > q2: # SHORT Take Profit at SMALL STATIC
        try:
            # print ('Placing Close BUY Order at Small Static Distance', round(short_tp_static,decimals))
            client.futures_create_order(side='BUY',price=round(short_tp_static2,decimals),quantity=closePosQ,type='LIMIT',symbol=symbol,timeInForce='GTX',reduceOnly=True)
        except:
            pass
            # print('Something wrong with limit Close order')
    
    elif real_pos_size != 0.0 and float(bid) < float(positionEntryPrice): # SHORT Take Profit at BID
        try:
            # print ('Placing Close BUY Order at BID')
            client.futures_create_order(side='BUY',price=bid,quantity=closePosQ,type='LIMIT',symbol=symbol,timeInForce='GTX',reduceOnly=True)
        except:
            pass
            # print('Something wrong with limit Close order')
    else:
        pass 
    
    # Pending Orders Block

    getMyPosition()

    for order in lcorders:
        if real_pos_size == 0.0 and order['status'] == "NEW" and order['reduceOnly'] == False and order['side'] == "SELL": # SHORT Cancel Pending Orders     
            try:
                client.futures_cancel_all_open_orders(symbol=symbol)
                #client.futures_cancel_order(symbol=symbol,orderId=order['orderId'])               
                # print('Removing pending order because price is lower EMA 6 High')
            except:
                pass
            # print('Something wrong with limit entry order(s)')
    
### SHORT Pending Orders if Trend is LONG ###
    '''
    if real_pos_size == 0.0 and float(ask) > real_6ema_high and long_trend == True and ema_dist_shrt == True: # SHORT pending order With Trend
        try:
            print('Placing Entry Order(s)...')
            client.futures_create_order(side='SELL',price=ask,quantity=q0,type='LIMIT',symbol=symbol,timeInForce='GTX')
            client.futures_create_order(side='SELL',price=short_emad_1,quantity=q1,type='LIMIT',symbol=symbol,timeInForce='GTX')
            client.futures_create_order(side='SELL',price=short_emad_2,quantity=q2,type='LIMIT',symbol=symbol,timeInForce='GTX')
            client.futures_create_order(side='SELL',price=short_emad_3,quantity=q3,type='LIMIT',symbol=symbol,timeInForce='GTX')
            client.futures_create_order(side='SELL',price=short_emad_4,quantity=q4,type='LIMIT',symbol=symbol,timeInForce='GTX')
            client.futures_create_order(side='SELL',price=short_emad_5,quantity=q5,type='LIMIT',symbol=symbol,timeInForce='GTX')
        except:
            pass
    '''
    if real_pos_size == 0.0 and float(ask) > real_6ema_high: # SHORT pending order Whithout Trend      
        try:
            print('Placing Entry Order(s)...')
            client.futures_create_order(side='SELL',price=ask,quantity=q0,type='LIMIT',symbol=symbol,timeInForce='GTX')
            client.futures_create_order(side='SELL',price=short1,quantity=q1,type='LIMIT',symbol=symbol,timeInForce='GTX')
            client.futures_create_order(side='SELL',price=short2,quantity=q2,type='LIMIT',symbol=symbol,timeInForce='GTX')
            client.futures_create_order(side='SELL',price=short3,quantity=q3,type='LIMIT',symbol=symbol,timeInForce='GTX')
            client.futures_create_order(side='SELL',price=short4,quantity=q4,type='LIMIT',symbol=symbol,timeInForce='GTX')
            client.futures_create_order(side='SELL',price=short5,quantity=q5,type='LIMIT',symbol=symbol,timeInForce='GTX')
        except:
            pass