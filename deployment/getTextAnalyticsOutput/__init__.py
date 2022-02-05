import logging
import azure.functions as func
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


# Authentication instance of Language Cognitive Service
def authenticate_client():
    ta_credential = AzureKeyCredential("680b4b1960da43e8a2b6f48029bb3d08")
    client = TextAnalyticsClient(
            endpoint="https://com668textanalyticsservice.cognitiveservices.azure.com/", 
            credential=ta_credential)
    return client


# Return a list of all keywords mined from the abstract and the title. If an error occurs or no keywords are found, return an empty list 
def get_paper_keywords(client, title, abstract):
    try:
        documents = [abstract, title]
        response = client.extract_key_phrases(documents = documents)[0]

        if not response.is_error and len(response.key_phrases) != 0:
            keywords = []
            for phrase in response.key_phrases:
                keywords.append(str(phrase).lower())
            
            logging.info("Found {} keywords: \n{}".format(len(keywords), keywords))
            return keywords
        else:
            if response.error:
                logging.info(response.id, response.error)
            else:
                logging.info('No keywords found in text!')
            return []
    except Exception as err:
        print("Encountered exception: {}".format(err))
        return []


# Return a list of all linked entites found in the paper. If no entites are found or no keywords are found, return empty list
def get_linked_entities(client, title, abstract):
    try:
        documents = [abstract, title]
        response = client.recognize_linked_entities(documents = documents)[0]

        if not response.is_error and len(response.entities) != 0:
            logging.info("Found the following linked entities:\n")
            entities = []
            for entity in response.entities:
                entity = dict()
                matches = []
                entity['name'] = str(entity.name)
                entity['url'] = str(entity.url)
                entity['data_source'] = str(entity.data_source)
                for match in entity.matches:
                    # TODO: Evaluate this and determine if any additional processing is needed to filter out useless links
                    match = dict()
                    match['text'] = str(match.text)
                    match['confidence_score'] = str(match.confidence_score)
                    match['offset'] = str(match.offset)
                    match['length'] = str(match.length)
                    matches.append(match)
                entity['matches'] = matches
                entities.append(entity)
            logging.info("{}".format(entities))
            return entities
        else:
            if response.error:
                logging.info(response.id, response.error)
                return []
            else:
                logging.info('No linked entities found in text!')
            return []
    except Exception as err:
        print("Encountered exception: {}".format(err))
        return []


def main(documents: func.DocumentList) -> str:
    logging.basicConfig(level="INFO")
    client = authenticate_client()
    if documents:
        for document in documents:
            # TODO: Check here to make sure that documents that are already processed don't get processed twice
            logging.info('Performing text analytics for document id: %s', document['id'])
            if True:
                title = document["title"]
                abstract = document["abstract"]
                logging.info('Searching for keywords...')
                keywords = get_paper_keywords(client, title, abstract)
                logging.info('Searching for linked entities...')
                entites = get_linked_entities(client, title, abstract)
        logging.info('Text analysis complete, writing output...')
        # TODO: Write output to CosmosDB instance
