import logging
import json
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
            for lentity in response.entities:
                entity = dict()
                matches = []
                entity['name'] = str(lentity.name)
                entity['url'] = str(lentity.url)
                entity['data_source'] = str(lentity.data_source)
                for ematch in lentity.matches:
                    # TODO: Evaluate this and determine if any additional processing is needed to filter out useless links
                    match = dict()
                    match['text'] = str(ematch.text)
                    match['confidence_score'] = str(ematch.confidence_score)
                    match['offset'] = str(ematch.offset)
                    match['length'] = str(ematch.length)
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


def main(documents: func.DocumentList, doc: func.Out[func.Document]) -> str:
    logging.basicConfig(level="INFO")
    client = authenticate_client()
    if documents:
        for document in documents:
            logging.info('Received analytics request for document {}'.format(document['id']))
            if len(document["keywords"]) == 0 and len(document["linked_topics"]) == 0:
                logging.info('Performing text analytics for document {}'.format(document['id']))
                title = document["title"]
                abstract = document["abstract"]
                logging.info('Searching for keywords...')
                keywords = get_paper_keywords(client, title, abstract)
                logging.info('Searching for linked entities...')
                linked_entities = get_linked_entities(client, title, abstract)

                logging.info('Text analysis complete, writing output to Cosmos instance...')
                # Formulate JSON and write output to Cosmos
                publication = {
                    "id": document['id'],
                    "title": document['title'],
                    "abstract": document['abstract'],
                    "authors": document['authors'],
                    "topics": document['topics'],
                    "likes": document['likes'],
                    "comments": document['comments'],
                    "url": document['url'],
                    "keywords": keywords,
                    "linked_topics": linked_entities
                }
                new_document = json.dumps(publication)
                try:
                    doc.set(func.Document.from_json(new_document))
                    logging.info('Document wrote successfully')
                except Exception as err:
                    logging.info('Encountered error: {}'.format(err))
            else:
                # Document has most likely already been processed, ignore this execution
                logging.info("Document {} already processed, skipping execution...")
        logging.info('Current document set completed')
    logging.info('Execution completed successfully.')
