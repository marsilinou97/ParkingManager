from fpdf import FPDF
import csv
from RevenueCategory import RevenueCategory
from Report import Report
import datetime
from RevenueController import total

def exportPDF(report):
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0,10,txt= str(report.get_start_range())+"   -   "+str(report.get_end_range()), ln=1, align="C")
    pdf.set_font("Arial", 'B', 14)

    pdf.cell(0, 10, "Revenue Report Total",0,0,"L")
    pdf.set_x(pdf.l_margin)
    pdf.cell(0, 10, "Quantity", 0, 0, "C")
    pdf.set_x(pdf.l_margin)
    pdf.cell(0, 10, "Revenue", 0, 1, "R")

    pdf.set_font("Arial",'' , 14)
    for revenuecategory in report.get_revenue_categories():
        pdf.cell(0,10, txt=str(revenuecategory.get_name()), ln=0, align="L")
        pdf.set_x(pdf.l_margin)
        pdf.cell(0,10, txt=str(revenuecategory.get_quantity()), ln=0, align="C")
        pdf.set_x(pdf.l_margin)
        pdf.cell(0,10, txt=str(revenuecategory.get_revenue()), ln=1, align="R")

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


def main():
    revenuecategory1 = RevenueCategory("Parking Transaction w/ Revenue", 500, 5000.00)
    revenuecategory2 = RevenueCategory("Key card transaction", 100, 0.00)
    revenuecategory3 = RevenueCategory("Validation Transaction", 200, 0.00)
    revenuecategory4 = RevenueCategory("Total", 0, 0);

    paymentmethod1 = RevenueCategory("Cash", 500, 5000.00)
    paymentmethod2 = RevenueCategory("Check", 100, 0.00)
    paymentmethod3 = RevenueCategory("Debit", 200, 0.00)
    paymentmethod4 = RevenueCategory("Credit", 4, 200.00)
    paymentmethod5 = RevenueCategory("Total", 0, 0);

    total(revenuecategory4, revenuecategory1, revenuecategory2, revenuecategory3)
    total(paymentmethod5, paymentmethod1, paymentmethod2, paymentmethod3, paymentmethod4)
    list = [revenuecategory1, revenuecategory2, revenuecategory3, revenuecategory4]
    list2 = [paymentmethod1, paymentmethod2, paymentmethod3, paymentmethod4, paymentmethod5]
    issued_on = datetime.datetime(2020, 2, 26)
    start_range = datetime.datetime(2020, 2, 26, 0, 0, 0)
    end_range = datetime.datetime(2020, 2, 26, 23, 59, 59)
    report1 = Report(issued_on, start_range, end_range, list, list2)
    print(report1)
    exportPDF(report1)
    exportCSV(report1)
main()
