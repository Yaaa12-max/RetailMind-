#1.读取Excel文件
#2.保存成CSV
import pandas as pd
import os

#创建processed文件夹，若没有的话
os.makedirs("data/processed", exist_ok=True)

#读取excel文件
df = pd.read_excel("data/raw/Online Retail.xlsx")

#保存为CSV文件
df.to_csv("data/processed/retail_raw.csv", index = False, encoding="utf-8-sig")

#检查
print("F")