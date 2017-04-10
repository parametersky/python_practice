import pisa 
data= open('1.htm').read()
result = file('test.pdf', 'wb') 
pdf = pisa.CreatePDF(data, result) 
result.close() 
pisa.startViewer('test.pdf') 