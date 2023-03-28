from PyQt5 import QtWidgets
from model import CircleModel
import sys

class CircleView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self._radius_label = QtWidgets.QLabel("Radius:")
        self._radius_spinbox = QtWidgets.QSpinBox()
        self._area_label = QtWidgets.QLabel("Area:")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self._radius_label)
        layout.addWidget(self._radius_spinbox)
        layout.addWidget(self._area_label)

        self.setLayout(layout)

    def get_radius(self):
        return self._radius_spinbox.value()

    def set_area(self, area):
        self._area_label.setText(f"Area: {area:.2f}")


class CircleController:
    def __init__(self, model, view):
        self._model = model
        self._view = view

        self._view._radius_spinbox.valueChanged.connect(self._on_radius_changed)

        self._update_area()

    def _on_radius_changed(self, radius):
        self._model.set_radius(radius)
        self._update_area()

    def _update_area(self):
        area = self._model.get_area()
        self._view.set_area(area)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    model = CircleModel()
    view = CircleView()
    controller = CircleController(model, view)

    view.show()

    sys.exit(app.exec_())
