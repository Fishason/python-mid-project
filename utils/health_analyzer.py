"""
@author  Fish
@version 1.0
"""
class HealthAnalyzer:
    @staticmethod
    def calculate_bmi(height, weight):
        bmi = weight / ((height / 100) ** 2)
        if bmi < 18.5:
            return bmi, "偏瘦"
        elif bmi < 24:
            return bmi, "正常"
        elif bmi < 28:
            return bmi, "超重"
        else:
            return bmi, "肥胖"

    @staticmethod
    def analyze_blood_pressure(bp_str):
        systolic, diastolic = map(int, bp_str.split('/'))
        if systolic < 120 and diastolic < 80:
            return "正常"
        elif systolic < 140 or diastolic < 90:
            return "高血压前期"
        else:
            return "高血压"

    def generate_health_report(self, patient):
        bmi, bmi_category = self.calculate_bmi(patient.height, patient.weight)
        bp_status = self.analyze_blood_pressure(patient.blood_pressure)
        report = (
            f"健康报告 - {patient.name} ({patient.patient_id})\n"
            f"检查日期: {patient.check_date}\n"
            f"BMI: {bmi:.2f} ({bmi_category})\n"
            f"血压: {bp_status}\n"
            f"血糖: {patient.blood_sugar}\n"
            f"胆固醇: {patient.cholesterol}\n"
        )
        report_path = f"{patient.patient_id}_report.txt"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        return report
