import pandas as pd
import sys

from pathlib import Path

input_file = Path(sys.argv[1])
cols_integers = ["f_07", "f_08", "f_09", "f_10", "f_11", "f_12", "f_13"]
cols_floats = ["f_22", "f_23", "f_24", "f_25", "f_26", "f_27", "f_28"]
integers_output = Path('data') / 'prepared' / 'integers.csv'
floats_output = Path('data') / 'prepared' / 'floats.csv'
both_output = Path('data') / 'prepared' / 'both.csv'

Path('data/prepared').mkdir(parents=True, exist_ok=True)

df = pd.read_csv(input_file, sep=',')

integers = df[cols_integers]
floats = df[cols_floats]
both = df[cols_floats+cols_integers]
integers.to_csv(integers_output, index=False)
floats.to_csv(floats_output, index=False)
both.to_csv(both_output, index=False)
