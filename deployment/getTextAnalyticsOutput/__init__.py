import logging
import azure.functions as func
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


def authenticate_client():
    ta_credential = AzureKeyCredential("680b4b1960da43e8a2b6f48029bb3d08")
    client = TextAnalyticsClient(
            endpoint="https://com668textanalyticsservice.cognitiveservices.azure.com/", 
            credential=ta_credential)
    return client


def abstract_analysis(client, title, abstract):
    try:
        documents = [abstract, title]
        response = client.extract_key_phrases(documents = documents)[0]

        if not response.is_error:
            logging.info("\tKey Phrases:")
            for phrase in response.key_phrases:
                logging.info("\t\t" + phrase)
        else:
            logging.info(response.id, response.error)

        result = client.recognize_linked_entities(documents = documents)[0]
        logging.info("Linked Entities:\n")
        for entity in result.entities:
            logging.info("\tName: ", entity.name, "\tId: ", entity.data_source_entity_id, "\tUrl: ", entity.url, "\n\tData Source: ", entity.data_source)
            logging.info("\tMatches:")
            for match in entity.matches:
                logging.info("\t\tText:{}".format(match.text))
                logging.info("\t\tConfidence Score: {0:.2f}".format(match.confidence_score))
                logging.info("\t\tOffset: {}".format(match.offset))
                logging.info("\t\tLength: {}".format(match.length))
    except Exception as err:
        print("Encountered exception: {}".format(err))


def main(documents: func.DocumentList) -> str:
    logging.basicConfig(level="INFO")
    client = authenticate_client()
    if documents:
        for document in documents:
            # TODO: Check here to make sure that documents that are already processed don't get processed twice
            logging.info('Performing text analytics for document id: %s', document['id'])
            title = document["title"]
            abstract = document["abstract"]
            abstract_analysis(client, title, abstract)
            logging.info('Text analysis complete, writing output...')
