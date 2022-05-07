<h1>Heart Disease Prediction</h1>
<h3><a href="https://share.streamlit.io/atom017/heart-disease-prediction/main/userInterface.py">DEMO APP</a></h3>




# Description
This project is the final project of Simbolo 'Introduction to Artificial Intelligence (Batch-4)' class.

# Project Overview


![screenshot](https://github.com/atom017/Heart-Disease-Prediction/blob/main/images/heart-diseaseUI.png)


## Dataset

Heart disease dataset is collected from [Kaggle Datasets](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)

<div >
    <img src="https://github.com/atom017/Heart-Disease-Prediction/blob/main/images/countBySex.png" align="left" height="250" width="250" />
    <img src="https://github.com/atom017/Heart-Disease-Prediction/blob/main/images/scatterplot.png" align="left" height="250" width="250"/>
</div>
<br />
<br />



## Data Pre-Processing
- Getting the rows and columns
```
dataset.shape
```
- Getting dataset information
```
dataset.info()
```

- Checking null values
```
dataset.isnull().sum()
```



## Evaluation
Evaluation of trained models
| Model  | Accuracy | Precision  | F1-Score |
| ------------- | ------------- | ------------- | ------------- |
| Logistic Regression  | 0.8049  | 0.7686  | 0.7854  |
| Naive Bayes  | 0.7805  | 0.7727  | 0.7762  |
| Random Forest  | 1  | 1  | 1  |


![ROC Curve](https://github.com/atom017/Heart-Disease-Prediction/blob/main/images/ROC%20curve.png)

## Contributors

## Credits
- https://www.educative.io/edpresso/data-normalization-in-python
- https://www.javatpoint.com/logistic-regression-in-machine-learning
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7332220/
- Gerke S, Minssen T, Cohen G. Ethical and legal challenges of artificial intelligence-driven healthcare. Artif Intell Healthcare. (2020) 295–336. doi: 10.1016/B978-0-12-818438-7.00012-5



