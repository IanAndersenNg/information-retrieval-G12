import argparse
import pandas as pd
from preprocess import full_preprocess, preprocessing_report
from utils import load_data, evaluate_model
from model import SentimentModel

def main(args):
    # print("Loading dataset...")
    df = load_data(args.data_path, max_reviews=args.max_reviews)
    
    print("--------------------------------------------------------")
    print(f"\nTotal reviews loaded: {len(df)}")
    # print("\nPreprocessing text data...")
    df['processed_text'] = df['text'].apply(full_preprocess)
    # print("Text preprocessing completed.")

    # Output preprocessing report
    preprocessing_report(df)
    print("\n--------------------------------------------------------")

    # Assign sentiment labels based on stars
    def classify_stars(stars):
        if stars >= 4:
            return 'positive'
        elif stars == 3:
            return 'neutral'
        else:
            return 'negative'

    df['sentiment_label'] = df['stars'].apply(classify_stars)

    #print("\nInitializing sentiment model...")
    sentiment_model = SentimentModel()

    #print("\nTraining model on processed reviews...")
    X_test_vec, y_test = sentiment_model.train(df['processed_text'], df['sentiment_label'])
    print(f"Model training completed. Evaluating on {len(y_test)} test samples.")

    y_pred = sentiment_model.model.predict(X_test_vec)
    evaluate_model(y_test, y_pred)
    print("\n--------------------------------------------------------")

    # print("\nTop important words contributing to sentiment classification:")
    # sentiment_model.top_features()

    print("\nRetrieving Top-5 Most Positive Reviews based on model confidence scores:")

    X_texts_for_test = df['processed_text'].iloc[y_test.index].reset_index(drop=True)
    original_meta = df[['useful', 'funny', 'cool']].iloc[y_test.index].reset_index(drop=True)

    # print("Basic Statistics of 'useful' Votes in Test Set:")
    # print(original_meta['useful'].describe())
    # print("Max useful vote:", original_meta['useful'].max())
    # print("Min useful vote:", original_meta['useful'].min())
    # print()

    # print("Sample rows with highest useful votes:")
    # print(original_meta.sort_values(by='useful', ascending=False).head(10))

    top_reviews = sentiment_model.rank_reviews_by_positive_score(X_texts_for_test, original_meta, 5)

    for i, row in top_reviews.iterrows():
        print(f"\nRank {i+1}:")
        print(f"Confidence Score: {row['positive_score']:.4f} ")
        print(f"Review Text: {row['review_text'][:150]}...")

    if args.save_model:
        sentiment_model.save_model()
        print("\nModel and vectorizer have been saved successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sentiment Detector on Yelp Reviews")
    parser.add_argument("--data_path", type=str, required=True, help="Path to review.json")
    parser.add_argument("--max_reviews", type=int, default=10000, help="Maximum number of reviews to load")
    parser.add_argument("--save_model", action="store_true", help="Save the trained model and vectorizer")

    args = parser.parse_args()
    main(args)
