import argparse
import numpy as np
import pandas as pd
from utils import read_json
from sklearn.feature_extraction.text import TfidfVectorizer


def tf_idf_analysis(corpus, topk=100):
    tf_idf = TfidfVectorizer(sublinear_tf=True, stop_words="english")
    vec = tf_idf.fit_transform(corpus)
    print(vec.shape)
    word_mean = vec.mean(axis=0).tolist()[0]
    print(len(word_mean))
    top_scored_words = np.argsort(word_mean)[::-1][0:topk]
    return tf_idf.get_feature_names_out()[top_scored_words]


def run(postive_reviews, negative_reviews):
    positive_words = tf_idf_analysis(postive_reviews)
    negative_words = tf_idf_analysis(negative_reviews)
    common_words = list(set(positive_words) & set(negative_words))
    print("positive words:")
    print(sorted([word for word in positive_words if word not in common_words]))
    print("negative words:")
    print(sorted([word for word in negative_words if word not in common_words]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str, required=True)
    args = parser.parse_args()
    yelp_review = read_json(f'{args.data_path}/yelp-dataset/yelp_academic_dataset_review.json')
    amazon_review = pd.read_csv('amazon-fine-food-reviews/Reviews.csv')
    trip_review = pd.read_csv('trip-advisor-hotel-reviews/tripadvisor_hotel_reviews.csv')
    imdb_review = pd.read_csv('imdb-dataset-of-50k-movie-reviews/IMDB Dataset.csv')
    print("Yelp")
    run(
        yelp_review[yelp_review["stars"] >= 4].text,
        yelp_review[yelp_review["stars"] < 3].text
    )
    print("Amazon")
    run(
        amazon_review[amazon_review["Score"] >= 4].Text,
        amazon_review[amazon_review["Score"] < 3].Text
    )
    print("Trip Advisor")
    run(
        trip_review[trip_review["Rating"] >= 4].Review,
        trip_review[trip_review["Rating"] < 3].Review
    )
    print("IMDB")
    run(
        imdb_review[imdb_review["sentiment"] == "positive"].review,
        imdb_review[imdb_review["sentiment"] == "negative"].review
    )
