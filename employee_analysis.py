"""
Employee Performance Data Visualization
Email: 23f1002057@ds.study.iitm.ac.in
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Create a sample dataset (you can replace this with pd.read_csv("your_file.csv"))
data = {
    "employee_id": ["EMP001","EMP002","EMP003","EMP004","EMP005","EMP006","EMP007","EMP008","EMP009","EMP010"],
    "department": ["R&D","Marketing","Operations","HR","IT","R&D","Operations","R&D","HR","IT"],
    "region": ["Middle East","Africa","Latin America","Latin America","Latin America",
               "Africa","Middle East","Middle East","Africa","Latin America"],
    "performance_score": [63.11,81.71,76.40,60.99,65.05,70.23,80.10,69.50,55.30,60.10],
    "years_experience": [1,15,11,3,11,8,10,2,4,5],
    "satisfaction_rating": [3.9,4.5,4.6,3.7,4.5,4.2,4.8,3.5,3.6,4.0]
}

df = pd.DataFrame(data)

# Step 2: Frequency count for "R&D" department
rd_count = (df["department"] == "R&D").sum()
print("Frequency of R&D Department:", rd_count)

# Step 3: Plot histogram of department distribution
plt.figure(figsize=(8,6))
sns.countplot(data=df, x="department", palette="viridis")
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Frequency")

# Save chart as image
plt.savefig("department_histogram.png")

# Step 4: Save everything to an HTML file
html_content = f"""
<html>
<head><title>Employee Data Visualization</title></head>
<body>
<h1>Employee Data Visualization</h1>
<p><b>Email:</b> 23f1002057@ds.study.iitm.ac.in</p>
<p><b>Frequency of R&D Department:</b> {rd_count}</p>
<img src="department_histogram.png" width="600">
</body>
</html>
"""

with open("employee_analysis.html", "w") as f:
    f.write(html_content)
