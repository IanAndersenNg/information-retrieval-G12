import argparse
import json
import nltk
import re
import time
from nltk.tokenize import sent_tokenize
from collections import Counter

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

negation_words = [
    'no', 'not', 'never', 'none', 'nobody', 'nothing', 'nowhere', 'neither', 'nor',
]

negation_contractions = [
    "don't", "doesn't", "didn't", "isn't", "aren't", "wasn't", "weren't",
    "haven't", "hasn't", "hadn't", "won't", "wouldn't", "couldn't", "can't",
    "shouldn't", "mightn't", "mustn't"
]

negative_prefixes = ['un', 'in', 'im', 'il', 'ir', 'non', 'dis', 'mis']

non_negative_words = [
    'in', 'into', 'inside', 'information', 'include', 'indeed', 'incredibly',
    'under', 'until', 'understand', 
    'discover', 'discussion', 'display',
    'important', 'improve', 'impression', 'impressive'
]

all_negation_patterns = negation_words + negation_contractions

def identify_negation_sentences(text):
    if not text or not isinstance(text, str):
        return []
    try:
        sentences = sent_tokenize(text)
    except:
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]

    negation_sentences = []
    for sentence in sentences:
        sentence_lower = sentence.lower()
        for pattern in all_negation_patterns:
            if re.search(r'\b' + re.escape(pattern) + r'\b', sentence_lower):
                negation_sentences.append(sentence)
                break
    
    return negation_sentences

def identify_advanced_negation(text):

    if not text or not isinstance(text, str):
        return []
    try:
        sentences = sent_tokenize(text)
    except:
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]

    results = []
    for sentence in sentences:
        sentence_lower = sentence.lower()
        negation_found = False
        negation_types = []
        for pattern in all_negation_patterns:
            if re.search(r'\b' + re.escape(pattern) + r'\b', sentence_lower):
                negation_found = True
                negation_types.append(f"Explicit negation: '{pattern}'")
        words = re.findall(r'\b\w+\b', sentence_lower)
        for word in words:
            if word in non_negative_words:
                continue
                
            for prefix in negative_prefixes:
                if word.startswith(prefix) and len(word) > len(prefix) + 1:
                    negation_found = True
                    negation_types.append(f"Negative prefix: '{word}' (prefix: '{prefix}')")
                    break
        
        if negation_found:
            results.append({
                'sentence': sentence,
                'negation_types': negation_types
            })
    
    return results

def analyze_yelp_reviews(input_file, num_reviews=1000):
    print(f"Analyzing {num_reviews} reviews from {input_file}")
    start_time = time.time()
    
    negation_reviews = 0
    total_reviews = 0
    all_negation_sentences = []
    negation_patterns_found = Counter()
    
    with open(input_file, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i >= num_reviews:
                break
                
            total_reviews += 1
            if total_reviews % 100 == 0:
                print(f"Processed {total_reviews} reviews...")
                
            try:
                review = json.loads(line)
                text = review.get('text', '')
                negation_sentences = identify_negation_sentences(text)
                if negation_sentences:
                    negation_reviews += 1
                    all_negation_sentences.extend(negation_sentences)
                    for sentence in negation_sentences:
                        sentence_lower = sentence.lower()
                        for pattern in all_negation_patterns:
                            if re.search(r'\b' + re.escape(pattern) + r'\b', sentence_lower):
                                negation_patterns_found[pattern] += 1
            except json.JSONDecodeError:
                continue
    
    processing_time = time.time() - start_time
    print(f"Analysis completed in {processing_time:.2f} seconds")
    
    return total_reviews, negation_reviews, all_negation_sentences, negation_patterns_found

def print_analysis_results(total_reviews, negation_reviews, all_negation_sentences, negation_patterns_found):
    """Prints the analysis results in a readable format"""
    print("\n===== ANALYSIS RESULTS =====")
    print(f"Total reviews analyzed: {total_reviews}")
    print(f"Reviews containing negation: {negation_reviews} ({negation_reviews/total_reviews*100:.2f}%)")
    print(f"Total negation sentences found: {len(all_negation_sentences)}")
    
    print("\nMost common negation patterns:")
    for pattern, count in negation_patterns_found.most_common(10):
        print(f"  {pattern}: {count} occurrences")
    
    print("\nSample negation sentences:")
    for i, sentence in enumerate(all_negation_sentences[:10], 1):
        print(f"{i}. {sentence}")
    
    if len(all_negation_sentences) > 10:
        print(f"... and {len(all_negation_sentences) - 10} more")
    
    print("\n===== LIMITATIONS =====")
    print("1. Simple pattern matching can miss complex negation structures")
    print("2. Cannot handle implicit negations (e.g., 'I barely ate' implies not eating much)")
    print("3. Doesn't account for double negatives which may become positive")
    print("4. Context-dependent negations are difficult to detect")
    print("5. Limited handling of negation scope (what exactly is being negated)")
    print("6. May incorrectly flag words with negative prefixes that aren't actually negations")
    print("7. Cannot handle sarcasm or figurative language that may reverse meaning")
    print("8. Doesn't detect negation in questions (e.g., 'Isn't this restaurant good?')")

def main(args):
    """Main function to run the analysis"""
    print("Negation Sentence Detector for Yelp Reviews")
    print("===========================================")

    input_file = args.data_path
    num_reviews = args.num_reviews  # Adjust based on available computational resources
    
    total_reviews, negation_reviews, all_negation_sentences, negation_patterns_found = analyze_yelp_reviews(
        input_file, num_reviews)
    
    print_analysis_results(total_reviews, negation_reviews, all_negation_sentences, negation_patterns_found)
    
    # Save a sample of negation sentences to file
    with open("negation_sentences_sample.txt", "w", encoding="utf-8") as f:
        f.write(f"Sample of {len(all_negation_sentences)} negation sentences found in {negation_reviews} out of {total_reviews} reviews:\n\n")
        for i, sentence in enumerate(all_negation_sentences[:100], 1):
            f.write(f"{i}. {sentence}\n\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Identifying Yelp Review Sentences with Negation")
    parser.add_argument("--data_path", type=str, required=True, help="Path to review.json")
    parser.add_argument("--num_reviews", type=int, required=True, help="Number of reviews to analyze")
    args = parser.parse_args()
    main(args)