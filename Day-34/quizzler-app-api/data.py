import requests

# Open Trivia DB Category IDs:
# 18 = Computers/Science, 9 = General Knowledge, None/Any = Any Category
CATEGORY_MAP = {
    "science": 18,
    "general": 9,
    "general knowledge": 9,
}

def get_question_data(amount: int = 10, category_name: str = "science") -> list:
    """Fetches boolean quiz questions dynamically from Open Trivia DB."""
    category_id = CATEGORY_MAP.get(category_name.strip().lower(), 18)

    parameters = {
        "amount": amount,
        "type": "boolean",
        "category": category_id,
    }
    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    return response.json()["results"]
