import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
df_pca=pd.read_csv("pca.csv")
loaded_model = pickle.load(open('kmeans.pkl', 'rb'))
b=pd.read_csv("columns.csv")
b=list(pd.read_csv("columns.csv").columns)

def calculate_score(data):
	best_case=int(data["0"])+int(data["2"]) + int(data["4"])+int(data["6"])+int(data["8"])
	worst_case=int(data["1"])+ int(data["3"]) + int(data["5"])+int(data["7"]) +int(data["9"])
	range = best_case - worst_case
	if range>=-20 and range<= -10:
		return 1
	if range>=-10 and range<= 0:
		return 2
	if range>=0 and range<= 10:
		return 3
	if range>=10 and range<= 20:
		return 4
