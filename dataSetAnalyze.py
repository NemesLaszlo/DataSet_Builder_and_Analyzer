import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import style
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

style.use('ggplot')


class dataAnalyzer:

    def __init__(self):
        self.df = pd.read_csv("dataset.csv")
        self.df_string = pd.read_csv("dataset.csv")
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

    def veg_non_column_kmeans(self):
        X = np.array(self.numerical_dataset.drop(['Veg_Non', 'Review', 'Price'], 1).astype(float))
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

    def sub_catagory_classification(self):
        numpy_datas_list_in_list = self.numpy_array_dataset.T

        catagory = numpy_datas_list_in_list[4]
        nutrient = numpy_datas_list_in_list[8]

        catagory_label = self.numerical_dataset.keys()[4]
        nutrient_label = self.numerical_dataset.keys()[8]

        plt.scatter(nutrient, catagory, c=np.array(self.numerical_dataset['sub_catagory']))
        plt.title('sub_catagory classification visualization')
        plt.xlabel(nutrient_label)
        plt.ylabel(catagory_label)

        plt.show()

    def sub_catagory_k_neighbors_classifier(self):
        data_predict_sub_catagory = np.array(self.numerical_dataset['sub_catagory'])
        data_without_sub_catagory = np.array(
            self.numerical_dataset.drop(['sub_catagory', 'Name', 'Price', 'description', 'Review'], 1).astype(float))

        x_train, x_test, y_train, y_test = train_test_split(data_without_sub_catagory, data_predict_sub_catagory,
                                                            random_state=0)
        knn = KNeighborsClassifier(n_neighbors=1)

        knn.fit(x_train, y_train)
        return round(knn.score(x_test, y_test), 2)

    def most_reviewed_recepites(self):
        keys = [cat for cat, df in self.df_string.groupby(['catagory'])]

        plt.bar(keys, self.df_string.groupby(['catagory']).sum()['Review'])
        plt.ylabel('Review')
        plt.xlabel('Catagory')
        plt.xticks(keys, rotation='vertical', size=4)

        plt.show()

    def catagory_price_review_plots(self):
        catagory_group = self.df_string.groupby('catagory')
        reviews_sum = catagory_group.sum()['Review']
        keys = [pair for pair, df in catagory_group]
        prices = self.df_string.groupby('catagory').mean()['Price']

        fig, ax1 = plt.subplots()

        ax2 = ax1.twinx()
        ax1.bar(keys, reviews_sum, color='g')
        ax2.plot(keys, prices, color='b')

        ax1.set_xlabel('Catagory')
        ax1.set_ylabel('Reviews', color='g')
        ax2.set_ylabel('Price ($)', color='b')
        ax1.set_xticklabels(keys, rotation='vertical', size=4)

        plt.show()
