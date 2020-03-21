import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import style
from sklearn.cluster import KMeans
from sklearn import preprocessing
style.use('ggplot')


class dataAnalyzer:

    def __init__(self):
        self.df = pd.read_csv("dataset.csv")
        self.numerical_dataset = self.handle_non_numerical_data(self.df)
        self.numpy_array_dataset = self.numerical_dataset.to_numpy()

    # Non-Numeric columns convert to numeric values
    def handle_non_numerical_data(self, dataset):
        columns = dataset.columns.values

        for column in columns:
            text_digit_vals = {}

            def convert_to_int(val):
                return text_digit_vals[val]

            if dataset[column].dtype != np.int64:
                column_contents = dataset[column].values.tolist()
                unique_elements = set(column_contents)
                x = 0
                for unique in unique_elements:
                    if unique not in text_digit_vals:
                        text_digit_vals[unique] = x
                        x += 1

                dataset[column] = list(map(convert_to_int, dataset[column]))

        return dataset

    def column_Veg_Non_kmeans(self):
        X = np.array(self.numerical_dataset.drop(['Veg_Non'], 1).astype(float))
        X = preprocessing.scale(X)
        Y = np.array(self.numerical_dataset['Veg_Non'])

        kmeans = KMeans(n_clusters=2)
        kmeans.fit(X)

        correct = 0
        for i in range(len(X)):
            predict_me = np.array(X[i].astype(float))
            predict_me = predict_me.reshape(-1, len(predict_me))
            prediction = kmeans.predict(predict_me)
            if prediction[0] == Y[i]:
                correct += 1

        accuracy = (correct / len(X)) * 100  # accuracy
        return round(accuracy, 2)

    def catagory_classification(self):
        numpy_datas_list_in_list = self.numpy_array_dataset.T

        sub_catagory = numpy_datas_list_in_list[2]
        nutrient = numpy_datas_list_in_list[8]

        sub_catagory_label = self.numerical_dataset.keys()[2]
        nutrient_label = self.numerical_dataset.keys()[8]

        plt.scatter(nutrient, sub_catagory, c=self.numerical_dataset['catagory'])
        plt.xlabel(nutrient_label)
        plt.ylabel(sub_catagory_label)

        plt.show()

    def k_neighbors_classifier(self):
        pass
