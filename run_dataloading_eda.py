from data_cleaning import DataCleaning
from exploratory_analysis import ExploratoryAnalysis, KMClustering
from agent_run import MainAgent
import asyncio


uncleaned_path = input("Please input uncleaned data path: ")

cleaner = DataCleaning(uncleaned_path)
cleaned_data_path = cleaner.clean_data()

exit() if "y" not in input("\nWould you like to go forward with descriptive statistics? ").lower() else print("\n") 

analysis = ExploratoryAnalysis(cleaned_data_path)

print(analysis.preliminary_statistics().to_markdown())

exit() if "y" not in input("\nWould you like to go forward with calculated statistics? ").lower() else print("\n") 

analysis.calculated_statistics()

exit() if "y" not in input("\nWould you like to go forward with clustering? ").lower() else print("\n") 

clustering = KMClustering(cleaned_data_path)

print(clustering.cluster().to_markdown())

exit() if "y" not in input("\nWould you like to go forward with agent questions? ").lower() else print("\n") 

usr_in = ""
query_agent = MainAgent(cleaned_data_path)
print("enter \"exit\" to exit at any time")

while "exit" not in usr_in.lower():
    usr_in = input("Enter question to agent: ")

    out = asyncio.run(
        query_agent.run_agent(
            usr_in
        )
    )
    print("\n", out,"\n\n")

print("thank you for using my HR agent!")