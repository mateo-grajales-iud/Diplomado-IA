from app.utils.AIConstants import *
from google import genai

def writePrompt(request):
    data = request["request"]
    parts = []
    target = ("tarea: genera un plan de alimentación de acuerdo a la información que te proporcionare")
    responseFormat = ("formato respuesta: Responde en JSON solo con los siguientes campos"
                     "Resumen: resumen de la solicitud, "
                     "Plan: este campo incluye el plan, el cual esta definido en los siguientes campos: "
                     "Dia [numero dia]: Plan para ese dia, este trae cual comida es (enumera las comidas y"
                     " verifica que sea la misma cantidad que se solicita) en el campo comida; el campo "
                     "información nutricional, que trae la información nutricional relevante de acuerdo a "
                     "la solicitud; y el campo observaciones, en el cual puedes poner observaciones relevantes. Ejemplo"
                     "{\"Resumen\" : \"...\",\"Plan\" :{\"Dia #\" :{\"Comida #\" :{\"comida\" : \"...\",\"informacion_nutricional\" : \"...\",\"observaciones\" : \"...\"}}}}" )
    parts.append(target)
    parts.append(responseFormat)
    if data.context: parts.append(f"contexto: {data.context}")
    if data.gender: parts.append(f"género: {data.gender}")
    if data.age: parts.append(f"edad: {data.age}")
    if data.weight: parts.append(f"peso: {data.weight}")
    if data.illnesses: parts.append(f"enfermedades: {data.illnesses}")
    if data.allergies: parts.append(f"alergias: {data.allergies}")
    if data.preferences: parts.append(f"preferencias alimenticias: {data.preferences}")
    if data.restricted: parts.append(f"ingredientes no permitidos: {data.restricted}")
    if data.location: parts.append(f"ubicación: {data.location}")
    if data.skill: parts.append(f"nivel de habilidad para la cocina: {data.skill}")
    if data.cost: parts.append(f"costo para el platillo: {data.cost}")
    if data.cuisine: parts.append(f"tipo de cocina: {data.cuisine}")
    if data.days: parts.append(f"días a calcular: {data.days}")
    if data.calories: parts.append(f"calorías maximas: {data.calories}")
    if data.meals: parts.append(f"cantidad de comidas por dia: {data.meals}")
    if data.snacks: parts.append(f"cantidad de snacks por dia: {data.snacks}")
    prompt = "\n ".join(parts)
    return prompt