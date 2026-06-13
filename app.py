import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Nassau Candy Dashboard",
    layout="wide"
)
st.title("🍬 Nassau Candy Analysis")
st.subheader("Factory-to-Customer Shipping Route Efficiency Analysis")

df = pd.read_csv("Raw Dataset.csv")

# DATA CLEANING & FEATURE ENGINEERING

# Convert Dates
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

# Create Lead Time
df['Lead_Time'] = (
    df['Ship Date'] - df['Order Date']
).dt.days

# Remove Invalid Records
df = df[df['Lead_Time'] >= 0]

# Factory Mapping
factory_map = {
    "Wonka Bar - Nutty Crunch Surprise":"Lot's O' Nuts",
    "Wonka Bar - Fudge Mallows":"Lot's O' Nuts",
    "Wonka Bar -Scrumdiddlyumptious":"Lot's O' Nuts",
    "Wonka Bar - Milk Chocolate":"Wicked Choccy's",
    "Wonka Bar - Triple Dazzle Caramel":"Wicked Choccy's",
    "Laffy Taffy":"Sugar Shack",
    "SweeTARTS":"Sugar Shack",
    "Nerds":"Sugar Shack",
    "Fun Dip":"Sugar Shack",
    "Fizzy Lifting Drinks":"Sugar Shack"
}

df["Factory"] = df["Product Name"].map(factory_map)

# Efficiency Score
max_lead_time = df['Lead_Time'].max()
df['Efficiency_Score'] = 100 - (
    df['Lead_Time'] / max_lead_time
) * 100

st.subheader("📊 Key Performance Indicators")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Shipments",
    len(df)
)

col2.metric(
    "Average Lead Time",
    f"{df['Lead_Time'].mean():.2f} Days"
)

col3.metric(
    "Total Sales",
    f"${df['Sales'].sum():,.0f}"
)

col4.metric(
    "Gross Profit",
    f"${df['Gross Profit'].sum():,.0f}"
)

threshold = st.sidebar.slider(
    "Lead Time Threshold (Days)",
    min_value=int(df["Lead_Time"].min()),
    max_value=int(df["Lead_Time"].max()),
    value=int(df["Lead_Time"].median())
)

delay_frequency = (
    (df["Lead_Time"] > threshold).mean()
) * 100

col5.metric(
    f"Delay Frequency (> {threshold} Days)",
    f"{delay_frequency:.2f}%"
)

df["Route_State"] = (
    df["Factory"] + " → " +
    df["State/Province"]
)

df["Route_Region"] = (
    df["Factory"] + " → " +
    df["Region"]
)

route_perf = (
    df.groupby("Route_State")
    .agg({
        "Lead_Time":["mean","std","count"]
    })
)

route_perf = (
    df.groupby("Route_State")
    .agg({
        "Lead_Time": ["mean", "std", "count"]
    })
)

route_perf.columns = [
    "Avg_Lead_Time",
    "Lead_Time_Variability",
    "Shipment_Count"
]

route_perf = route_perf.reset_index()

st.subheader("Route Performance Table")

st.dataframe(route_perf)

top_routes = (
    route_perf
    .sort_values("Avg_Lead_Time")
    .head(10)
)

bottom_routes = (
    route_perf
    .sort_values(
        "Avg_Lead_Time",
        ascending=False
    )
    .head(10)
)

st.subheader("🏆 Top 10 Most Efficient Routes")

fig = px.bar(
    top_routes,
    x="Route_State",
    y="Avg_Lead_Time",
    title="Top 10 Most Efficient Routes"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("⚠️ Bottom 10 Least Efficient Routes")

fig = px.bar(
    bottom_routes,
    x="Route_State",
    y="Avg_Lead_Time",
    title="Bottom 10 Least Efficient Routes"
)

st.plotly_chart(fig, use_container_width=True)

#State-wise delay chart

state_delay = (
    df.groupby("State/Province")["Lead_Time"]
    .mean()
    .reset_index()
)

state_delay = state_delay.sort_values(
    "Lead_Time",
    ascending=False
)

st.subheader("📍 State-wise Lead Time Distribution")

fig = px.box(
    df,
    x="State/Province",
    y="Lead_Time",
    title="Lead Time Distribution Across States"
)

st.plotly_chart(fig, use_container_width=True)

#Create Region Summary
region_perf = (
    df.groupby("Region")
    .agg({
        "Sales": "sum",
        "Gross Profit": "sum",
        "Lead_Time": "mean"
    })
    .reset_index()
)

#Sales by Region (Donut Chart)
st.subheader("🌍 Regional Sales Contribution")

fig = px.pie(
    region_perf,
    values="Sales",
    names="Region",
    hole=0.5,
    title="Sales Contribution by Region"
)

st.plotly_chart(fig, use_container_width=True)

#Lead Time by Region

st.subheader("🚚 Average Lead Time by Region")

fig = px.line(
    region_perf,
    x="Region",
    y="Lead_Time",
    markers=True,
    title="Average Lead Time Across Regions"
)

st.plotly_chart(fig, use_container_width=True)

#Ship Mode Summary
shipmode_perf = (
    df.groupby("Ship Mode")
    .agg({
        "Sales": "sum",
        "Gross Profit": "sum",
        "Lead_Time": "mean"
    })
    .reset_index()
)

#Sales & Profit Comparison

st.subheader("🚚 Ship Mode Performance")

fig = px.bar(
    shipmode_perf,
    x="Ship Mode",
    y=["Sales", "Gross Profit"],
    barmode="group",
    title="Sales and Gross Profit by Ship Mode"
)

st.plotly_chart(fig, use_container_width=True)

#Average Lead Time by Ship Mode

st.subheader("⏱️ Average Lead Time by Ship Mode")

fig = px.funnel(
    shipmode_perf.sort_values("Lead_Time"),
    x="Lead_Time",
    y="Ship Mode"
)

st.plotly_chart(fig, use_container_width=True)

#Sales vs Lead Time Relationship

st.subheader("🎯 Sales vs Lead Time Relationship")

fig = px.scatter(
    df,
    x="Lead_Time",
    y="Sales",
    color="Ship Mode",
    size="Gross Profit",
    hover_data=[
        "Factory",
        "State/Province",
        "Product Name"
    ],
    title="Sales vs Lead Time Relationship"
)

st.plotly_chart(fig, use_container_width=True)

#Lead Time Distribution

st.subheader("📈 Lead Time Distribution")

fig = px.histogram(
    df,
    x="Lead_Time",
    nbins=30,
    title="Distribution of Lead Time"
)

st.plotly_chart(fig, use_container_width=True)

#Factory Performance Analysis

st.subheader("🏭 Factory-wise Lead Time Distribution")

fig = px.box(
    df,
    x="Factory",
    y="Lead_Time",
    title="Factory Performance Comparison"
)

st.plotly_chart(fig, use_container_width=True)

#---------insights and recommendations--------------------

st.markdown("---")
st.header("🔍 Key Insights")

st.markdown("""
- Standard Class shipping achieved the highest sales, highest gross profit, and lowest average lead time.
- Pacific and Atlantic regions contributed more than 60% of total sales.
- Approximately 42.2% of shipments experienced delivery delays above the average threshold.
- Factory-wise lead time distributions were nearly identical across all manufacturing facilities.
- Lead times were concentrated into three distinct shipment clusters: fast, average, and slow deliveries.
""")

st.header("💡 Recommendations")

st.markdown("""
- Optimize routes with consistently high lead times and poor delivery performance.
- Expand business operations and customer reach in high-revenue regions.
- Prioritize and strengthen Standard Class shipping operations.
- Implement continuous monitoring for high-delay destinations and routes.
- Adopt predictive analytics for lead-time forecasting and route optimization.
""")

with open("Nassau Candy.pdf", "rb") as file:
    st.download_button(
        label="📄 Download Project Report",
        data=file,
        file_name="Nassau Candy.pdf",
        mime="application/pdf"
    )

st.markdown("---")
st.markdown("""
**Factory-to-Customer Shipping Route Efficiency Analysis for Nassau Candy Distributor**

Developed by: **Kamali**

Tools Used: Python | Pandas | Plotly | Streamlit
""")