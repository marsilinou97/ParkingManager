from RevenueCategory import RevenueCategory
from Report import Report
from datetime import date


revenuecategory1 = RevenueCategory("Parking Transaction w/ Revenue,", 500, 5000.00)
revenuecategory2 = RevenueCategory("Key card transaction,", 100, 0.00)
revenuecategory3 = RevenueCategory("Validation Transaction,", 200, 0.00)
list = [revenuecategory1,revenuecategory2, revenuecategory3]
report1 = Report(date.today(), list)
print(report1)
    