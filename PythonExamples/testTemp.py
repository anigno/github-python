import timeit


spot = {
    "name": "Entity Name",
    "type": "Entity Type",
    "position": {
        "type": "Point", "coordinates": [35.7664567776933, 33.3206398118678, 1595.85032722353]
    },
    "ownerID": "AAA"
}

number_of_times = 100000




duration = timeit.timeit(setup='from copy import deepcopy', stmt=f'deepcopy({spot})', number=number_of_times)
print(f"{number_of_times} times of deepcopy(spot) took {duration} secs. Average of {duration / number_of_times} per sec.")
