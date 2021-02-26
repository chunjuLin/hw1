# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108000216.csv'
data = []
header = []
maximum = [-999,-999,-999,-999,-999]

with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
      if(row['TEMP'] == '-99.000'):
        row['TEMP'] = ''
      elif(row['TEMP'] == '-999.000'):
         row['TEMP'] = ''

      elif(row['station_id'] == 'C0A880'):
         if(row['TEMP'] != ''):
            if(maximum[0] < float(row['TEMP'])):
               maximum[0] = float(row['TEMP'])
      elif(row['station_id'] == 'C0F9A0'):
          if(row['TEMP'] != ''):
            if(maximum[1] < float(row['TEMP'])):
                maximum[1] = float(row['TEMP'])
      elif(row['station_id'] == 'C0G640'):
          if(row['TEMP'] != ''):
            if(maximum[2] < float(row['TEMP'])):
                maximum[2] = float(row['TEMP'])
      elif(row['station_id'] == 'C0R190'):
          if(row['TEMP'] != ''):
            if(maximum[3] < float(row['TEMP'])):
                maximum[3] = float(row['TEMP'])
      elif(row['station_id'] == 'C0X260'):
          if(row['TEMP'] != ''):
            if(maximum[4] < float(row['TEMP'])):
                maximum[4] = float(row['TEMP'])
    
#=======================================


# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
target_data = data[:10]
def PRINT(name, MAX):
    print('[', end = '')
    print("'", end = '')
    print(name, end = '')
    print("'", end = '')
    print(', ',end = '')
    if(MAX == -999):
        print('None', end ='')
    else:
        print(MAX, end = '')
    print(']', end = '')

#=======================================

# Part. 4
#=======================================
# Print result
print("[", end = '')
PRINT('C0A880',maximum[0])
print(', ', end = '')
PRINT('C0F9A0',maximum[1])
print(', ', end = '')
PRINT('C0G640',maximum[2])
print(', ', end = '')
PRINT('C0R190',maximum[3])
print(', ', end = '')
PRINT('C0X260',maximum[4])
print(']')


#print(data[1]['station_id'])
#print(data)
#========================================