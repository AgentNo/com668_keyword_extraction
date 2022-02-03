import logging

import azure.functions as func


def main(documents: func.DocumentList) -> str:
    logging.basicConfig(level="INFO")
    if documents:
        logging.info('Document id: %s', documents[0]['id'])
