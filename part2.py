import argparse
import asyncio
from data_cleaning import DataCleaning
from agent_run import MainAgent


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data-path"
    )
    parser.add_argument(
        "--clean",
        action="store_true"
    )

    args = parser.parse_args()

    if args.clean:
        cleaner = DataCleaning(args.data_path)
        cleaned_data_path = cleaner.clean_data()
    else:
        cleaned_data_path = "data/Employee_dataset_cleaned.csv"


    query_agent = MainAgent(cleaned_data_path)
    print('enter "exit" to exit at any time')

    usr_in = ""
    while "exit" not in usr_in.lower():
        usr_in = input("Enter question to agent: ")
        if "exit" in usr_in.lower():
            break

        out = asyncio.run(
            query_agent.run_agent(usr_in)
        )
        print("\n", out, "\n\n")

    print("thank you for using my HR agent!")


if __name__ == "__main__":
    run()