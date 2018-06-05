# MachineLearning
### Day 1 
* Pandas module
    1. Convert dictionaries to Dataframes
    2. Slicing dataframes
    3. Making new columsn in dataframes
* SKLearn and Quandl module
    1. Get financial and economic datasets using Quandl
    2. Performing mathematical operations on dataframe columns
    3. Dataframe functions - .head() .tail() .shift() .fillna() dropna()
### Day 2  
* Train, test, predict data using Linear regression or Simple vector machine model
    1. Features vs labels
    2. Training and predicting using a model
        1. Prepare training data and split in 2 parts, ~80% to train ~20% to test [ model_selection.train_test_split() ]
        2. Define a classifier/model, like LinearRegression, SVM (Simple vector Machine) and then Train the classifier using .fit()
        3. Test accuracy of the classifier with respect to test data from step 1 [~20% of data]
        4. Predict -  Label = classifier.predict('Features')
            ![](https://github.com/PrateekKumarSingh/Python/blob/master/Python%20Machine%20Learning/SampleFiles/StockPrediction.png)
* Best fit line and how regression works
    1. What is slope(m) and intercept(b)
    2. Linear Regression = mX + b

### Day 3
* What are Squared error?
* Squared error vs Absolute errors
* R-Squared / Coeffcient of determination
* Classification with K-Nearest neighbor (KNN)

### Day 4
* Euclidean distance

    ![](https://github.com/PrateekKumarSingh/Python/blob/master/Python%20Machine%20Learning/SampleFiles/Euclidean_Distance.jpg)
* Making your own k-NN (k-Nearest Neighbor) algorithm in python
* Comparing the accuracy and confidence of your algorithm with SKLearn module's neighbors.KNeighborsClassifier()
* Accuracy vs confidence in k-NN algorithm

### Day 19
* SKLearn Support Vector Machine (SVM) classifier
* Making your own Support Vector Machine (SVM) algorithm in python [Courtesy: ![Harrison](https://pythonprogramming.net) ] 
