import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
ROOT=Path(__file__).resolve().parent
df=pd.read_csv(ROOT/"data/hr_employee_data.csv")
s=df.groupby("department",as_index=False).agg(employees=("employee_id","count"),attrition_rate=("attrition","mean"))
s["attrition_pct"]=(100*s.attrition_rate).round(2)
with pd.ExcelWriter(ROOT/"hr_attrition_report.xlsx",engine="openpyxl") as w:
 df.to_excel(w,sheet_name="Employees",index=False); s.to_excel(w,sheet_name="Department_Summary",index=False)
print("Overall attrition %:",round(100*df.attrition.mean(),2)); print(s)
s.plot(x="department",y="attrition_pct",kind="bar",legend=False,title="Attrition by Department"); plt.tight_layout(); plt.savefig(ROOT/"attrition_by_department.png")
