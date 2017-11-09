import os
import yaml
from copy import deepcopy


class GraphSchema(object):
    def __init__(self, schema_path, host, port):
        self._schema_path = schema_path
        self._raw_definitions = {}
        self._entity_types = []
        self._schemas = {}
        self._load_conf(host, port)
        self._load_yamls()
        self._prepare_schemas()

    @property
    def schema_path(self):
        return self._schema_path

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def version(self):
        return self._version

    @property
    def base_url(self):
        return self._base_url

    @property
    def url_prefix(self):
        return self._url_prefix        

    @property
    def entity_types(self):
        return self._entity_types

    @property
    def raw_definitions(self):
        return self._raw_definitions

    @property
    def schemas(self):
        return self._schemas

    def _load_conf(self, host, port):
        conf_file = os.path.join(self.schema_path, 'schemas', 'settings.conf')
        if not os.path.isfile(conf_file):
            raise Exception('Unable to locate settings.conf file in schema folder!')

        with open(conf_file, 'r') as c:
            try:
                cfg = yaml.load(c)
            except yaml.YAMLError as exc:
                raise Exception(exc)

        self._id = cfg['id']
        self._name = cfg['name']
        self._version = cfg['version']
        self._base_url = '/schemas/%s/%s' % (self.id, self.version)
        self._url_prefix = '%s:%s%s' % (host, port, self.base_url)

    def _load_yamls(self):
        d = os.path.join(self.schema_path, 'schemas')
        for x in os.walk(d):
            path = x[0]
            category = os.path.basename(path)
            files = x[-1]
            for f in files:
                if not f.endswith('.yaml'): continue
                entity_type = os.path.splitext(f)[0]
                with open(os.path.join(path, f), 'r') as s:
                    # no entity can be defined more than once
                    if entity_type in self.raw_definitions:
                        raise Exception("Entity redefined: %s!" % entity_type)

                    if not entity_type.startswith('_'):
                        self._entity_types.append(entity_type)

                    self._raw_definitions[entity_type] = yaml.load(s)

    def _prepare_schemas(self):
        self._schemas = deepcopy(self.raw_definitions)

        # let's start with _definitions
        # may need to generalize this for later to include more definitions start with '_' 
        definitions = self.schemas['_definitions']
        definitions['id'] = "%s/%s" % (self.url_prefix, definitions['id'])

        """
        # for some reason added 'id' does not work 
        for i in definitions:
            if i in ('$schema', 'id'): continue
            for p in definitions[i].get('properties', {}):
                definitions[i]['properties'][p]['id'] = '%s/%s' % (i, p)
        """

        # now others
        for e in self.schemas:
            if e.startswith('_'): continue
            self.schemas[e]['id'] = "%s/%s" % (self.url_prefix, self.schemas[e]['id'])

            """
            # for some reason added 'id' does not work 
            for p in self.schemas[e]['properties']:
                self.schemas[e]['properties'][p]['id'] = p
            """
