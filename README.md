# python_mid_term_project_notes

### 项目文档：患者管理系统

------

#### **项目概述**

**项目名称：** 患者管理系统
 **项目描述：**
 本项目是一个简单的患者管理系统，旨在通过命令行界面（CLI）实现患者信息的增删查改等功能。用户可以通过交互式菜单操作系统，管理存储在本地文件中的患者数据。

**技术栈：**

- 编程语言：Python
- 数据存储：文本文件（`patient_records.txt`）
- 模块化设计：数据管理和患者管理分工明确

------

#### **项目功能**

1. **患者信息录入**
    用户可以录入患者的基本信息（如姓名、性别、年龄、身高、体重、血压、诊断结果等）。
2. **患者信息查询**
    根据患者ID查询对应的详细信息。
3. **患者信息修改**
    更新指定患者的某些字段信息。
4. **患者信息删除**
    删除指定患者的信息。
5. **文件存储与读取**
    将患者信息存储在本地文件中，并支持系统重启后的数据加载。

------

#### **系统架构**

1. **主程序 (`main.py`)**
   - 提供用户交互界面，通过菜单形式调用核心功能。
   - 实现系统的主逻辑控制。
2. **患者管理模块 (`patient.py`)**
   - 定义 `Patient` 类，封装患者信息及操作方法。
3. **数据管理模块 (`data_manager.py`)**
   - 实现数据的存储与加载逻辑。
   - 处理文件操作（读取和写入）。

------

#### **模块说明**

##### **Patient类 (`patient.py`)**

**属性：**

- `patient_id`：患者ID
- `name`：姓名
- `age`：年龄
- `gender`：性别
- `weight`：体重（kg）
- `height`：身高（cm）
- `diagnosis`：诊断结果
- `systolic_bp`：收缩压（mmHg）
- `diastolic_bp`：舒张压（mmHg）
- `last_visit`：最后就诊日期

**方法：**

- `__str__`：格式化患者信息为字符串。

##### **数据管理 (`data_manager.py`)**

**功能：**

- **文件加载：** 从本地文件读取患者信息，并转化为 `Patient` 对象列表。
- **文件存储：** 将 `Patient` 对象列表写入本地文件。
- **患者操作：** 提供增删改查接口。

------

#### **功能实现细节**

1. **主程序逻辑**

   - 用户选择对应的功能编号。
   - 根据输入调用患者管理模块或数据管理模块。

2. **数据存储格式**

   - 每条记录以一行为单位，字段用四个空格分隔。

   - 示例：

     ```
     P001    John Doe    30    M    70.5    175.0    Normal    120.0    80.0    2023-10-01
     P002    Jane Smith    28    F    60.0    165.0    Normal    110.0    70.0    2023-10-01
     ```

3. **异常处理**

   - **文件不存在：** 自动创建空文件。
   - **编码问题：** 使用 `utf-8` 读取和写入文件。
   - **数据不完整：** 跳过字段数不足的记录，并记录日志。

------

#### **使用指南**

1. **启动项目**

   - 确保 Python 环境已安装（建议版本 ≥ 3.7）。
   - 将项目文件夹下载到本地。

2. **运行程序**

   ```bash
   python main.py
   ```

3. **功能菜单**

   - 输入功能编号进行操作：

     ```
     1. 查询患者信息
     2. 添加新患者
     3. 修改患者信息
     4. 删除患者信息
     5. 退出系统
     ```

------

#### **代码示例**

**主程序菜单部分：**

```python
class HealthSystem:
    def __init__(self):
        self.data_manager = DataManager('patient_records.txt')

    def run(self):
        while True:
            print("\n1. 查询患者信息")
            print("2. 添加新患者")
            print("3. 修改患者信息")
            print("4. 删除患者信息")
            print("5. 退出系统")
            choice = input("选择操作: ").strip()
            if choice == '1':
                patient_id = input("输入患者ID: ").strip()
                patient = self.data_manager.get_patient(patient_id)
                print(patient if patient else "未找到该患者信息。")
            elif choice == '2':
                # 添加患者逻辑
                pass
            elif choice == '3':
                # 修改患者逻辑
                pass
            elif choice == '4':
                # 删除患者逻辑
                pass
            elif choice == '5':
                print("系统已退出。")
                break
            else:
                print("无效输入，请重新选择。")
```

------

#### **总结**

本项目通过模块化设计，实现了患者信息管理的基本功能，适合作为初学者熟悉 Python 文件操作与类设计的练习项目。未来可以通过引入数据库、数据分析模块等进一步提升项目的实用性和扩展性。