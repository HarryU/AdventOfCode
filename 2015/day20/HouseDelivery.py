import matplotlib.pyplot as plt


def totalPresents(house):
    total = 0
    factors = getFactors(house)
    for factor in factors:
        total += 10 * factor
    return total


def getFactors(number):
    factors = set()
    for i in range(1, int((number**0.5)+1)):
        if number % i == 0:
            factors.add(i)
            factors.add(number / i)
    return factors

if __name__ == '__main__':
    presents = 0
    input = 33100000
    i = 1
    houses = list()
    values = list()
    while presents < input:
        presents = totalPresents(i)
        print 'House ', i, ' gets ', presents
        i += 1
        houses.append(i)
        values.append(presents)

    plt.plot(houses, values)
    plt.show()
