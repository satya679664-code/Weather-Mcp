import urllib.request



def get_weather(location:str) -> str:
    """

    Fetches the current weather for a given location using the wttr.in service.

    Args:
        location (str): The location for which to fetch the weather.

    Returns:
        str: A string containing the current weather information for the specified location.
   """
    
    url = f"https://wttr.in/{location}?format=3"
    try:
        with urllib.request.urlopen(url) as response:
            result = response.read().decode('utf-8')
            return result
    except Exception as e:
        return f"Error fetching weather data: {e}"



# get_weather("India")