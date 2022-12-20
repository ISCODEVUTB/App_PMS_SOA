class Cart(object):

    def __init__(self, id_product: int, name: str = "Name", sup_name: str = "Name", price: int = 0, motor: str = "Name",
                 security: str = "Name", gearbox: str = "Name") -> None:
        """Cart builder object"""

        self._id_product = id_product
        self._name = name
        self._price = price
        self._motor = motor
        self._security = security
        self._gearbox = gearbox
        self._sup_name = sup_name

    @property
    def id_product(self) -> int:
        return self._id_product

    @id_product.setter
    def id_product(self, id_product: int) -> None:
        self._id_product = id_product

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def motor(self) -> str:
        return self._motor

    @motor.setter
    def motor(self, motor: str) -> None:
        self._motor = motor

    @property
    def security(self) -> str:
        return self._security

    @security.setter
    def security(self, security: str) -> None:
        self._security = security

    @property
    def gearbox(self) -> str:
        return self._gearbox

    @gearbox.setter
    def gearbox(self, gearbox: str) -> None:
        self._gearbox = gearbox

    @property
    def sup_name(self) -> str:
        return self._sup_name

    @sup_name.setter
    def sup_name(self, sup_name: str) -> None:
        self._sup_name = sup_name

    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def price(self, price: int) -> None:
        self._price = price

    def car_info(self, info: dict):
        return f"This is a car {info}"