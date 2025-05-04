import re
import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Initialize English stopwords
STOPWORDS = set(stopwords.words('english'))

NEGATION_WORDS = set([
    "no", "not", "never", "n't", "none", "nobody", "nothing", "neither", "nowhere",
    "hardly", "scarcely", "barely"
])

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def handle_negation(text):
    tokens = word_tokenize(text)
    new_tokens = []
    negate = False
    negate_count = 0

    for token in tokens:
        if token in NEGATION_WORDS:
            negate = True
            negate_count = 0
            continue
        if negate and negate_count < 3:
            new_tokens.append('NOT_' + token)
            negate_count += 1
        else:
            negate = False
            new_tokens.append(token)
    return ' '.join(new_tokens)

def tokenize_and_remove_stopwords(text):
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token not in STOPWORDS]
    return ' '.join(tokens)

def full_preprocess(text):
    text = clean_text(text)
    text = handle_negation(text)
    text = tokenize_and_remove_stopwords(text)
    return text

def preprocessing_report(df, text_column='processed_text'):
    """
    Only print statistics after preprocessing:
    - Average, min, max word count
    - Top 10 frequent words
    """
    print("\n--- Preprocessing Analysis Report ---")
    
    df['word_count'] = df[text_column].apply(lambda x: len(x.split()))
    
    print(f"Average word count per review: {df['word_count'].mean():.2f}")
    print(f"Max word count in a review: {df['word_count'].max()}")
    print(f"Min word count in a review: {df['word_count'].min()}")

    all_words = ' '.join(df[text_column]).split()
    counter = Counter(all_words)
    top_10_words = counter.most_common(10)

    print("\nTop 10 frequent words after preprocessing:")
    for word, freq in top_10_words:
        print(f"{word}: {freq}")

def preprocessing_visualization(df, text_column='processed_text'):
    """
    Plot:
    - Word count distribution histogram
    - Top 10 frequent words bar chart
    """
    df['word_count'] = df[text_column].apply(lambda x: len(x.split()))
    
    plt.figure(figsize=(8,6))
    df['word_count'].plot(kind='hist', bins=30, color='skyblue', edgecolor='black')
    plt.title('Distribution of Review Word Counts')
    plt.xlabel('Word Count per Review')
    plt.ylabel('Number of Reviews')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    all_words = ' '.join(df[text_column]).split()
    counter = Counter(all_words)
    top_10_words = counter.most_common(10)

    top_words, top_counts = zip(*top_10_words)
    plt.figure(figsize=(8,6))
    plt.bar(top_words, top_counts, color='lightcoral', edgecolor='black')
    plt.title('Top 10 Frequent Words')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
