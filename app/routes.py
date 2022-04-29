from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet

# planets = [Planet(1, 'Mercury', {'radius_km': 2440, 'temperature_F': 800, 'color':'Yellow', 'distance_from_sun_km': 57909227},'It is shrinking.'),
#             Planet(2, 'Venus', {'radius_km': 6051.8, 'temperature_F': 867, 'color':'Green and purple', 'distance_from_sun_km': 108209475},'Its spine clockwise on its axis.'),
#             Planet(3, 'Earth', {'radius_km': 6378, 'temperature_F': 57, 'color':'Green and blue', 'distance_from_sun_km': 149600000}, 'Has uneven gravitational field.'),
#             Planet(4, 'Mars', {'radius_km': 33962, 'temperature_F': -82, 'color':'red', 'distance_from_sun_km': 227943824}, 'Has 2 moons called Deimos and Phobos.'),
#             Planet(5, 'Jupiter', {'radius_km': 71492 ,'temperature_F': -238, 'color':'gray and red', 'distance_from_sun_km': 778340821}, 'Clouds On Jupiter Are Only 50 km Thick.'),
#             Planet(6, 'Saturn', {'radius_km': 60268 , 'temperature_F': -285, 'color':'yellow and brown', 'distance_from_sun_km': 1426666000}, 'It could float in water because it is mostly made of gas.'),
#             Planet(7, 'Uranus', {'radius_km': 25559 ,'temperature_F': -353, 'color':'blue-green', 'distance_from_sun_km': 2870658000}, 'Turns on its axis once every 17 hours, 14 minutes.'),
#             Planet(8, 'Neptune', {'radius_km': 24764 , 'temperature_F': -373, 'color':'blue', 'distance_from_sun_km': 4498396000}, 'Only One Human Spacecraft Has Performed a Flyby of Neptune.')]
            
planets_bp = Blueprint('planets_bp', __name__, url_prefix='/planets')

@planets_bp.route('', methods=['GET'])
def get_all_planets():
    planets = Planet.query.all()
    planets_response = []

    for planet in planets:
        planets_response.append({
        'id': planet.id,
        'name': planet.name,
        'description': planet.description,
        'fun_fact': planet.fun_fact
    })
    return jsonify(planets_response)

@planets_bp.route('', methods=['POST'])
def create_planet():
    request_body = request.get_json()

    new_planet = Planet(name=request_body['name'],
                        description=request_body['description'],
                        fun_fact=request_body['fun_fact'])
    
    db.session.add(new_planet)
    db.session.commit()

    return {'msg': f'Successfuly created a planet with id {new_planet.id}'}, 201


# @planets_bp.route('', methods=['GET'])
# def get_all_planets():
#     planets_resp = []
#     for planet in planets:
#         planets_resp.append({
#             'id': planet.id,
#             'name': planet.name,
#             'description': planet.description,
#             'fun_fact': planet.fun_fact
#         })
#     return jsonify(planets_resp)

# @planets_bp.route('/<planet_id>',methods = ['GET'])
# def get_one_planet(planet_id):
#     planet = validate_input(planet_id)
#     rsp = {
#         'id': planet.id,
#         'name': planet.name,
#         'description': planet.description,
#         'fun_fact': planet.fun_fact
#         }
#     return jsonify(rsp)

# def validate_input(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except ValueError:
#         abort(make_response({'msg': f'Invalid id {planet_id}'}, 400))
    
#     for planet in planets:
#         if planet_id == planet.id:
#             return planet

#     abort(make_response ({'msg': f'Planet with id {planet_id} does not exist'}, 404))
    