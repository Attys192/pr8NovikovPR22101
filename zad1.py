class Soda:
    def __init__(self,supplements = None):
        self.supplements = supplements
    def show_my_drink(self):
        if self.supplements:
            print(f"Газировка и {self.supplements}")
        else:
           print("Обычная газировка")
supll1 = Soda("вишня")
supll1.show_my_drink()

supll2 = Soda("вода")
supll2.show_my_drink()

supll3 = Soda()
supll3.show_my_drink()



        
