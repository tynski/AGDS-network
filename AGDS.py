from countNumberFrequency import countNumberFrequency


class AGDS(object):
    def __init__(self):
        self.sepal_length = {}
        self.sepal_width = {}
        self.petal_length = {}
        self.petal_width = {}
        self.species = {}
        self.flowers = {}
        self.weights = {}

    def add_params(self):
        self.sepal_length = countNumberFrequency(sorted([flower[0] for flower in list(self.flowers.values())]))
        self.sepal_width = countNumberFrequency(sorted([flower[1] for flower in list(self.flowers.values())]))
        self.petal_length = countNumberFrequency(sorted([flower[2] for flower in list(self.flowers.values())]))
        self.petal_width = countNumberFrequency(sorted([flower[3] for flower in list(self.flowers.values())]))
        self.species = countNumberFrequency(sorted([flower[4] for flower in list(self.flowers.values())]))

    def add_flowers(self, iris):
        for i in range(len(iris.target)):
            self.flowers['R' + str(i)] = [iris.data[i, 0], iris.data[i, 1], iris.data[i, 2], iris.data[i, 3], iris.target[i]]

    def compute_weights(self, flower1, flower2):
        features1 = self.flowers[flower1]
        features2 = self.flowers[flower2]


