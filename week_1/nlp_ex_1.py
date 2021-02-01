import streamlit as st

# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time

import re

"""
# NLP Quiz 1
"""

positive_div, negative_div = st.beta_columns([1, 1])
positive_input_text = None
negative_input_text = None
vocabulary = None
freq_count = None


@st.cache(allow_output_mutation=True)
def get_positive_data():
    return [], []


@st.cache(allow_output_mutation=True)
def get_negative_data():
    return [], []


with positive_div:
    positive_input_text = st.text_input(label="Enter positve tweet")
    add_pos_tweet = st.button("Add +ve tweet")

with negative_div:
    negative_input_text = st.text_input(label="Enter negative tweet")
    add_neg_tweet = st.button("Add -ve tweet")

create_vocabulary = st.button("Create vocabulary")

if add_pos_tweet and positive_input_text:
    get_positive_data()[0].append(positive_input_text)
    get_positive_data()[1].append("+")

if add_neg_tweet and negative_input_text:
    get_negative_data()[0].append(negative_input_text)
    get_negative_data()[1].append("-")


tweet_df = pd.DataFrame(
    data={
        "tweets": get_positive_data()[0] + get_negative_data()[0],
        "polarity": get_positive_data()[1] + get_negative_data()[1],
    }
)

if not tweet_df.empty:
    st.write(tweet_df)


if create_vocabulary:
    vocabulary = tweet_df["tweets"].str.split(" ").explode()
    set_tweets = pd.unique(tweet_df["tweets"].str.split(" ").explode())

    """### Unique Words"""
    st.write(pd.DataFrame(data={"word": set_tweets}))

    freq_count = vocabulary.value_counts()
    """### Word Count"""
    st.write(freq_count.T)


# vocab = negative_tweets_vocab + positive_tweets_vocab
# vocab = set(vocab)

# positive_tweets = ["I am happy because I am learning NLP", "I am happy"]
# negative_tweets = ["I am sad, I am not learning NLP", "I am sad"]

# # Build a Vocabulary from the positive and negative tweets
# positive_tweets_vocab = ' '.join(positive_tweets)
# positive_tweets_vocab = re.sub(",", '', positive_tweets_vocab)
# positive_tweets_vocab = positive_tweets_vocab.split()

# # Build Negative tweets vocabulary
# negative_tweets_vocab = ' '.join(negative_tweets)
# negative_tweets_vocab = re.sub(",", '', negative_tweets_vocab)
# negative_tweets_vocab = negative_tweets_vocab.split()

# # Build a vocabulary containing both negative and positve classes
# vocab = negative_tweets_vocab + positive_tweets_vocab
# vocab = set(vocab)

# print(f'vocabulary: {vocab}\n')
# print(f'The vocabulary is of length {len(vocab)}')
