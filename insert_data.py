from sklearn import datasets


def load_dataset_to_model(model):
    iris = datasets.load_iris()
    model.add_params(iris)
    model.add_flowers(iris)
