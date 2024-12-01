"""
@author  Fish
@version 1.0
"""
import re
from datetime import datetime

class Patient:
    def __init__(self, patient_id, name, age, gender, height, weight, blood_pressure, blood_sugar, cholesterol, check_date):
        """
        功能：初始化患者对象
        参数：所有患者基本信息字段
        异常：无
        """
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.blood_pressure = blood_pressure
        self.blood_sugar = blood_sugar
        self.cholesterol = cholesterol
        self.check_date = check_date

    def validate(self):
        """
        功能：验证患者数据的有效性
        返回：bool - 验证是否通过
        异常：ValueError - 数据验证失败时抛出，包含具体错误信息
        """
        if not self.patient_id.startswith("P"):
            raise ValueError("患者ID必须以'P'开头")
        if not 0 <= self.age <= 120:
            raise ValueError("年龄必须在0到120之间")
        if self.gender not in ['男', '女']:
            raise ValueError("性别必须为'男'或'女'")
        if not 50 <= self.height <= 250:
            raise ValueError("身高必须在50cm到250cm之间")
        if not 20 <= self.weight <= 200:
            raise ValueError("体重必须在20kg到200kg之间")
        if not re.match(r"^\d+/\d+$", self.blood_pressure):
            raise ValueError("血压格式不正确，应为'收缩压/舒张压'")
        if not isinstance(self.blood_sugar, float):
            raise ValueError("血糖必须为浮点数")
        if not isinstance(self.cholesterol, float):
            raise ValueError("胆固醇必须为浮点数")
        try:
            datetime.strptime(self.check_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("日期格式错误，应为'YYYY-MM-DD'")
        return True

    def to_string(self):
        return f"{self.patient_id}\t{self.name}\t{self.age}\t{self.gender}\t{self.height}\t{self.weight}\t{self.blood_pressure}\t{self.blood_sugar}\t{self.cholesterol}\t{self.check_date}"

    def __str__(self):
        return f"ID: {self.patient_id}, 姓名: {self.name}, 年龄: {self.age}, 性别: {self.gender}, 身高: {self.height}cm, 体重: {self.weight}kg, 血压: {self.blood_pressure}, 血糖: {self.blood_sugar}, 胆固醇: {self.cholesterol}, 检查日期: {self.check_date}"
