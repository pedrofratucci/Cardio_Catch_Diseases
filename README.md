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

#  Mind Map
![mind_map](https://user-images.githubusercontent.com/81817799/113487755-37f5f700-9490-11eb-8896-7f74e6c4b95b.png)

# Exploratory Data Analysis

## Univariate Analysis

### Categorical features distribution analysis
In process...

### Numerical features distribution analysis
In process...

## Bivariate Analysis

### HYPOTESE 1: Chances of having Heart diseases increases by being a man

![H1_TR](https://user-images.githubusercontent.com/81817799/113488476-cb312b80-9494-11eb-8625-f82a64366c67.png)


### HYPOTESE 2: Chances of having Heart diseases increases by increase the Body Mass Index

![H2_TR](https://user-images.githubusercontent.com/81817799/113488531-25ca8780-9495-11eb-99d4-406e6be50996.png)


### HYPOTESE: Chances of having Heart diseases increases by increase the Cholesterol level

![H3_TR](https://user-images.githubusercontent.com/81817799/113488691-0aac4780-9496-11eb-8341-082fdb23718b.png)


### HYPOTESE: Chances of having Heart diseases increases by increase the Glucose level

![H4_TR](https://user-images.githubusercontent.com/81817799/113488699-10a22880-9496-11eb-859d-de4cd53a7f75.png)


### HYPOTESE 5: Chances of having Heart diseases increases by being a smoker

![H5_TR](https://user-images.githubusercontent.com/81817799/113488705-15ff7300-9496-11eb-91ac-6612bbac593e.png)


### HYPOTESE 6: Chances of having Heart diseases increases by intake alcohol through life

![H6_TR](https://user-images.githubusercontent.com/81817799/113488576-662a0580-9495-11eb-8cab-bab65fb4fb7a.png)


### HYPOTESE 7: Chances of having Heart diseases decreases by being an active person through life

![H7_TR](https://user-images.githubusercontent.com/81817799/113488582-7346f480-9495-11eb-871c-97a92c43d0a1.png)

### HYPOTESE 8: Chances of having Heart diseases increases by being an older person

![H8_TR](https://user-images.githubusercontent.com/81817799/113488599-8063e380-9495-11eb-845b-5e39e5f57002.png)

### HYPOTESE 9: Chances of having Heart diseases increases by being hypertensive person

![H9_TR](https://user-images.githubusercontent.com/81817799/113488611-8e196900-9495-11eb-9d28-466b3a3ab602.png)


### HYPOTESE 10: Chances of having Heart diseases is higher between hypertensive elderly people than general hypertensive people

![H10_TR](https://user-images.githubusercontent.com/81817799/113488622-9b365800-9495-11eb-9a5a-3d1092ea18bf.png)

## Multivariate Analysis
In process...

# Business Solution Performance

## Business accuracy methods comparison**
![bussines_method](https://user-images.githubusercontent.com/81817799/113519039-457ab200-9560-11eb-9044-66c996505334.png)




## Business revenue methods comparison**
![business_revenue](https://user-images.githubusercontent.com/81817799/113519146-d2be0680-9560-11eb-9fe4-ce45bf133a51.png)
  
  
# Model Deploy

In process...

# Further Improvements

Optimize the machine learning model precision interval for values over 75%, so the diagnosis test price always remain R$ 2.500,00.


# References

In process...
