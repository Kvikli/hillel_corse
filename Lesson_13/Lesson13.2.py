class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        if start < self.min_value or start > self.max_value:
            raise ValueError(f"Початкове значення {start} виходить за межі [{self.min_value}, {self.max_value}]")
        self.current = start

    def set_max(self, max_value):
        if max_value < self.min_value:
            raise ValueError(f"Максимальне значення {max_value} не може бути менше мінімального {self.min_value}")
        self.max_value = max_value
        if self.current > self.max_value:
            self.current = self.max_value

    def set_min(self, min_value):
        if min_value > self.max_value:
            raise ValueError(f"Мінімальне значення {min_value} не може бути більше максимального {self.max_value}")
        self.min_value = min_value
        if self.current < self.min_value:
            self.current = self.min_value

    def step_up(self):
        if self.current >= self.max_value:
            raise ValueError("Досягнуто максимуму")
        self.current += 1

    def step_down(self):
        if self.current <= self.min_value:
            raise ValueError("Досягнуто мінімуму")
        self.current -= 1

    def get_current(self):
        return self.current


# Приклади перевірки
counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Достигнут минимум
assert counter.get_current() == 7, 'Test4'
