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
        dict = {"Data NOK": "https://firi.com/no", "Api": "https://developers.firi.com/",
                "coinmarketcap": "https://coinmarketcap.com/", "Author": "https://follow-e-lo.com/", "fb": "25.09.2022", "lb": "12.05.2023", "25":"25.12.2024", "?":"25.12.2025"}
        return dict

    def get_btcnok(self):
        logging.info("BTCNOK:")
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
            stats["volume"] = result["volume"]
            # limits
            stats["Low 2"] = 120000
            stats["Low 1"] = 170000
            stats["High 1"] = 500000
            stats["High 2"] = 620000
            logging.info(stats)
        except Exception as ex:
            logging.error(ex)
        return stats

    def get_solnok(self):
        logging.info("SOLNOK:")
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
            stats["Low 2"] = 250
            stats["Low 1"] = 500
            stats["High 1"] = 2000
            # has been here two times 2021 and 2024
            # stats["High 2"] = 2000
            stats["High 2"] = 3000
            logging.info(stats)
        except Exception as ex:
            logging.error(ex)
        return stats

    def get_adanok(self):
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
            stats["Low 2"] = 1.8
            stats["Low 1"] = 2
            stats["High 1"] = 8
            stats["High 2"] = 12
            logging.info(stats)
        except Exception as ex:
            logging.error(ex)
        return stats

    def get_dotnok(self):
        logging.info("DOTNOK:")
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
            stats["Low 2"] = 30
            stats["Low 1"] = 60
            stats["High 1"] = 110
            stats["High 2"] = 150
            logging.info(stats)
        except Exception as ex:
            logging.error(ex)
        return stats

    def get_xrpnok(self):
        logging.info("XRPNOK:")
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
            stats["Low 2"] = 1.8
            stats["Low 1"] = 2
            stats["High 1"] = 10
            stats["High 2"] = 15
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
            low_2 = float(coin_dict["Low 2"])
            low_1 = float(coin_dict["Low 1"])
            high_1 = float(coin_dict["High 1"])
            high_2 = float(coin_dict["High 2"])
            current_value = float(coin_dict["last"])
            volume = float(coin_dict["volume"])
            
            # SOL EXAMPLE, < 125
            if current_value <low_2:
                market = "Bear Low 2. " + coin_dict["Coin"] + ";" + coin_dict["last"]
                # send to queue
                self.queueInstance.send_msg(market)
                # https://stackoverflow.com/questions/58246398/how-do-i-send-email-from-an-azure-function-app
                # insert into table storage
                self.tableInstance.insert_entity(str(coin_dict["Coin"]), "Bear Low 2.", str(coin_dict["last"]), volume)
                logging.info("ALERTMSG-COIN-LOW-2")
            
            # SOL EXAMPLE, >= 125 and < 250
            elif current_value >=low_2 and current_value < low_1:
                market = "Bear Low 1. " + coin_dict["Coin"] + ";" + coin_dict["last"]
                # send to queue
                self.queueInstance.send_msg(market)
                # insert into table storage
                self.tableInstance.insert_entity(str(coin_dict["Coin"]), "Bear Low 1.", str(coin_dict["last"]), volume)
                
                # logging.info("ALERTMSG-COIN")
            
            # SOL EXAMPLE, >= 250 and < 1000
            elif current_value >= low_1 and current_value < high_1:
                market = "Waiting. " + coin_dict["Coin"] + ";" + coin_dict["last"]
                # wait....
                # insert into table storage
                self.tableInstance.insert_entity(str(coin_dict["Coin"]), "Waiting.", str(coin_dict["last"]), volume)
           
            # SOL EXAMPLE, >= 1000 and < 1500
            elif current_value >= high_1 and current_value < high_2:
                market = "Bull High 1. " + coin_dict["Coin"] + ";" + coin_dict["last"]
                self.queueInstance.send_msg(market)
                # insert into table storage
                self.tableInstance.insert_entity(str(coin_dict["Coin"]), "Bull High 1.", str(coin_dict["last"]), volume)
                # logging.info("ALERTMSG-COIN")

            # SOL EXAMPLE >= 1500 and < 3000
            elif current_value >= high_2 and current_value < (high_2 * 1.5):
                # earning if follow only buy limit
                market = "Bull High 2. " + coin_dict["Coin"] + ";" + coin_dict["last"]
                # send to queue
                self.queueInstance.send_msg(market)
                # insert into table storage
                self.tableInstance.insert_entity(str(coin_dict["Coin"]), "Bull High 2.", str(coin_dict["last"]), volume)
                logging.info("ALERTMSG-COIN-HIGH-2")
            
            elif current_value >= high_2 * 2:
                # earning if follow only buy limit
                market = "Bull high * 2. " + coin_dict["Coin"] + ";" + coin_dict["last"]
                # send to queue
                self.queueInstance.send_msg(market)
                # insert into table storage
                self.tableInstance.insert_entity(str(coin_dict["Coin"]), "Bear High * 2.", str(coin_dict["last"]), volume)
                logging.info("ALERTMSG-COIN-MONEY")

            else:
                market = "Status. " + coin_dict["Coin"] + ";" + coin_dict["last"]
                self.queueInstance.send_msg(market)

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
    
    

