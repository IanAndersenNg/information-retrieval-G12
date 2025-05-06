import argparse
import random
import re
from collections import defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from utils import read_json


ps = PorterStemmer()


def get_frequency(corpus):
    tokens = []
    for text in corpus:
        # remove punctuation and lower all the characters
        tokens.extend(word_tokenize(re.sub(r"[^\w\s]", "", text.lower())))
        # tokens.extend(word_tokenize(text))
    stemmed_tokens = [ps.stem(w) for w in tokens]
    original_frequency = defaultdict(int)
    stemmed_frequency = defaultdict(int)
    for token in tokens:
        original_frequency[token] += 1
    for token in stemmed_tokens:
        stemmed_frequency[token] += 1
    original_frequency = sort_frequency(original_frequency)
    stemmed_frequency = sort_frequency(stemmed_frequency)
    return original_frequency, stemmed_frequency


def sort_frequency(counter):
    freq_arr = sorted([(key, value) for key, value in counter.items()], key=lambda x: x[1])
    return freq_arr[::-1]


def get_topk(freq, k, ignore_words):
    topk = []
    i = 0
    while len(topk) < k:
        if freq[i][0] not in ignore_words:
            topk.append(freq[i])
        i += 1
    return topk


def run(corpus):
    freq1, freq2 = get_frequency(corpus)
    print(
        "Top 10 before stemming: ",
        get_topk(freq1, 10,  ignore_words=stopwords.words("english"))
    )
    print("Top 10 after stemming: ",
          get_topk(freq2, 10, ignore_words=[ps.stem(w) for w in stopwords.words("english")])
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str, required=True)
    args = parser.parse_args()
    yelp_review = read_json(f'{args.data_path}/yelp-dataset/yelp_academic_dataset_review.json')
    b = random.choice(yelp_review["business_id"])
    selected_reviews = yelp_review[yelp_review["business_id"] == b]
    print(b, f"{len(selected_reviews)} reviews")
    run(selected_reviews["text"])
