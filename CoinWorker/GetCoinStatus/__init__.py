import logging
import requests

from GetCoinStatus.worker import Worker

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("#### Main start ####")
    workerInstance = Worker()

    solnok = workerInstance.get_solnok()
    sol_status = workerInstance.calculate_status(solnok)
    
    adanok = workerInstance.get_adanok()
    ada_status = workerInstance.calculate_status(adanok)

    dotnok = workerInstance.get_dotnok()
    dot_status = workerInstance.calculate_status(dotnok)

    xrpnok = workerInstance.get_xrpnok()
    xrp_status = workerInstance.calculate_status(xrpnok)
    # just insert in az table, not API result
    btcnok = workerInstance.get_btcnok()
    btc_status = workerInstance.calculate_status(btcnok)
    
    coinmarket = workerInstance.get_coin_market()

    length_of_queue = workerInstance.queue_length()
    li = [sol_status, dot_status, xrp_status, ada_status, btc_status, coinmarket, length_of_queue]
    return func.HttpResponse(str(li), mimetype="text/json")
    # return func.HttpResponse(str(li), mimetype="text/html")
    # return func.HttpResponse(str(li), mimetype="text/xml")
    
    # HttpResponse Class
    # https://learn.microsoft.com/en-us/python/api/azure-functions/azure.functions.httpresponse?view=azure-python
    
