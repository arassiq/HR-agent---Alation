import pandas as pd

class DataCleaning:
    def __init__(self, data_path: str):
        self.data = pd.read_csv(data_path)
        self.clean_save_path = "data/Employee_dataset_cleaned.csv"
        print("Succesfully loaded data")

    def clean_phone(self, phone_number):
        number = str(phone_number).replace("-", "")
        if len(number) != 10:
            return None

        return f"({number[0:3]}) {number[3:6]}-{number[6:11]}"

    def clean_data(self):
        self.data = self.data.drop_duplicates(subset=["Email"])

        self.data["Phone"] = self.data["Phone"].apply(self.clean_phone)

        self.data["Salary"] = self.data["Salary"].round(0).astype("Int64")

        self.data[["Department", "Region"]] = (self.data["Department_Region"].str.split("-", expand=True))
        self.data = self.data.drop(columns=["Department_Region"])

        self.data.to_csv(self.clean_save_path, index=False)

        print(f"Succesfully cleaned data and saved to: {self.clean_save_path}")

        return self.clean_save_path
