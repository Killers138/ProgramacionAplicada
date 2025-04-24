import csv

notes = ''
with open('notes.csv', newline='') as f:
    data = cdv.reader(f, delimiter=',')
    notes = list(data)
    
    
#print(notes)\

def getData(notes):
    for i in range(1, len(notes)):
        for j in range(len (notes[i])):
             print (notes[0][j] + ': ' + notes [i][j])
        print('')

def getAverage(notes):
    for i in range(1, len(notes)):
        sum = 0
        med = 0

        print(notes[0][0] + ': ' notes [i][j])
        for j in range(1, len(notes[i])):
             sum += float(notes[i][j])
             med = round(suma/3, 2)

        average.append(med)
        print('Media: ' + str(med))


getData (notes)
getAverage(notes)
print(average)

#Escribimos en le archivo los datos de media de cada alumno.\

notes[0].append('Media')

for i in range(1, len(notes)):
     notes[i].append(average[i-1])

with open ('notes.csv', 'w', newline='') as f:
      Writer = csv.writer(f, delimiter=',')
      writer.writerows(notes)