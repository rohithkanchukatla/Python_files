class figures:
    info='figures are many'
    def __init__(self,name) -> None:
        self.name='swuaree'
    
    
    
    
class Square(figures):
    #desc='I have 4 sides'

    def __init__(self,name) -> None:
        super().__init__(name)
        self.name=name
    
    def number(self):
        print(f'square of {self.name} has four sides and height is ')
    


square1=Square('name')
square1.height=10


square1.number()
print(square1.info)


