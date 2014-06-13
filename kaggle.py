import pandas as pd
import numpy as np


def get_df(fn):
    # Read in the csv values
    df = pd.read_csv(fn, sep ='\t', na_values='?')

    # Deal with NaN values
    sections = ['is_news', 'news_front_page']
    for section in sections:
        df[section][pd.isnull(df[section])] = 0

    df['alchemy_category'][pd.isnull(df['alchemy_category'])] = 'other'
    df['alchemy_category_score'][pd.isnull(df['alchemy_category_score'])] = 0.0


def tokenize_df(df, n_grams):
    json_in = df['boilerplate']
    content = ' '.join([json_in[x] for x in item_list if x in json_in])


    return



if __name__ == '__main__':

    df = get_df('train.tsv')

    tokens = tokenize_df
