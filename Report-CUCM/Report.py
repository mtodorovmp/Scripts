import csv
from datetime import datetime

new_file = []
new_file2 = []

# Read data from the original file
with open('report.csv', encoding='utf8') as csv_file:
    data = csv.DictReader(csv_file)
    data = sorted(data, key=lambda d: int(d['dateTimeConnect']))

    for stat in data:
        originalCalledPartyNumber = stat['originalCalledPartyNumber']
        dateTimeConnect = stat['dateTimeConnect']
        dateTimeDisconnect = stat['dateTimeDisconnect']

        dateTimeConnect = datetime.utcfromtimestamp(int(dateTimeConnect)).strftime('%m/%d/%Y %I:%M:%p')
        dateTimeDisconnect = datetime.utcfromtimestamp(int(dateTimeDisconnect)).strftime('%m/%d/%Y %I:%M:%p')

        info = {
            'callingPartyNumber': stat['callingPartyNumber'],
            'originalCalledPartyNumber': originalCalledPartyNumber,
            'finalCalledPartyNumber': stat['finalCalledPartyNumber'],
            'dateTimeConnect': dateTimeConnect,
            'dateTimeDisconnect': dateTimeDisconnect
        }

        if originalCalledPartyNumber == '3400':
            new_file.append(info)

        the_time = datetime.utcfromtimestamp(int(stat['dateTimeConnect'])).time()
        if originalCalledPartyNumber == '3400' and not 8 < the_time.hour < 16:
            new_file2.append(info)

# Write data to a new CSV file
today = datetime.now().strftime('%m_%d')
filename = f'{today}.csv'

with open(filename, mode='w', newline='', encoding='utf8') as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(['callingPartyNumber', 'originalCalledPartyNumber', 'finalCalledPartyNumber', 'dateTimeConnect',
                     'dateTimeDisconnect'])

    for row in new_file:
        writer.writerow([row['callingPartyNumber'], row['originalCalledPartyNumber'], row['finalCalledPartyNumber'],
                         row['dateTimeConnect'], row['dateTimeDisconnect']])

    writer.writerow([])  # Empty row
    writer.writerow(['After 4 PM'])  # Label for separation
    writer.writerow([])  # Empty row

    for row in new_file2:
        writer.writerow([row['callingPartyNumber'], row['originalCalledPartyNumber'], row['finalCalledPartyNumber'],
                         row['dateTimeConnect'], row['dateTimeDisconnect']])
