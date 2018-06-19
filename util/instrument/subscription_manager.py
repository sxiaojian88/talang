from talang.util.instrument.instrument import Instrument
try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser


class SubscriptionManager:
    def __init__(self, config_path):
        """
        Constructor
        """
        self.config = ConfigParser.ConfigParser()
        self.config.read(config_path)
        
    def get_instmt_ids(self):
        """
        Return all the instrument ids
        """
        return self.config.sections()
    
    def get_instrument(self, instmt_id):
        """
        Return the instrument object by instrument id
        :param instmt_id: Instrument ID
        :return Instrument object
        """
        exchange_name = self.config.get(instmt_id, 'exchanges')
        instmt_name = self.config.get(instmt_id, 'instmt_name')
        instmt_code = self.config.get(instmt_id, 'instmt_code')
        base_coin = self.config.get(instmt_id,'base_coin')
        quote_coin = self.config.get(instmt_id, 'quote_coin')
        enabled = int(self.config.get(instmt_id, 'enabled'))
        params = dict(self.config.items(instmt_id))
        del params['exchanges']
        del params['instmt_name']
        del params['instmt_code']
        del params['base_coin']
        del params['quote_coin']
        del params['enabled']
        
        if enabled == 1:
            return Instrument(exchange_name, instmt_name, instmt_code, base_coin, quote_coin,**params)
        else:
            return None
        
    def get_subscriptions(self):
        """
        Get all the subscriptions from the configuration file
        :return List of instrument objects
        """
        instmts = [self.get_instrument(inst) for inst in self.get_instmt_ids()]
        return [instmt for instmt in instmts if instmt is not None]
        
