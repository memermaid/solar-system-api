def test_get_one_planet(client, three_saved_planets):
    response = client.get('/planets/2')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        'id': 2, 
        'name': 'Venus', 
        'description': 'radius_km 6051.8, temperature_F: 867, color:Green and purple, distance_from_sun_km: 108209475', 
        'fun_fact': 'Its spine clockwise on its axis.'
    }

def test_get_one_planet_not_existing_id(client):
    response = client.get('/planets/2')
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {'msg': 'Planet with id 2 does not exist'}


def test_get_all_planets(client, three_saved_planets):
    response = client.get('/planets')
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 3

def test_post_one_planet(client):
    response = client.post('/planets', json = {'id':1, 
                                            'name': 'Mars', 
                                            'description': 'radius_km: 33962, temperature_F: -82, color: red, distance_from_sun_km: 227943824', 
                                            'fun_fact':'Has 2 moons called Deimos and Phobos.'})
    response_body = response.get_json()

    assert response_body == {'msg': 'Successfuly created a planet with id 1'}
    assert response.status_code == 201