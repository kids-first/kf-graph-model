# Kids First Graph Model

We use extended JSON schema specification to define Kids First Graph Model.
Nodes (a.k.a entities) in the graph are represented by individual JSON documents while
edges are defined as normal JSON properties referencing to related nodes. As a guiding
principle, we leverage JSON schema as much as possible to define and enforce constraints in the
graph model.

Note: the work is still at early phase, but this should give us a good starting point to explore
modeling more complicated use cases, such as, pedigrees, clinical longitudinal data and
phenotype ontology etc.
