from os import path
import time
from dataSetBuilder import DataSetScrape
from dataSetCleanAndPrepare import dataSetBasicAnalyze
from dataSetAnalyze import dataAnalyzer


def main():
    dataSet_File = str(path.exists('dataset.csv'))

    if not dataSet_File:
        dataSet_Builder = DataSetScrape()
        start = time.process_time()
        print('Starting!')
        dataSet_Builder.dataset_build_all()
        print('Time spent in scraping', time.process_time() - start, 'seconds.')

        print("Starting dataSet clean and build ... ")
        base_analyze = dataSetBasicAnalyze()
        base_analyze.dataset_clean_prepare()
        print("Everything fine!")

        analyzer = dataAnalyzer()
        kmeans_result = analyzer.veg_non_column_kmeans()
        print("KMeans result is {kmeans}.".format(kmeans=kmeans_result))

        knn_result = analyzer.sub_catagory_k_neighbors_classifier()
        print("KNeighborsClassifier result is {knn}".format(knn=knn_result))

        analyzer.most_reviewed_recepites()

        analyzer.catagory_price_review_plots()

        analyzer.sub_catagory_classification()
    else:
        print("dataset.csv exists!")
        analyzer = dataAnalyzer()

        kmeans_result = analyzer.veg_non_column_kmeans()
        print("KMeans result is {kmeans}".format(kmeans=kmeans_result))

        knn_result = analyzer.sub_catagory_k_neighbors_classifier()
        print("KNeighborsClassifier result is {knn}".format(knn=knn_result))

        analyzer.most_reviewed_recepites()

        analyzer.catagory_price_review_plots()

        analyzer.sub_catagory_classification()


if __name__ == "__main__":
    main()
