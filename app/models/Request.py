class Request:
    
    def __init__(
        self,
        role: str = None,
        context: str = None,
        gender: str = None,           # 'masculino' o 'femenino'
        age: int = None,
        weight : float = None,
        illnesses: str = None,
        allergies: str = None,
        preferences: str = None,
        restricted: str = None,
        location: str = None,
        skill: str = None,
        cost: str = None,
        cuisine: str = None,
        days: int = None,
        calories: int = None,
        meals: int = None,
        snacks: int = None,
    ):
        self.role = role
        self.context = context
        self.gender = gender
        self.age = age
        self.weight = weight
        self.illnesses = illnesses
        self.allergies = allergies
        self.preferences = preferences
        self.restricted = restricted
        self.location = location
        self.cuisine = cuisine
        self.skill = skill
        self.cost = cost
        self.days = days
        self.calories = calories
        self.meals = meals
        self.snacks = snacks

    def __repr__(self):
        return (
            f"Request(role={self.role!r}, context={self.context!r}, gender={self.gender!r}, age={self.age!r}, weight={self.weight!r}, "
            f"illnesses={self.illnesses!r}, allergies={self.allergies!r}, preferences={self.preferences!r}, "
            f"restricted={self.restricted!r}, location={self.location!r}, "
            f"cuisine={self.cuisine!r}, skill={self.skill!r}, cost={self.cost!r}, days={self.days!r}, calories={self.calories!r}, meals={self.meals!r}, snacks={self.snacks!r})"
    )