import glob
import os

import pandas as pd


def combine(path, filename):
    os.chdir(path)
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

    # combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
    # export to csv
    combined_csv.to_csv(filename,
                        index=False,
                        encoding='utf-8-sig')
