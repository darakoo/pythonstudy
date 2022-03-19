class Candy:
    country = 'korea'

    def __init__(self, shape, color) -> None:
        self.shape = shape
        self.color = color
    
    def __del__(self):
        print('del called')
    
    def candy_info(self):
        print(f'shape is {self.shape}')
        print(f'color is {self.color}')
        print(f'Candy.country is {Candy.country}')
        print(f'self.country is {self.country}')

candy = Candy('square', 'blue')
candy.candy_info()
# print(f'country is {Candy.country}')
