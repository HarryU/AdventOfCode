import CookieRecipe
import unittest

class TestCookieRecipe(unittest.TestCase):
    def setUp(self):
        self.filename = 'testInput.txt'

    def test_ParsingIngredients(self):
        recipe = CookieRecipe.Recipe(self.filename)
        testIngredients = {'Butterscotch': {'capacity': -1, 'durability': -2, 'flavor': 6, 'texture': 3, 'calories': 8},
                     'Cinnamon': {'capacity': 2, 'durability': 3, 'flavor': -2, 'texture': -1, 'calories': 3}}
        self.assertEqual(testIngredients, recipe.ingredients)

    def test_RecipeTotalValue(self):
        recipe = CookieRecipe.Recipe(self.filename)
        testIngredientAmounts = {'Butterscotch':44,
                                 'Cinnamon': 56}
        self.assertEqual(62842880, recipe.GetTotalScore(testIngredientAmounts))

    def test_FindOptimalProportions(self):
        recipe = CookieRecipe.Recipe(self.filename)
        testIngredientAmounts = {'Butterscotch': 44,
                                 'Cinnamon': 56}
        optimalAmouts, bestScore = recipe.GetOptimalAmounts()
        self.assertEqual(testIngredientAmounts, optimalAmouts)

    def test_Part2TotalScore(self):
        recipe = CookieRecipe.Recipe(self.filename)
        testIngredientAmounts = {'Butterscotch': 40,
                                 'Cinnamon': 60}
        self.assertEqual(57600000, recipe.GetTotalScorePart2(testIngredientAmounts))

    def test_Part2OptimalProportions(self):
        recipe = CookieRecipe.Recipe(self.filename)
        testIngredientAmounts = {'Butterscotch': 40,
                                 'Cinnamon': 60}
        optimalAmouts, bestScore = recipe.GetOptimalAmountsPart2()
        self.assertEqual(testIngredientAmounts, optimalAmouts)
