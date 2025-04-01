import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page title
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("sales_data.csv", parse_dates=["Date"])
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
category_filter = st.sidebar.multiselect("Select Category", df["Category"].unique(), default=df["Category"].unique())

# Filter data
filtered_df = df[df["Category"].isin(category_filter)]

# Metrics
st.title("📊 Sales Dashboard")
total_sales = filtered_df["Sales"].sum()
avg_sales = filtered_df["Sales"].mean()
st.metric("Total Sales ($)", f"${total_sales:,.2f}")
st.metric("Average Sales ($)", f"${avg_sales:,.2f}")

# Line chart - Sales Over Time
st.subheader("📈 Sales Over Time")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x="Date", y="Sales", data=filtered_df, marker="o", ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# Bar chart - Sales by Category
st.subheader("📊 Sales by Category")
category_sales = filtered_df.groupby("Category")["Sales"].sum().reset_index()
fig, ax = plt.subplots()
sns.barplot(x="Category", y="Sales", data=category_sales, ax=ax)
st.pyplot(fig)

st.write("Data Preview:")
st.dataframe(filtered_df)
