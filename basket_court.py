from cat.mad_hatter.decorators import tool, hook

@tool
def court_basket(city, cat):
    """Which basketball court do you want to book? Input is the city."""
    court = {
        "Rome": "Celio",
        "Naples": "Quartieri Spagnoli",
        "Milan": "Lambrate",
    }

    response = cat.llm("Find a city near: Milan.")

    if city not in court.keys():
        return response
    else:
        return f"{court[city]}"
    
@hook
def agent_prompt_prefix(prefix, cat):

    prefix = """You are Mario the former basketball player. You're an expert in Basketball, and you learn kids how to play motherfucker street basketball.
"""

    return prefix