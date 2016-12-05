from operator import mul

class Recipe:
    def __init__(self, filename):
        self.ingredients = dict()
        self.parse(filename)

    def parse(self, filename):
        with open(filename, 'r') as input:
            for line in input:
                name = line.split(':')[0]
                self.ingredients[name] = dict()
                characteristics = line.split(':')[1].strip(' \n').split(', ')
                for characteristic in characteristics:
                    split = characteristic.split(' ')
                    self.ingredients[name][split[0]] = int(split[1])

    def GetTotalScore(self, ingredientAmounts):
        assert sum(ingredientAmounts.values()) == 100
        totalCharacteristics = [0 for _ in range(len(self.ingredients[self.ingredients.keys()[0]]))]
        totalCalories = 0
        for ingredient in ingredientAmounts:
            ingredientCharacteristics = self.ingredients[ingredient]
            amount = ingredientAmounts[ingredient]
            for i, ingredientCharacteristic in enumerate(ingredientCharacteristics):
                value = self.ingredients[ingredient][ingredientCharacteristic]
                if ingredientCharacteristic == 'calories':
                    totalCalories += amount * value
                totalCharacteristics[i] += amount * value
        totalCharacteristics = [max(0, value) for value in totalCharacteristics]
        score = reduce(mul, totalCharacteristics) / totalCalories
        return score


    def GetTotalScorePart2(self, ingredientAmounts):
        assert sum(ingredientAmounts.values()) == 100
        totalCharacteristics = [0 for _ in range(len(self.ingredients[self.ingredients.keys()[0]]))]
        totalCalories = 0
        for ingredient in ingredientAmounts:
            ingredientCharacteristics = self.ingredients[ingredient]
            amount = ingredientAmounts[ingredient]
            for i, ingredientCharacteristic in enumerate(ingredientCharacteristics):
                value = self.ingredients[ingredient][ingredientCharacteristic]
                if ingredientCharacteristic == 'calories':
                    totalCalories += amount * value

                totalCharacteristics[i] += amount * value
        totalCharacteristics = [max(0, value) for value in totalCharacteristics]
        if totalCalories == 500:
            score = reduce(mul, totalCharacteristics) / totalCalories
            return score
        return 0

    def GetOptimalAmounts(self):
        bestTotalScore = 0
        bestIngredients = dict()
        for amounts in self.GetAllPossibleCombinations(len(self.ingredients.keys()), 100):
            ingredientAmounts = dict(zip(self.ingredients.keys(), amounts))
            score = self.GetTotalScore(ingredientAmounts)
            if score > bestTotalScore:
                bestIngredients = ingredientAmounts
                bestTotalScore = score
        return bestIngredients, bestTotalScore


    def GetOptimalAmountsPart2(self):
        bestTotalScore = 0
        bestIngredients = dict()
        for amounts in self.GetAllPossibleCombinations(len(self.ingredients.keys()), 100):
            ingredientAmounts = dict(zip(self.ingredients.keys(), amounts))
            score = self.GetTotalScorePart2(ingredientAmounts)
            if score > bestTotalScore:
                bestIngredients = ingredientAmounts
                bestTotalScore = score
        return bestIngredients, bestTotalScore

    def GetAllPossibleCombinations(self, n, s):
        if n == 1:
            yield (s,)
        else:
            for i in xrange(s + 1):
                for j in self.GetAllPossibleCombinations(n - 1, s - i):
                    yield (i,) + j

if __name__ == '__main__':
    recipe = Recipe('input.txt')
    bestCombination, bestScore = recipe.GetOptimalAmounts()
    print 'Part 1: ', bestScore
    best2, score2 = recipe.GetOptimalAmountsPart2()
    print 'Part 2: ', score2