from datetime import datetime, timedelta, timezone
import matplotlib.pyplot as plt


# Define the date range
start_date = datetime(2023, 1, 1, tzinfo=timezone(timedelta(hours=0)))
end_date = datetime(2025, 12, 31, tzinfo=timezone(timedelta(hours=0)))

# Read the releases.txt file
with open('releases.txt', 'r') as file:
    lines = file.readlines()

# Extract user names and dates
filtered_users = []
for line in lines:
    parts = line.split(' - ')
    user = parts[1].strip().lower()  # Convert user name to lowercase
    date_str = parts[2]
    release_date = datetime.strptime(date_str.strip(), '%a %b %d %H:%M:%S %Y %z')

    # Filter by date range
    if start_date <= release_date <= end_date:
        filtered_users.append(user)

# Count occurrences of each user
user_counts = {}
for user in filtered_users:
    if user in user_counts:
        user_counts[user] += 1
    else:
        user_counts[user] = 1

# Prepare data for the pie chart
labels = user_counts.keys()
sizes = user_counts.values()

# Generate the pie chart
plt.figure(figsize=(10, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Add a title
plt.title('Proportion of Releases by User since 2023/01/01')

# Save the plot to a file
plt.savefig('releases_pie.png')
print("Pie saved as 'releases_pie.png'")