from model import CircleModel

class CircleView:
    def get_radius(self):
        return float(input("Enter the radius of the circle: "))

    def set_area(self, area):
        print(f"The area of the circle is {area:.2f}")


class CircleController:
    def __init__(self, model, view):
        self._model = model
        self._view = view

        self._update_area()

    def run(self):
        radius = self._view.get_radius()
        self._model.set_radius(radius)
        self._update_area()

    def _update_area(self):
        area = self._model.get_area()
        self._view.set_area(area)

if __name__ == '__main__':
    model = CircleModel()
    view = CircleView()
    controller = CircleController(model, view)

    controller.run()