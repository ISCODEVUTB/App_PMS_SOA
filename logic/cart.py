class Cart(object):

    def __init__(self, idProduct: int, name: str = "Name", supName: str = "Name", price: int = 0, motor: str = "Name", security: str = "Name",
                 gearbox: str = "Name"):
        """Cart builder object"""

        self._idProduct = idProduct
        self._name = name
        self._price = price
        self._motor = motor
        self._security = security
        self._gearbox = gearbox
        self._supName = supName

    @property
    def idProduct(self) -> int:
        return self._idProduct

    @idProduct.setter
    def idProduct(self, idProduct: int):
        self._idProduct = idProduct

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def prince(self, price: int):
        self._price = price

    @property
    def motor(self) -> str:
        return self._motor

    @motor.setter
    def motor(self, motor: str):
        self._motor = motor

    @property
    def security(self) -> str:
        return self._security

    @security.setter
    def security(self, security: str):
        self._security = security

    @property
    def gearbox(self) -> str:
        return self._gearbox

    @gearbox.setter
    def gearbox(self, gearbox: str):
        self._gearbox = gearbox

    @property
    def supName(self) -> str:
        return self._supName

    @supName.setter
    def supName(self, supName: str):
        self._supName = supName

    def __str__(self):
        return '({0}, {1}, {2}, {3}, {4}, {5})'.format(self.idProduct, self.name, self.supName, self.price, self.motor, self.security,
                                                  self.gearbox)


if __name__ == '__main__':
    carro = Cart(idProduct=1, name="AUDI R8", price=1049200218)
    print(carro)