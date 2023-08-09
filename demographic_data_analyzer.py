import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Author: SHAREN RAJENTHIRAN

def analyze_demographic_data(print_calculations=True):


    df = pd.read_csv('adult-data.csv')
    

    # How many people of each race are represented in this dataset?
    num_race = df['race'].value_counts()
    
    
    # What is the average age of men?
    avg_male_age = df[df['sex']=='Male']['age'].min()
    
    # What is the percentage of people who have a Bachelor's degree?
    bachelor = df[df['education']=='Bachelors']
    bachelor_total = bachelor.value_counts().sum()
    total_education = df['education'].value_counts().sum()
    percentage_bachelor = (bachelor_total/total_education)*100
    round(percentage_bachelor,1)

    # What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    ad_education_50K_above = df[df['education'].isin(['Bachelors','Masters','Doctorate'])][df['salary']=='>50K'] #isin = filter data
    ad_education_50K_above_total = ad_education_50K_above.value_counts().sum()
    percentage_ad_education_50K_above = (ad_education_50K_above_total/total_education)*100
    round(percentage_ad_education_50K_above,1)

    # What percentage of people without advanced education make more than 50K?
    not_ad_education_50K_above = df[~df['education'].isin(['Bachelors','Masters','Doctorate'])][df['salary']=='>50K']
    not_ad_education_50K_above_total = not_ad_education_50K_above.value_counts().sum()
    percentage_not_ad_education_50K_above_total  = (not_ad_education_50K_above_total/total_education)*100
    round(percentage_not_ad_education_50K_above_total,1)

    # What is the minimum number of hours a person works per week?
    min_work = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_work_50K = df[df['hours-per-week']==min_work][df['salary']=='>50K']
    min_work_50K_total = min_work_50K.value_counts().sum()
    total_hours_per_week = df['hours-per-week'].value_counts().sum()
    percentage_min_work_50K = (min_work_50K_total/total_hours_per_week)*100
    
    

    # What country has the highest percentage of people that earn >50K and what is that percentage?
    country_50K = df[df['salary']=='>50K']['native-country']
    # country_50K_sort = country_50K.value_counts().sort_values(ascending=False)
    country_50K_percentage = (country_50K.value_counts()/country_50K.value_counts().sum())*100 
    country_50K_sort_percentage = country_50K_percentage.sort_values(ascending=False)
    round(country_50K_sort_percentage,1)

    # Identify the most popular occupation for those who earn >50K in India
    india_50K =df[df['salary']=='>50K'][df['native-country']=='India']
    india_50K_occ_sort = india_50K.sort_values(by='occupation')
    india_50K_occ_sort_count = india_50K_occ_sort.value_counts(subset=['occupation'])
    
    if print_calculations:
        print("Data: \n", df)
        print("Number of people of each race: \n", num_race) 
        print("Average age of men: ", avg_male_age)
        print(f"Percentage of people with Bachelors: {percentage_bachelor}% ")
        print(f"Percentage of people with advanced education with salary >50K: {round(percentage_ad_education_50K_above,1)}%")
        print(f"Percentage of people without advanced education with salary >50K: { round(percentage_not_ad_education_50K_above_total,1)}% ")
        print(f"Minimum number of hours a person works per week: {min_work} hours/week")
        print(f"Percentage of the people who work the minimum number of hours per week have a salary of more than 50K: {percentage_min_work_50K}% ")
        print("Country with their percentage of people that earn >50K \n:", round(country_50K_sort_percentage,1))
        print("Most popular occupation for those who earn >50K in India:", india_50K_occ_sort_count)

    return {
        'Data' : df,
        'Number of people of each race': num_race,
        'Average age of men': avg_male_age,
        'Percentage of people with Bachelors': percentage_bachelor,
        'Percentage of people with advanced education with salary >50K': round(percentage_ad_education_50K_above,1),
        'Percentage of people without advanced education with salary >50K': round(percentage_not_ad_education_50K_above_total,1),
        'Minimum number of hours a person works per week': min_work,
        'Percentage of the people who work the minimum number of hours per week have a salary of more than 50K': percentage_min_work_50K,
        'Country with their percentage of people that earn >50K': round(country_50K_sort_percentage,1),
        'Most popular occupation for those who earn >50K in India': india_50K_occ_sort_count
    }
    

analyze_demographic_data()