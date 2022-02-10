import csv

## put here the full path of the generated file of the annotation tool, e.g.: /Users/jim/Desktop/AU_video.txt
file_name = 'C:/Users/wania/Desktop/AU_video.txt'
with open(file_name) as fil:
 content = fil.readlines()

outputs = []

for elem in content:
 if 'N/A' in elem:
   continue
 else:
   line = elem.split(',')
   outputs.append([int(line[1]),int(line[3]),int(line[5]),int(line[7]),int(line[9]),int(line[11])])

print(outputs)

with open('annotations.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(('wrinkles', 'freakles', 'glasses', 'hair_color', 'hair_top', 'no_face_shown'))
    writer.writerows(outputs)
     