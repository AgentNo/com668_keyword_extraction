from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from azure.cosmos import CosmosClient

# Test PDF located at https://com668storageaccount.blob.core.windows.net/teststorage/2202.00225.pdf

# Authenticate the client using your key and endpoint 
def authenticate_client():
    key = "680b4b1960da43e8a2b6f48029bb3d08"
    endpoint = "https://com668textanalyticsservice.cognitiveservices.azure.com/"
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client


def get_paper_abstract():
    client = CosmosClient('https://com668projectdb.documents.azure.com:443/', 'nBmaD6ZLF7uEp3t2p96QiHdR9yHHaRcXZhnTnq1FGv0N4WgprlkFNpbNZxiEVITzrO80BxqVs0YM4GaP77Wr2w==')
    database = client.get_database_client('publications')
    papers_container = database.get_container_client('papers')
    query = 'SELECT * FROM c WHERE c.id = "{}"'.format('09f8fa65-fe97-4e3b-abf9-6fe0c59ddf46')
    items = list(papers_container.query_items(query=query, enable_cross_partition_query=True))
    abstract = items[0]['abstract']
    return abstract


def key_phrase_extraction_example(client):

    try:
        abstract = get_paper_abstract()
        documents = [abstract]
        response = client.extract_key_phrases(documents = documents)[0]

        if not response.is_error:
            print("\tKey Phrases:")
            for phrase in response.key_phrases:
                print("\t\t", phrase)
        else:
            print(response.id, response.error)

        result = client.recognize_linked_entities(documents = documents)[0]
        print("Linked Entities:\n")
        for entity in result.entities:
            print("\tName: ", entity.name, "\tId: ", entity.data_source_entity_id, "\tUrl: ", entity.url,
            "\n\tData Source: ", entity.data_source)
            print("\tMatches:")
            for match in entity.matches:
                print("\t\tText:", match.text)
                print("\t\tConfidence Score: {0:.2f}".format(match.confidence_score))
                print("\t\tOffset: {}".format(match.offset))
                print("\t\tLength: {}".format(match.length))

    except Exception as err:
        print("Encountered exception. {}".format(err))

client = authenticate_client()
key_phrase_extraction_example(client)
