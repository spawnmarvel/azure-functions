import requests
import logging
from datetime import datetime
from GetCoinStatus.st_queue import StorageQueue


logging.info("Running worker")

# https://developers.firi.com/


class Worker:

    def __init__(self):
        self.queueInstance = StorageQueue()
        # self.queueInstance.send_msg("HeartBeat")
        # a test for log analytics workspace log alerts
        # logging.info("ALERTMSG-COIN")

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

    def get_solnok(self):
        logging.info("SOLNOK:")
        MARKET_SOLNOK = "https://api.firi.com/v2/markets/SOLNOK"
        stats = {}
        stats["Api version"] = "1.6. Mail alert LL-HH"
        try:
            rv = requests.get(MARKET_SOLNOK, headers={"User-Agent": "XY"})
            result = rv.json()
            logging.debug(result)
            logging.debug(rv.status_code)
            market = ""
            stats["Status Code"] = rv.status_code
            stats["Coin"] = "SOLNOK"
            low = result["low"]
            high = result["high"]
            change = result["change"]
            last = result["last"]
            # stats["low"] = low
            # stats["high"] = high
            stats["change"] = change
            current_time = str(datetime.now())
            stats["Time"] = current_time
            stats["last"] = last
            # limits
            stats["Buy warning"] = 50
            stats["Buy alert"] = 100
            stats["Hold warning"] = 700
            stats["Hold alert"] = 1000
            logging.info(stats)
        except Exception as ex:
            logging.error(ex)
        return stats

    def get_adanok(self):
        logging.info("ADANOK:")
        MARKET_ADANOK = "https://api.firi.com/v2/markets/ADANOK"
        stats = {}
        stats["Api version"] = "1.6. Mail alert LL-HH"
        try:
            rv = requests.get(MARKET_ADANOK, headers={"User-Agent": "XY"})
            result = rv.json()
            logging.debug(result)
            logging.debug(rv.status_code)
            market = ""
            stats["Status Code"] = rv.status_code
            stats["Coin"] = "ADANOK"
            low = result["low"]
            high = result["high"]
            change = result["change"]
            last = result["last"]
            # stats["low"] = low
            # stats["high"] = high
            stats["change"] = change
            current_time = str(datetime.now())
            stats["Time"] = current_time
            stats["last"] = last
            # limits
            stats["Buy warning"] = 1.8
            stats["Buy alert"] = 2
            stats["Hold warning"] = 8
            stats["Hold alert"] = 12
            logging.info(stats)
        except Exception as ex:
            logging.error(ex)
        return stats

    def get_dotnok(self):
        logging.info("DOTNOK:")
        MARKET_DOTNOK = "https://api.firi.com/v2/markets/DOTNOK"
        stats = {}
        stats["Api version"] = "1.5. Mail alert LL-HH"
        try:
            rv = requests.get(MARKET_DOTNOK, headers={"User-Agent": "XY"})
            result = rv.json()
            logging.debug(result)
            logging.debug(rv.status_code)
            market = ""
            stats["Status Code"] = rv.status_code
            stats["Coin"] = "DOTNOK"
            low = result["low"]
            high = result["high"]
            change = result["change"]
            last = result["last"]
            # stats["low"] = low
            # stats["high"] = high
            stats["change"] = change
            current_time = str(datetime.now())
            stats["Time"] = current_time
            stats["last"] = last
            # limits
            stats["Buy warning"] = 30
            stats["Buy alert"] = 60
            stats["Hold warning"] = 110
            stats["Hold alert"] = 150
            logging.info(stats)
        except Exception as ex:
            logging.error(ex)
        return stats

    def get_xrpnok(self):
        logging.info("XRPNOK:")
        MARKET_DOTNOK = "https://api.firi.com/v2/markets/XRPNOK"
        stats = {}
        stats["Api version"] = "1.5. Mail alert LL-HH"
        try:
            rv = requests.get(MARKET_DOTNOK, headers={"User-Agent": "XY"})
            result = rv.json()
            logging.debug(result)
            logging.debug(rv.status_code)
            market = ""
            stats["Status Code"] = rv.status_code
            stats["Coin"] = "XRPNOK"
            low = result["low"]
            high = result["high"]
            change = result["change"]
            last = result["last"]
            # stats["low"] = low
            # stats["high"] = high
            stats["change"] = change
            current_time = str(datetime.now())
            stats["Time"] = current_time
            stats["last"] = last
            # limits
            stats["Buy warning"] = 1.8
            stats["Buy alert"] = 2
            stats["Hold warning"] = 10
            stats["Hold alert"] = 15
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
            buy_w = float(coin_dict["Buy warning"])
            buy_a = float(coin_dict["Buy alert"])
            hold_w = float(coin_dict["Hold warning"])
            hold_a = float(coin_dict["Hold alert"])
            current_last = float(coin_dict["last"])
            
            # SOL EXAMPLE, < 50
            if current_last < buy_w:
                market = "Bear and Buy alert 1. " + coin_dict["Coin"] + ";" + coin_dict["last"]
                # send to queue
                self.queueInstance.send_msg(market)
                # https://stackoverflow.com/questions/58246398/how-do-i-send-email-from-an-azure-function-app
                logging.info("ALERTMSG-COIN")
            
            # SOL EXAMPLE, >= 50 and < 100
            elif current_last >= buy_w and current_last < buy_a:
                market = "Bear and Buy warning 2. " + coin_dict["Coin"] + ";" + coin_dict["last"]
                # send to queue
                self.queueInstance.send_msg(market)
                logging.info("ALERTMSG-COIN")
            
            # SOL EXAMPLE, >= 100 and < 800
            elif current_last >= buy_a and current_last < hold_w:
                market = "Bear and Hold alert 1. " + coin_dict["Coin"] + ";" + coin_dict["last"]
                # self.queueInstance.send_msg(market)
           
            # SOL EXAMPLE, >= 800 and < 1000
            elif current_last >= hold_w and current_last < hold_a:
                market = "Bull and Hold warning 2. " + coin_dict["Coin"] + ";" + coin_dict["last"]
                self.queueInstance.send_msg(market)
                logging.info("ALERTMSG-COIN")

            elif current_last >= hold_a:
                # earning if follow only buy limit
                market = "Bull and Sell alert 1. " + coin_dict["Coin"] + ";" + coin_dict["last"]
                # send to queue
                self.queueInstance.send_msg(market)
                logging.info("ALERTMSG-COIN")
            
            elif current_last >= hold_a * 2:
                # earning if follow only buy limit
                market = "Bull and Sell alert * 2. " + coin_dict["Coin"] + ";" + coin_dict["last"]
                # send to queue
                self.queueInstance.send_msg(market)
                logging.info("ALERTMSG-COIN")

            else:
                market = "What is market now?. View last"

            # add status here market
            coin_dict["status"] = market
            logging.info(coin_dict)
        except Exception as ex:
            logging.error(ex)
        return coin_dict

    def get_coin_market(self):
        dict = {"Data NOK": "https://firi.com/no", "Api": "https://developers.firi.com/",
                "coinmarketcap": "https://coinmarketcap.com/", "Author": "https://follow-e-lo.com/", "ft": "25.09.2022", "lb": "12.05.2023"}
        return dict

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
    
    

