import time
from dataSetBuilder import DataSetScrape
from dataSetCleanAndPrepare import dataSetBasicAnalyze


def main():
    dataSet_Builder = DataSetScrape()
    start = time.process_time()
    print('Starting!')
    dataSet_Builder.dataset_build_all()
    print('Time spent in scraping', time.process_time() - start, 'seconds.')

    print("Starting dataSet clean and build ... ")
    base_analyze = dataSetBasicAnalyze()
    base_analyze.dataset_clean_prepare()
    print("Everything fine!")


if __name__ == "__main__":
    main()
