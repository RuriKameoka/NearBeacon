import pandas as pd
import numpy as np
import glob

list_fileName_iOS = glob.glob('data/Day1_iOS/*.csv') # iOSファイル名のリスト

for i in range(0,len(list_fileName_iOS)):
	tmp_df = pd.read_csv(list_fileName_iOS[i])
	print(list_fileName_iOS[i], tmp_df["major"][0])
	array_epTime = np.array(np.int_(tmp_df["epoch_time"]))