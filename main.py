import time
from dataSetBuilder import DataSetScrape
from dataSetCleanAndPrepare import dataSetBasicAnalyze


def main():
    # dataSet_Builder = DataSetScrape()
    # start = time.process_time()
    # print('starting')

    # dataSet_Builder.basic_data_build()
    # dataSet_Builder.data_vegetarian_build()
    # dataSet_Builder.data_chicken_build()
    # dataSet_Builder.data_meat_build()
    # dataSet_Builder.data_seafood_build()
    # dataSet_Builder.data_rice_build()
    # dataSet_Builder.data_bread_build()
    # dataSet_Builder.data_desserts_build()
    #dataSet_Builder.data_durga_puja_build()

    # print('time spent in scraping', time.process_time() - start, 'seconds')

    base_analyze = dataSetBasicAnalyze()
    base_analyze.dataset_clean_prepare()


if __name__ == "__main__":
    main()
