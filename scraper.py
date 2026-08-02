import pandas as pd
import random
from datetime import datetime, timedelta

# 1. Define the regions based on AREIS Subnational Scoring targets
regions = ['Kano, Nigeria', 'Accra, Ghana', 'Nairobi, Kenya', 'Copperbelt, Zambia', 'Gauteng, South Africa']
roles = ['Field Data Engineer', 'Site Surveyor', 'Community Engagement Lead', 'ESG Compliance Officer']
skills_matrix = ['QField, KoboToolbox', 'Solar PV Sizing, AutoCAD', 'Community Liaison, Local Dialect', 'Environmental Auditing']

# 2. Simulate the scraped raw data from professional networks
def generate_scraped_talent_data(num_records):
    data = []
    for _ in range(num_records):
        region = random.choice(regions)
        role = random.choice(roles)
        
        # Match skills to roles for realism
        if role == 'Field Data Engineer':
            primary_skill = 'QField, KoboToolbox'
        elif role == 'Site Surveyor':
            primary_skill = 'Solar PV Sizing, AutoCAD'
        elif role == 'Community Engagement Lead':
            primary_skill = 'Community Liaison, Local Dialect'
        else:
            primary_skill = 'Environmental Auditing'

        record = {
            'Candidate_ID': f"PFG-{random.randint(1000, 9999)}",
            'Location': region,
            'Profile_Role': role,
            'Core_Competency': primary_skill,
            'Years_Experience': random.randint(1, 10),
            'Estimated_Availability_Days': random.randint(14, 60),
            'Data_Source': random.choice(['LinkedIn Scrape', 'Upwork API', 'Local Job Board'])
        }
        data.append(record)
    return pd.DataFrame(data)

# 3. Generate and clean the dataset
df_talent = generate_scraped_talent_data(250)

# 4. Create an aggregated view for HR Strategy
# Grouping by Location and Role to find average availability and talent pool size
df_strategic_view = df_talent.groupby(['Location', 'Profile_Role']).agg(
    Talent_Pool_Size=('Candidate_ID', 'count'),
    Avg_Days_to_Available=('Estimated_Availability_Days', 'mean'),
    Avg_Experience_Years=('Years_Experience', 'mean')
).reset_index()

# Round the numerical columns for clean reporting
df_strategic_view['Avg_Days_to_Available'] = df_strategic_view['Avg_Days_to_Available'].round(0)
df_strategic_view['Avg_Experience_Years'] = df_strategic_view['Avg_Experience_Years'].round(1)

# 5. Export to CSV to be ingested by Excel/Google Sheets
df_talent.to_csv('PFG_Raw_Talent_Pool.csv', index=False)
df_strategic_view.to_csv('PFG_Strategic_Readiness.csv', index=False)

print("Data pipeline executed successfully. CSVs generated for dashboard integration.")
