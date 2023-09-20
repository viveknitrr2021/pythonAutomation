from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

pdf.image('D:/pythonAutomation/com/resources/tiger.jpeg', w=80, h=50)

pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=50, txt="Malayan Tiger", align='C', ln=1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=0, h=20, txt="Description", ln=1)

text = """
The Malayan tiger is a tiger from a specific population of the Panthera tigris tigris 
subspecies that is native to Peninsular Malaysia. This population inhabits the southern 
and central parts of the Malay Peninsula and has been classified as critically endangered 
on the IUCN Red List since 2015. As of April 2014, the population was estimated at 80 to 
120 mature individuals with a continuous declining trend.

In the Malay language, the tiger is called harimau, also abbreviated to rimau.It is also 
known as the southern Indochinese tiger, to distinguish it from tiger populations in 
northern parts of Indochina, which are genetically different to this population.
"""

pdf.set_font(family='Times', size=12)
pdf.multi_cell(w=0, h=15, txt=text)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=20, txt="Kingdom: ")
pdf.set_font(family='Times',  size=14)
pdf.cell(w=100, h=20, txt="Animalia", ln=1)

pdf.output('output.pdf')
