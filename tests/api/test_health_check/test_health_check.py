def test_health_check(client):
    response = client.get("")
    assert response.status_code == 200
    assert response.json() == {"status": "Ok", 'version': '0.1.0'}