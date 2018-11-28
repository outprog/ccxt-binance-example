import ccxt, configparser

config = configparser.ConfigParser()
config.read('config.ini')

exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': config['BINANCE']['ApiKey'],
    'secret': config['BINANCE']['Secret'],
    'timeout': 50000,
    'enableRateLimit': True,
})

symbol = 'EOS/ETH'

### market

# markets = exchange.fetch_markets(symbol)
# print(markets)

orderbook = exchange.fetch_order_book(symbol, 5, {})
print('orderbook:', orderbook)
bid = orderbook['bids'][0]
ask = orderbook['asks'][0]
print('bids(highest):', bid[0], bid[1])
print('asks(lower):', ask[0], ask[1])

### user

balances = exchange.fetch_balance()
print(balances['ETH'])
print(balances['EOS'])
print(balances['ADA'])

# trades = exchange.fetch_my_trades(symbol)
# print(trades)

### exchange

amount = 50.0
price = orderbook['asks'][0][0]
order = exchange.create_limit_buy_order(symbol, amount, price, {})
print(order)

# orders = exchange.fetch_open_orders(symbol)
# print(orders)

# orders = exchange.fetch_closed_orders(symbol)
# print(orders)

# exchange.cancel_order(orders[0]['id'], symbol)