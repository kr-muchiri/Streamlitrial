import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Data (Replace with your actual DataFrame)
df = pd.DataFrame({
    'Statistic': ['Height', 'Weight', 'Age'],
    'SEW Count': [10, 20, 30],
    'BER Count': [40, 50, 60]
})

# Title
st.title('Statistics Dashboard')

# Show the dataframe
st.write('### Data')
st.write(df)

# Create bar plot
st.write('### Bar Plot')
fig, ax = plt.subplots()
df.plot(x='Statistic', y=['SEW Count', 'BER Count'], kind='bar', ax=ax)
plt.xlabel('Statistic')
plt.ylabel('Count')
plt.xticks(rotation=0)
st.pyplot(fig)

# Create heatmap
st.write('### Heatmap')
heatmap_data = df[['Statistic', 'SEW Count', 'BER Count']].set_index('Statistic')
fig, ax = plt.subplots()
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)
