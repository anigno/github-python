import random


def getDays():
    days = ['sun', 'mon', 'tue', 'wed', 'thr', 'fri', 'sat']
    return days


def getRandomWeatherReport():
    weather = ['sunny', 'rainy', 'hot', 'lovely']
    report = weather[random.randint(0, len(weather) - 1)]
    return report


def main():
    days = getDays()
    for d in days:
        r = getRandomWeatherReport()
        print("Weather on {0} is {1}".format(d, r))
    print("\nlast weather was: "+ r)


if __name__ == "__main__":
    main()
