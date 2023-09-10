class Kvadrat(GeometriskFigur):
    def __init__(self, sidlängd):
        super().__init__("Kvadrat")
        self.sidlängd = sidlängd

    def area(self):
        return self.sidlängd ** 2

    def omkrets(self):
        return 4 * self.sidlängd

    def visa_information(self):
        return f"Figur: {self.namn}, Sidelängd: {self.sidlängd}, Area: {self.area()}, Omkrets: {self.omkrets()}"



