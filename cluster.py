import pandas as pd
import yaml
import json


from pathlib import Path
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score


params = yaml.safe_load(open('params.yaml'))['cluster']
k = params['k']
file = params['file']

data_file = Path('data/normalized/'+file)
plots_file = Path('prc.json')

df = pd.read_csv(data_file)
model = KMeans(n_clusters=k)
labels = model.fit_predict(df)

score_silhouette = silhouette_score(df, labels, metric='euclidean')
score_db = davies_bouldin_score(df, labels)
print(score_db)
print(score_silhouette)

with open(plots_file, 'a') as f:
    json.dump(
        {
            'file': file,
            'k': k,
            'scores': {
                'silhouette': score_silhouette,
                'davies_bouldin': score_db
            }
        }, f)
