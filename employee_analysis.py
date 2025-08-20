"""
Employee Performance Data Visualization
Email: 23f1002057@ds.study.iitm.ac.in
"""
import pandas as pd
import matplotlib.pyplot as plt

# Example employee dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Helen",
             "Ian", "Jack", "Kathy", "Leo", "Mona", "Nina", "Oscar"],
    "Department": ["R&D", "Sales", "R&D", "HR", "Sales", "R&D", "HR", "Sales",
                   "R&D", "Sales", "R&D", "HR", "Sales", "R&D", "R&D"]
}
df = pd.DataFrame(data)

# Frequency count
freq = df["Department"].value_counts()

# --- Save Histogram ---
plt.figure(figsize=(6,4))
freq.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Employee Department Distribution")
plt.xlabel("Department")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("department_histogram.png")
plt.close()

# --- Generate HTML file with frequency table + image ---
html_content = """
<html>
<head><title>Employee Analysis</title></head>
<body>
<h1>Employee Department Analysis</h1>
<p>This analysis shows the number of employees in each department.</p>

<h2>Department Frequency Counts</h2>
<ul>
"""
# Add frequency counts explicitly (e.g. "R&D: 15")
for dept, count in freq.items():
    html_content += f"<li>{dept}: {count}</li>\n"

html_content += """
</ul>

<h2>Histogram</h2>
<img src="department_histogram.png" alt="Department Histogram">

</body>
</html>
"""

with open("employee_analysis.html", "w") as f:
    f.write(html_content)

print("HTML file generated with frequency counts and histogram!")
