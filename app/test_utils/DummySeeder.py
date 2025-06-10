from app.models.Request import Request
import random

def dummyRequest():
    return Request(role=" Eres un nutricionista experto en dietas y amplios conocimientos de cocina nacional e internacional",
        context=random.choice([
            "Quiero mejorar mi rendimiento físico",
            "Busco una dieta saludable",
            "Necesito bajar de peso"
        ]),
        gender=random.choice(["masculino", "femenino"]),
        age=random.randint(18, 65),
        weight=round(random.uniform(50, 120), 1),
        illnesses=random.choice(["Diabetes", "Ninguna", "Hipertensión"]),
        allergies=random.choice(["Maní", "Gluten", "Ninguna"]),
        preferences=random.choice(["Keto", "Vegano", "Vegetariano", "Omnívoro"]),
        liked=random.choice(["Pollo", "Arroz", "Frutas"]),
        disliked=random.choice(["Brócoli", "Tofu", "Pescado"]),
        restricted=random.choice(["Lácteos", "Azúcar", "Ninguno"]),
        medical=random.choice(["Baja en sal", "Alta en fibra", "Sin restricciones"]),
        location=random.choice(["Bogotá, Colombia", "Madrid, España", "CDMX, México"]),
        skill=random.choice(["bajo", "medio", "alto"]),
        cuisine=random.choice(["local", "italiana", "japonesa", "mexicana"]),
        days=random.randint(1, 7),
        calories=random.randint(800, 4000),
        meals=random.randint(1, 5),
        snacks=random.randint(1, 5),
    )
