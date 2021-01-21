#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[42]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset.  
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])


# ## District Summary
# 
# * Calculate the total number of schools
# 
# * Calculate the total number of students
# 
# * Calculate the total budget
# 
# * Calculate the average math score 
# 
# * Calculate the average reading score
# 
# * Calculate the percentage of students with a passing math score (70 or greater)
# 
# * Calculate the percentage of students with a passing reading score (70 or greater)
# 
# * Calculate the percentage of students who passed math **and** reading (% Overall Passing)
# 
# * Create a dataframe to hold the above results
# 
# * Optional: give the displayed data cleaner formatting

# In[43]:


school_data_complete.head()


# In[44]:


# Number of schools in the Distrcit (.(n)number of unique school Id's)
Totnumschools=school_data_complete ['School ID'].nunique()
# Number of students in the Distrcit (.(n)number of unique student Id's)
Totnumstudents= school_data_complete ['Student ID'].nunique()
# School budgets 
Budget=school_data_complete['budget'].unique()
# Total District Budgets 
Tot_Budget=sum(Budget)
# Average math_score
Avg_mscore= school_data_complete ['math_score'].mean()
# Average reading_score
Avg_rscore= school_data_complete ['reading_score'].mean()
# Passing math score
Pass_mscore=school_data_complete.loc[school_data_complete['math_score']>=70]
Pass_mscore_percent= len(Pass_mscore)/Totnumstudents*100
# Passing reading score 
Pass_rscore=school_data_complete.loc[school_data_complete['reading_score']>=70]
Pass_rscore_percent= len(Pass_rscore)/Totnumstudents*100
#Percent of Overall Passing
Overall_passing=school_data_complete.loc[(school_data_complete['math_score']>=70) & (school_data_complete['reading_score']>=70)].count()["student_name"]
Percent_ops=Overall_passing/Totnumstudents*100


# In[4]:


dis_sum_data ={
    "Total Number of Schools":[Totnumschools],
    "Total Number of Students":[Totnumstudents],
    "Total Budget":[Tot_Budget],
    "Avg Math Score":[Avg_mscore],
    "Avg Reading Score":[Avg_rscore],
    "% Passing Math Score":[Pass_mscore_percent],
    "% Passing Reading Score":[Pass_rscore_percent],
    "% Percent Overall Passing":[Percent_ops]}
    
Dist_Summ_data=pd.DataFrame(dis_sum_data,columns=["Total Number of Schools",
                                                  "Total Number of Students",
                                                  "Total Budget",
                                                  "Avg Math Score",
                                                  "Avg Reading Score",
                                                 "% Passing Math Score",
                                                 "% Passing Reading Score",
                                                  "% Percent Overall Passing"
                                                 ])

Dist_Summ_data["Total Number of Students"]=Dist_Summ_data["Total Number of Students"].map("{:,}".format)
Dist_Summ_data["Total Budget"]=Dist_Summ_data["Total Budget"].map("${:,}".format)
Dist_Summ_data["Avg Reading Score"]=Dist_Summ_data["Avg Reading Score"].map("{:.2f}".format)
Dist_Summ_data["Avg Math Score"]=Dist_Summ_data["Avg Math Score"].map("{:.2f}".format)
Dist_Summ_data["% Passing Math Score"]=Dist_Summ_data["% Passing Math Score"].map("{:.2f}".format)
Dist_Summ_data["% Passing Reading Score"]=Dist_Summ_data["% Passing Reading Score"].map("{:.2f}".format)
Dist_Summ_data["% Percent Overall Passing"]=Dist_Summ_data["% Percent Overall Passing"].map("{:.2f}".format)
Dist_Summ_data


# ## School Summary

# * Create an overview table that summarizes key metrics about each school, including:
#   * School Name
#   * School Type
#   * Total Students
#   * Total School Budget
#   * Per Student Budget
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * % Overall Passing (The percentage of students that passed math **and** reading.)
#   
# * Create a dataframe to hold the above results

# In[45]:


school_data_complete.head()


# In[46]:


grouped_df=school_data_complete.groupby("school_name")


# In[12]:


#School names
school_name=grouped_df['school_name'].unique()
#School type
sc_type=grouped_df['type'].first()
#Total Students 
Tot_students=grouped_df['Student ID'].count()
#School Budget
sc_budget=grouped_df['budget'].mean()
#Per Student Budget 
perstu_budget=sc_budget/Tot_students
#Average math_score 
Avg_mscore=grouped_df['math_score'].mean()
#Average reading_score 
Avg_rscore=grouped_df['reading_score'].mean()
#Percent Passing math
Passing_mpercent = school_data_complete[school_data_complete['math_score'] >=70].groupby(['school_name']).count()['math_score']
Percent_passing_math=Passing_mpercent/Tot_students*100
#Percent Passing reading
Passing_rpercent= Passing_rpercent= school_data_complete[school_data_complete['reading_score'] >=70].groupby(['school_name']).count()['reading_score']
Percent_passing_reading=Passing_rpercent/Tot_students*100
#Percent Overall passing 
Overall_passing=school_data_complete[(school_data_complete['math_score']>=70) & (school_data_complete['reading_score']>=70)].groupby(['school_name']).count()['student_name']/Tot_students*100


# In[47]:


school_sum_data={"School Type":sc_type,
                 "Total Students":Tot_students,
                 "Total School Budget":sc_budget,
                 "Per_Student_Budget":perstu_budget,
                "Average Math Score":Avg_mscore,
                "Average Reading Score":Avg_rscore,
                "% Passing Math":Percent_passing_math,
                "% Passing Reading":Percent_passing_reading,
                "% Overall Passing":Overall_passing }         
          
    
School_Summ_data=pd.DataFrame(school_sum_data,columns=["School Type",
                                                     "Total Students",
                                                     "Total School Budget",
                                                     "Per_Student_Budget",
                                                     "Average Math Score",
                                                     "Average Reading Score",
                                                     "% Passing Math",
                                                     "% Passing Reading",
                                                     "% Overall Passing",])



                 
School_Summ_data                                                
 


# ## Top Performing Schools (By % Overall Passing)

# * Sort and display the top five performing schools by % overall passing.

# In[48]:


School_Summ_data.sort_values('% Overall Passing',ascending=False).head()


# ## Bottom Performing Schools (By % Overall Passing)

# * Sort and display the five worst-performing schools by % overall passing.

# In[49]:


School_Summ_data.sort_values('% Overall Passing').head()


# ## Math Scores by Grade

# * Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
#   * Create a pandas series for each grade. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[130]:


SDC=school_data_complete
SDC


# In[131]:


# 9th grade average math score by school 
nine_s=SDC.loc[SDC['grade']=='9th']
nine_s.head()
grouped_nine_s=nine_s.groupby('school_name')
nine=grouped_nine_s['math_score'].mean()

# 10th grade average math score by school 
ten_s=SDC.loc[SDC['grade']=="10th"]
ten_s.head()
grouped_ten_s=ten_s.groupby('school_name')
ten=grouped_ten_s['math_score'].mean()

# 11th grade average math score by school 
eleven_s=SDC.loc[SDC['grade']=='11th']
eleven_s.head()
grouped_eleven_s=eleven_s.groupby('school_name')
eleven=grouped_eleven_s['math_score'].mean()

#12th grade average math score by school
twelfth_s=SDC.loc[SDC['grade']=="12th"]
twelfth_s.head()
grouped_twelfth_s=twelfth_s.groupby('school_name')
twelfth=grouped_twelfth_s['math_score'].mean()


# In[132]:


math_score_data={"9th":nine,
                 "10th":ten,
                 "11th":eleven,
                 "12th":twelfth}         
          
    
math_score_data=pd.DataFrame(math_score_data,columns=["9th",
                                                     "10th",
                                                     "11th",
                                                     "12th",
                                                     ])
math_score_data


# ## Reading Score by Grade 

# * Perform the same operations as above for reading scores

# In[134]:


# 9th grade average reading score by school 
nine_s=SDC.loc[SDC['grade']=='9th']
nine_s.head()
grouped_nine_s=nine_s.groupby('school_name')
r_nine=grouped_nine_s['reading_score'].mean()

# 10th grade average reading score by school 
ten_s=SDC.loc[SDC['grade']=="10th"]
ten_s.head()
grouped_ten_s=ten_s.groupby('school_name')
r_ten=grouped_ten_s['reading_score'].mean()

# 11th grade average reading score by school 
eleven_s=SDC.loc[SDC['grade']=='11th']
eleven_s.head()
grouped_eleven_s=eleven_s.groupby('school_name')
r_eleven=grouped_eleven_s['reading_score'].mean()

#12th grade average reading score by school
twelfth_s=SDC.loc[SDC['grade']=="12th"]
twelfth_s.head()
grouped_twelfth_s=twelfth_s.groupby('school_name')
r_twelfth=grouped_twelfth_s['reading_score'].mean()

reading_score_data={"9th":r_nine,
                 "10th":r_ten,
                 "11th":r_eleven,
                 "12th":r_twelfth}         
          
    
reading_score_data=pd.DataFrame(reading_score_data,columns=["9th",
                                                     "10th",
                                                     "11th",
                                                     "12th",
                                                     ])
reading_score_data


# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[208]:


spending_data={"Per_Student_Budget":perstu_budget,
               "Average Math Score":Avg_mscore,
                "Average Reading Score":Avg_rscore,
                "% Passing Math":Percent_passing_math,
                "% Passing Reading":Percent_passing_reading,
                "% Overall Passing":Overall_passing}
spending_data_df=pd.DataFrame(spending_data)
spending_data_df.head()


# In[220]:


bins=[0,540,597,627,657]
group_names=["0-585","586-630","631-645","646-680"]


# In[221]:


spending_data_df["Spending Ranges (Per Student)"]=pd.cut(spending_data_df["Per_Student_Budget"], bins, labels=group_names, include_lowest=True)

spending_data_df


# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[ ]:





# ## Scores by School Type

# * Perform the same operations as above, based on school type

# In[ ]:





# In[ ]:




