class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        self.supplies = set(supplies)
        self.visited = set()
        result = []
        dict1 = {}
        for i in range(len(recipes)):
            dict1[recipes[i]] = ingredients[i]
        def dfs(recipe):
            if recipe in self.supplies:
                return True
            if recipe not in dict1:
                return False
            if recipe in self.visited:
                return False
            self.visited.add(recipe)
            for neighbour in dict1[recipe]:
                if not dfs(neighbour):
                    return False
            self.visited.remove(recipe)
            self.supplies.add(recipe)
            return True
        for i in recipes:
            self.visited = set()
            if dfs(i):
                result.append(i)

        return result