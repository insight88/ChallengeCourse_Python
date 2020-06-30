class Car():

    def __init__(self, **kwargs):
    # class 내부에 기본으로 정의된 함수 __init__을 재정의
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")
        # get(key, default_value)
    
    def __str__(self):
        return f"Car with {self.wheels} wheels"

class Convertible(Car):
# inheriting, extended class of Car

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # super : parent class에 접근하는 명령어
        self.time = kwargs.get("time", 10)

    def take_off(self):
        return "taking off"

    def __str__(self):
        return f"Car with no roof"

porche = Convertible(color="green", price="$40")
print(porche.color)