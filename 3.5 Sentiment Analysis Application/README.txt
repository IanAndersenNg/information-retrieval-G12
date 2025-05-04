===========================================
README 
===========================================

Group Number: G12 

Assignment Component: 3.5 Application - Yelp Review Sentiment Detector
-------------------------------------------
1. Third-Party Libraries Used (with Download Links)
-------------------------------------------

The following freely available Python libraries were used:

- scikit-learn: https://scikit-learn.org/stable/
- pandas: https://pandas.pydata.org/
- nltk: https://www.nltk.org/
- matplotlib (for visualizations only)
- seaborn (for visualizations only)
These libraries are all compatible with Python 3.8+.

Note: Visualizations are optional and handled separately in `visualizations.ipynb`.

------------------------
2.Installation & Execution
------------------------

Step 1 – Install Python and Dependencies  
• Ensure Python 3.8 or later is installed.  
• Install required packages via pip:

    pip install pandas scikit-learn nltk matplotlib seaborn tqdm

• Download required NLTK data:

    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')

Step 2 – Prepare the Dataset  
• Download from: https://www.yelp.com/dataset  
• Extract the file yelp_academic_dataset_review.json  
• Place it in your working directory

Step 3 – Run the Application  

Example Command (in terminal):

    python main.py --data_path "your_path/yelp_academic_dataset_review.json" --max_reviews 10000 --save_model

   Parameters:
   - --data_path: Full path to `review.json` file from Yelp Open Dataset.
   - --max_reviews: (Optional) Number of reviews to load (default is 10000).
   - --save_model: (Optional) Whether to save the trained model and vectorizer.

-------------------------------------------
3. Sample Output Explanation
-------------------------------------------

> Initial preprocessing results showing dataset size and common terms.
Total reviews loaded: 10000
Average word count per review: 52.70
Top 10 frequent words after preprocessing:
food: 5148, good: 4905, place: 4779, ...

> Performance metrics for each sentiment class. Positive class is best predicted; neutral is the hardest to classify.
Model training completed. Evaluating on 2000 test samples.

==Classification Report==
              precision    recall  f1-score   support
    negative     0.8404    0.7582    0.7971       368
     neutral     0.5781    0.1623    0.2534       228
    positive     0.8635    0.9865    0.9209      1404

> Confusion matrix clarifies prediction distribution per class.
==Confusion Matrix==
               Pred positive  Pred neutral  Pred negative
True positive           1385            10              9
True neutral             147            37             44
True negative             72            17            279

> Top reviews with strongest positive sentiment predictions, useful for showcasing system interpretability.
Retrieving Top-5 Most Positive Reviews...

Rank 1:
Confidence Score: 0.9975
Review Text: trying find great local spot breakfast...
...
-------------------
Visualization Notes
-------------------
Optional visualizations are generated using `visualizations.ipynb`. This includes:
- Word frequency charts
- Class distribution pie chart
- Precision/Recall/F1 bar plots
- Top contributing words per class

Run the notebook separately for visualization purposes.

-------------------------------------------
4. Notes
-------------------------------------------
Only source code files are included in /SourceCode/ folder:
- main.py  
- model.py  
- preprocess.py  
- utils.py  


