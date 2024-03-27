import requests
import logging
from datetime import datetime
from GetCoinStatus.st_queue import StorageQueue

from GetCoinStatus.st_table import StorageTable


logging.info("Running worker")

# https://developers.firi.com/


class Worker:

    def __init__(self):
        self.queueInstance = StorageQueue()
        self.tableInstance = StorageTable()
        # test
        self.tableInstance.create_tabel()
       
   
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

    
    
    def get_bids_asks_orderbooks(self, coin_name):
        coin = str(coin_name)        
        logging.info("Coin depth for " + coin)

        COIN_DEPTH = "https://api.firi.com/v1/markets/" + coin + "/depth"
        return_dict ={}
        ba = ""
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
            # highest price one buyer is willing to pay , we are looking at sum of all buyers
            current_bids = result["bids"]
            # lowest price one buyer is willing to sell, we are looking at sum of all sellers
            current_asks = result["asks"]
            bids = 0
            asks = 0
            for b in current_bids:
                # when bid volume > ask volume, selling is stronger and price likely to move down
                bids +=1
            for a in current_asks:
                # when ask volume > bid volume, buying is stronger and price likely to move up
                asks +=1
            logging.debug(stats)
            market = ""
            if bids > asks:
                market = ". More sellers, price down."
            else:
                market = ". More buyers, price up."

            ba = "Bids " + str(bids) + ". Asks " +str(asks) + market
            return_dict["depth"]= ba
            logging.info(return_dict)

        except Exception as ex:
            logging.error(ex)
        return return_dict
    
    
    
    def get_btcnok(self):
        coin = "BTCNOK"
        logging.info(coin)
        MARKET_BTCNOK = "https://api.firi.com/v2/markets/BTCNOK"
        stats = {}
        stats["Api version"] = "2.0"
        try:
            rv = requests.get(MARKET_BTCNOK, headers={"User-Agent": "XY"})
            result = rv.json()
            logging.debug(result)
            logging.debug(rv.status_code)
            stats["Status Code"] = rv.status_code
            stats["Coin"] = "BTCNOK"
            change = result["change"]
            last = result["last"]
            stats["change"] = change
            current_time = str(datetime.now())
            stats["Time"] = current_time
            stats["last"] = last
            # what volume is thsi, daily sold?
            stats["volume"] = result["volume"]
            # limits
            stats["Low 2"] = 500000
            stats["Low 1"] = 570000
            stats["High 1"] = 700000
            stats["High 2"] = 720000
            logging.info(stats)
            dict = self.get_bids_asks_orderbooks(coin)
            stats["Depth"] = dict["depth"]
        except Exception as ex:
            logging.error(ex)
        return stats

    def get_solnok(self):
        coin = "SOLNOK"
        logging.info(coin)
        MARKET_SOLNOK = "https://api.firi.com/v2/markets/SOLNOK"
        stats = {}
        stats["Api version"] = "2.0"
        try:
            rv = requests.get(MARKET_SOLNOK, headers={"User-Agent": "XY"})
            result = rv.json()
            logging.debug(result)
            logging.debug(rv.status_code)
            stats["Status Code"] = rv.status_code
            stats["Coin"] = "SOLNOK"
            change = result["change"]
            last = result["last"]
            stats["change"] = change
            current_time = str(datetime.now())
            stats["Time"] = current_time
            stats["last"] = last
            stats["volume"] = result["volume"]
            # limits
            stats["Low 2"] = 300
            stats["Low 1"] = 500
            stats["High 1"] = 2000
            # has been here two times 2021 and 2024
            # stats["High 2"] = 2000
            stats["High 2"] = 3000
            logging.info(stats)
            dict = self.get_bids_asks_orderbooks(coin)
            stats["Depth"] = dict["depth"]
        except Exception as ex:
            logging.error(ex)
        return stats

    def get_adanok(self):
        coin = "ADANOK"
        logging.info("ADANOK:")
        MARKET_ADANOK = "https://api.firi.com/v2/markets/ADANOK"
        stats = {}
        stats["Api version"] = "1.6"
        try:
            rv = requests.get(MARKET_ADANOK, headers={"User-Agent": "XY"})
            result = rv.json()
            logging.debug(result)
            logging.debug(rv.status_code)
            stats["Status Code"] = rv.status_code
            stats["Coin"] = "ADANOK"
            change = result["change"]
            last = result["last"]
            stats["change"] = change
            current_time = str(datetime.now())
            stats["Time"] = current_time
            stats["last"] = last
            stats["volume"] = result["volume"]
            # limits
            stats["Low 2"] = 4
            stats["Low 1"] = 6.2
            stats["High 1"] = 15
            stats["High 2"] = 20
            dict = self.get_bids_asks_orderbooks(coin)
            stats["Depth"] = dict["depth"]
            logging.info(stats)
        except Exception as ex:
            logging.error(ex)
        return stats

    def get_dotnok(self):
        coin = "DOTNOK"
        logging.info(coin)
        MARKET_DOTNOK = "https://api.firi.com/v2/markets/DOTNOK"
        stats = {}
        stats["Api version"] = "1.5"
        try:
            rv = requests.get(MARKET_DOTNOK, headers={"User-Agent": "XY"})
            result = rv.json()
            logging.debug(result)
            logging.debug(rv.status_code)
            stats["Status Code"] = rv.status_code
            stats["Coin"] = "DOTNOK"
            change = result["change"]
            last = result["last"]
            stats["change"] = change
            current_time = str(datetime.now())
            stats["Time"] = current_time
            stats["last"] = last
            stats["volume"] = result["volume"]
            # limits
            stats["Low 2"] = 50
            stats["Low 1"] = 65
            stats["High 1"] = 150
            stats["High 2"] = 350
            dict = self.get_bids_asks_orderbooks(coin)
            stats["Depth"] = dict["depth"]
            logging.info(stats)
        except Exception as ex:
            logging.error(ex)
        return stats

    def get_xrpnok(self):
        coin = "XRPNOK"
        logging.info(coin)
        MARKET_DOTNOK = "https://api.firi.com/v2/markets/XRPNOK"
        stats = {}
        stats["Api version"] = "1.5"
        try:
            rv = requests.get(MARKET_DOTNOK, headers={"User-Agent": "XY"})
            result = rv.json()
            logging.debug(result)
            logging.debug(rv.status_code)
            stats["Status Code"] = rv.status_code
            stats["Coin"] = "XRPNOK"
            change = result["change"]
            last = result["last"]
            stats["change"] = change
            current_time = str(datetime.now())
            stats["Time"] = current_time
            stats["last"] = last
            stats["volume"] = result["volume"]
            # limits
            stats["Low 2"] = 3.5
            stats["Low 1"] = 4
            stats["High 1"] = 10
            stats["High 2"] = 20
            dict = self.get_bids_asks_orderbooks(coin)
            stats["Depth"] = dict["depth"]
            logging.info(stats)
        except Exception as ex:
            logging.error(ex)
        return stats

    def calculate_status(self, coin_dict):
        logging.debug("Get Coin dict")
        logging.info(coin_dict)
        # msg = coin_dict["Coin"] + ";" + coin_dict["last"]
        try:
            logging.info("Caluclate status")
            name = str(coin_dict["Coin"])
            low_2 = float(coin_dict["Low 2"])
            low_1 = float(coin_dict["Low 1"])
            high_1 = float(coin_dict["High 1"])
            high_2 = float(coin_dict["High 2"])
            current_value = float(coin_dict["last"])
            volume = float(coin_dict["volume"])
            change = float(coin_dict["change"])
            depth = coin_dict["Depth"]
            
            # SOL EXAMPLE, < 125
            if current_value <low_2:
                market = "Bear Low 2. Buy." + name+ "." + str(current_value)
                # send to queue
                self.queueInstance.send_msg(market)
                # https://stackoverflow.com/questions/58246398/how-do-i-send-email-from-an-azure-function-app
                # insert into table storage
                self.tableInstance.insert_entity(name, "Bear Low 2. Buy.", current_value, volume, change, depth)
                logging.info("ALERTMSG-COIN-LOW-2")
            
            # SOL EXAMPLE, >= 125 and < 250
            elif current_value >=low_2 and current_value < low_1:
                market = "Bear Low 1. Buy some."+ name+ "." + str(current_value)
                # send to queue
                self.queueInstance.send_msg(market)
                # insert into table storage
                self.tableInstance.insert_entity(name, "Bear Low 1. Buy some.", current_value, volume, change, depth)
                logging.info("ALERTMSG-COIN-LOW-1")
            
            # SOL EXAMPLE, >= 250 and < 1000
            elif current_value >= low_1 and current_value < high_1:
                market = "Waiting. " + name+ "." + str(current_value)
                # wait....
                # insert into table storage
                self.tableInstance.insert_entity(name, "Waiting.", current_value, volume, change, depth)
           
            # SOL EXAMPLE, >= 1000 and < 1500
            elif current_value >= high_1 and current_value < high_2:
                market = "Bull High 1." + name+ "." + str(current_value) 
                self.queueInstance.send_msg(market)
                # insert into table storage
                self.tableInstance.insert_entity(name, "Bull High 1.", current_value, volume, change, depth)
                # logging.info("ALERTMSG-COIN")

            # SOL EXAMPLE >= 1500 and < 3000
            elif current_value >= high_2 and current_value < (high_2 * 1.5):
                # earning if follow only buy limit
                market = "Bull High 2. Sell some." + name+ "." + str(current_value) 
                # send to queue
                self.queueInstance.send_msg(market)
                # insert into table storage
                self.tableInstance.insert_entity(name, "Bull High 2. Sell some.", current_value, volume, change, depth)
                logging.info("ALERTMSG-COIN-HIGH-2")
            
            elif current_value >= high_2 * 2:
                # earning if follow only buy limit
                market = "Bull high * 2. Sell more." + name+ "." + str(current_value)
                # send to queue
                self.queueInstance.send_msg(market)
                # insert into table storage
                self.tableInstance.insert_entity(name, "Bear High * 2. Sell more.", current_value, volume, change, depth)
                logging.info("ALERTMSG-COIN-MONEY")

            else:
                market = "Status. " + name+ "." + str(current_value) 
                self.queueInstance.send_msg(market)
                self.tableInstance.insert_entity(name, "Status.", current_value, volume, change, depth)

            # add status here market
            coin_dict["status"] = market
            logging.info(coin_dict)
        except Exception as ex:
            logging.error(ex)
        return coin_dict

    def get_solnok_bid(self):
        logging.info("SOLNOK BID:")
        SOLNOK_BID = "https://api.firi.com/v1/markets/SOLNOK/history"
        stats = {}
        stats["Api version"] = "1.1"
        try:
            rv = requests.get(SOLNOK_BID, headers={"User-Agent": "XY"})
            result = rv.json()
            logging.debug(result)
            logging.debug(rv.status_code)
            logging.debug(str(type(result)))
            logging.debug(result)
            stats["Status Code"] = rv.status_code
            stats["Coin"] = "SOLNOK BID-ASK"
            total_bid_amount = 0.0
            total_ask_amount = 0.0
            for rv in result:
                if rv["type"] == "bid":
                    logging.debug(rv["amount"])
                    total_bid_amount = total_bid_amount + float(rv["amount"])
                elif rv["type"] == "ask":
                    logging.debug(rv["amount"])
                    total_ask_amount = total_ask_amount + float(rv["amount"])

            stats["bid total"] = total_bid_amount
            stats["ask total"] = total_ask_amount
            stats["status"] = ""
            if total_bid_amount > total_ask_amount:
                stats["status"] = "Bids are higher, people want to buy (Highest price to pay)"
            else:
                stats["status"] = "Ask are higher, people want to sell (Lowest price to pay)"

            logging.info(stats)

        except Exception as ex:
            logging.error(ex)
        return stats

    def get_adanok_bid(self):
        logging.info("SOLNOK BID:")
        SOLNOK_BID = "https://api.firi.com/v1/markets/ADANOK/history"
        stats = {}
        stats["Api version"] = "1.1"
        try:
            rv = requests.get(SOLNOK_BID, headers={"User-Agent": "XY"})
            result = rv.json()
            logging.debug(result)
            logging.debug(rv.status_code)
            logging.debug(str(type(result)))
            logging.debug(result)
            stats["Status Code"] = rv.status_code
            stats["Coin"] = "ADANOK BID-ASK"
            total_bid_amount = 0.0
            total_ask_amount = 0.0
            for rv in result:
                if rv["type"] == "bid":
                    logging.debug(rv["amount"])
                    total_bid_amount = total_bid_amount + float(rv["amount"])
                elif rv["type"] == "ask":
                    logging.debug(rv["amount"])
                    total_ask_amount = total_ask_amount + float(rv["amount"])

            stats["bid total"] = total_bid_amount
            stats["ask total"] = total_ask_amount
            stats["status"] = ""
            if total_bid_amount > total_ask_amount:
                stats["status"] = "Bids are higher, people want to buy (Highest price to pay)"
            else:
                stats["status"] = "Ask are higher, people want to sell (Lowest price to pay)"

            logging.info(stats)

        except Exception as ex:
            logging.error(ex)
        return stats

    def get_dotnok_bid(self):
        logging.info("DOTNOK BID:")
        SOLNOK_BID = "https://api.firi.com/v1/markets/DOTNOK/history"
        stats = {}
        stats["Api version"] = "1.1"
        try:
            rv = requests.get(SOLNOK_BID, headers={"User-Agent": "XY"})
            result = rv.json()
            logging.debug(result)
            logging.debug(rv.status_code)
            logging.debug(str(type(result)))
            logging.debug(result)
            stats["Status Code"] = rv.status_code
            stats["Coin"] = "DOTNOK BID-ASK"
            total_bid_amount = 0.0
            total_ask_amount = 0.0
            for rv in result:
                if rv["type"] == "bid":
                    logging.debug(rv["amount"])
                    total_bid_amount = total_bid_amount + float(rv["amount"])
                elif rv["type"] == "ask":
                    logging.debug(rv["amount"])
                    total_ask_amount = total_ask_amount + float(rv["amount"])

            stats["bid total"] = total_bid_amount
            stats["ask total"] = total_ask_amount
            stats["status"] = ""
            if total_bid_amount > total_ask_amount:
                stats["status"] = "Bids are higher, people want to buy (Highest price to pay)"
            else:
                stats["status"] = "Ask are higher, people want to sell (Lowest price to pay)"

            logging.info(stats)

        except Exception as ex:
            logging.error(ex)
        return stats

    def get_xrpnok_bid(self):
        logging.info("XRPNOK BID:")
        SOLNOK_BID = "https://api.firi.com/v1/markets/DOTNOK/history"
        stats = {}
        stats["Api version"] = "1.1"
        try:
            rv = requests.get(SOLNOK_BID, headers={"User-Agent": "XY"})
            result = rv.json()
            logging.debug(result)
            logging.debug(rv.status_code)
            logging.debug(str(type(result)))
            logging.debug(result)
            stats["Status Code"] = rv.status_code
            stats["Coin"] = "XRPNOK BID-ASK"
            total_bid_amount = 0.0
            total_ask_amount = 0.0
            for rv in result:
                if rv["type"] == "bid":
                    logging.debug(rv["amount"])
                    total_bid_amount = total_bid_amount + float(rv["amount"])
                elif rv["type"] == "ask":
                    logging.debug(rv["amount"])
                    total_ask_amount = total_ask_amount + float(rv["amount"])

            stats["bid total"] = total_bid_amount
            stats["ask total"] = total_ask_amount
            stats["status"] = ""
            if total_bid_amount > total_ask_amount:
                stats["status"] = "Bids are higher, people want to buy (Highest price to pay)"
            else:
                stats["status"] = "Ask are higher, people want to sell (Lowest price to pay)"

            logging.info(stats)

        except Exception as ex:
            logging.error(ex)
        return stats

    def receive_queue_msg(self):
        stats = {}
        try:
            stats = {"Queue": self.queueInstance.receieve_msg()}
            logging.info(stats)
        except Exception as ex:
            logging.error(ex)
        return stats
    
    def queue_length(self):
        stats = {}
        try:
            stats = {"Queue": self.queueInstance.get_queue_length()}
            logging.info(stats)
        except Exception as ex:
            logging.error(ex)
        return stats
    
    

