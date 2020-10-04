import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, ConceptsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-03-16',
    iam_apikey='DQSBRRNuGPDQaJLIP9xDts1r_DUAqGhNMGjP65-lAlMi',
    url='https://api.us-east.natural-language-understanding.watson.cloud.ibm.com/instances/93c69b8a-599f-470c-ba51-cbe944a21173'
)

response = natural_language_understanding.analyze(
    text='Create new group',
    features=Features(concepts=ConceptsOptions(), entities=["create"])).get_result()

print(json.dumps(response, indent=2))