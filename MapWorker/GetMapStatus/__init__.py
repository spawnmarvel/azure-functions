import logging

import azure.functions as func

from GetMapStatus.worker import Worker


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    workerInstance = Worker()
    row = workerInstance.get_row()
    county = workerInstance.get_all()

    # li = [sol_status, dot_status, xrp_status, ada_status, coinmarket, length_of_queue]
    li = [row, county]
    return func.HttpResponse(str(li), mimetype="text/json")
