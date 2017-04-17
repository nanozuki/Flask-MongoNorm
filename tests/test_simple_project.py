


def test_init_and_read(client):
    TheModel.delete_many()
    TheModel(2)
    rtn = client.get(url_for('.index'))
    assert rtn['test_id'] == 2
