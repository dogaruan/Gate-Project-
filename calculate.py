from datetime import datetime, timedelta
import smtplib

def calculate_work_hours():
    session = SessionLocal()
    today = datetime.now().date()
    access_logs = session.query(AccessLog).filter(AccessLog.access_time >= today).all()
    
    employee_hours = {}
    for log in access_logs:
        if log.person_id not in employee_hours:
            employee_hours[log.person_id] = {'in': None, 'out': None}
        
        if log.direction == 'in':
            employee_hours[log.person_id]['in'] = log.access_time
        elif log.direction == 'out':
            employee_hours[log.person_id]['out'] = log.access_time
    
    underworked_employees = []
    for emp_id, times in employee_hours.items():
        if times['in'] and times['out']:
            worked_hours = (times['out'] - times['in']).total_seconds() / 3600
            if worked_hours < 8:
                underworked_employees.append((emp_id, worked_hours))
    
    send_underwork_notifications(underworked_employees)

def send_underwork_notifications(underworked_employees):
    for emp_id, hours_worked in underworked_employees:
        
