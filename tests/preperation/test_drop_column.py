from geoflow.preperation import drop_column

def test_drop_column():
    node = {"output_table_name": "node_table"}
    column_name = "column_to_drop"
    statement = drop_column(node, column_name)
    expected_statement = """
    ALTER TABLE node_table 
    DROP COLUMN IF EXISTS 'column_to_drop';
    """
    assert statement.strip() == expected_statement.strip()