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
        kmeans_result = analyzer.column_Veg_Non_kmeans()
        print("KMeans result is {kmeans}.".format(kmeans=kmeans_result))
    else:
        print("dataset.csv exists!")
        analyzer = dataAnalyzer()
        kmeans_result = analyzer.column_Veg_Non_kmeans()
        print("KMeans result is {kmeans}".format(kmeans=kmeans_result))


if __name__ == "__main__":
    main()
