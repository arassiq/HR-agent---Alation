import pandas as pd
import matplotlib.pyplot as plt
import scipy

class ExploratoryAnalysis:
    def __init__(self, data="data/Employee_dataset_cleaned.csv"):
        self.data = pd.read_csv(data)

    def preliminary_statistics(self):
        total_rows = len(self.data)
        for col in self.data:
            if "int" in str(self.data[col].dtype) or "float" in str(self.data[col].dtype):
                unique_count = self.data[col].nunique()
                print(f"{col}: \n\tmean: {round(self.data[col].mean(), 2)}, \n\tmedian: {self.data[col].median()}, \n\tstandard deviation: {round(self.data[col].std(),2)}, \n\tunique_count: {unique_count}, \n\tuniqueness ratio: {unique_count/total_rows}")
            else: 
                unique_count = self.data[col].nunique()
                print(f"{col}: \n\tunique_count: {unique_count}, \n\tuniqueness ratio: {unique_count/total_rows}")



    def calculated_statistics(self):
        salary_per_department = (self.data.groupby("Department")["Salary"].sum() / 1000)

        salary_per_department.plot(kind="bar")
        plt.title("Total Salary per Department")
        plt.xlabel("Department")
        plt.ylabel("Total Salary (Thousands)")
        plt.xticks(rotation=35)
        plt.tight_layout()
        plt.show()

        performance_map = {
            "Poor": 1,
            "Average": 2,
            "Good": 3,
            "Excellent": 4
        }
        self.data["Performance_Ordinal"] = self.data["Performance_Score"].map(performance_map)
        performance_by_department = (self.data.groupby("Department")["Performance_Ordinal"].mean())

        performance_by_department.plot(kind="bar")
        plt.title("Performance by Department")
        plt.xlabel("Department")
        plt.ylabel("Performance (1=Poor, 4=Excellent)")
        plt.xticks(rotation=35)
        plt.tight_layout()
        plt.show()

        employees_by_region = (self.data.groupby("Region")["Employee_ID"].count())
        employees_by_region.plot(kind="bar")
        plt.title("Count of Employee by Region")
        plt.xlabel("Region")
        plt.ylabel("Employee Count")
        plt.xticks(rotation=35)
        plt.tight_layout()
        plt.show()

            

exploratory_analysis = ExploratoryAnalysis()
#exploratory_analysis.preliminary_statistics()
exploratory_analysis.calculated_statistics()