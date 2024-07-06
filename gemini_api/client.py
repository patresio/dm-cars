import google.generativeai as genai
from decouple import config

genai.configure(api_key=config("GOOGLE_API_KEY"))


def get_car_ai_bio(model, brand, year):
    model = genai.GenerativeModel("gemini-1.0-pro-latest")
    prompt = f"""
        Faça uma descrição de venda do carro {model} da marca {brand} do ano {year} em apenas 250 caracteres. Mostre as melhores especificações do modelo.
    """
    response = model.generate_content(prompt)
    return response.text
