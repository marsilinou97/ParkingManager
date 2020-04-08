from typing import Optional

from fpdf import FPDF
import csv

from DatabaseDAO import add_revenue_category, execute_query_with_return, add_report, connect_report_with_category
from RevenueCategory import RevenueCategory
from Report import Report
import datetime
from RevenueController import total
from database_test import clear_table, select_all_from_table, display_from_table, select_latest_entry_in_column
import DatabaseDAO as dao

def get_report(month: int, year: int, day: int = 1) -> Optional[Report]:
    values = dict(month=month, year=year, day=day)
    results = dao.execute_query_with_return(
        f"""SELECT R.ISSUED_ON, R.START_RANGE, R.END_RANGE, RC.REVENUE_CATEGORY, RC.QUANTITY, RC.REVENUE
                FROM REPORTS R
                         INNER JOIN REPORTS_REVENUE_CATEGORIES RRC ON R.ID = RRC.REPORT
                         INNER JOIN REVENUE_CATEGORIES RC ON RRC.REVENUE_CATEGORY = RC.ID
                WHERE date_part('day', START_RANGE) = %(day)s
                  AND date_part('month', START_RANGE) = %(month)s
                  AND date_part('year', START_RANGE) = %(year)s;""", values, False)
    revenue_categories = list()
    payment_categories = list()
    if len(results) > 0:
        for result in results:
            result = result[3:]
            if result[0].lower() in ['cash', 'debit', 'check', 'card', 'credit']:
                revenue_categories.append(RevenueCategory(*result))
            else:
                payment_categories.append(RevenueCategory(*result))
        report = Report(*results[0][:3], revenue_categories, payment_categories)
        print(report)
    else:
        print("No matching report")

def get_report(month: int, year: int, day: int = 1) -> Optional[Report]:
    values = dict(month=month, year=year, day=day)
    results = execute_query_with_return(
        f"""SELECT R.ISSUED_ON, R.START_RANGE, R.END_RANGE, RC.REVENUE_CATEGORY, RC.QUANTITY, RC.REVENUE
                FROM REPORTS R
                         INNER JOIN REPORTS_REVENUE_CATEGORIES RRC ON R.ID = RRC.REPORT
                         INNER JOIN REVENUE_CATEGORIES RC ON RRC.REVENUE_CATEGORY = RC.ID
                WHERE date_part('day', START_RANGE) = %(day)s
                  AND date_part('month', START_RANGE) = %(month)s
                  AND date_part('year', START_RANGE) = %(year)s;""", values, False)
    revenue_categories = list()
    payment_categories = list()
    if len(results) > 0:
        for result in results:
            result = result[3:]
            if result[0].lower() in ['cash', 'debit', 'check', 'card', 'credit']:
                revenue_categories.append(RevenueCategory(*result))
            else:
                payment_categories.append(RevenueCategory(*result))
        report = Report(*results[0][:3], revenue_categories, payment_categories)
        print(report)
    else:
        print("No matching report")

# get_report(month=1, year=2020)

def exportPDF(report):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, txt=str(report.get_start_range()) + "   -   " + str(report.get_end_range()), ln=1, align="C")
    pdf.set_font("Arial", 'B', 14)

    pdf.cell(0, 10, "Revenue Report Total", 0, 0, "L")
    pdf.set_x(pdf.l_margin)
    pdf.cell(0, 10, "Quantity", 0, 0, "C")
    pdf.set_x(pdf.l_margin)
    pdf.cell(0, 10, "Revenue", 0, 1, "R")

    pdf.set_font("Arial", '', 14)
    for revenuecategory in report.get_revenue_categories():
        pdf.cell(0, 10, txt=str(revenuecategory.get_name()), ln=0, align="L")
        pdf.set_x(pdf.l_margin)
        pdf.cell(0, 10, txt=str(revenuecategory.get_quantity()), ln=0, align="C")
        pdf.set_x(pdf.l_margin)
        pdf.cell(0, 10, txt=str(revenuecategory.get_revenue()), ln=1, align="R")

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Payment Method", 0, 0, "L")
    pdf.set_x(pdf.l_margin)
    pdf.cell(0, 10, "Quantity", 0, 0, "C")
    pdf.set_x(pdf.l_margin)
    pdf.cell(0, 10, "Revenue", 0, 1, "R")

    pdf.set_font("Arial", '', 14)
    for revenuecategory in report.get_payment_categories():
        pdf.cell(0, 10, txt=str(revenuecategory.get_name()), ln=0, align="L")
        pdf.set_x(pdf.l_margin)
        pdf.cell(0, 10, txt=str(revenuecategory.get_quantity()), ln=0, align="C")
        pdf.set_x(pdf.l_margin)
        pdf.cell(0, 10, txt=str(revenuecategory.get_revenue()), ln=1, align="R")

    pdf.output(str(report.get_issued_on().date())+'.pdf')

def exportCSV(report):
    with open(str(report.get_issued_on().date())+'.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Revenue Report Total", "Quantity", "Revenue"])
        for revenuecategory in report.get_revenue_categories():
            writer.writerow([revenuecategory.get_name(), revenuecategory.get_quantity(), revenuecategory.get_revenue()])
        writer.writerow(["Payment Method", "Quantity", "Revenue"])
        for revenuecategory in report.get_payment_categories():
            writer.writerow([revenuecategory.get_name(), revenuecategory.get_quantity(), revenuecategory.get_revenue()])

def link_reports():
    current_rc_id = select_latest_entry_in_column("revenue_categories", "id")[0]
    current_report_id = select_latest_entry_in_column("reports", "id")[0]
    print(current_rc_id, "and", current_report_id)
    for i in range(9):
        connect_report_with_category(current_report_id, current_rc_id-i)

def main():
    # clear_table("reports_revenue_categories")
    # clear_table("revenue_categories");
    # clear_table("reports")

    # add_revenue_category("Parking Transaction w/ Revenue", 500, 5000.00)
    # add_revenue_category("Key card transaction", 100, 0.00)
    # add_revenue_category("Validation Transaction", 200, 0.00)
    # add_revenue_category("Total",0,0)
    # #
    # add_revenue_category("Cash", 500, 5000.00)
    # add_revenue_category("Check", 100, 0.00)
    # add_revenue_category("Debit", 200, 0.00)
    # add_revenue_category("Credit", 4, 200.00)
    # add_revenue_category("Total", 0, 0)
    # display_from_table("revenue_categories")
    # display_from_table("reports")

    link_reports()
    # issued_on = datetime.datetime(2020, 2, 26)
    # start_range = datetime.datetime(2020, 2, 26, 0, 0, 0)
    # end_range = datetime.datetime(2020, 2, 26, 23, 59, 59)
    # add_report(start_range, end_range, 1, issued_on)

    #link_reports()  #

    for row in select_all_from_table("reports_revenue_categories"):
        print(row)

    # get_report(2,2020,6)

    # paymentmethod1 = RevenueCategory("Cash", 500, 5000.00)
    # paymentmethod2 = RevenueCategory("Check", 100, 0.00)
    # paymentmethod3 = RevenueCategory("Debit", 200, 0.00)
    # paymentmethod4 = RevenueCategory("Credit", 4, 200.00)
    # paymentmethod5 = RevenueCategory("Total", 0, 0);

    # total(revenuecategory4, revenuecategory1, revenuecategory2, revenuecategory3)
    # total(paymentmethod5, paymentmethod1, paymentmethod2, paymentmethod3, paymentmethod4)
    # list = [revenuecategory1, revenuecategory2, revenuecategory3, revenuecategory4]
    # list2 = [paymentmethod1, paymentmethod2, paymentmethod3, paymentmethod4, paymentmethod5]

    # report1 = Report(issued_on, start_range, end_range, list, list2)
    # print(report1)
    # exportPDF(report1)
    # exportCSV(report1)
main()
