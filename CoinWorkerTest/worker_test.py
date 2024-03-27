import requests
import logging
from datetime import datetime

logging.basicConfig(filename="log.log", filemode="a",format="%(asctime)s - %(thread)d - %(process)d - %(filename)s - %(lineno)d - %(funcName)20s() %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S",level=logging.INFO)
logging.info("Running worker")

# https://developers.firi.com/


class Worker:

    def __init__(self):
        pass
       
   
    def get_all(self):
        stats = {}
        stats["Api version"] = "1.0"
        try:
            MARKETS = "https://api.firi.com/v2/markets"
            rv = requests.get(MARKETS, headers={"User-Agent": "XY"})
            result = rv.json()
            logging.debug(result)
            logging.debug(rv.status_code)
            stats["Status Code"] = rv.status_code
        except Exception as ex:
            logging.error(ex)
        return stats
    
    def get_coin_market(self):
        bears = ["1/4/2002–10/9/2002, days 278, -33.75", "10/9/2007–11/20/2008, days 408, -51.93", "1/6/2009–3/9/2009, days 62, -27.62", "2/19/2020–3/23/2020, days 33, -33.92", "1/3/2022–10/12/2022, days 282, 25.43"]
        dict = {"Data NOK": "https://firi.com/no", "Api": "https://developers.firi.com/",
                "coinmarketcap": "https://coinmarketcap.com/", "Author": "https://follow-e-lo.com/", "firstb": "25.09.2022", "Bear market:": "Down -61% to -20%, avg(30%)", "5 last bears": bears}
        return dict

    def get_solnok_orderbooks(self, coin_name):
        coin = str(coin_name)        
        logging.info("Coin depth for " + coin)

        COIN_DEPTH = "https://api.firi.com/v1/markets/" + coin + "/depth"
        return_dict ={}
        stats = {}
        stats["Api version"] = "1.1"
        try:
            rv = requests.get(COIN_DEPTH, headers={"User-Agent": "XY"})
            result = rv.json()
            logging.debug(result)
            logging.debug(rv.status_code)
            logging.debug(str(type(result)))
            logging.debug(result)
            stats["Status Code"] = rv.status_code
            stats["Coin"] = coin
            # highest price for one buyer, we are looking at sum of all buyers
            current_bids = result["bids"]
            # lowest price for one buyer, we are looking at sum of all sellers
            current_asks = result["asks"]
            bids = 0
            asks = 0
            for b in current_bids:
                # when bid > ask, selling is stronger and price likely to move down
                bids +=1
            for a in current_asks:
                # when ask > bid, byuing is stronger and price likely to move up
                asks +=1
            logging.debug(stats)
            ba = "Bids " + str(bids) + ". Asks " +str(asks)
            return_dict["Depth"]= ba
            logging.info(return_dict)
            stats["Depth"] = return_dict["Depth"]
            logging.info(stats)

        except Exception as ex:
            logging.error(ex)
        return stats


wo = Worker()
wo.get_solnok_orderbooks("SOLNOK")
wo.get_solnok_orderbooks("XRPNOK")
wo.get_solnok_orderbooks("DOTNOK")
wo.get_solnok_orderbooks("BTCNOK")
wo.get_solnok_orderbooks("ADANOK")