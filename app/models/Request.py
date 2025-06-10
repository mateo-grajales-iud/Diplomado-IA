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
        liked: str = None,
        disliked: str = None,
        restricted: str = None,
        medical: str = None,
        location: str = None,
        skill: str = None,
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
        self.liked = liked
        self.disliked = disliked
        self.restricted = restricted
        self.medical = medical
        self.location = location
        self.cuisine = cuisine
        self.skill = skill
        self.days = days
        self.calories = calories
        self.meals = meals
        self.snacks = snacks

    def __repr__(self):
        return (
            f"Request(role={self.role!r}, context={self.context!r}, gender={self.gender!r}, age={self.age!r}, weight={self.weight!r}, "
            f"illnesses={self.illnesses!r}, allergies={self.allergies!r}, preferences={self.preferences!r}, liked={self.liked!r}, "
            f"disliked={self.disliked!r}, restricted={self.restricted!r}, medical={self.medical!r}, location={self.location!r}, "
            f"cuisine={self.cuisine!r}, skill={self.skill!r}, days={self.days!r}, calories={self.calories!r}, meals={self.meals!r}, snacks={self.snacks!r})"
    )