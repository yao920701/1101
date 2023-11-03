# 輸入學生資料
sid = input("請輸入您的學號：")
sname = input("請輸入您的姓名：")
fchina = float(input("請輸入您的國文成績："))
fmath = float(input("請輸入您的數學成績："))
finfo = float(input("請輸入您的電腦成績："))

# 計算總分和平均分，使用round函數四捨五入至小數點後2位
total_score = round(fchina + fmath + finfo, 2)
average_score = round(total_score / 3, 2)

# 判斷是否及格
result = "合格" if average_score >= 60 else "不合格"

# 印出學生資料
print("-" * 30)
print(f"{sname}({sid})同學您好：")
print("以下是您的各科成績與分數評定")
print(f"國文：{fchina} / 數學：{fmath} / 電腦：{finfo}")
print(f"總分：{total_score} / 平均：{average_score}")
print("-" * 30)
print(f"成績判定：{result}")
