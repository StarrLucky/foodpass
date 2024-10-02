class user:
    username = ""
    password = ""
    meals = []

    def __init__(self, username, password, meals) -> None:
        self.username = username
        self.password = password
        self.meals = meals
    
    def test(self):
        print(self.meals)

