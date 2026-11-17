class Phone:
    def __init__(self, brand, model, color, storage, year, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.storage = storage
        self.year = year
        self.price = price


    def __str__(self):
        return f'{self.brand} {self.model} {self.color} {self.storage} {self.year} {self.price}'

    def to_dict(self) -> dict:
        return {"brand": self.brand, "model": self.model, "color": self.color, "storage": self.storage, "year": self.year, "price": self.price}

    @staticmethod
    def from_dict(dict_data) -> Phone:
        return Phone(dict_data["brand"], dict_data["model"], dict_data["color"], dict_data["storage"], dict_data["year"], dict_data["price"])


