def eat(food, is_healthy):
    message = "unhealthy"
    
    # checking the instance of boolean...
    if not isinstance(is_healthy, bool):
        raise ValueError

    if is_healthy:
        message = "healthy"
    return f"I am eating {food}, which is {message}"

def nap(number_of_hours):
    if number_of_hours >= 2:
        return f"Yoo this is a long nap"
    return f"Yoo this is a short nap"