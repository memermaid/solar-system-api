import pytest
from app import create_app, db
from flask.signals import request_finished
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({'TESTING': True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app
    
    with app.app_context():
        db.drop_all()
        
    
@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def three_saved_planets(client):
    mercury = Planet(id=1, name='Mercury', description='radius_km 2440, temperature_F: 800, color: Yellow, distance_from_sun_km : 57909227', fun_fact='It is shrinking.')
    venus =  Planet(id=2, name='Venus', description='radius_km 6051.8, temperature_F: 867, color:Green and purple, distance_from_sun_km: 108209475', fun_fact='Its spine clockwise on its axis.')
    earth= Planet(id=3, name='Earth', description='radius_km 6378, temperature_F 57, color: Green and blue, distance_from_sun_km: 149600000', fun_fact='Has uneven gravitational field.')
    

    db.session.add_all([mercury, venus, earth])
    db.session.commit()