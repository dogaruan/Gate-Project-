import os
import pandas as pd
from models import AccessLog
from database import SessionLocal
import shutil

def process_file(file_path, gate_name):
    session = SessionLocal()
    data = pd.read_csv(file_path)
    
    for _, row in data.iterrows():
        log = AccessLog(
            person_id=row['idPersoana'],
            access_time=row['data'],
            direction=row['sens'],
            gate_name=gate_name,
            gate_id=row['idPoarta']
        )
        session.add(log)
    session.commit()
    session.close()

def monitor_intrari_folder(folder_path, backup_folder):
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            gate_name = filename.split('.')[0]  
            process_file(os.path.join(folder_path, filename), gate_name)
            shutil.move(os.path.join(folder_path, filename), os.path.join(backup_folder, filename))
