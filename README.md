![image](https://github.com/user-attachments/assets/29150c7c-04a8-43ff-9f1a-e0f6753480f2)

# ✨ Site Phishing AI Detector ✨ 

##  Overview  
This project kicks phishing websites to the curb using machine learning. It breaks down website features (like URL structure, subdomain depth, and path levels) to determine if a site is legit or a phishing scam. Built with **TensorFlow** for the brain, **Git LFS** for the heavy lifting, and a lot of data crunching to deliver fast, accurate results.

---
##  GamePlan

1. **Import Necessary Packages:**
    - `tensorflow` (for ML model training)
    - `pandas` (for data handling)
    - `requests` (for fetching website data)
    - `BeautifulSoup` (for parsing HTML)

2. **Data Collection:**
    - Gather website data (URL structure, subdomain depth, domain age, etc.)

3. **Model Training:**
    - Train a machine learning model to classify websites as phishing or safe.

4. **Testing & Evaluation:**
    - Test the model’s performance and optimize it.

5. **Deployment:**
    - Set up the model to detect phishing websites in real-time.


---

### 🔥 Prereq :
- Python 3.x
- TensorFlow for the model
- Git LFS to handle those big files

### ⚡Setup :

1. **Clone the Repo**:
    ```bash
    git clone https://github.com/your-username/Tensorflow-AI-Phishing-Detector.git
    cd Tensorflow-AI-Phishing-Detector
    ```

2. **Set Up Virtual Environment**:

    - Windows:
    ```bash
    python -m venv env
    .\env\Scripts\Activate
    ```

    - macOS/Linux:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Activate Git LFS**:
    ```bash
    git lfs install
    ```

5. **Run the Project**:

    - **Train the Model**:
    ```bash
    python model_training.py
    ```

    - **Test the Model**:
    ```bash
    python model_testing.py
    ```

    - **Run Web API**:
    ```bash
    python web_api.py
    ```

6. **Deactivate the Virtual Environment**:
    ```bash
    deactivate
    ```

---

## 📁 Project Structure

```bash
/phishing-detector
├── model_training.py   # The beast that trains the model
├── model_testing.py    # Tests the model to make sure it works
├── web_api.py          # API to serve the model like a pro
├── /data               # Where the dataset lives
├── requirements.txt    # All the Python dependencies you need
└── .gitignore          # Ignore those big files we don't want



