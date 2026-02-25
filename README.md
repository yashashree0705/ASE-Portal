# ASE-Portal
Web app for Ador Welding Limited (AWL) users to log in and view two reports

Overview:
•	Purpose: Web app for Ador Welding Limited (AWL) users to log in and view two reports:
1.	Billing Report – line-level billing/invoice data (customer, invoice, product, qty, values).
2.	Achievement Report – product-group summary (target vs actual sales, RM margins, percentages).

•	Data source: Oracle EBS only. No SQL Server, no Postgres, no separate app DB. User identity and all report data are fetched from Oracle.

•	Recommended stack: Backend: Python + FastAPI (talks to Oracle via oracledb). Frontend: Any (e.g. React, Next.js, or simple HTML/Jinja templates served by FastAPI).
