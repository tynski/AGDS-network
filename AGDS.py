from countNumberFrequency import countNumberFrequency
import numpy as np


class AGDS(object):
    def __init__(self):
        self.sepal_length = {}
        self.sepal_width = {}
        self.petal_length = {}
        self.petal_width = {}
        self.species = {}
        self.flowers = {}

    def add_params(self):
        self.sepal_length = countNumberFrequency(sorted([flower[0] for flower in list(self.flowers.values())]))
        self.sepal_width = countNumberFrequency(sorted([flower[1] for flower in list(self.flowers.values())]))
        self.petal_length = countNumberFrequency(sorted([flower[2] for flower in list(self.flowers.values())]))
        self.petal_width = countNumberFrequency(sorted([flower[3] for flower in list(self.flowers.values())]))
        self.species = countNumberFrequency(sorted([flower[4] for flower in list(self.flowers.values())]))

        self.sepal_length_max = max(self.sepal_length)
        self.sepal_length_min = min(self.sepal_length)
        self.sepal_width_max = max(self.sepal_width)
        self.sepal_width_min = min(self.sepal_width)

        self.petal_length_max = max(self.petal_length)
        self.petal_length_min = min(self.petal_length)
        self.petal_width_max = max(self.petal_width)
        self.petal_width_min = min(self.petal_width)

        self.species_max = max(self.species)
        self.species_min = min(self.species)

    def add_flowers(self, iris):
        for i in range(len(iris.target)):
            self.flowers['R' + str(i)] = [iris.data[i, 0], iris.data[i, 1], iris.data[i, 2], iris.data[i, 3], iris.target[i]]

    def compute_weights(self, flower1, flower2):
        features1 = self.flowers[flower1]
        features2 = self.flowers[flower2]
        r_sepal_length = self.sepal_length_max - self.sepal_length_min
        r_sepal_width = self.sepal_width_max - self.sepal_width_min
        r_petal_length = self.petal_length_max - self.petal_length_min
        r_petal_width = self.petal_width_max - self.petal_width_min
        r_species = self.species_max - self.species_min

        sepal_length_weight = 1 - abs(features1[0] - features2[0]) / r_sepal_length
        sepal_width_weight = 1 - abs(features1[1] - features2[1]) / r_sepal_width
        petal_length_weight = 1 - abs(features1[2] - features2[2]) / r_petal_length
        petal_width_weight = 1 - abs(features1[3] - features2[3]) / r_petal_width
        species_weight = 1 - abs(features1[4] - features2[4]) / r_species

        weights = [sepal_length_weight, 
                    sepal_width_weight, 
                    petal_length_weight, 
                    petal_width_weight, 
                    species_weight]
        
        return np.around(weights, decimals=3)



