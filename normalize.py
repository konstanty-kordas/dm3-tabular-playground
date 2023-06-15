import pandas as pd
import sys

from pathlib import Path

from sklearn.preprocessing import MinMaxScaler


input_folder = Path(sys.argv[1])

Path('data/normalized').mkdir(parents=True, exist_ok=True)

for input_file in input_folder.glob("*.csv"):
    df = pd.read_csv(input_file, sep=',')
    # print(df)
    norm = MinMaxScaler(feature_range=(0,1)).fit(df)
    data_minmax = pd.DataFrame(norm.transform(df), columns=norm.get_feature_names_out())
    new_path = list(input_file.parts)
    new_path[1] ="normalized"
    new_path = Path(*new_path)
    data_minmax.to_csv(new_path,index=False)
    # data_minmax.to_csv()

    # for col in df.columns:
    #     print(col)