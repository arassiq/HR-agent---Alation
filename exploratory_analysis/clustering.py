from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd 
import matplotlib.pyplot as plt

class KMClustering:
    def __init__(self, data="data/Employee_dataset_cleaned.csv"):
        self.data = pd.read_csv(data)

    def inertia_viz(self, X_scaled):
        inertia = []
        for k in range(1, 8):
            model = KMeans(n_clusters=k, n_init=10, random_state=42)
            model.fit(X_scaled)
            inertia.append(model.inertia_)
        
        plt.plot(range(1, 8), inertia, marker="o")
        plt.title("Inertia")
        plt.xlabel("clusters")
        plt.ylabel("values")
        plt.tight_layout()
        plt.show() # no clear elbow, change minimizes at 3 clusters

    def cluster(self):

        performance_map = {
            "Poor": 1,
            "Average": 2,
            "Good": 3,
            "Excellent": 4
        }

        #converting performance to ordinal
        self.data["Performance_Ordinal"] = self.data["Performance_Score"].map(performance_map)

        #converting remote work to a numerical boolean 
        self.data["Remote_Work"] = self.data["Remote_Work"].astype(int)

        #converting Join Date to years since joined
        self.data["Tenure_Years"] = ((pd.to_datetime("today") - pd.to_datetime(self.data["Join_Date"])).dt.days / 365)

        #scaling using eucladian distance so larger variables don't dominate clustering
        X = self.data[["Performance_Ordinal", "Remote_Work", "Salary", "Tenure_Years"]].dropna() #only clustering on our 4 numerical columns
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        #self.inertia_viz(X_scaled)

        #initializing the KMeans model and fitting onto our data with a cluster size of 4
        model = KMeans(n_clusters=4, n_init=10, random_state=42)
        clusters = model.fit_predict(X_scaled)

        #aggregation of clusters into dataframe for clean output 
        df_clustered = self.data.loc[X.index].copy()
        df_clustered["cluster"] = clusters

        df_clustered = df_clustered.groupby("cluster")[["Performance_Ordinal", "Remote_Work", "Salary", "Tenure_Years"]].mean()
        
        return df_clustered