class user:
    username = ""
    password = ""
    lunchboxes = []
    meals = []

    def __init__(self, username, password, meals, lunchboxes) -> None:
        self.username = username
        self.password = password
        self.meals = meals
        self.lunchboxes = lunchboxes
    
    def test(self):
        print(self.meals)

