import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:Saffronblood%40123@localhost/companydb2")

df = pd.read_sql("SELECT * FROM employees;", engine)

avg_salary_dept = df.groupby('department')['salary'].mean().sort_values()

count_dept = df['department'].value_counts()

top_performers = df.sort_values('performance_score', ascending=False).head(5)

# Bar chart: Average salary per department
plt.figure(figsize=(8,5))
avg_salary_dept.plot(kind='bar', color='skyblue')
plt.title("Average Salary per Department")
plt.ylabel("Average Salary")
plt.xlabel("Department")
plt.tight_layout()
plt.savefig("avg_salary_per_department.png")
plt.show()

# Pie chart: Employee distribution per department
plt.figure(figsize=(6,6))
count_dept.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title("Employee Distribution by Department")
plt.ylabel("")  
plt.tight_layout()
plt.savefig("employee_distribution.png")
plt.show()

# Bar chart: Top 5 performers
plt.figure(figsize=(8,5))
plt.bar(top_performers['name'], top_performers['performance_score'], color='green')
plt.title("Top 5 Performers")
plt.ylabel("Performance Score")
plt.xlabel("Employee")
plt.tight_layout()
plt.savefig("top_performers.png")
plt.show()

