-- Import CSV as hr_employee_data
SELECT ROUND(100.0*AVG(attrition),2) AS attrition_pct FROM hr_employee_data;
SELECT department,COUNT(*) AS employees,ROUND(100.0*AVG(attrition),2) AS attrition_pct FROM hr_employee_data GROUP BY department;
SELECT overtime,ROUND(100.0*AVG(attrition),2) AS attrition_pct FROM hr_employee_data GROUP BY overtime;
SELECT years_at_company,ROUND(100.0*AVG(attrition),2) AS attrition_pct FROM hr_employee_data GROUP BY years_at_company ORDER BY years_at_company;
