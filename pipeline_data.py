from PySide6.QtWidgets import QLabel, QApplication, QVBoxLayout, QWidget

class Sensor:
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor

    def alerta(self):
        if self.valor > 30:
            return f'Sensor {self.nombre}: ALERTA'
        else:
            return f'Sensor {self.nombre}: NORMAL'

with open('../datos.csv', encoding='utf-8-sig') as file:
    lines = file.read().splitlines()
    lines.pop(0)

lista_datos = []
lista_sensores = []
for line in lines:
    lista_datos.append(line.split(','))

for s in lista_datos:
    lista_sensores.append(Sensor(s[0], int(s[1])))

app = QApplication([])
ventana = QWidget()
layout = QVBoxLayout()

for sensor in lista_sensores:
    layout.addWidget(QLabel(sensor.alerta()))

ventana.setLayout(layout)
ventana.show()
app.exec()