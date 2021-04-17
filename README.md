# Cardio Catch Diseases Prediction
![Main figure](https://sejaumdatascientist.com/wp-content/uploads/2020/09/doctor.png)


# Business Problem

Cadio Catch Diseases is a company specialized in detecting heart disease in the early stages. The company is in the Service Business, which offers an early diagnosis of a cardiovascular disease for a certain price.

Currently, the cardiovascular disease diagnosis is manually, by a specialists team. The diagnosis current accuracy lies between 55% and 65%, due to the complexity of the diagnosis and also the team fatigue, who take turns to minimize the risks. The cost of each diagnosis, including the devices and the analysts payroll, is R$ 1,000.00.

The diagnosis price, paid by the client, varies depending on the precision achieved by the specialists team. The client pays R$ 500,00 for each 5% accuracy above 50%. For example, for a 55% accuracy, the diagnosis costs R$ 500.00 for the client, for a 60% accuracy, the price is R$ 1000.00 and so on. If the diagnostic accuracy is 50%, its free of charge.

As we see, the diagnosis acurracy deviation make the CCD company diagnosis either a profitable operation or a unprofitable operation. This diagnosis ROI creates an unpredictable revenue for the CCD company.


# Objective and Solution Proposal

### Objective

Increment the Cardio Catch Diseases company (CCD) profit. By increase the diagnostics tests precision and stability.

### Solution Proposal

Create a binary classification toll with statics model and machine learning to increase the diagnostics tests precision and stability.


# Dataset Summary

- **id** - [int]: Patients ID register in the system
- **age** - [int]: Patients age in days 
- **height** - [float]: Patients height in cm
- **weight** - [float]: Patients weight in kg
- **gender** - [binary]: Patients gender
- **ap_hi** - [float]: Patients diastolic blood pressure
- **ap_lo** - [float]: Patients diastolic blood pressure
- **cholesterol** - [categorical]: Patients cholesterol level
- **gluc** - [categorical]: Patients glucose level
- **smoke** - [binary]: Check if Patients is a smoker
- **alco** - [binary]: Check if Patients is a drinker
- **active** - [binary]: Check if patients practices physical activities
- **cardio** - [binary]: Check if patients practices has cardiovascular diseases

#  Mind Map Hypoteses
![mind_map](https://user-images.githubusercontent.com/81817799/113487755-37f5f700-9490-11eb-8896-7f74e6c4b95b.png)


# Exploratory Data Analysis

## Univariate Analysis


### Categorical features distribution analysis

![cat_features_distribution](https://user-images.githubusercontent.com/81817799/115087403-76ee6880-9ee4-11eb-8acc-eda5658acc9f.png)

- Most of the patients are woman
- Most of the patients have a normal cholesterol level
- Most of the patients have a normal glucose level
- Most of the patients are a non smoker person
- Most of the patients are a non drinker person
- Most of the patients practice a physical activity
- Most of the patients have a normal or a overweight BMI level
- There are no younger patients
-  Most of the patients are a half age person
- Most of the patients have a prehypertension hypertension level


### Numerical features distribution analysis

![num_features_distribution](https://user-images.githubusercontent.com/81817799/115087441-8bcafc00-9ee4-11eb-94bf-578467169c16.png)

All numerical variables have a large number of outliers yet, except the 'age' feature.


## Bivariate Analysis

### HYPOTESE 1: Chances of having Heart diseases increases by being a man

![H1_TF](https://user-images.githubusercontent.com/81817799/115087356-64742f00-9ee4-11eb-82e2-fc2b914992f0.png)
The proportion between sick and healthy men compared to the proportion between sick and healthy women are almost the same.


### HYPOTESE 2: Chances of having Heart diseases increases by increase the Body Mass Index

![H2_TF](https://user-images.githubusercontent.com/81817799/115087548-b3ba5f80-9ee4-11eb-9b16-4261d8a2fd9c.png)
The proportion between sick and healthy people increase with the BMI Level growth.


### HYPOTESE 3: Chances of having Heart diseases increases by increase the Cholesterol level

![H3_TF](https://user-images.githubusercontent.com/81817799/115087575-c2a11200-9ee4-11eb-800f-e226677df9ba.png)
The proportion between sick and healthy people increase with the Cholesterol Level growth.


### HYPOTESE 4: Chances of having Heart diseases increases by increase the Glucose level

![H4_TF](https://user-images.githubusercontent.com/81817799/115087600-d187c480-9ee4-11eb-8771-11cbc1133486.png)
The proportion between sick and healthy people increase with the Glucose Level growth.


### HYPOTESE 5: Chances of having Heart diseases increases by being a smoker

![H5_TF](https://user-images.githubusercontent.com/81817799/115087637-e1070d80-9ee4-11eb-9a4b-4b16e613e18b.png)
The proportion between sick and healthy non smokers compared to the proportion between sick and healthy smokers are almost the same.


### HYPOTESE 6: Chances of having Heart diseases increases by intake alcohol through life

![H6_TF](https://user-images.githubusercontent.com/81817799/115087653-ebc1a280-9ee4-11eb-85ca-31bc146adceb.png)
The proportion between sick and healthy non drinkers compared to the proportion between sick and healthy drinkers are almost the same.


### HYPOTESE 7: Chances of having Heart diseases decreases by being an active person through life

![H7_TF](https://user-images.githubusercontent.com/81817799/115087668-f7ad6480-9ee4-11eb-9d75-c4da3bf39a70.png)
The proportion between sick and healthy non sportists compared to the proportion between sick and healthy sportists is lower.


### HYPOTESE 8: Chances of having Heart diseases increases by being an older person

![H8_TF](https://user-images.githubusercontent.com/81817799/115087688-05fb8080-9ee5-11eb-8a3f-c9a0c79cf7f0.png)
The proportion between sick and healthy people increase with the Age Range Level growth.


### HYPOTESE 9: Chances of having Heart diseases increases by being hypertensive person

![H9_TF](https://user-images.githubusercontent.com/81817799/115087716-14e23300-9ee5-11eb-863d-51de3ede10ca.png)
The proportion between sick and healthy people increase with the Hypertension Level growth.


### HYPOTESE 10: Chances of having Heart diseases is higher between hypertensive elderly people than general hypertensive people

![H10_TF](https://user-images.githubusercontent.com/81817799/115087736-20355e80-9ee5-11eb-9f0e-8be1ab286740.png)
Between elderlies, the proportion between sick and healthy people increase with the Hypertension Level growth
This increase exponentially higher than the increase between people in general
Prehypertense elderlies are more likely to have cardiovascular diseases than prehypertense people in general


## Multivariate Analysis

![features_relations](https://user-images.githubusercontent.com/81817799/115087781-3ba06980-9ee5-11eb-8e91-e36fcf065adf.png)
**There are some variables that have considerable impact over 'cardio_disease' result values:**

- 'high_pressure'
- 'hypertension_level'
- 'low_pressure'
- 'age'
- 'cholesterol'
- 'BMI'
- 'age_range'
- 'weight'

# Machine Learning

To start, the following machine learning models were tested:

![machine_learning_models](https://user-images.githubusercontent.com/81817799/115121127-778c0b00-9f87-11eb-8188-cdb5d34ff69f.png)

- **On the business side:** We are aiming Precision score. Because each 5% increases on it is a R$ 500 increase in the diagnosis test price

- **On the patient side:** We are aiming Recall score. Because it reduces the chance of having a False Negative test result. As we know, false negatives results, frequently, comforts people into not retest. And in this case, there will be people with a growing disease that they don't know

So, we will choose the Top 4 best F1 Score models above to analyze, which is a metric that takes into account the Precision and the Recall metrics.

# Final Machine Learning model

![final_machine_learning_models](https://user-images.githubusercontent.com/81817799/115121225-dc476580-9f87-11eb-88ae-a919e2825645.png)

- All LGBM models have almost the same metrics, in general
- Taking in account that the LGBM Tuned model have a considerable Precision Deviation that, is the best case, will not predict with a precision higher than 75%, which is a turning point to increase by R$ 500 the test price. So it will be cut out
- Taking in account that the LGBM Default model have a lower Recall and lower F1 score than the LGBM Tuned & Calibrated model, it will be cut out, thinking about the patients interests

So, **we will choose the LGBM Tuned & Calibrated as the final model to propose.**

**OBS:** For more about the decisions made and how it was done: [Cardio Catch Diseases notebook](https://github.com/pedrofratucci/Cardio_Catch_Diseases/blob/main/notebooks/cardio_catch_deseases_PH.ipynb).

# Business Solution Performance

## Business accuracy methods comparison

In process...


## Business revenue methods comparison

In process...
  
  
# Model Deploy

In process...


# Further Improvements

Optimize the machine learning model precision interval for values over 75%, so the diagnosis test price always remain R$ 2.500,00.


# References

## Business Problem Source
- https://sejaumdatascientist.com/projeto-de-data-science-diagnostico-precoce-de-doencas-cardiovasculares/

## Data Source
- https://www.kaggle.com/sulianova/cardiovascular-disease-dataset

## Supplementary Materials
- https://www.medicalnewstoday.com/articles/327178#categories
