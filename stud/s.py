import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
studperf_df=pd.read_csv('StudentsPerformance.csv')
studperf_df.info()
studperf_df.info(verbose=False) # short summary 
studperf_df.describe()
print(studperf_df.head(15))
#Remove unnecessary features (E.g. drop unwanted columns) from the dataset such as ‘lunch’ and ‘test preparation course’
stuperf_df = studperf_df.drop(['lunch'], axis=1,inplace = False)
print('\\n====Understanding Inplace False : The Copied Dataframe====')
print(stuperf_df.head(3))
#Manipulate data by replacing empty column values in ‘parental level of education’ with a default value.
stuperf_df["parental level of education"] =stuperf_df["parental level of education"].fillna("Not applicable")
print(stuperf_df.head(5))
print(stuperf_df.head(5))
#Convert the attribute ‘race/ethnicity’ to have ‘groupA’ to be ‘Asian Students’, ‘groupB’ to be ‘African Students’ ,  ‘groupC’ to be ‘Afro-Asian #Students’, ‘groupD’ to be ‘American Students’ and ‘groupE’ to be ‘European Students’
stuperf_df["race/ethnicity"]=stuperf_df["race/ethnicity"].map({"group A" : "Asian students",
	"group B" : "African students",
	"group C" : "Afro-Asian students",
	"group D" : "American students",
	"group E" : "European students"})
print(stuperf_df.head(2))
#  #Tally of the Number of Male & Female students who took up the ‘test preparation course’ and those who did not.
# ax = sns.countplot(x="test preparation course",hue='gender',palette='Set3',data=stuperf_df)
# ax.set(title="Course completion based on gender", xlabel='Course', ylabel='Total')
# plt.show()
# #Total Number of Male & Female Students belonging to each student group
# ax = sns.countplot(x="race/ethnicity",hue="gender",palette="Set2",data=stuperf_df)
# ax.set(title="Total number of male and female students belonging to each group", xlabel="Groups", ylabel="Total")
# plt.show()
# #No of students who ‘failed’(less than 40), ‘second class’(between 40 & 50).
# #'first class’(between 60 & 75) and ‘distinction’(above 75) in ‘Maths’,
# #‘Reading’ and ‘Writing’.
# interval=(0,40,50,60,75)
# categories = ["Fail", "2nd class","1st class","Distinction"]
# stuperf_df["Marks_cats"]=pd.cut(stuperf_df.mathscore,interval,labels=categories)
# ax=sns.countplot(x="Marks_cats",hue="gender",palette="Set1",data=stuperf_df)
# ax.set(title="Marks categorisation for math",xlabel="Categories",ylabel="Number of students")
# plt.show()
# stuperf_df["Marks_Cats"]=pd.cut(stuperf_df.readingscore,interval,labels=categories)
# ax=sns.countplot(x="Marks_Cats",hue="gender",palette="Set1",data=stuperf_df)
# ax.set(title="Marks categorisation for reading",xlabel="Categories",ylabel="Number of students")
# plt.show()
# stuperf_df["Marks_Cats"]=pd.cut(stuperf_df.writingscore,interval,labels=categories)
# ax=sns.countplot(x="Marks_Cats",hue="gender",palette="Set1",data=stuperf_df)
# ax.set(title="Marks categorisation for writing",xlabel="Categories",ylabel="Number of students")
# plt.show()
