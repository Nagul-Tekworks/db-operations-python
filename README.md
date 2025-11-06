# db-operations-python

📊 Data Loading with Python (MySQL, Supabase, REST API)

This repository demonstrates how to connect Python with multiple data sources — MySQL, Supabase, and REST APIs — and load data into Pandas DataFrames for analysis or processing.

📁 data-loading-with-python/
│
├── mysql_connectivity.py           # Connects to MySQL and loads table data into DataFrame
├── supabase_connectivity.py        # Connects to Supabase and loads data into DataFrame
├── api_data_loader.py              # Fetches data from REST APIs and converts to DataFrame
└── README.md                       # Project documentation

🚀 Features

✅ Establish secure connection with MySQL database

✅ Connect to Supabase (PostgreSQL) using credentials

✅ Fetch and process data from REST API endpoints

✅ Load all data into Pandas DataFrames

✅ Export data to CSV or Excel if needed
⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

2. Install Required Packages
   pip install -r requirements.txt
If you don’t have a requirements.txt, you can install manually:
pip install pandas mysql-connector-python psycopg2-binary requests
