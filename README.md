# 互動式線性迴歸視覺化工具

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://aiot-homework-1-jyacwt63mddsyzgaihevrj.streamlit.app)

這是一個使用 Streamlit 建立的互動式 Web 應用程式，用於視覺化線性迴歸的基本概念。使用者可以動態生成數據、調整模型參數，並即時觀察迴歸線和離群值的變化。

## 🌟 功能亮點

- **動態數據生成**: 根據線性方程式 `y = ax + b + noise` 生成數據。
- **互動式參數調整**: 透過滑桿即時調整數據點數量 (`n`)、係數 (`a`)、截距 (`b`) 和雜訊變異數 (`var`)。
- **即時視覺化**: 使用散佈圖呈現生成的數據點。
- **線性迴歸分析**: 計算並繪製紅色的線性迴歸線。
- **離群值識別**: 自動識別並標示出前 5 個離群值。
- **顯示迴歸方程式**: 在介面上顯示計算出的迴歸線方程式。

## 🖼️ 應用程式預覽

*建議在此處插入您的應用程式截圖！*

![App Screenshot](URL_TO_YOUR_SCREENSHOT.png)

## 🚀 如何在本地端執行

若要在您自己的電腦上執行此專案，請依照以下步驟操作。

### 1. 複製倉庫

```bash
git clone https://github.com/Terry20030721/AIOT-Homework-1.git
cd AIOT-Homework-1
```

### 2. 安裝相依套件

確保您已安裝 Python 3.7+。然後執行以下指令安裝所有必要的函式庫：

```bash
pip install -r requirements.txt
```

### 3. 執行應用程式

```bash
streamlit run app.py
```

應用程式將會在您的瀏覽器中自動開啟。

## 🛠️ 使用技術

- **Streamlit**: 用於建立互動式 Web UI。
- **Pandas**: 用於數據處理。
- **NumPy**: 用於數值計算與數據生成。
- **Scikit-learn**: 用於執行線性迴歸模型。
- **Matplotlib**: 用於數據視覺化。
