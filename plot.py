import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Read the file
file_path = 'releases.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

# Extract dates from the lines
dates = []
print(lines)
for line in lines:
    print(line)
    parts = line.split('-')
    print(parts[0])
    if len(parts) == 3:
        date_str = parts[2].strip()
        date = datetime.strptime(date_str, '%a %b %d %H:%M:%S %Y %z')
        print(f'${parts[1]} - ${date.date()}')
        dates.append(date.date())

# Create a DataFrame
df = pd.DataFrame(dates, columns=['date'])


# Aggregate the number of releases per month
df['month'] = df['date'].apply(lambda x: x.strftime('%Y-%m'))
monthly_release_counts = df['month'].value_counts().sort_index()

# Count the number of releases per date
release_counts = df['date'].value_counts().sort_index()

# Plot the line graph
plt.figure(figsize=(12, 6))
monthly_release_counts.plot(kind='line', marker='o')
plt.xlabel('Month')
plt.ylabel('Number of Releases')
plt.title('Number of Releases per Month')
#plt.xticks(rotation=45)
plt.xticks(ticks=range(len(monthly_release_counts)), labels=monthly_release_counts.index, rotation=70)
plt.grid(True)
plt.tight_layout()



# Plot the histogram
#plt.figure(figsize=(10, 6))
#release_counts.plot(kind='bar')
#release_counts.plot(kind='line', marker='o')
#plt.xlabel('Date')
#plt.ylabel('Number of Releases')
#plt.title('Number of Releases per Date')
#plt.xticks(rotation=45)
#plt.tight_layout()
#plt.show()

# Save the plot to a file
plt.savefig('releases_histogram.png')
print("Histogram saved as 'releases_histogram.png'")
