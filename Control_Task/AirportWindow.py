
from controller import Controller
from my_window import *


class AirportWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, main_controller: Controller):
        super().__init__()
        self.setupUi(self)
        self.main_controller = main_controller
        # связываем смену данных в комбобоксе с функцией заполнения списка аэропортами
        self.comboBox.currentIndexChanged.connect(self.fill_airports)
        self.countries = self.main_controller.load_countries()
        self.fill_combobox_countries()
        # связываем клик по кнопке с методом открытия карты
        self.pushButton.clicked.connect(self.open_map)


    def open_map(self):
        name_airport = self.comboBox_2.currentText()
        country_name = self.comboBox.currentText()
        airports = self.countries[country_name].airports
        airport = None
        for a in airports:
            if a.display_name() == name_airport:
                airport = a
        self.main_controller.display_map(airport.latitude, airport.longitude)

    # функция заполнения странами
    def fill_combobox_countries(self):
        for k in self.countries:
            self.comboBox.addItem(k)

    # функция заполнения аэропортами
    def fill_airports(self):
        country_name = self.comboBox.currentText()
        airports = self.countries[country_name].airports
        self.comboBox_2.clear()
        for a in airports:
            self.comboBox_2.addItem(a.display_name())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    contr = Controller()
    mainWindow = AirportWindow(contr)
    mainWindow.show()
    sys.exit(app.exec())
