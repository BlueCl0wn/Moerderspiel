from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, inch
print(A4[0])
canvas = Canvas("names.pdf", pagesize=A4)
canvas.setFont("Times-Roman", 16)
border = 1
border *= cm
n1 = 4
n2 = 9
x = "MathildeDarek"
l1 = list(range(int(border), int(A4[0]-border), int((A4[0]-2*border)/(n1))))
l2 = list(range(int(border), int(A4[1]-border), int((A4[1]-2*border)/(n2))))
print(l1)
for i in l1[:-1]:
    for j in l2[:-1]:
        canvas.drawString(i, j, x)

canvas.save()
