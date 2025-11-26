

class Soldier:
    def __init__(self,personal_number:int,first_name:str,last_name:str,gender:str,city:str,distance:int,placement_status:str):
        if personal_number.isdigit():
            num = str(personal_number)
            if num.startswith('8'):
                self.personal_number = personal_number
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.city = city
        self.distance = distance
        self.placement_status = placement_status

class Drom:
    id = 1
    seats_available = 10
    def __init__(self):
        if Drom.seats_available == 0:
            raise ValueError("No seats available")
        self.id = Drom.id
        self.list_soldiers = []
        Drom.id += 1
        Drom.seats_available -= 1


class Residential_building:
    id = 1
    for _ in range(10):
        def __init__(self):
            self.id = Residential_building.id
            self.room = Drom()
            Residential_building.id += 1

class Base:
    id = 0
    if id == 0:
        for i in range(2):
            def __init__(self):
                Base.id += 1
                self.id = Base.id
                self.residential_building = Residential_building()
    else:
        def __init__(self):
            Base.id += 1
            self.id = Base.id
            self.residential_building = Residential_building()


