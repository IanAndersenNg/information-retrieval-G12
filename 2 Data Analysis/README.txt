===========================================
README 
===========================================

Group Number: G12 

Assignment Component: 2 Data Analysis
-------------------------------------------
1. Third-Party Libraries Used (with Download Links)
-------------------------------------------

The following freely available Python libraries were used:

- scikit-learn: https://scikit-learn.org/stable/
- pandas: https://pandas.pydata.org/
- nltk: https://www.nltk.org/
- matplotlib (for visualizations only)
These libraries are all compatible with Python 3.8+.

Note: Visualizations are presented in `stemming.ipynb`.

------------------------
2.Installation & Execution
------------------------

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