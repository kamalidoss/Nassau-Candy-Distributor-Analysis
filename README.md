# 🍬 Nassau Candy Distributor – Factory-to-Customer Shipping Route Efficiency Analysis

## 📌 Project Overview

This project focuses on analyzing factory-to-customer shipping route efficiency and logistics performance using Python and Streamlit. The project applies data preprocessing, exploratory data analysis (EDA), KPI monitoring, route efficiency evaluation, regional logistics analysis, lead-time assessment, and interactive visualizations to transform raw shipment data into actionable business insights.

The analysis evaluates delivery performance, route efficiency, shipping mode effectiveness, regional contribution, factory operations, and lead-time distribution to support data-driven supply chain decision-making.

---

## 🎯 Project Objectives

* Analyze shipment and logistics data of Nassau Candy Distributor.
* Evaluate shipping route efficiency using lead-time analysis.
* Identify the most efficient and least efficient delivery routes.
* Compare logistics performance across regions and states.
* Analyze the impact of shipping modes on delivery performance.
* Examine factory-wise delivery efficiency and operational consistency.
* Develop an interactive Streamlit dashboard for logistics monitoring.
* Provide actionable recommendations for route optimization and supply chain improvement.

---

## 📊 Dataset Information

| Attribute         | Details                            |
| ----------------- | ---------------------------------- |
| Domain            | Logistics & Supply Chain Analytics |
| Business Type     | Distribution & Transportation      |
| Total Shipments   | 10,194                             |
| Total Sales       | $141,784                           |
| Gross Profit      | $93,443                            |
| Average Lead Time | 1320.84 Days                       |

### Dataset Features

| Feature          | Description                        |
| ---------------- | ---------------------------------- |
| Order ID         | Unique shipment order identifier   |
| Order Date       | Shipment order date                |
| Ship Date        | Delivery date                      |
| Ship Mode        | Shipping method used               |
| Customer ID      | Unique customer identifier         |
| State/Province   | Destination state                  |
| Region           | Destination region                 |
| Product Name     | Product shipped                    |
| Sales            | Revenue generated                  |
| Units            | Quantity shipped                   |
| Gross Profit     | Profit generated                   |
| Cost             | Product cost                       |
| Lead_Time        | Delivery lead time                 |
| Factory          | Source manufacturing facility      |
| Route_State      | Factory-to-state route             |
| Route_Region     | Factory-to-region route            |
| Efficiency_Score | Calculated route efficiency metric |

---

## ❓ Problem Statement

Nassau Candy Distributor handles a large volume of shipments across multiple regions and transportation routes. Variations in delivery lead times, route performance, and regional logistics efficiency can affect customer satisfaction and operational effectiveness.

This project aims to answer:

* Which routes are the most efficient?
* Which routes experience the highest delivery delays?
* Which regions contribute the highest sales?
* How do shipping modes impact delivery performance?
* Are factories operating with consistent efficiency?
* What patterns exist in lead-time distribution?
* How can route efficiency be improved?
* How can logistics analytics support better decision-making?

---

## 🛠 Tools & Technologies

### Platform

* Streamlit

### Programming Language

* Python

### Libraries Used

#### Data Processing

* Pandas
* NumPy

#### Visualization

* Plotly Express
* Plotly Graph Objects

#### Dashboard Development

* Streamlit

---

## 🧹 Data Preprocessing & Cleaning

### Steps Performed

* Missing value validation
* Duplicate record verification
* Data type conversion
* Lead-time calculation
* Route engineering
* Factory-level categorization
* Region-wise aggregation
* Shipment performance analysis

### Feature Engineering

#### Numerical Features

* Lead Time
* Route Efficiency Score
* Gross Profit
* Sales Contribution
* Shipment Volume

#### Analytical Features

* Factory-to-State Routes
* Factory-to-Region Routes
* Delay Frequency
* Regional Performance Metrics
* Shipping Mode Analysis

---

## 🔍 Exploratory Data Analysis (EDA)

### Activities Performed

* Shipment Distribution Analysis
* Route Performance Analysis
* Regional Sales Analysis
* Factory Performance Analysis
* Shipping Mode Analysis
* Lead Time Distribution Analysis
* Delay Frequency Analysis
* Efficiency Score Analysis

### EDA Outcome

* Efficient and inefficient routes identified.
* Regional logistics performance evaluated.
* Shipping mode effectiveness measured.
* Factory consistency analyzed.
* Delivery delay patterns identified.
* Route optimization opportunities discovered.

---

## 📈 KPI Dashboard Analysis

| KPI Metric                   | Value        |
| ---------------------------- | ------------ |
| Total Shipments              | 10,194       |
| Average Lead Time            | 1320.84 Days |
| Total Sales                  | $141,784     |
| Gross Profit                 | $93,443      |
| Delay Frequency (>1274 Days) | 42.20%       |

### KPI Insights

* The company processed 10,194 shipments across multiple regions.
* Total sales reached $141,784 with gross profit of $93,443.
* Average lead time was 1320.84 days.
* Approximately 42.20% of shipments exceeded the average delay threshold.
* The distribution network maintained strong profitability and operational consistency.

---

## 📊 Visualizations

### Route Performance Analysis

* Top 10 Most Efficient Routes
* Bottom 10 Most Inefficient Routes

### Regional Analysis

* Regional Sales Contribution
* Average Lead Time by Region

### Shipping Analysis

* Ship Mode Performance
* Average Lead Time by Ship Mode

### Delivery Analysis

* State-wise Lead Time Distribution
* Lead Time Histogram
* Delay Frequency Analysis

### Factory Analysis

* Factory-wise Lead Time Distribution
* Factory Performance Comparison

### Relationship Analysis

* Sales vs Lead Time Scatter Plot

---

## 📌 Key Insights

* Standard Class generated the highest sales and gross profit.
* Pacific region contributed 32.7% of total revenue.
* Atlantic region contributed 29.1% of total revenue.
* Pacific and Atlantic regions together generated approximately 61.8% of total sales.
* Wicked Choccy's → Maine was the most efficient route.
* Sugar Shack → New Jersey was the least efficient route.
* Regional lead-time differences remained highly consistent across the network.
* Factory-wise analysis showed nearly identical performance across all factories.
* Route and destination characteristics influence delivery performance more than factory operations.

---

## 📊 Types of Analysis

### Descriptive Analysis

Shipment data was analyzed to understand logistics performance, route efficiency, sales contribution, and delivery trends.

### Diagnostic Analysis

Route inefficiencies, regional differences, shipping mode effectiveness, and delivery delays were identified.

### Predictive Analysis

Current shipment patterns suggest opportunities for lead-time prediction and route optimization models.

### Prescriptive Analysis

The organization should prioritize route optimization, delay reduction strategies, and logistics performance monitoring.

---

## 💡 Recommendations

* Optimize underperforming routes with consistently high lead times.
* Focus improvement efforts on low-efficiency destination states.
* Strengthen logistics planning for delay-prone regions.
* Maintain Standard Class shipping as the primary distribution strategy.
* Monitor route-level KPIs continuously.
* Implement predictive lead-time monitoring systems.
* Use route efficiency metrics for transportation planning.

---

## 🚀 Future Enhancements

### Real-Time Logistics Monitoring

Integrate live shipment tracking for real-time operational visibility.

### Lead Time Prediction

Develop machine learning models for delivery forecasting.

### Route Optimization Engine

Implement intelligent route recommendation systems.

### GIS-Based Logistics Mapping

Visualize routes geographically using mapping technologies.

### Supply Chain Risk Analysis

Detect high-risk routes and delivery bottlenecks proactively.

### AI-Driven Logistics Analytics

Apply predictive analytics for transportation optimization and performance improvement.

---

## ✅ Conclusion

The Nassau Candy Shipping Route Efficiency Analysis Project successfully transformed logistics and shipment data into actionable business insights through data analytics, KPI monitoring, and interactive visualization.

The analysis revealed that the distribution network processed over 10,000 shipments while generating strong revenue and profitability. Standard Class shipping emerged as the most operationally effective shipping method, while route-specific factors had a greater impact on delivery performance than factory operations.

The Streamlit dashboard provides an effective logistics intelligence solution for monitoring route efficiency, identifying bottlenecks, optimizing transportation performance, and supporting data-driven supply chain decision-making.

---

## 👩‍💻 Author

**Kamali.K**

Data Analytics Intern

Aspiring Data Analyst
