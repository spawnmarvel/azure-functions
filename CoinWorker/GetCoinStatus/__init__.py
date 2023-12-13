import logging
import requests

from GetCoinStatus.worker import Worker

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    workerInstance = Worker()

    solnok = workerInstance.get_solnok()
    sol_status = workerInstance.calculate_status(solnok)
    
    adanok = workerInstance.get_adanok()
    ada_status = workerInstance.calculate_status(adanok)

    dotnok = workerInstance.get_dotnok()
    dot_status = workerInstance.calculate_status(dotnok)

    xrpnok = workerInstance.get_xrpnok()
    xrp_status = workerInstance.calculate_status(xrpnok)

    # solbid = workerInstance.get_solnok_bid()
    # adabid = workerInstance.get_adanok_bid()
    # dotbid = workerInstance.get_dotnok_bid()
    # xrpbid = workerInstance.get_xrpnok_bid()
    # url coin market
    coinmarket = workerInstance.get_coin_market()

    # queue
    # msg_from_queue = workerInstance.receive_queue_msg()
    length_of_queue = workerInstance.queue_length()
    li = [sol_status, dot_status, xrp_status, ada_status, coinmarket, length_of_queue]
    return func.HttpResponse(str(li), mimetype="text/json")
