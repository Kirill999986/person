class Person:
    def __init__(self, name = 'Petya', health_status = 75, mood = 75, capital = 1253.60):
        self.name = name
        self.health_status = health_status
        self.mood = mood
        self.capital = capital

    def work(self):
        self.capital = self.capital + 500
        self.health_status = self.health_status - 15
        self.mood = self.mood - 30
    def wolk(self):
        self.mood = self.mood + 10
    def go_to_the_doctor(self):
        self.capital = self.capital - 300
        self.health_status = self.health_status + 30
    def __str__(self):
        return \
            f' === {self.name} ===\n' \
            f' состояние здоровья {self.health_status}\n' \
            f' настроение {self.mood}\n' \
            f' капитал {self.capital}\n'