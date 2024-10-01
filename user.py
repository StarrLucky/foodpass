class user:
    login = ""
    pasword = ""
    meals = []

    def __init__(self, login, password, meals) -> None:
        self.login = login
        self.pasword = password
        self.meals = meals
    
    def test(self):
        print(self.meals)

