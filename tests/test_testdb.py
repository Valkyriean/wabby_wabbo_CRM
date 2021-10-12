from flaskr.dbmodels import Company

# test whether a seperate database is set


def test_testing_db(client, db):
    """Start with a blank database."""
    db_name = db.connection.get_database("crm_test_db").name
    assert db_name.endswith("_test_db")

# test whether testing database only contain a test data


def test_empty_db(client, db):
    objs = Company.objects
    assert len(objs) == 1
