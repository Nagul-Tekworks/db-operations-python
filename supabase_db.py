from sqlalchemy import create_engine
import pandas as pd


DATABASE_URL = "postgresql://postgres.qfwxfyakjktjzibiabnt:9052425905@aws-1-ap-southeast-1.pooler.supabase.com:6543/postgres"

# Create engine
engine = create_engine(DATABASE_URL)

df = pd.read_sql("SELECT * FROM public.Student", engine)
print("Connection successful!......")
print(df)
