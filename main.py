from fpdf import FPDF
import pandas as pd

pdf= FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(False,margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font("Arial",style="B", size=12)
    pdf.set_text_color(100, 0, 0)
    #pdf.cell(w=0, h=12, txt= "Hello", align="L", ln=1, border=1)
    pdf.cell(w=0, h=12, txt= row["Topic"], align="L", ln=1)
    pdf.line(10,21,200,21)
    pdf.ln(260)
    pdf.set_font("Arial", style="I", size=8)
    pdf.set_text_color(180, 0, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R")
    for i in range(row["Pages"]-1):
        pdf.add_page()
        #footer
        pdf.set_font("Arial", style="I", size=8)
        pdf.set_text_color(180, 0, 180)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

pdf.output("output.pdf")

