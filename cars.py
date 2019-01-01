import csv
import os


class CarBase:

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        t = os.path.splitext(self.photo_file_name)
        return t[1]

    @property
    def car_type(self):
        if isinstance(self, Car):
            return "car"
        elif isinstance(self, Truck):
            return "truck"
        elif isinstance(self, SpecMachine):
            return "spec_machine"
        else:
            return ""


        
class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        whl = body_whl.split("x")
        try:
            self.body_width = float(whl[0])
        except Exception:
            self.body_width = 0.0
        
        try:
            self.body_height = float(whl[1])
        except Exception:
            self.body_height = 0.0

        try:
            self.body_length = float(whl[2])
        except Exception:
            self.body_length = 0.0

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                car_type = row[0]
                brand = row[1]
                carrying = float(row[5])
                photo_file_name = row[3]
            except Exception:
                pass
            else:
                if (car_type == "car"):
                    try:
                        passenger_seats_count = int(row[2])
                    except Exception:
                        pass
                    else:
                        new_car = Car(brand, photo_file_name, carrying, passenger_seats_count)
                        car_list.append(new_car) 
                elif (car_type == "truck"):
                    try:
                        body_whl = row[4]
                    except Exception:
                        pass
                    else:
                        new_track = Truck(brand, photo_file_name, carrying, body_whl)
                        car_list.append(new_track)
                elif (car_type == "spec_machine"):
                    try:
                        extra = row[6]
                    except Exception:
                        pass
                    else:
                        new_spec_machine = SpecMachine(brand, photo_file_name, carrying, extra)
                        car_list.append(new_spec_machine)
            #print(row)
    return car_list


#for car in get_car_list("cars.csv"):
#     if isinstance(car, Truck): 
#    print(car.car_type)





