import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix


def load_data(filepath, max_reviews=10000):
    import json

    data = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i >= max_reviews:
                break
            review = json.loads(line)
            text = review.get('text', None)
            stars = review.get('stars', None)
            useful = review.get('useful', 0)
            funny = review.get('funny', 0)
            cool = review.get('cool', 0)
            if text is not None and stars is not None:
                data.append({
                    'text': text,
                    'stars': stars,
                    'useful': useful,
                    'funny': funny,
                    'cool': cool
                })
    return pd.DataFrame(data)

def evaluate_model(y_true, y_pred):

    print("\n==Classification Report==")
    print(classification_report(y_true, y_pred, digits=4))
    
    labels = ["positive", "neutral", "negative"]

    print("\n==Confusion Matrix (Rows=True Labels, Columns=Predicted Labels)==")
    cm = confusion_matrix(y_true, y_pred, labels=labels)

    # Use pandas DataFrame for pretty printing
    cm_df = pd.DataFrame(cm, index=[f"True {label}" for label in labels],
                            columns=[f"Pred {label}" for label in labels])

    print(cm_df)