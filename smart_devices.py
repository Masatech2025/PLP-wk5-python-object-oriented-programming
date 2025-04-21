class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB

    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB"

class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, strap_type):
        super().__init__(brand, model, storage)
        self.strap_type = strap_type

    def track_steps(self, steps):
        print(f"{self.model} tracked {steps} steps!")

    def get_info(self):
        return f"{self.brand} {self.model} with {self.storage}GB and a {self.strap_type} strap"


phone1 = Smartphone("Samsung", "Galaxy S21", 128)
phone2 = Smartphone("Apple", "iPhone 13", 256)

print(phone1.get_info())
phone2.make_call("+2348012345678")

watch = Smartwatch("Fitbit", "Versa 3", 4, "rubber")
print(watch.get_info())
watch.track_steps(10000)