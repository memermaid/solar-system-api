from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, fun_fact):
        self.id = id
        self.name = name
        self.description = description
        self.fun_fact = fun_fact

planets = [Planet(1, 'Mercury', {'radius_km': 2440, 'temperature_F': 800, 'color':'Yellow', 'distance_from_sun_km': 57909227},'It is shrinking.'),
            Planet(2, 'Venus', {'radius_km': 6051.8, 'temperature_F': 867, 'color':'Green and purple', 'distance_from_sun_km': 108209475},'Its spine clockwise on its axis.'),
            Planet(3, 'Earth', {'radius_km': 6378, 'temperature_F': 57, 'color':'Green and blue', 'distance_from_sun_km': 149600000}, 'Has uneven gravitational field.'),
            Planet(4, 'Mars', {'radius_km': 33962, 'temperature_F': -82, 'color':'red', 'distance_from_sun_km': 227943824}, 'Has 2 moons called Deimos and Phobos.'),
            Planet(5, 'Jupiter', {'radius_km': 71492 ,'temperature_F': -238, 'color':'gray and red', 'distance_from_sun_km': 778340821}, 'Clouds On Jupiter Are Only 50 km Thick.'),
            Planet(6, 'Saturn', {'radius_km': 60268 , 'temperature_F': -285, 'color':'yellow and brown', 'distance_from_sun_km': 1426666000}, 'It could float in water because it is mostly made of gas.'),
            Planet(7, 'Uranus', {'radius_km': 25559 ,'temperature_F': -353, 'color':'blue-green', 'distance_from_sun_km': 2870658000}, 'Turns on its axis once every 17 hours, 14 minutes.'),
            Planet(8, 'Neptune', {'radius_km': 24764 , 'temperature_F': -373, 'color':'blue', 'distance_from_sun_km': 4498396000}, 'Only One Human Spacecraft Has Performed a Flyby of Neptune.')]
            
planets_bp = Blueprint('planets_bp', __name__, url_prefix='/planets')

@planets_bp.route('', methods=['GET'])
def get_all_planets():
    planets_resp = []
    for planet in planets:
        planets_resp.append({
            'id': planet.id,
            'name': planet.name,
            'description': planet.description,
            'fun_fact': planet.fun_fact
        })
    return jsonify(planets_resp)