### AI Prompt: 使用 Streamlit 打造互動式線性迴歸視覺化工具

**專案目標:**
建立一個名為「互動式線性迴歸視覺化工具」的 Web 應用程式。此應用程式讓使用者能夠動態調整參數以生成數據、執行線性迴歸分析，並將數據點、迴歸線和離群值（Outliers）視覺化。

**技術棧:**
- **語言:** Python
- **框架:** Streamlit
- **函式庫:** NumPy, Scikit-learn, Matplotlib (或 Plotly), Pandas

**核心功能:**

**1. 使用者介面 (UI):**
- 使用 Streamlit 建立一個簡潔的互動式網頁介面。
- 在側邊欄 (sidebar) 放置所有參數調整控制項。
- **控制項包括:**
    - **數據點數量 (n):** 滑桿 (Slider)，範圍 100 到 1000。
    - **係數 (a):** 滑桿，範圍 -10.0 到 10.0。
    - **雜訊變異數 (var):** 滑桿，範圍 0 到 1000。
- 主畫面應顯示：
    - 應用程式標題。
    - 生成的數據視覺化圖表。
    - 計算出的迴歸線方程式。

**2. 數據生成:**
- 根據使用者在 UI 選擇的 `n`, `a`, `var` 來生成數據。
- `x` 值：在 0 到 100 之間生成 `n` 個均勻分佈的點。
- `y` 值：根據公式 `y = a*x + b + noise` 計算。
    - `b` (截距) 可設為一個固定值（例如 5）或也提供一個滑桿讓使用者調整。
    - `noise` (雜訊)：從常態分佈 `N(0, var)` 中生成 `n` 個隨機值。
- 將生成的 `(x, y)` 數據點儲存於 Pandas DataFrame 中。

**3. 線性迴歸與離群值分析:**
- 使用 `scikit-learn` 的 `LinearRegression` 模型來擬合生成的數據。
- 計算迴歸線的方程式 (斜率和截距)。
- **離群值識別:**
    - 計算每個數據點與迴g歸線之間的垂直距離（殘差）。
    - 找出距離最遠（絕對殘差最大）的 5 個點，將其標記為離群值。

**4. 視覺化:**
- 使用 Matplotlib 或 Plotly 繪製圖表。
- **圖表內容:**
    - 將生成的 `(x, y)` 數據點以散佈圖 (Scatter Plot) 形式繪製。
    - 在同一張圖上，以紅色線條繪製計算出的線性迴歸線。
    - 在圖表上特別標示出 5 個離群值（例如使用不同顏色、較大尺寸或加上註記）。

**期望成果:**
- 一個單一的 Python 腳本 (`app.py`)。
- 應用程式應具備完全的互動性：當使用者拖動任何一個滑桿時，圖表、迴歸線和離群值標示都應即時更新，無需重新載入頁面。

**執行指令:**
```bash
streamlit run app.py
```

---

### 開發與提交流程摘要

這部分記錄了我們成功完成專案開發與提交到 GitHub 的主要步驟。

**1. 專案初始化**
- **使用者**: 要求建立 `prompt.md` 以記錄對話。
- **Gemini**: 建立 `prompt.md`。

**2. 產生 AI Prompt**
- **使用者**: 提供互動式線性迴歸視覺化工具的專案計畫。
- **Gemini**: 根據計畫，產生一份詳細的 AI prompt 並寫入 `prompt.md`。

**3. 產生應用程式碼**
- **使用者**: 要求根據 prompt 建立 `app.py`。
- **Gemini**: 產生完整的 Streamlit 應用程式碼並存於 `app.py`。

**4. 更新文件**
- **使用者**: 要求將執行指令加入 `prompt.md`。
- **Gemini**: 將 `streamlit run app.py` 指令區塊更新至 `prompt.md`。

**5. 提交至 GitHub**
- **使用者**: 要求將專案上傳到 GitHub。
- **Gemini**: 執行以下成功的 Git 操作流程：
    1. `git add app.py prompt.md README.md`
    2. `git commit -m "feat: Initial commit for Streamlit linear regression app"`
    3. `git push origin main --force` (使用 force push 解決歷史不一致問題)

**6. 部署至 Streamlit Cloud**
- **使用者**: 提出要將應用部署到 Streamlit Community Cloud。
- **Gemini**: 
    1. 解釋需要 `requirements.txt` 檔案。
    2. 建立 `requirements.txt` 並加入相依套件。
    3. 將新檔案 commit 並 push 到 GitHub。
    4. 提供在 Streamlit Cloud 網站上進行部署的步驟指南。

**7. 建立 README 文件**
- **使用者**: 在部署後，要求建立一份專業的 `README.md` 文件。
- **Gemini**: 
    1. 向使用者詢問 Streamlit 應用的公開 URL。
    2. 根據使用者提供的 URL，撰寫一份包含專案介紹、功能、本地端執行方法等內容的 `README.md`。
    3. 將 `README.md` commit 並 push 到 GitHub。

**8. 更新 README 文件**
- **使用者**: 要求加入專案實作細節，並刪除截圖區塊。
- **Gemini**: 
    1. 分析使用者提供的文字與專案實際作法的差異。
    2. 撰寫了更貼近專案實際情況的「核心實作流程」章節。
    3. 刪除了預覽截圖區塊。
    4. 將更新後的 `README.md` commit 並 push 到 GitHub。