import argparse
import random
import re
import nltk
from utils import read_json

len_choice = ["very_short", "short", "medium", "long", "very_long", "all"]


def sentence_preprocessing(sentence):
    # separate the sentences by punctuations and remove the comma right after words
    sentences = [s.replace(",", "").strip() for s in re.split(f'[!.()?]', sentence) if s]
    return sentences


def run(sentence):
    sentence1 = sentence_preprocessing(sentence)
    print(sentence1)
    print([nltk.pos_tag(s.split(" ")) for s in sentence1])
    print(sum([len(s.split(" ")) for s in sentence1]), "words")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str, required=True)
    parser.add_argument('--length', default='all', choices=len_choice)
    args = parser.parse_args()
    yelp_review = read_json(f'{args.data_path}/yelp-dataset/yelp_academic_dataset_review.json')
    yelp_review["text_length"] = yelp_review["text"].apply(lambda x: len(x.split(" ")))
    q_len = [0] + [yelp_review["text_length"].quantile(q) for q in [0.25, 0.5, 0.75, 0.95]] + [yelp_review["text_length"].max()]
    length_map = {len_choice[i]: [q_len[i], q_len[i + 1]] for i in range(5)}
    if args.length != "all":
        sentence = random.choice(
            yelp_review[
                (yelp_review["text_length"] >= length_map[args.length][0]) &
                (yelp_review["text_length"] <= length_map[args.length][1])
            ]["text"].values
        )
        run(sentence)
    else:
        for key in length_map:
            sentence = random.choice(
                yelp_review[
                    (yelp_review["text_length"] >= length_map[key][0]) &
                    (yelp_review["text_length"] <= length_map[key][1])
                ]["text"].values
            )
            run(sentence)
