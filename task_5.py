class Results():
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses

    def number_of_wins(self, sport):
        return f'{sport} побед: {self.victories}'
    def number_of_draws(self, sport):
        return f'{sport} ничьих: {self.draws}'
    def number_of_losses(self, sport):
        return f'{sport} поражений: {self.losses}'
    def total_points(self, coefficient):
        return f'Общее количество очков: {self.victories * coefficient + self.draws}'
    
class Football(Results):
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)
    
    def number_of_wins(self):
        return super().number_of_wins('Футбольных')
    def number_of_draws(self):
        return super().number_of_draws('Футбольных')
    def number_of_losses(self):
        return super().number_of_losses('Футбольных')
    def total_points(self):
        return super().total_points(3)

class Hockey(Results):
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)
    
    def number_of_wins(self):
        return super().number_of_wins('Хокейных')
    def number_of_draws(self):
        return super().number_of_draws('Хокейных')
    def number_of_losses(self):
        return super().number_of_losses('Хокейных')
    def total_points(self):
        return super().total_points(2)
    
football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

for i in football_team, hockey_team:
    print(i.number_of_wins())
    print(i.number_of_draws())
    print(i.number_of_losses())
    print(i.total_points())

