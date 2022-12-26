from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(250))
    email = db.Column(db.String(250))
    people = db.relationship('Person', secondary='favorites_people', backref='users')
    planets = db.relationship('Planet', secondary='favorites_planets', backref='users')
    ships = db.relationship('Ship', secondary='favorites_ships', backref='users')

    def save(self):
        db.session.add(self)  # INSERT
        db.session.commit()  # Guarda el INSERT

    def update(self):
        db.session.commit()  # Guarda el UPDATE

    def delete(self):
        db.session.delete(self)  # DELETE
        db.session.commit()  # Guarda el DELETE

    def get_people(self):
        return list(map(lambda person: person.to_dict(), self.people))
    
    def get_planets(self):
        return list(map(lambda planet: planet.to_dict(), self.planets))
    
    def get_ships(self):
        return list(map(lambda ship: ship.to_dict(), self.ships))

    def to_dict(self):
        return {
            "id": self.id,
            "password": self.password,
            "email": self.email
        }

class Person(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    height = db.Column(db.String(250))
    mass = db.Column(db.String(250))
    hair_color = db.Column(db.String(250))
    skin_color = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))
    birth_year = db.Column(db.String(250))
    gender = db.Column(db.String(250))

    def save(self):
        db.session.add(self)  # INSERT
        db.session.commit()  # Guarda el INSERT

    def update(self):
        db.session.commit()  # Guarda el UPDATE

    def delete(self):
        db.session.delete(self)  # DELETE
        db.session.commit()  # Guarda el DELETE

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender
        }
        
class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    rotation_period = db.Column(db.String(250))
    orbital_period = db.Column(db.String(250))
    diameter = db.Column(db.String(250))
    climate = db.Column(db.String(250))
    gravity = db.Column(db.String(250)) 
    terrain = db.Column(db.String(250))
    surface_water = db.Column(db.String(250))
    population = db.Column(db.String(250))
    

    def save(self):
        db.session.add(self)  # INSERT
        db.session.commit()  # Guarda el INSERT

    def update(self):
        db.session.commit()  # Guarda el UPDATE

    def delete(self):
        db.session.delete(self)  # DELETE
        db.session.commit()  # Guarda el DELETE

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "population": self.population
        }

class Ship(db.Model):
    __tablename__ = 'ships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    model = db.Column(db.String(250))
    manufacturer = db.Column(db.String(250))
    cost_in_credits = db.Column(db.String(250))
    length = db.Column(db.String(250))
    max_atmosphering_speed = db.Column(db.String(250))
    crew = db.Column(db.String(250))
    passengers = db.Column(db.String(250))
    cargo_capacity = db.Column(db.String(250))
    consumables = db.Column(db.String(250))
    hyperdrive_rating = db.Column(db.String(250))
    MGLT = db.Column(db.String(250))
    starship_class = db.Column(db.String(250))
    

    def save(self):
        db.session.add(self)  # INSERT
        db.session.commit()  # Guarda el INSERT

    def update(self):
        db.session.commit()  # Guarda el UPDATE

    def delete(self):
        db.session.delete(self)  # DELETE
        db.session.commit()  # Guarda el DELETE

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "crew": self.crew,
            "passengers": self.passengers,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "hyperdrive_rating": self.hyperdrive_rating,
            "MGLT": self.MGLT,
            "starship_class": self.starship_class
        }

class FavoritePerson(db.Model):
    __tablename__ = 'favorites_people'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    person_id = db.Column(db.Integer, db.ForeignKey('people.id'))

    def save(self):
        db.session.add(self)  # INSERT
        db.session.commit()  # Guarda el INSERT

    def update(self):
        db.session.commit()  # Guarda el UPDATE

    def delete(self):
        db.session.delete(self)  # DELETE
        db.session.commit()  # Guarda el DELETE

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "person_id": self.person_id
        }

class FavoritePlanet(db.Model):
    __tablename__ = 'favorites_planets'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))

    def save(self):
        db.session.add(self)  # INSERT
        db.session.commit()  # Guarda el INSERT

    def update(self):
        db.session.commit()  # Guarda el UPDATE

    def delete(self):
        db.session.delete(self)  # DELETE
        db.session.commit()  # Guarda el DELETE

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }

class FavoriteShip(db.Model):
    __tablename__ = 'favorites_ships'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    ship_id = db.Column(db.Integer, db.ForeignKey('ships.id'))

    def save(self):
        db.session.add(self)  # INSERT
        db.session.commit()  # Guarda el INSERT

    def update(self):
        db.session.commit()  # Guarda el UPDATE

    def delete(self):
        db.session.delete(self)  # DELETE
        db.session.commit()  # Guarda el DELETE

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "ship_id": self.ship_id
        }
        