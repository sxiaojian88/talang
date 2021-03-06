import talang.data.quote.quote_tickers as tickers_api
from talang.util.model.Symbol import Symbol
from talang.util.model.Symbol import Symbols
import talang.util.util_data as ut


class QuoteSymbols:

    def get_all_symbols(self, exchange, usdt_value_limit=0):
        sybs = Symbols()
        if ut.okex_exchange.lower() == exchange.lower():
            ex_qt = tickers_api.QuoteTickers()
            tks = ex_qt.get_tikers_value(exchange, usdt_value_limit)
            for ticker in tks.Tickers_list:
                syb = Symbol()
                syb.symbol = ticker.Symbol
                syb.exchange = exchange
                syb.time = ticker.Time
                syb.base_coin = ut.get_base_coin(exchange,ticker.Symbol)
                syb.quote_coin = ut.get_quote_coin(exchange,ticker.Symbol)
                sybs.add_symbol(syb)
        else:
            print('no support exchange')

        return sybs

    def get_basecoinsymbols_by_quote_coin(self, exchange, quote_coin, usdt_value_limit=0):
        sybs= Symbols()
        if ut.okex_exchange.lower() == exchange.lower():
            ex_qt = tickers_api.QuoteTickers()
            tks = ex_qt.get_tikers_value(exchange, usdt_value_limit)
            for ticker in tks.Tickers_list:
                syb = Symbol()
                syb.symbol = ticker.Symbol
                syb.exchange = exchange
                syb.time = ticker.Time
                syb.base_coin = ut.get_base_coin(exchange, ticker.Symbol)
                syb.quote_coin = ut.get_quote_coin(exchange, ticker.Symbol)
                if str.lower(quote_coin) == syb.quote_coin.lower():
                    sybs.add_symbol(syb)
        return sybs

    def get_samebasecoin_of_diff_quote_coin(self, exchange, quote_coin_a, quote_coin_b, usdt_value_limit=0):
        same_basecoin = []
        sybs_a = Symbols()
        sybs_b = Symbols()
        if ut.okex_exchange.lower() == exchange.lower():
            ex_qt = tickers_api.QuoteTickers()
            tks = ex_qt.get_tikers_value(exchange, usdt_value_limit)
            for ticker in tks.Tickers_list:
                syb = Symbol()
                syb.symbol = ticker.Symbol
                syb.exchange = exchange
                syb.time = ticker.Time
                syb.base_coin = ut.get_base_coin(exchange, ticker.Symbol)
                syb.quote_coin = ut.get_quote_coin(exchange, ticker.Symbol)
                if str.lower(quote_coin_a) == syb.quote_coin.lower():
                    sybs_a.add_symbol(syb)
                if str.lower(quote_coin_b) == syb.quote_coin.lower():
                    sybs_b.add_symbol(syb)

        #sybs_a.print_detail()
        #sybs_b.print_detail()

        for syb_a in sybs_a.symbols_list:
            for syb_b in sybs_b.symbols_list:
                if str.lower(syb_a.base_coin).strip() == str.lower(syb_b.base_coin).strip() :
                    same_basecoin.append(syb_a.base_coin)

        return same_basecoin

    #只要跟coins有相关的，不论是base_coin,还是quote_coin都把此symbol返回
    def get_symbols_by_coins(self, exchange, coins, usdt_value_limit=0):
        sybs_a = Symbols()
        if ut.okex_exchange.lower() == exchange.lower():
            ex_qt = tickers_api.QuoteTickers()
            tks = ex_qt.get_tikers_value(exchange, usdt_value_limit)
            for ticker in tks.Tickers_list:
                syb = Symbol()
                syb.symbol = ticker.Symbol
                syb.exchange = exchange
                syb.time = ticker.Time
                syb.base_coin = ut.get_base_coin(exchange, ticker.Symbol)
                syb.quote_coin = ut.get_quote_coin(exchange, ticker.Symbol)
                for coin in coins:
                    if str.lower(coin) == syb.quote_coin.lower() or str.lower(coin) == syb.base_coin.lower():
                        sybs_a.add_symbol(syb)
                        break       #已添加就退出coin循环，避免重复添加。比如xrp_usdt，coins中如果有xrp,usdt时，不break的话就会添加两次。
        return sybs_a


if __name__ == '__main__':
    ex_qt = QuoteSymbols()
    exchange_name = 'okex'
    sybs = Symbols()
    sybs = ex_qt.get_all_symbols(exchange_name)
    sybs.print_detail()