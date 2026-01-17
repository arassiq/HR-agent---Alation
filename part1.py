import argparse
from data_cleaning import DataCleaning
from exploratory_analysis import ExploratoryAnalysis, KMClustering

def run():
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "--data-path",
        required=True
    )
    
    parser.add_argument(
        "--cluster",
        action="store_true"
    )

    args = parser.parse_args()

    cleaner = DataCleaning(args.data_path)
    cleaned_data_path = cleaner.clean_data()

    analysis = ExploratoryAnalysis(cleaned_data_path)
    print(analysis.preliminary_statistics().to_markdown())
    analysis.calculated_statistics()

    if args.cluster:
        clustering = KMClustering(cleaned_data_path)
        print(clustering.cluster().to_markdown())

if __name__ == "__main__":
    run()
