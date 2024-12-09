import pandas as pd
dataset = pd.read_csv("C:\\Users\\ASUS\\Downloads\\data set.csv", header=0)
# Q1: How many men and women are represented in this dataset?
gender_counts = dataset['sex'].value_counts()
print("Q1: Count of men and women")
print(gender_counts)

# Q2: What is the average age of women?
average_age_women = dataset[dataset['sex'] == 'Female']['age'].mean()
print("\nQ2: Average age of women")
print(f"{average_age_women:.2f}")

# Q3: Percentage of German citizens
total_count = len(dataset)
german_count = len(dataset[dataset['native-country'] == 'Germany'])
german_percentage = (german_count / total_count) * 100
print("\nQ3: Percentage of German citizens")
print(f"{german_percentage:.2f}%")

# Q4-5: Mean and standard deviation of age for >50K and <=50K earners
more_than_50k = dataset[dataset['salary'] == '>50K']
less_than_50k = dataset[dataset['salary'] == '<=50K']

mean_age_more = more_than_50k['age'].mean()
std_age_more = more_than_50k['age'].std()
mean_age_less = less_than_50k['age'].mean()
std_age_less = less_than_50k['age'].std()

print("\nQ4-5: Mean and Std dev of age for >50K and <=50K earners")
print(f"Mean age (>50K): {mean_age_more:.2f}, Std dev (>50K): {std_age_more:.2f}")
print(f"Mean age (<=50K): {mean_age_less:.2f}, Std dev (<=50K): {std_age_less:.2f}")

# Q6: Do all >50K earners have at least high school education?
high_school_or_above = ['Bachelors', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', 'Masters', 'Doctorate']
higher_education_only = all(dataset[dataset['salary'] == '>50K']['education'].isin(high_school_or_above))
print("\nQ6: Do all >50K earners have at least high school education?")
print(higher_education_only)

# Q7: Age statistics for each race and gender
age_stats = dataset.groupby(['race', 'sex'])['age'].describe()
print("\nQ7: Age statistics for each race and gender")
print(age_stats)

max_age_amer_indian_eskimo_men = dataset[
    (dataset['race'] == 'Amer-Indian-Eskimo') & (dataset['sex'] == 'Male')
]['age'].max()
print("\nMaximum age of Amer-Indian-Eskimo men:", max_age_amer_indian_eskimo_men)

# Q8: Proportion of high earners among married vs single men
married_statuses = ['Married-civ-spouse', 'Married-spouse-absent', 'Married-AF-spouse']
dataset['marital-category'] = dataset['marital-status'].apply(
    lambda x: 'Married' if x in married_statuses else 'Single'
)

proportion_married = len(dataset[(dataset['sex'] == 'Male') & 
                                  (dataset['marital-category'] == 'Married') & 
                                  (dataset['salary'] == '>50K')]) / len(dataset[(dataset['sex'] == 'Male') & (dataset['marital-category'] == 'Married')])

proportion_single = len(dataset[(dataset['sex'] == 'Male') & 
                                 (dataset['marital-category'] == 'Single') & 
                                 (dataset['salary'] == '>50K')]) / len(dataset[(dataset['sex'] == 'Male') & (dataset['marital-category'] == 'Single')])

print("\nQ8: Proportion of high earners among married vs single men")
print(f"Married: {proportion_married:.2f}, Single: {proportion_single:.2f}")

# Q9: Maximum working hours and earnings proportion
max_hours = dataset['hours-per-week'].max()
max_hours_workers = dataset[dataset['hours-per-week'] == max_hours]

num_max_hours_workers = len(max_hours_workers)
percent_high_earners = len(max_hours_workers[max_hours_workers['salary'] == '>50K']) / num_max_hours_workers * 100

print("\nQ9: Maximum working hours and high earners among them")
print(f"Max hours per week: {max_hours}")
print(f"Number of people working max hours: {num_max_hours_workers}")
print(f"Percentage of >50K earners among them: {percent_high_earners:.2f}%")

# Q10: Average working hours by salary and country
avg_hours_country = dataset.groupby(['native-country', 'salary'])['hours-per-week'].mean().unstack()
japan_hours = avg_hours_country.loc['Japan']

print("\nQ10: Average working hours in Japan")
print(japan_hours)

