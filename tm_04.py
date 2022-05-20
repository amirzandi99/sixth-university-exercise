def price(dates, codes, hours):
    p = 7.99
    e = 1.99
    fileName = "Charges.txt"
    myFile = open(fileName,"w")
    test = "Charges for " + dates[0] + "/" + dates[1] + "\nCharge\nCustomer Hours used per hour Average cost\n"
    myFile.write(test)
    # 
    for i in range(len(hours)):
        test = "\t" + codes[i] + "\t" + hours[i] + "\t"
        if(float(hours[i]) < 10):
            test += "\t" + str(p) + "\t" + str(float(hours[i]) * e / float(hours[i])) + "\t"
        else:
            test += str(float(hours[i]) * e) + "\t" + str(float(hours[i]) * float(hours[i]) / float(hours[i])) + "\t"
        test += "\n"
        myFile.write(test)
    # 
    myFile.close()
# 
def round_money(x):
    r = "{:.2f}".format(x)
    return r
# 
# 
temp = []
dates = []
codes = []
hours = []
fileName = "Data_file.txt"
myFile = open(fileName,"r")
note = myFile.readlines()
for i in note:
    txt = ""
    for j in range(len(i)-1):
        txt += i[j]
    temp.append(txt.split(' '))
for i in range(len(temp)):
    if(i == 0):
        dates.append(temp[i][0])
        dates.append(temp[i][1])
    else:
        codes.append(temp[i][0])
        hours.append(temp[i][1])
myFile.close()
# 
price(dates, codes, hours)