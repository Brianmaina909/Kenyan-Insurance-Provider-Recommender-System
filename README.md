# RECOMMENDER SYSTEM FOR BEST INSURANCE PROVIDER IN KENYA

![image](https://github.com/user-attachments/assets/eac03e44-40c0-46b2-aa02-5fb7f015ea39)


## Authors
[Brian Maina]
[Purity Gitonga] 
[Myles Mulusa] 
[Janet Mualuko] 
[Philip Kinga]


## Business Understanding

According to Cytonn's report on Kenya's listed insurance sector for H1 2023, insurance penetration in Kenya remains historically low. As of FY 2022, penetration stood at just 2.3%, according to the Kenya National Bureau of Statistics (KNBS) 2023 Economic Survey. This is notably below the global average of 7.0%, as reported by the Swiss Re Institute. The low penetration rate is largely attributed to the perception of insurance as a luxury rather than a necessity, and it is often purchased only when required or mandated by regulation. Additionally, a pervasive mistrust of insurance providers has significantly contributed to the low uptake.

Despite the critical importance of non-liability insurance—such as health, property, and personal accident coverage—for financial protection against unforeseen events, many individuals find it challenging to identify a trustworthy insurance provider due to opaque information on claim settlement records. This project seeks to address this pressing issue by simplifying the process of selecting a suitable insurance provider based on their performance in settling non-liability claims. By enhancing transparency and fostering trust in insurance providers, the project aims to boost insurance uptake and overall customer satisfaction.


## Problem Statement

Kenya faces a significant challenge with low insurance penetration, standing at just 2.3% as of FY 2022, well below the global average of 7.0%. This disparity is largely due to the perception of insurance as a luxury rather than a necessity, coupled with widespread mistrust towards insurance providers. Many Kenyans only purchase insurance when mandated or compelled by regulation, undermining the financial protection benefits offered by non-liability insurance such as health, property, and personal accident coverage.

## Data Understanding

![image](https://github.com/user-attachments/assets/1723f1a3-904a-4b44-8feb-3dba78d3bbc4)

Our approach will involve analyzing aggregated data from multiple sources, including historical claim settlement records, insurer performance metrics, and customer feedback. By normalizing and processing this data, we aim to develop a robust recommendation model that aligns with consumer needs and market dynamics.

The dataset obtained from Insurance Regulatory Authority(IRA) website (https://www.ira.go.ke/index.php/publications/statistical-reports/claims-settlement-*statistics*) contains the following columns:

Date: Date of the record.

Insurer: Name of the insurance company.

Claims_outstanding_at_the_beginning: Claims outstanding at the beginning of the period.

Claims_intimated_and_revived: Claims intimated- this comprises of the number of claims that have been reported to the insurers during the quarter.

Revived claims – these are claims previously closed but have been revived by the policyholders/claimant during the quarter

Claims_revised: claims whose reserves amount have been changed during the quarter.

Total_Claims_Payable: Total claims payable.

Claims_paid: these are the claims paid by the insurers during the quarter. The claims paid may include those outstanding at the beginning of the period and those intimated and revived during the quarter.

Claims_declined: Claims declined during the period.

Claims_closed_as_no_claims: notified claims for which the insurer makes provisions for liability, but the liability does not crystalize during the quarter.

Total_Claims_Action_during_the_Quarter: summation of the number of claims paid, claims declined, claims closed as no claims, and claims outstanding at the end of the quarter.

Claims_outstanding_at_the_end: Claims outstanding at the end of the period.

Claims_declined_ratio_(%): proportion of the number of claims declined in relation to the total number of claims actionable during the quarter

Claims_closed_as_no_claims_ratio (%): proportion of claims closed as no claims in relation to the total number of claims actionable during the quarter.

Claim_payment_ratio_(%): proportion of the number of claims paid in relation to the total number of claims actionable during the quarter.

Claim_payment_ratio_(%)_prev: Previous claim payment ratio.


## Methods

1. Data preparation was conducted including the identification and handling:
    - Columns
    - Missing values
    - Duplicates
    - Outliers
    - Insurer Names

  2. Exploratory Data Analysis
      A statistical overview of the data was done using univariate, bivariate and multivariate analysis to visualize the distributions and relationships between various variables. Scatter plots, heat maps, histograms, line graphs among other visualizations were used.

  3. Feature Engineering
      We created a reliability score from the ratios columns by encoding them.

  4. Data Preprocessing
      This includes splitting the dataset, normalize/standardize the data, performing one hot encoding and label encoding then addressing multicollinearity.


## Modeling

1. Linear Regression
    Based on the results from the Linear Regression model:
     - Root Mean Squared Error (RMSE) = 70.38813; the RMSE is quite high, indicating significant deviations between the model's predictions and the actual values. This suggests that the model isn't accurately capturing the relationship between the features and the target variable, which in this case is the 'Claim Payment Ratio'.
     - The R² value being -10.1732 indicates that the model is performing much worse than a simple baseline model that would predict the mean of the target variable. A negative R² suggests that the Linear Regression model doesn't fit the data at all and might even be misaligned with the underlying patterns in the data.
     - The MAE indicates an average absolute difference of about 19.6 percentage points between the predicted and actual values. This significant level of error shows that the model's predictions are not accurate.
    These metrics suggest that Linear Regression is not suitable for this project. The negative R² and high error values imply that the linear assumptions are not capturing the complexity of the data. This poor fit indicates that the relationships between the independent variables and the target variable are likely non-linear or more complex than what a linear model can capture.

2. Random Forest
    The results from the Random Forest model are as follows:
     - Root Mean Squared Error (RMSE) = 7.764: This relatively low RMSE indicates that the model's predictions are close to the actual values, suggesting a good fit.
     - The R² value of 0.8641 suggests that the model explains approximately 86.41% of the variance in the target variable ('Claim Payment Ratio'). This high R² value indicates a strong correlation between the predicted and actual values, showing that the model captures the data's patterns well.
     - An MAE of 4.0435 indicates that, on average, the predictions differ from the actual values by about 4.04 percentage points. This low level of error further suggests that the model's predictions are quite accurate.
    These results from the Random Forest model demonstrate a significant improvement over the Linear Regression model. The low MSE and MAE, coupled with a high R² value, indicate that the Random Forest model is well-suited for predicting the 'Claim Payment Ratio.' This suggests that the model effectively captures the complex, non-linear relationships between the features and the target variable.

3. Gradient Boost
    The results from the Gradient Boosting model after tuning:
     - Root Mean Squared Error (RMSE) = 7.1997: The RMSE is relatively low, indicating that the model's predictions are close to the actual values. This suggests a good level of accuracy in the predictions made by the model.
     - R-squared (R²) = 0.8831: The R² value of 0.8831 indicates that the model explains approximately 88.31% of the variance in the target variable ('Claim Payment Ratio'). This high R² value shows that the model effectively captures the relationship between the input features and the target variable, making it a strong fit for the data.
     - Mean Absolute Error (MAE) = 3.6030: The MAE of 3.6030 indicates that, on average, the predictions deviate from the actual values by about 3.60 percentage points. This low MAE further highlights the model's accuracy in making predictions.
    The Gradient Boosting model with the best parameters demonstrates strong predictive performance, as evidenced by the low MSE and MAE, and a high R² value. These metrics indicate that the model has a high degree of accuracy in predicting the 'Claim Payment Ratio,' which is crucial for identifying reliable insurance providers. In comparison to the Random Forest models (both untuned and tuned), the Gradient Boosting model has achieved better results. The lower RMSE and MAE, along with a higher R², suggest that Gradient Boosting is better suited for this task. The model's ability to capture complex patterns and interactions in the data makes it an excellent choice for accurately ranking insurers based on their claim settlement reliability.

4. XG Boost
     - Best Cross-Validation Score: 0.9533: This score indicates the model's performance on the validation set during the tuning process, reflecting how well the model generalizes to unseen data. A score of 0.9533 suggests strong predictive power and generalization ability.
     - Root Mean Squared Error (RMSE) = 7.233: The RMSE value indicates the average squared difference between the predicted and actual values. A lower RMSE reflects a higher accuracy, and this value suggests that the model performs well in predicting the target variable.
     - R-squared (R²) = 0.8823: The R² value indicates that the model explains about 88.23% of the variance in the target variable ('Claim Payment Ratio'). This high R² shows that the model captures a significant portion of the variability in the data, making it a good fit.
     - Mean Absolute Error (MAE) = 3.5491: The MAE measures the average magnitude of errors in the predictions, without considering their direction. An MAE of 3.5491 indicates that, on average, the predictions differ from the actual values by about 3.55 percentage points.
    The tuned XGBoost model demonstrates strong performance, with a high cross-validation score and good accuracy metrics (MSE, R², and MAE). The best parameters selected through hyperparameter tuning have optimized the model's ability to generalize and predict the target variable accurately. In comparison to other models (such as Gradient Boosting and Random Forest), XGBoost provides competitive results, particularly with a slightly better cross-validation score. The MSE, R², and MAE values are comparable to those of the Gradient Boosting model, suggesting that both models are suitable for the task. However, the slight edge in cross-validation score may make XGBoost a preferred choice in terms of overall reliability and generalization.

 5. Neural Network
     The results from the Neural Network model are as follows:
      - Root Mean Squared Error (RMSE) = 2105.81: This value indicates the average squared difference between the predicted and actual values. A lower MSE is generally better, but in this case, the high value suggests significant errors in the predictions.
      - R-squared (R²): -3.75. An R² value close to 1 indicates a good fit, while a value close to 0 indicates that the model does not explain the variance well. A negative R² value, like -3.75, suggests that the model performs worse than a horizontal line (a model that predicts the mean of the target variable for all inputs).
      - Mean Absolute Error (MAE): 13.14. This metric measures the average magnitude of the errors in the predictions, without considering their direction. A higher MAE indicates less accurate predictions.


## Conclusion

The XGBoost Regressor emerged as the best model for predicting the 'Claim Payment Ratio' and achieving the project's goal of developing a reliable recommender system for insurance providers. It demonstrated strong predictive power, generalization ability, and robustness, making it the ideal choice for helping Kenyan customers identify the most dependable insurance options.

We will save the trained model and proceed with its deployment. This involves integrating the model into a production environment where it can be utilized for making predictions in real-time. Our next steps will include setting up the necessary infrastructure, ensuring the model's scalability, and monitoring its performance to maintain accuracy and reliability. This deployment phase is crucial for transitioning from development to delivering real-world value.


## Deployment

We intergrated the XG Boost model into Streamlit app from the job libraries and used some sample features for testing as shown in the Appcode notebook.


## Recommendation

From our findings in the above, we recommend a collaboration with the industry stakeholders such as (Association of Kenya Insurers)AKI and IRA to get more data to improve our models results. We also would like to be part of consumer protection trainings that are conducted by IRA through out the year in various counties to help the consumer get the insurers rating.

## Next Steps

- Seek Additional Data: Gather data on loss ratios and premiums collected by insurers to enhance model accuracy.

- Integrate a Chatbot: Develop a chatbot feature that provides users with quarterly financial information of insurers.

- Product-Specific Rating: Improve the model to allow rating of insurers based on specific products, such as Just Money Market Fund.

- Pursue Partnership with IRA: Collaborate with the Insurance Regulatory Authority (IRA) to participate in customer education programs across the country, demonstrating how to use the tool effectively.
