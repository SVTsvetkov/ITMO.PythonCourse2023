import json
import folium
import webbrowser
from country import Country
from airport import Airport


class Controller:
    # функция загрузки данных из json файла
    def load_countries(self):
        f = open('airports.json')
        data = json.load(f)
        f.close()
        countries = {}  # словарь стран
        for k in data:
            country_name = k['country']
            city_name = k['city']
            airport_name = k['airport']
            latitude = k['latitude']
            longitude = k['longitude']
            if country_name in countries:
                country = countries[country_name]
            else:
                country = Country(country_name)
                countries[country_name] = country
            airport = Airport(airport_name, city_name, latitude, longitude)
            country.airports.append(airport)

        return countries

    # функция для отображения координаты на карте
    def display_map(self, latitude, longitude):
        # Создаем карту с центром в указанных координатах
        my_map = folium.Map(location=[latitude, longitude], zoom_start=15)

        # Добавляем маркер с указанными координатами
        folium.Marker([latitude, longitude]).add_to(my_map)

        # Сохраняем карту в HTML файл
        my_map.save("map.html")

        # Открываем HTML файл в браузере
        webbrowser.open("map.html")
