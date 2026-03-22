import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ---- CONFIGURACIÓN DE LA PÁGINA ----
st.set_page_config(page_title="Dashboard de Ventas", layout="wide")

st.title("Dashboard de Ventas ")
st.markdown("Análisis interactivo de ventas por categoría, región y segmento.")

# ---- CARGA DE DATOS ----
RUTA = Path(__file__).parent / "data" / "Sample_Superstore.csv"

@st.cache_data
def cargar_datos():
    df = pd.read_csv(RUTA, encoding="latin1")
    df["Order Date"] = pd.to_datetime(df["Order Date"], format="mixed", dayfirst=False)
    return df

df = cargar_datos()

# ---- FILTROS EN LA BARRA LATERAL ----
st.sidebar.header(" Filtros")

regiones = st.sidebar.multiselect(
    "Región",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

categorias = st.sidebar.multiselect(
    "Categoría",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

segmentos = st.sidebar.multiselect(
    "Segmento",
    options=df["Segment"].unique(),
    default=df["Segment"].unique()
)

# ---- APLICAR FILTROS ----
df_filtrado = df[
    df["Region"].isin(regiones) &
    df["Category"].isin(categorias) &
    df["Segment"].isin(segmentos)
]

# ---- KPIs ----
# Calculamos el total general para comparar con el filtrado
# Esto nos permite mostrar el delta — cuánto representa el filtro actual
ventas_total = df["Sales"].sum()
ganancias_total = df["Profit"].sum()
unidades_total = df["Quantity"].sum()

ventas_filtradas = df_filtrado["Sales"].sum()
ganancias_filtradas = df_filtrado["Profit"].sum()
unidades_filtradas = df_filtrado["Quantity"].sum()

col1, col2, col3 = st.columns(3)

with col1:
    # delta muestra la diferencia entre el valor filtrado y el total
    # Así el usuario sabe qué porcentaje representa su selección
    delta_ventas = ventas_filtradas - ventas_total
    st.metric(" Ventas Totales", f"${ventas_filtradas:,.0f}", delta=f"${delta_ventas:,.0f}")

with col2:
    delta_ganancias = ganancias_filtradas - ganancias_total
    st.metric(" Ganancias Totales", f"${ganancias_filtradas:,.0f}", delta=f"${delta_ganancias:,.0f}")

with col3:
    delta_unidades = unidades_filtradas - unidades_total
    st.metric(" Unidades Vendidas", f"{unidades_filtradas:,}", delta=f"{delta_unidades:,}")

st.divider()

# ---- GRÁFICAS FILA 1 ----
col4, col5 = st.columns(2)

with col4:
    st.subheader("Ventas por Categoría")

    ventas_categoria = df_filtrado.groupby("Category")["Sales"].sum().reset_index()
    fig1 = px.bar(
        ventas_categoria,
        x="Category",
        y="Sales",
        color="Category",
        text_auto=".2s"
    )
 
    st.plotly_chart(fig1, use_container_width=True)

with col5:
    st.subheader("Ventas por Región")
    ventas_region = df_filtrado.groupby("Region")["Sales"].sum().reset_index()
    fig2 = px.bar(
        ventas_region,
        x="Region",
        y="Sales",
        color="Region",
        text_auto=".2s"
    )
    st.plotly_chart(fig2, use_container_width=True)

# ---- GRÁFICAS FILA 2 ----
col6, col7 = st.columns(2)

with col6:
    st.subheader("Ganancias por Segmento")
   
    ganancias_segmento = df_filtrado.groupby("Segment")["Profit"].sum().reset_index()
    fig3 = px.pie(
        ganancias_segmento,
        values="Profit",
        names="Segment",
        hole=0.4
    )
    st.plotly_chart(fig3, use_container_width=True)

with col7:
    st.subheader("Top 10 Subcategorías por Ventas")
   
    top_sub = df_filtrado.groupby("Sub-Category")["Sales"].sum().reset_index()
    top_sub = top_sub.nlargest(10, "Sales")
    fig4 = px.bar(
        top_sub,
        x="Sales",
        y="Sub-Category",
        orientation="h",
        color="Sales",
        text_auto=".2s"
    )
    st.plotly_chart(fig4, use_container_width=True)

# ---- GRÁFICA DE TENDENCIA ----
st.subheader(" Tendencia de Ventas Mensual")
ventas_tiempo = df_filtrado.set_index("Order Date")["Sales"].resample("ME").sum().reset_index()
# px.line() crea una gráfica de líneas
# markers=True → agrega un punto en cada mes, más fácil de leer
fig5 = px.line(
    ventas_tiempo,
    x="Order Date",
    y="Sales",
    markers=True
)
st.plotly_chart(fig5, use_container_width=True)

st.divider()

# ---- TABLA DE DATOS ----
st.subheader(" Datos filtrados")
st.write(f"Mostrando **{len(df_filtrado):,} registros**")
st.dataframe(df_filtrado, use_container_width=True)