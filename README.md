# 📊 Dashboard de Ventas — Sample Superstore

## Overview
Interactive sales dashboard built with Streamlit and Plotly, analyzing retail transactions from the Sample Superstore dataset.

**Descripción:** Dashboard web interactivo de análisis de ventas construido con Python puro. Permite filtrar datos por región, categoría y segmento, visualizando KPIs en tiempo real, gráficas dinámicas y tendencias de ventas mensuales.

🔗 **Live App:** [Ver dashboard en vivo](https://dashboard-ventas-kelly.streamlit.app)

---

## Objectives
- Build an interactive web app using Python and Streamlit
- Implement dynamic filters that update charts and KPIs in real time
- Visualize sales performance by category, region, and customer segment
- Deploy the app publicly on Streamlit Cloud

---

## Key Features
- 💰 **3 KPIs** — Total Sales, Total Profit, Units Sold (with delta indicators)
- 🔽 **4 interactive filters** — Region, Category, Segment (sidebar)
- 📊 **5 Plotly charts** — Bar charts, donut chart, top 10 subcategories, monthly trend line
- 📋 **Filtered data table** — updates automatically with every filter change
- 🌐 **Public deployment** — accessible from any device, no installation required

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.14 | Main language |
| pandas | Data loading & filtering |
| Plotly Express | Interactive charts |
| Streamlit | Web app framework |
| Git + GitHub | Version control |
| Streamlit Cloud | Public deployment |

---

## Project Structure

```
dashboard-ventas/
├── data/
│   └── Sample_Superstore.csv    ← dataset
├── outputs/
├── app.py                       ← main Streamlit app
└── README.md
```

---

## Visualizations
- Sales by Category (bar chart)
- Sales by Region (bar chart)
- Profit by Segment (donut chart)
- Top 10 Sub-Categories by Sales (horizontal bar chart)
- Monthly Sales Trend 2014–2017 (line chart)

---

## Data Source
**Kaggle** — Sample Superstore Dataset  
Dataset: 9,994 records | 19 variables | 4 regions | 3 product categories

---

## How to Run Locally

```bash
# Clone the repository
git clone https://github.com/kellyvalentina/dashboard-ventas.git

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 👩‍💻 Author
**Kelly Valentina**  
