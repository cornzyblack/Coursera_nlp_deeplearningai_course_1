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
    return []


@st.cache(allow_output_mutation=True)
def get_negative_data():
    return []


with positive_div:
    positive_input_text = st.text_input(label="Enter positve tweet")

with negative_div:
    negative_input_text = st.text_input(label="Enter negative tweet")

add_tweet = st.button("Add tweet")

create_vocabulary = st.button("Create vocabulary")

if add_tweet and positive_input_text:
    get_positive_data().append(positive_input_text)

if add_tweet and negative_input_text:
    get_negative_data().append(negative_input_text)


tweet_df = pd.DataFrame(
    data=get_positive_data() + get_negative_data(), columns=["Tweets"]
)

if not tweet_df.empty:
    st.write(tweet_df)


if create_vocabulary:
    vocabulary = tweet_df["Tweets"].str.split(" ").explode()
    set_tweets = pd.unique(tweet_df["Tweets"].str.split(" ").explode())
    st.write(set_tweets)

    freq_count = vocabulary.value_counts()
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
