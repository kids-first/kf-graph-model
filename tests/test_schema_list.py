def test_schema_list(graph_schemas):
    all_schemas = set(graph_schemas.schemas)
    expected_schemas = {'_definitions', 'program', 'project', 'sequence_alignment',
                        'mutect2_ssm_calling', 'aliquot', 'sample', 'case', 'exposure',
                        'family', 'read_group', 'read_group_qc', 'hpo',
                        'genetic_testing_status', 'cardiac_abnormality'}

    assert all_schemas == expected_schemas
