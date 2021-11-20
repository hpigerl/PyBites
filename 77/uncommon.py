def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
    cities between the two"""
    return (
        len(my_cities)
        + len(other_cities)
        - 2 * len([city for city in my_cities if city in other_cities])
    )
