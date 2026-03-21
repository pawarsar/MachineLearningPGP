import pyautogui
import time
 
def type_string_after_delay(text, delay_seconds=5):
    # Replace newlines with '/n'
    processed_text = text.replace("\n", "/n")
    print(f"Waiting for {delay_seconds} seconds...")
    time.sleep(delay_seconds)
    print("Typing the string...")
    pyautogui.write(processed_text)
 
# Example usage
string_to_type = """
Criteria
Define the problem and perform an Exploratory Data Analysis
- Problem definition
- Data background and contents
- Univariate analysis
- Bivariate analysis
- Key meaningful observations for each of the plot
Points
10
Criteria
Data pre-processing
Prepare the data for analysis:
- Missing Value Treatment (if needed)
- Outlier Detection (treat, if needed)
- Feature Engineering
- Data preparation for modelling
Points
6
Criteria
Model building - Decision Tree
- Define model evaluation criterion
- Build the model and comment on the model performance.
- Visualize the decision rules and important features
Points
10
Criteria
Model Performance Evaluation and Improvement
- Try and improve the model performance by pruning (Both Post and Pre pruning)
- Check the performance of the pruned models, compare the performance of all the models built, and select the final model
- Find the decision rules and check feature importance for the final model
Points
20
Criteria
Actionable Insights & Recommendations
- Conclude with the key takeaways for the marketing team 
- What would your advice be on how to do this campaign?
Points
6
Criteria
Notebook Overall Quality
- Structure and flow
- Well-commented code
- Conclusion and Business Recommendations
Points
8 
"""
type_string_after_delay(string_to_type)


# !pip install uszipcode==1.0.1
# !pip install "sqlalchemy-mate==2.0.0.0"