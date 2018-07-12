import pandas as pd
import argparse
from collections import OrderedDict
import numpy as np

def main(input_csv, amount, partition=False):
    df = pd.read_csv(input_csv)
    if 'youtube_id' in df.columns:
        columns = OrderedDict([
            ('youtube_id', 'video-id'),
            ('time_start', 'start-time'),
            ('time_end', 'end-time'),
            ('label', 'label-name')])
        df.rename(columns=columns, inplace=True)
    #
    a = df.values
    columns = df.columns
    del df
    if partition:
        
    else:
        a = np.random.permutation(a)
        a = a[:amount, :]

        df = pd.DataFrame(a, columns=columns)
        df = df.sort_values(by=['label-name'])
        df.to_csv("sample.csv", index=False, columns=columns)

if __name__ == '__main__':
    description = 'Random sample entries in dataset.'
    p = argparse.ArgumentParser(description=description)
    p.add_argument('input_csv', type=str,
                   help=('CSV file containing the following format: '
                         'YouTube Identifier,Start time,End time,Class label'))
    p.add_argument('amount', type=int, help="Number of samples to draw or the number of partitions to be split.")
    p.add_argument('partition', type="store_true", help="Partition the dataset into parts.")
    main(**vars(p.parse_args()))