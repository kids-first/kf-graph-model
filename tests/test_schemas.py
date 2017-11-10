from jsonschema import Draft4Validator


def test_schemas(graph_schemas):
    for s in graph_schemas.schemas:
        print(s)  # print so that when error occurs we know which schema to check
        jschema = graph_schemas.schemas.get(s)
        Draft4Validator.check_schema(jschema)
