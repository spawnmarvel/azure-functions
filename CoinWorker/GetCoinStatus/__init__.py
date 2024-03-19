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
    coinmarket = workerInstance.get_coin_market()

    length_of_queue = workerInstance.queue_length()
    li = [sol_status, dot_status, xrp_status, ada_status, coinmarket, length_of_queue]
    return func.HttpResponse(str(li), mimetype="text/json")
