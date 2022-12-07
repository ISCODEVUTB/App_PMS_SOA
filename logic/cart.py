class Cart(object):

    def __init__(self, id_product: int, name: str = "Name", sup_name: str = "Name", price: int = 0, motor: str = "Name",
                 security: str = "Name", gearbox: str = "Name"):
        """Cart builder object"""

        self._idProduct = id_product
        self._name = name
        self._price = price
        self._motor = motor
        self._security = security
        self._gearbox = gearbox
        self._supName = sup_name

    @property
    def id_product(self) -> int:
        return self._idProduct

    @id_product.setter
    def id_product(self, id_product: int):
        self._idProduct = id_product

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
    def sup_name(self) -> str:
        return self._supName

    @sup_name.setter
    def sup_name(self, sup_name: str):
        self._supName = sup_name

    def __str__(self):
        return '({0}, {1}, {2}, {3}, {4}, {5}, {6})'.format(self.id_product, self.name, self.sup_name, self.price, self.motor
                                                       , self.security, self.gearbox)


if __name__ == '__main__':
    car = Cart(id_product=1, name="AUDI R8", price=1049200218)
    print(car)
