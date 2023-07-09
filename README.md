# Student Placement Predictor
<br/>

![placement app](https://github.com/Ddhruv-IOT/Student-Placement-Predictor/assets/54676859/42f2255c-b2af-4550-a405-392e598c24d6)
<br/>

## About Project

Welcome to our **student placement predictor app**! Powered by Machine Learning techniques and a streamlined user interface built with Streamlit, our app offers a simple yet effective solution to determine whether a student will secure a placement or not. By analyzing crucial factors such as class 10 and 12 marks, the chosen stream, UG degree type, and CGPA, as well as PG degree type and CGPA, our app swiftly generates a straightforward "Yes" or "No" prediction. Leveraging a robust dataset from Kaggle, our app is designed to provide students with quick and accurate placement forecasts, helping them make informed decisions about their future career paths. Try out our user-friendly student placement predictor app today and gain valuable insights into your placement prospects!

## Tools and Technologies Used:

### Python Libraries used:
- Streamlit, for web-based user interface
- Numpy, for data analysis
- Pandas, for data analysis
- Seaborn, for data visualization
- Matplotlib, for data visualization
- Sklearn, for model training and usage

### Softwares Used 
- Git Bash
- Anaconda
- Spyder
- Jupyter Notebook
- VS Code

### OS Used:
- Windows 10

## Working:
The student placement predictor app is built using the popular machine learning library, scikit-learn (sklearn). The heart of the app lies in utilizing the logistic regression algorithm, which is well-suited for binary classification problems like predicting student placements.

Here's how the app works:

1. **Data Preprocessing:** The app takes input from the user, including class 10 and 12 marks, stream opted, UG degree type and CGPA, and PG degree type and CGPA. These inputs are then preprocessed to ensure they are in a suitable format for model training.

2. **Train-Test Split:** The dataset obtained from Kaggle is divided into two subsets: the training set and the testing set. The training set is used to train the logistic regression model, while the testing set is used to evaluate its performance.

3. **Feature Encoding:** Categorical variables such as the chosen stream, UG degree type, and PG degree type need to be encoded numerically before being used in the model. This is achieved using techniques like one-hot encoding or label encoding.

4. **Model Training:** The training set, consisting of the preprocessed input features and corresponding placement outcomes, is used to train the logistic regression model. The model learns patterns and relationships between the input features and the placement outcomes.

5. **Prediction:** Once the model is trained, the app takes the user's input and applies the necessary preprocessing steps. The preprocessed input is then fed into the trained logistic regression model, which predicts whether the student will get placement or not, yielding a "Yes" or "No" output.

6. **User Interface:** The app is designed using Streamlit, a Python library for creating interactive web applications. The user interface allows users to enter their input, triggers the prediction process, and displays the predicted placement outcome.

By leveraging the power of sklearn's logistic regression algorithm, along with train-test split for model evaluation and Streamlit for a user-friendly interface, our student placement predictor app delivers quick and accurate predictions to assist students in making informed decisions about their career paths.

## Demo:
[Continue to Website](https://ddhruv-iot-student-placement-predictor-app-00ecmy.streamlit.app/)
<br/>
[Continue to LinkedIn Post](https://www.linkedin.com/posts/ddhruv-arora_datascience-research-internship-activity-7035923937725231104-jUuy?utm_source=share&utm_medium=member_desktop)
<br/>
<h6> As the app is hosted using a free tire service, it takes a few minutes depending on the server's ability to get up and running, so kindly be patient. </h6>

# Thank you
- Thank you all for using my app.
- All suggestions are warmly welcomed.
