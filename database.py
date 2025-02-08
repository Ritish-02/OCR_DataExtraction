import mysql.connector
import json
conn = mysql.connector.connect(host="localhost",user="root",password="020703",database="ocr_db")
cursor = conn.cursor()
def insert_data(data):
    cursor.execute("insert into patients (name,dob) values (%s,%s)",(data["patient_name"],data["dob"]))
    patient_id = cursor.lastrowid
    cursor.execute("insert into forms_data (patient_id,form_json) values (%s,%s)",(patient_id,json.dumps(data)))
    conn.commit()
    print("Data inserted into MYSQL database")