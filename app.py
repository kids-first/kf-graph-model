#!/usr/bin/env python
import os
import connexion
from connexion import NoContent
import yaml
import logging
from py_graph import GraphSchema

with open('config.yaml') as f:
    cfg = yaml.load(f)

schema_path = cfg['schema_path']
host = cfg['host']
port = cfg['port']

graph_schemas = GraphSchema(schema_path, host, port)


def list_schemas(schemas=graph_schemas):
    return schemas.entity_types


def get_schema(gs=graph_schemas, entity=None, raw=False):
    if raw:
        s = gs.raw_definitions
    else:
        s = gs.schemas

    if entity in s:
        return s[entity]
    else:
        return NoContent, 404

logging.basicConfig(level=logging.INFO)

app = connexion.App(__name__)
base_path = graph_schemas.base_url
app.add_api('swagger.yaml', base_path=base_path)

if __name__ == '__main__':
    # run standalone gevent server
    app.run(port=port, server='gevent')
