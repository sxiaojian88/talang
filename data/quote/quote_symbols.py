import talang.data.quote.quote_tickers as tickers_api
from talang.util.model.Symbol import Symbol
from talang.util.model.Symbol import Symbols
import talang.util.util_data as ut


class QuoteSymbols:

    def get_all_symbols(self, exchange):
        sybs = Symbols()
        if ut.okex_exchange.lower() == exchange.lower():
            ex_qt = tickers_api.QuoteTickers()
            tks = ex_qt.get_tikers_value(exchange)
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


if __name__ == '__main__':
    ex_qt = QuoteSymbols()
    exchange_name = 'okex'
    sybs = Symbols()
    sybs = ex_qt.get_all_symbols(exchange_name)
    sybs.print_detail()