"""
@author  Fish
@version 1.0
"""
import os
from models.patient import Patient

class DataManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as f:
                pass  # Create file if not exists
        patients = []
        with open(self.file_path, 'r', encoding='utf-8') as f:
            for line in f:
                #print(f"Reading line: {line.strip()}")  # 调试日志，打印读取的行
                fields = line.strip().split("    ")  # 修改为四个空格作为分隔符
                #print(f"Parsed fields: {fields}")  # 调试日志，打印分割后的字段
                if len(fields) == 10:  # 确保每行有正确数量的字段
                    patient = Patient(
                        fields[0], fields[1], int(fields[2]), fields[3], float(fields[4]), float(fields[5]),
                        fields[6], float(fields[7]), float(fields[8]), fields[9]
                    )
                    patients.append(patient)
        #print(f"Loaded patients: {patients}")  # 调试日志，打印加载的患者数据
        return patients

    def save_data(self, patients):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            for patient in patients:
                f.write(patient.to_string() + '\n')

    def add_patient(self, patient):
        patients = self.load_data()
        if any(p.patient_id == patient.patient_id for p in patients):
            raise ValueError("患者ID已存在")
        if patient.validate():
            patients.append(patient)
            self.save_data(patients)

    def get_patient(self, patient_id):
        patients = self.load_data()
        for patient in patients:
            if patient.patient_id == patient_id:
                return patient
        return None

    def update_patient(self, patient):
        patients = self.load_data()
        for i, p in enumerate(patients):
            if p.patient_id == patient.patient_id:
                patients[i] = patient
                self.save_data(patients)
                return
        raise ValueError("患者不存在")

    def delete_patient(self, patient_id):
        patients = self.load_data()
        patients = [p for p in patients if p.patient_id != patient_id]
        self.save_data(patients)

    def get_all_patients(self):
        return self.load_data()
