def test_good(client):
    response = client.get('/good')
    assert response.status_code == 200

