def test_schema_list(graph_schemas):
    all_schemas = set(graph_schemas.schemas)
    expected_schemas = {'_definitions', 'program', 'project', 'alignment',
                        'muse_ssm_calling', 'aliquot', 'sample',
                        'case', 'exposure', 'family', 'read_group'}

    assert all_schemas == expected_schemas
