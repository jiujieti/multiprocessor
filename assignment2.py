import xml.etree.ElementTree as ET
import os
import xlsxwriter
tree = ET.parse(r'C:\Python27\dse.xml')
root = tree.getroot()
top_level_specification = root.find('{uri:poosl}top_level_specification')
instance = top_level_specification.find('{uri:poosl}instance')
instance_list = instance.findall('{uri:poosl}instantiation_expression')
workbook = xlsxwriter.Workbook('2node-s2-arm11-mips.xlsx')
worksheet = workbook.add_worksheet()
row = 0
node = []
for instantiation_expression in instance_list:
    parameter_name = instantiation_expression.get('parameter_name')
    if parameter_name == "MapTask1To" or parameter_name == "MapTask2To" or parameter_name == "MapTask3To" or parameter_name == "MapTask4To" or parameter_name == "MapTask5To" or parameter_name == "MapTask6To" or parameter_name == "MapTask7To" or parameter_name == "MapTask8To":
        body_expression = instantiation_expression.find('{uri:poosl}body_expression')
        node.append(body_expression.find('{uri:poosl}constant'))



def excel_function(index1,index2,index3,index4,index5,index6,index7,index8,ro):
    tree.write('output.xml','UTF-8')
    o = os.system(r'rotalumis.exe -f output.xml')
    col = 0
    worksheet.write(ro,col,index1)
    worksheet.write(ro,col+1,index2)
    worksheet.write(ro,col+2,index3)
    worksheet.write(ro,col+3,index4)
    worksheet.write(ro,col+4,index5)
    worksheet.write(ro,col+5,index6)
    worksheet.write(ro,col+6,index7)
    worksheet.write(ro,col+7,index8)
    print row
    f1 = open('Application.log','r')
    line1 = f1.readlines()
    latency = line1[6][9:]
    f2 = open('Battery.log','r')
    line2 = f2.readlines()
    power = line2[2][24:41]
    energy = float(latency)*float(power)
    energy_latency = float(energy)*float(latency)
    worksheet.write(ro,col+8,float(latency))
    worksheet.write(ro,col+9,float(power))
    worksheet.write(ro,col+10,energy)
    worksheet.write(ro,col+11,energy_latency)


for t8 in range (1,3):
    node[7].text = '"'+'Node'+ str(t8)+'"'
    for t7 in range (1,3):
        node[6].text = '"'+'Node'+ str(t7)+'"'
        for t6 in range (1,3):
            node[5].text = '"'+'Node'+ str(t6)+'"'
            for t5 in range (1,3):
                node[4].text = '"'+'Node'+ str(t5)+'"'
                for t4 in range (1,3):
                    node[3].text = '"'+'Node'+ str(t4)+'"'
                    for t3 in range (1,3):
                        node[2].text = '"'+'Node'+ str(t3)+'"'
                        for t2 in range (1,3):
                            node[1].text = '"'+'Node'+ str(t2)+'"'
                            for t1 in range (1,3):
                                node[0].text = '"'+'Node'+ str(t1)+'"'
                                excel_function(t1,t2,t3,t4,t5,t6,t7,t8,row)
                                row = row + 1


workbook.close()




