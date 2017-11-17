[![Build Status](https://travis-ci.org/kids-first/kf-graph-model.svg?branch=master)](https://travis-ci.org/kids-first/kf-graph-model)

# Kids First Graph Model

We use extended [JSON Schema](http://json-schema.org/) specification to define Kids First Graph Model.
Nodes (a.k.a entities) in the graph are represented by individual JSON documents while
edges are defined as normal JSON properties referencing to related nodes. As a guiding
principle, we leverage JSON Schema as much as possible to define and enforce constraints in the
graph model. Extended rules will be enforced at application level.

Note: the work is still at early phase, but this should give us a good starting point to explore
modeling more complicated use cases, such as, pedigrees, clinical longitudinal data and
phenotype ontology etc.

A lightweight API service is included to serve the JSON schemas online. To start the service
using default settings:

```
python app.py
```

The schemas will be available under: http://localhost:8081/schemas/kf-graph-model/v0.0.1/.
Append the entity type to the URL to get it's own schema,
eg, [read_group](http://localhost:8081/schemas/kf-graph-model/v0.0.1/read_group)

Run tests with `pytest`.
