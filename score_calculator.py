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
	ext_score=20+int(data["0"])-int(data["1"])+int(data["2"])-int(data["3"])+int(data["4"])-int(data["5"])+int(data["6"])-int(data["7"])+int(data["8"])-int(data["9"])
	est_score=38-int(data["10"])+int(data["11"])-int(data["12"])+int(data["13"])-int(data["14"])-int(data["15"])-int(data["16"])-int(data["17"])-int(data["18"])-int(data["19"])
	agr_score=14-int(data["20"])+int(data["21"])-int(data["22"])+int(data["23"])-int(data["24"])+int(data["25"])-int(data["26"])+int(data["27"])+int(data["28"])+int(data["29"])
	csn_score=14+int(data["30"])-int(data["31"])+int(data["32"])-int(data["33"])+int(data["34"])-int(data["35"])+int(data["36"])-int(data["37"])+int(data["38"])+int(data["39"])
	opn_score=8+int(data["40"])-int(data["41"])+int(data["42"])-int(data["43"])+int(data["44"])-int(data["45"])+int(data["46"])+int(data["47"])+int(data["48"])+int(data["49"])

	ext_score_new=0+ext_score
	est_score_new=0+est_score
	agr_score_new=0+agr_score
	csn_score_new=0+csn_score
	opn_score_new=0+opn_score

	time_list=list(map(int, data['timeCount'].split(',')))
	del data['timeCount']
	positive_time=time_list[0]+time_list[2]+time_list[4]+time_list[6]+time_list[8]+time_list[11]+time_list[13]+time_list[21]+time_list[23]+time_list[25]+time_list[27]+time_list[28]+time_list[29]+time_list[30]+time_list[32]+time_list[34]+time_list[36]+time_list[38]+time_list[39]+time_list[40]+time_list[42]+time_list[44]+time_list[46]+time_list[47]+time_list[48]+time_list[49]
	if positive_time>180 and agr_score>20:
		agr_score_new-=4
	for i in range(1,6):
		if list(data.values()).count(str(i))>40:
			if csn_score>20:
				csn_score_new-=4
			break
	if list(data.values()).count('3')>40 and opn_score>20:
		opn_score_new-=4
	answers_consistency=[int(data["7"])+int(data["8"]),int(data["10"])+int(data["11"]),int(data["11"])+int(data["12"]),int(data["13"])+int(data["19"]),int(data["20"])+int(data["21"]),int(data["21"])+int(data["26"]),int(data["31"])+int(data["36"]),int(data["33"])+int(data["36"]),int(data["35"])+int(data["36"]),int(data["34"])+int(data["37"]),int(data["37"])+int(data["38"]),int(data["41"])+int(data["46"]),int(data["42"])+int(data["45"])]
	if answers_consistency.count(6)==len(answers_consistency) and est_score>20:
		est_score_new-=4

	df=pd.read_csv("percentile.csv")
	percentile={"ext_percentile":df.iloc[ext_score]['EXT_count'],"est_percentile":df.iloc[est_score]['EST_count'],"agr_percentile":df.iloc[agr_score]['AGR_count'],"opn_percentile":df.iloc[opn_score]['OPN_count'],"csn_percentile":df.iloc[csn_score]['CSN_count']}
	my_data=[]
	temp=[]
	for i in data:
		temp.append(float(data[i]))
	my_data.append(temp)
	temp=[]
	for i in range(50):
		temp.append(3.0)
	my_data.append(temp)
	my_data = pd.DataFrame(my_data, columns=b[:50])
	my_personality = loaded_model.predict(my_data)
	my_data['cluster'] = my_personality
	pca_fit = pca.fit_transform(my_data)
	df_pca1 = pd.DataFrame(data=pca_fit, columns=['PCA1', 'PCA2'])
	df_pca1['Clusters'] = my_data['cluster']
	plt.figure(figsize=(10,10))
	sns.scatterplot(data=df_pca, x='PCA1', y='PCA2', hue='Clusters', palette='tab10', alpha=0.8)
	plt.scatter(x=df_pca1['PCA1'][0], y=df_pca1['PCA2'][0], c='DarkBlue',s=80)
	plt.title('Personality Clusters Prediction')
	plt.savefig('static/images/alda.png')
	return {"original_scores":{"ext_score":ext_score,"est_score":est_score,"agr_score":agr_score,"csn_score":csn_score,"opn_score":opn_score},
			"new_scores":{"ext_score":ext_score_new,"est_score":est_score_new,"agr_score":agr_score_new,"csn_score":csn_score_new,"opn_score":opn_score_new},
			"percentile":percentile}