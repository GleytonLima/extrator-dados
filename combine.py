import glob
import os

import pandas as pd

os.chdir("./data/siasus_municipio_ano_mes_sexo")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
# export to csv
combined_csv.to_csv("sia_sus_manaus.csv",
                    index=False,
                    encoding='utf-8-sig')
