![image](https://github.com/user-attachments/assets/29150c7c-04a8-43ff-9f1a-e0f6753480f2)
✨Site Phishing AI Detector ✨
🚀 Project Overview
This project kicks phishing websites to the curb using machine learning. It breaks down website features (like URL structure, subdomain depth, and path levels) to determine if a site is legit or a phishing scam. Built with TensorFlow for the brain, Git LFS for the heavy lifting, and a lot of data crunching to deliver fast, accurate results.

⚡Game Plan 
Data Collection: Grab key features from websites (URL, subdomain level, etc.).

Model Training: Train a badass ML model that spots phishing websites.

Testing & Evaluation: Test the model’s accuracy. It better work.

Deployment: Get the model into action to catch phishing websites in real time.

How to Run Project

Prereq:

Python 3.x

TensorFlow for the model

Git LFS to handle those big files

🔥 Setup Instructions
Clone the Repo:

bash
Copy
git clone https://github.com/your-username/Tensorflow-AI-Phishing-Detector.git
cd Tensorflow-AI-Phishing-Detector
Set Up the Virtual Environment:

On Windows:

bash
Copy
python -m venv env
.\env\Scripts\Activate
On macOS/Linux:

bash
Copy
python3 -m venv env
source env/bin/activate
Install Dependencies:

bash
Copy
pip install -r requirements.txt
Activate Git LFS:

bash
Copy
git lfs install
Run the Project:

Train the Model:

bash
Copy
python model_training.py
Test the Model:

bash
Copy
python model_testing.py
Run Web API:

bash
Copy
python web_api.py
Deactivate the Virtual Environment:

bash
Copy
deactivate

📁 Project Structure
bash
Copy
/phishing-detector
  ├── model_training.py       # The beast that trains the model
  ├── model_testing.py        # Tests the model to make sure it works
  ├── web_api.py             # API to serve the model like a pro
  ├── /data                  # Where the dataset lives
  ├── requirements.txt       # All the Python dependencies you need
  └── .gitignore             # Ignore those big files we don't want

📌 Notes
Git LFS: We use Git LFS to manage large files, such as datasets and models.

Data:  For the most realistic results, it's best to download the Site Phishing Data online.



