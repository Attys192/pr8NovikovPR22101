class Nikola:
    __slots__ = ['name', 'age'] 
    def __init__(self, name, age):
        if name == "Николай":
            self.name = name
        else:
            self.name = f"Я не {name}, а Николай"
        self.age = age
    def __setattr__(self, key, value):
        if key not in self.__slots__:
            raise AttributeError(f"Нельзя добавить '{key}' в класс Nikola")
        super().__setattr__(key, value)
        
person1 = Nikola("Николай", 30)
print(person1.name) 

person2 = Nikola("Максим", 25)
print(person2.name)  

person3 = Nikola("Никита", 18)
print(person3.name)
try:
    person1.lastname = "Иванов"
except AttributeError as e:
    print(e)
        

    