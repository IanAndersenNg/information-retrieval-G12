from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd


class SentimentModel:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            max_features=10000,  # Limit vocabulary size
            min_df=5,            # Ignore very rare words
            ngram_range=(1, 2),  # Use unigrams and bigrams
            stop_words=None      # We already remove stopwords in preprocessing
        )
        self.model = LogisticRegression(max_iter=1000, random_state=42)

    # Train TF-IDF + Logistic Regression model.
    def train(self, texts, labels):
        X_train, X_test, y_train, y_test = train_test_split(
            texts, labels, test_size=0.2, random_state=42, stratify=labels
        )

        # Transform texts to TF-IDF vectors
        X_train_vec = self.vectorizer.fit_transform(X_train)
        X_test_vec = self.vectorizer.transform(X_test)

        self.model.fit(X_train_vec, y_train)

        return X_test_vec, y_test 

    # Predict labels for given texts.
    def predict(self, texts):
        X_vec = self.vectorizer.transform(texts)
        return self.model.predict(X_vec)

    def top_features(self, n=10):

        feature_names = self.vectorizer.get_feature_names_out()
        coefs = self.model.coef_  
        classes = self.model.classes_

        for idx, sentiment in enumerate(classes):
            coef = coefs[idx]
            top_positive_idx = coef.argsort()[::-1][:n]
            top_negative_idx = coef.argsort()[:n]

            print(f"\nTop words for class '{sentiment}':")
            print("Positive Contribution:")
            for i in top_positive_idx:
                print(f"  {feature_names[i]}: {coef[i]:.4f}")
            print("Negative Contribution:")
            for i in top_negative_idx:
                print(f"  {feature_names[i]}: {coef[i]:.4f}")


    def save_model(self, model_path="sentiment_model.pkl", vectorizer_path="tfidf_vectorizer.pkl"):
        """
        Save trained model and vectorizer.
        """
        joblib.dump(self.model, model_path)
        joblib.dump(self.vectorizer, vectorizer_path)
    
    def rank_reviews_by_positive_score(self, X_texts, original_meta, top_n=5):
        X_vec = self.vectorizer.transform(X_texts)
        positive_probs = self.model.predict_proba(X_vec)[:, list(self.model.classes_).index('positive')]

        ranked_df = pd.DataFrame({
            'review_text': X_texts,
            'positive_score': positive_probs,
            'useful': original_meta['useful'].values,
            'funny': original_meta['funny'].values,
            'cool': original_meta['cool'].values
        })

        ranked_df = ranked_df.sort_values(by='positive_score', ascending=False).head(top_n)
        return ranked_df.reset_index(drop=True)

