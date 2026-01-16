import pandas as pd
import matplotlib.pyplot as plt

class ExploratoryAnalysis:
    def __init__(self, data="data/Employee_dataset_cleaned.csv"):
        self.data = pd.read_csv(data)

    def preliminary_statistics(self):
        total_rows = len(self.data) #storing total rows for use in the uniqueness ratio, do not want to keep re-calculating
        #creating dataframe to ourput our statistics with
        out_df = pd.DataFrame(columns=["Uniqueness_Count", "Uniqueness_Ratio", "Mean", "Median", "Standard_Deviation"])
        
        for col in self.data:
            #only calculating numerical metrics on float and int column types
            if "int" in str(self.data[col].dtype) or "float" in str(self.data[col].dtype):
                unique_count = self.data[col].nunique() 
                out_df.loc[col] = {
                    "Uniqueness_Count": unique_count,
                    "Uniqueness_Ratio": unique_count / total_rows,
                    "Mean": round(self.data[col].mean(), 2),
                    "Median": self.data[col].median(),
                    "Standard_Deviation": round(self.data[col].std(), 2)
                }

            else:
                #metrics for non-numerical data types
                unique_count = self.data[col].nunique()
                out_df.loc[col] = {
                    "Uniqueness_Count": unique_count,
                    "Uniqueness_Ratio": unique_count / total_rows,
                    #"Mean": None,
                    #"Median": None,
                    #"Standard_Deviation": None
                }
        return out_df



    def calculated_statistics(self):
        #normalizing to the thousands place for clean output
        salary_per_department = (self.data.groupby("Department")["Salary"].sum() / 1000)

        salary_per_department.plot(kind="bar")
        plt.title("Total Salary per Department")
        plt.xlabel("Department")
        plt.ylabel("Total Salary (Thousands)")
        plt.xticks(rotation=35)
        plt.tight_layout()
        plt.show()

        #converting performance values to ordinal for use with bar chart, as i want to find the average before reporting
        performance_map = {
            "Poor": 1,
            "Average": 2,
            "Good": 3,
            "Excellent": 4
        }
        #updating our data frame to include ordinal performance, but not change the original scores
        self.data["Performance_Ordinal"] = self.data["Performance_Score"].map(performance_map)
        performance_by_department = (self.data.groupby("Department")["Performance_Ordinal"].mean()) #finding the mean for seamless reporting

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