def kelvin_to_fahrenheit(kelvin):
    """
    takes an int in kelvin and converts it to fahrenheit
    """
    return round(kelvin * 1.8 - 459.67, 2)


def approx_coordinates(lat_, long_, decimal=5):
    """  
    rounds latitude and longitude coordinates to a given decimal place 
    default is 5.
    """
    return (round(lat_, decimal), round(long_, decimal))