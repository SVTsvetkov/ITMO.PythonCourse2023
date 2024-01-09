# класс для хранения информации об аэропорте
class Airport:
    def __init__(self, name, city, latitude, longitude):
        self.name = name
        self.city = city
        self.latitude = latitude
        self.longitude = longitude

    # функция для отображения в комбобоксе
    def display_name(self):
        return f'{self.name} ({self.city})'
