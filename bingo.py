import random, os
filename = "bingokaarten.html"
title = "42 mistake bingo"
os.remove(filename)
file = open(filename, "w")
file.write("<html><head><STYLE TYPE='text/css'>H2 {page-break-before: always}</STYLE><title></title></head><body><center>")
for x in range(100):
    if x/2 == int(x/2):
        file.write("<h2></h2>")
    sample = random.sample(range(1, 42),25)
    z = 0
    file.write("<BR><BR><BR><BR><table width='500px' style='border: 1pt solid #000000; background: "\
               "#fff;border-radius:10px;-moz-border-radius:10px;-webkit-border-radius:10px;'><THEAD style='border: "\
               "1pt solid #000000; background: #000000;border-radius:10px;-moz-border-radius:10px;-webkit-border-radius:10px;' text='white'"\
               "><TR><TD colspan=5><font color='#fff' size='20px'><center>"+ title +"</center></font></TR></THEAD><TBODY>")
    for y in range(5):
        file.write("<tr>")
        for q in sample[z:z+5]:
            file.write("<td align='center' style='border: 1pt solid #000000;'><font size='20px'>" + str(q) +"</font></td>")
        file.write("")
        file.write("</tr>")
        z += 5
    file.write("</TBODY></table>")
    
file.write("</center></body></html>")
file.close()
print("BINGO!")
