import os
from glob import glob
import json
from jsonschema import RefResolver, Draft4Validator, ValidationError


def test_jsons(graph_schemas):
    root_url = graph_schemas.url_prefix

    # pre-cache all schemas here with keys being full url
    schemastore = {}
    for schema_id in graph_schemas.schemas:
        schemastore["%s/%s" % (root_url, schema_id)] = graph_schemas.schemas[schema_id]

    # get all testing json documents
    doc_path = os.path.join(graph_schemas.schema_path, 'example_docs')
    for j in glob(os.path.join(doc_path, '*.json')):
        print(j)  # print file name
        ok, _, schema_id, _, _ = j.split('.')  # eg. ok.12.case.01.json

        resolver = RefResolver("%s/%s" % (root_url, schema_id),
                               graph_schemas.schemas[schema_id], schemastore)

        with open(j, 'r') as f:
            json_data = json.load(f)

        if os.path.basename(ok.lower()) == 'ko':
            invalid = False
            try:
                Draft4Validator(graph_schemas.schemas[schema_id], resolver=resolver).validate(json_data)
            except:
                invalid = True

            if invalid:  # expect to be invalid
                assert True
            else:
                print('JSON doc %s should fail but it passed schema validation!' % j)
                assert False
        elif os.path.basename(ok.lower()) == 'ok':
            Draft4Validator(graph_schemas.schemas[schema_id], resolver=resolver).validate(json_data)
        else:
            print("Testing JSON doc %s name has to start with 'ok' or 'ko'!" % j)
            assert False
