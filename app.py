
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.title("互動式線性迴歸視覺化工具")

# --- 1. 使用者介面 (UI) ---
st.sidebar.header("參數調整")

n_points = st.sidebar.slider("數據點數量 (n)", 100, 1000, 300)
coeff_a = st.sidebar.slider("係數 (a)", -10.0, 10.0, 2.5)
intercept_b = st.sidebar.slider("截距 (b)", -20.0, 20.0, 5.0)
noise_var = st.sidebar.slider("雜訊變異數 (var)", 0.0, 1000.0, 50.0)

# --- 2. 數據生成 ---
@st.cache_data
def generate_data(n, a, b, var):
    x = np.linspace(0, 100, n)
    noise = np.random.normal(0, np.sqrt(var), n)
    y = a * x + b + noise
    return pd.DataFrame({'x': x, 'y': y})

data = generate_data(n_points, coeff_a, intercept_b, noise_var)

# --- 3. 線性迴歸與離群值分析 ---
x_reshaped = data['x'].values.reshape(-1, 1)
y_true = data['y'].values

model = LinearRegression()
model.fit(x_reshaped, y_true)

y_pred = model.predict(x_reshaped)

# 計算殘差與離群值
residuals = np.abs(y_true - y_pred)
data['residuals'] = residuals

outliers = data.nlargest(5, 'residuals')

# --- 4. 視覺化 ---
fig, ax = plt.subplots(figsize=(10, 6))

# 繪製所有數據點
ax.scatter(data['x'], data['y'], alpha=0.6, label="Generated Data")

# 繪製迴歸線
ax.plot(data['x'], y_pred, color='red', linewidth=2, label="Regression Line")

# 標示離群值
ax.scatter(outliers['x'], outliers['y'], color='orange', s=100, edgecolor='black', zorder=5, label="Top 5 Outliers")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Linear Regression and Outliers")
ax.legend()
ax.grid(True)

# 在 Streamlit 中顯示圖表
st.pyplot(fig)

# --- 顯示迴歸方程式 ---
st.subheader("迴歸線方程式")
model_coeff = model.coef_[0]
model_intercept = model.intercept_
st.latex(f"y = {model_coeff:.2f}x + {model_intercept:.2f}")

# 顯示離群值數據
st.subheader("前 5 大離群值")
st.dataframe(outliers)
