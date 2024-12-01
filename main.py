"""
@author  Fish
@version 1.0
"""
from utils.data_manager import DataManager
from utils.health_analyzer import HealthAnalyzer
from models.patient import Patient

class HealthSystem:
    def __init__(self):
        self.data_manager = DataManager("data/patient_records.txt")
        self.health_analyzer = HealthAnalyzer()

    def display_menu(self):
        print("1. 查看患者信息")
        print("2. 添加新患者")
        print("3. 更新患者信息")
        print("4. 删除患者")
        print("5. 生成健康报告")
        print("0. 退出")

    def input_patient_data(self):
        patient_id = input("患者ID: ")
        name = input("姓名: ")
        age = int(input("年龄: "))
        gender = input("性别 (男/女): ")
        height = float(input("身高 (cm): "))
        weight = float(input("体重 (kg): "))
        blood_pressure = input("血压 (收缩压/舒张压): ")
        blood_sugar = float(input("血糖: "))
        cholesterol = float(input("胆固醇: "))
        check_date = input("检查日期 (YYYY-MM-DD): ")
        return Patient(patient_id, name, age, gender, height, weight, blood_pressure, blood_sugar, cholesterol, check_date)

    def run(self):
        while True:
            self.display_menu()
            choice = input("选择操作: ")
            if choice == '1':
                patient_id = input("输入患者ID: ")
                patient = self.data_manager.get_patient(patient_id)
                print(patient if patient else "患者不存在")
            elif choice == '2':
                patient = self.input_patient_data()
                self.data_manager.add_patient(patient)
            elif choice == '3':
                patient = self.input_patient_data()
                self.data_manager.update_patient(patient)
            elif choice == '4':
                patient_id = input("输入患者ID: ")
                self.data_manager.delete_patient(patient_id)
            elif choice == '5':
                patient_id = input("输入患者ID: ")
                patient = self.data_manager.get_patient(patient_id)
                if patient:
                    print(self.health_analyzer.generate_health_report(patient))
                else:
                    print("患者不存在")
            elif choice == '0':
                break
            else:
                print("无效选项，请重新输入！")


if __name__ == "__main__":
    HealthSystem().run()
