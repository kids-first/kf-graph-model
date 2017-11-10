import os
from glob import glob
import json
from jsonschema import RefResolver, Draft4Validator, ValidationError


def test_jsons(graph_schemas):
    schemastore = graph_schemas.schemas
    root_uri = graph_schemas.url_prefix

    # get all testing json documents
    doc_path = os.path.join(graph_schemas.schema_path, 'example_docs')
    for j in glob(os.path.join(doc_path, '*.json')):
        print(j)  # print file name
        ok, _, schema_id, _, _ = j.split('.')  # eg. ok.12.case.01.json

        resolver = RefResolver("%s/%s" % (root_uri, schema_id),
                               schemastore.get(schema_id), schemastore)

        with open(j, 'r') as f:
            json_data = json.load(f)

        error = False
        try:
            Draft4Validator(schemastore.get(schema_id), resolver=resolver).validate(json_data)
        except:
            error = True

        if os.path.basename(ok.lower()) == 'ko':
            if error:
                assert True
            else:
                print('JSON doc %s should fail but it passed validation!' % j)
                assert False
        elif os.path.basename(ok.lower()) == 'ok':
            if error:
                print('JSON doc %s should pass but it failed validation!' % j)
                assert False
            else:
                assert True
        else:
            print('JSON doc %s does not follow naming convention!' % j)
            assert False
