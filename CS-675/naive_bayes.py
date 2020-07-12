#Naive Bayes Algorithm Implementation without using numpy library
#First Machine Learning code ,.,.,
import sys

#function for reading Data File
def readDataFile(Filename,mode):
    data=[]
    file=open(Filename,mode)

    line = file.readline()

    while(line != ''):
        columns = line.split()
        arrRowData=[]
        for i in range(0,len(columns),1):
            arrRowData.append(float(columns[i]))
        data.append(arrRowData)
        line = file.readline()
    file.close()
    return data

#function for reading Label File
def readLabelFile(filename,mode):
    ldata={}
    file=open(filename,mode)

    line=file.readline()

    while(line != ''):
        columns = line.split()
        ldata[int(columns[1])]=int(columns[0])
        line = file.readline()

    file.close()
    return ldata






fileReadMode='r'

#Read Data File
dataFile= 'test.data'  # sys.argv[1]
data=readDataFile(dataFile,fileReadMode)
#print("Data File is : \n", data)

#ReadLabelFile
labelFile='train.0' # sys.argv[2]
label=readLabelFile(labelFile,fileReadMode)
#print("Labels are : \n ", label)

#Rows and Column
rows=len(data)
columns=len(data[0])
#print("rows :",rows,"columns :",columns)

#Calculate Mean
mean0=[]
mean1=[]
for i in range(0,columns,1):
    mean0.append(0)
    mean1.append(0)

#print("mean0 :", mean0, "\nmean1 : ",mean1)

#Number of occurences
n0=0.0000001
n1=0.0000001


for i in range(0,rows,1):
    if(label.get(i) != None and label.get(i)==0):
         n0 += 1
         for j in range(0,columns,1):
             mean0[j] += data[i][j]

    if(label.get(i) != None and label.get(i)==1):
        n1 += 1
        for j in range(0,columns,1):
            mean1[j] += data[i][j]


for j in range(0,columns,1):
    mean0[j] /= n0
    mean1[j] /= n1

# print(n0,n1)
print("Means : \n\tmean0 :", mean0, "\n\tmean1 : ",mean1)

#Calculate Variance

var0=[]
var1=[]

for i in range(0,columns,1):
    var0.append(0.0000001)
    var1.append(0.0000001)


for i in range(0,rows,1):
    if(label.get(i) != None and label.get(i)==0):
        for j in range(0,columns,1):
            var0[j] += ((mean0[j] - data[i][j])**2)

    if(label.get(i) != None and label.get(i)==1):
        for j in range(0,columns,1):
            var1[j] += ((mean1[j] - data[i][j])**2)


#Calculate Variance
for j in range(0,columns,1):
    var0[j] /= n0
    var1[j] /= n1


print("\nVariances :\n\tvar0=",var0,"\n\tvar1=",var1)

#Output Predictions for the data for which label is not available
print("\nLabel Predictions :")
for i in range(0,rows,1):
    w0 = 0
    w1 = 0
    if(label.get(i)==None):
        for j in range(0,columns,1):
            w0 += ((mean0[j]-data[i][j])**2)/var0[j]
            w1 += ((mean1[j]-data[i][j])**2)/var1[j]
        if(w0 > w1):
            print("\t1\t",i)
        else:
            print("\t0\t",i)




