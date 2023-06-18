# DangQuocToan_20051051_51
import csv
sum = 0
with open('D:\GT\DangQuocToan_20051051'+ "/" 'num_input.csv') as f:
    reader = csv.reader(f)
    for row in reader:
      #print(row)
        for i in row:
          # new_str1 = i.strip('')
          # count = int(countStr)
            if i != '':
                s = int(i)
                sum += s
        #sum += int(str(i))
        #count += int(str())
    print(sum)
