# information-retrieval-G12

=====================================================================
## Assignment Component: 3.2 Data Analysis
Navigate to the directory 2_Data_Analysis/
### Third-Party Libraries Used (with Download Links)

The following freely available Python libraries were used:

- scikit-learn: https://scikit-learn.org/stable/
- pandas: https://pandas.pydata.org/
- nltk: https://www.nltk.org/
- matplotlib (for visualizations only)
  These libraries are all compatible with Python 3.8+.

Note: Visualizations are presented in `stemming.ipynb`.

### Installation & Execution

Step 1 – Install Python and Dependencies  
• Ensure Python 3.8 or later is installed.  
• Install required packages via pip:

    pip install pandas scikit-learn nltk matplotlib


Step 2 – Prepare the Datasets
• For writing style analysis, the following datasets are required
- Yelp dataset: https://www.yelp.com/dataset
- Amazon Fine Food Reviews: https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews
- Trip Advisor Hotel Reviews: https://www.kaggle.com/datasets/andrewmvd/trip-advisor-hotel-reviews
- IMDB Review: https://www.kaggle.com/datasets/pawankumargunjan/imdb-review
• Arrange your working directory like the followings.
|- yelp-dataset
|  |- yelp_academic_dataset_review.json
|
|- amazon-fine-food-reviews
|  |- Reviews.csv
|
|- trip-advisor-hotel-reviews
|  |- tripadvisor_hotel_reviews.csv
|
|- imdb-review
|- IMDB Dataset.csv


Step 3 – Run the Analysis

1. Tokenization and Stemming: python stemming.py --data_path "your_path/"

    - Parameters:
        - --data_path: your working directory that saves the data
    - Sample Output:
      DcBLYSvOuWcNReolRVr12A 3217 reviews
      Top 10 before stemming:  [('oysters', 4963), ('good', 1955), ('food', 1649), ('charbroiled', 1569), ('service', 1230), ('dragos', 1199), ('great', 1073), ('place', 1069), ('shrimp', 1058), ('lobster', 967)]
      Top 10 after stemming:  [('oyster', 5669), ('good', 2030), ('food', 1669), ('order', 1633), ('charbroil', 1603), ('place', 1293), ('drago', 1263), ('servic', 1240), ('great', 1074), ('shrimp', 1072)]
    - Note that the line charts for visualization can be obtained by running the jupyter notebook stemming_visualization.ipynb

2. POS tagging: python stemming.py --data_path "your_path/" --length "very_short/short/medium/long/very_long/all"
    - Parameters:
        - --data_path: your working directory that saves the data
        - --length: the code will randomly select a sentence from a subset based on the user choice which is defined as follows
            - very_short: sentences shorter than the 25th percentile of the whole dataset.
            - short: sentences longer than the 25th percentile and shorter than the 50th percentile of the whole dataset.
            - medium: sentences longer than the 50th percentile and shorter than the 75th percentile of the whole dataset.
            - long: sentences longer than the 75th percentile and shorter than the 95th percentile of the whole dataset.
            - very long: sentences longer than the 95th percentile of the whole dataset.
              Note that if "all" is specified, the code will run all of the options.
    - Sample Output (for a very short sentence):
      Amazing hand drawn noodles and delicious roasted duck soup. The broth is amazing, good portion of fresh made noodles and great pieces of roasted Peking duck. Best noodle restaurant in all of Philadelphia according to many locals
      [[('Amazing', 'JJ'), ('hand', 'NN'), ('drawn', 'NN'), ('noodles', 'NNS'), ('and', 'CC'), ('delicious', 'JJ'), ('roasted', 'VBN'), ('duck', 'NN'), ('soup', 'NN')], [('The', 'DT'), ('broth', 'NN'), ('is', 'VBZ'), ('amazing', 'VBG'), ('good', 'JJ'), ('portion', 'NN'), ('of', 'IN'), ('fresh', 'JJ'), ('made', 'VBN'), ('noodles', 'NNS'), ('and', 'CC'), ('great', 'JJ'), ('pieces', 'NNS'), ('of', 'IN'), ('roasted', 'JJ'), ('Peking', 'NNP'), ('duck', 'NN')], [('Best', 'NNP'), ('noodle', 'NN'), ('restaurant', 'NN'), ('in', 'IN'), ('all', 'DT'), ('of', 'IN'), ('Philadelphia', 'NNP'), ('according', 'VBG'), ('to', 'TO'), ('many', 'JJ'), ('locals', 'NNS')]]
      37 words

3. Writing style: python stemming.py --data_path "your_path/"
    - Parameters:
        - --data_path: your working directory that saves the data
    - Sample Output: Due to space limitation, only the result of Yelp dataset is presented here
      Yelp
      Positive words: ['amazing', 'area', 'atmosphere', 'awesome', 'beer', 'best', 'bit', 'breakfast', 'clean', 'coffee', 'definitely', 'delicious', 'dinner', 'excellent', 'family', 'fantastic', 'fast', 'favorite', 'fresh', 'friendly', 'fun', 'happy', 'helpful', 'highly', 'hot', 'looking', 'lot', 'love', 'loved', 'lunch', 'perfect', 'prices', 'quick', 'salad', 'sandwich', 'sauce', 'selection', 'small', 'spot', 'super', 'tasty', 'visit', 'wonderful', 'worth']
      Negative words: ['10', '20', '30', 'ask', 'asked', 'away', 'bad', 'business', 'called', 'car', 'check', 'cold', 'customer', 'customers', 'disappointed', 'half', 'horrible', 'hour', 'left', 'long', 'manager', 'minutes', 'money', 'need', 'ok', 'pay', 'phone', 'room', 'rude', 'said', 'server', 'store', 'table', 'terrible', 'think', 'told', 'took', 'waited', 'waiting', 'waitress', 'wanted', 'wasn', 'won', 'worst']


=====================================================================
## Assignment Component: 3.3 Development of a Search Engine
Navigate to the directory 3_Search_Engine/
### Third Party Libraries Used

The following freely available libraries were used:
 - Lucene: https://lucene.apache.org/
   - Core package: https://mvnrepository.com/artifact/org.apache.lucene/lucene-core
   - Query Parser: https://mvnrepository.com/artifact/org.apache.lucene/lucene-queryparser
   - Highlighter: https://mvnrepository.com/artifact/org.apache.lucene/lucene-highlighter
   - Analysis commons: https://mvnrepository.com/artifact/org.apache.lucene/lucene-analysis-common
 - Jackson databinding: https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind
 - Lombok: https://mvnrepository.com/artifact/org.projectlombok/lombok

### Install Java
Java installation instructions may be found here:<br>
https://adoptium.net/temurin/releases/?version=17
<br><br>
As the project was built using JDK 17, JDK 17+ is recommended

### Install Maven
Maven installation instructions may be found here:<br>
https://maven.apache.org/install.html
<br><br>
Maven is a simple package manager which removes the need to manually install packages. To further simplify the execution process, it's suggested to add the maven's bin directory to PATH, as explained in the instructions above.

### Execution
Execute the following commands in succession:
```declarative
mvn clean compile
```
```declarative
mvn exec:java
```

To exit, enter 0.

To index, enter 1, provide the path of that you want to save the search index file at. Relative path will suffice.

To search documents for a term, enter 2, provide the field name and term to search for, and the topN results.

To search documents for a phrase, enter 3, provide the field name and phrase to search for, and the topN results.

To retrieve a full review by its review id, enter 4, then enter its review id.

=====================================================================
## Assignment Component: 3.4 Sentences with Negation
Navigate to the directory 4_Identifying_Sentences_with_Negation/
### Third-Party Libraries Used (with Download Links)

The following freely available Python libraries were used:
- nltk: https://www.nltk.org/

### Installation & Execution

Step 1 – Install Python and Dependencies 
• Ensure Python 3.8 or later is installed.  
• Install required packages via pip:

    pip install nltk

Step 2 – Prepare the Dataset  
• Download from: https://www.yelp.com/dataset  
• Extract the file yelp_academic_dataset_review.json  
• Place it in your working directory

Step 3 – Run the Application

Example Command (in terminal):

    python main.py --data_path "your_path/yelp_academic_dataset_review.json" --num_reviews 10000

### Sample Output Explanation
Upon completing analysis, the program will display the analysis execution time, number of reviews analyzed, number of reviews containing negation, and total negation sentences found.
The most common negation patterns, along with their corresponding occurrences within the processed reviews, will also be displayed. 
Sample negation sentences, as well as the limitations of the analysis will then be displayed. 

=====================================================================
## Assignment Component: 3.5 Application - Yelp Review Sentiment Detector
Navigate to the directory 5_Sentiment_Analysis_Application/
### Third-Party Libraries Used (with Download Links)

The following freely available Python libraries were used:

- scikit-learn: https://scikit-learn.org/stable/
- pandas: https://pandas.pydata.org/
- nltk: https://www.nltk.org/
- matplotlib (for visualizations only)
- seaborn (for visualizations only)
  These libraries are all compatible with Python 3.8+.

Note: Visualizations are optional and handled separately in `visualizations.ipynb`.

### Installation & Execution

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


### Sample Output Explanation

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

#### Visualization Notes
Optional visualizations are generated using `visualizations.ipynb`. This includes:
- Word frequency charts
- Class distribution pie chart
- Precision/Recall/F1 bar plots
- Top contributing words per class

Run the notebook separately for visualization purposes.

### Notes
Only source code files are included in /SourceCode/ folder:
- main.py
- model.py
- preprocess.py
- utils.py  


