import csv
import datetime

def read_data(file_name, fieldnames):
    data_list = []
    with open(file_name, encoding='utf8') as csv_file:
        data = csv.DictReader(csv_file)
        for profile in data:
            info = {field: profile[field] for field in fieldnames}
            data_list.append(info)
    return data_list

def write_data(file_name, fieldnames, data_list):
    with open(file_name, mode='w', newline='', encoding='utf8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for data in data_list:
            print(data)
            writer.writerow(data)

today = datetime.date.today()

# Process Unity.csv
unity_fieldnames = ['Department', 'DisplayName', 'EmailAddress', 'FirstName', 'LastName', 'Extension']
unity_data = read_data('Unity.csv', unity_fieldnames)
unity_output_file = '{}.csv'.format(today.strftime('%Y-%m-%d-COMPANYExport'))
write_data(unity_output_file, unity_fieldnames, unity_data)

# Process Phone.csv
phone_fieldnames = ['DEVICE NAME', 'DESCRIPTION', 'DIRECTORY NUMBER 1']
phone_data = read_data('Phone.csv', phone_fieldnames)
filtered_phone_data = [data for data in phone_data if data['DEVICE NAME'].startswith(('SEP', 'BOT', 'CSF', 'TCT', 'TAB', 'CIPC'))]
phone_output_file = '{}.csv'.format(today.strftime('%Y-%m-%d-COMPANYPHONELINEEXPORT'))
write_data(phone_output_file, phone_fieldnames, filtered_phone_data)

# Process Profile.csv
profile_fieldnames = ['DESCRIPTION', 'DIRECTORY NUMBER 1', 'LINE TEXT LABEL 1']
profile_data = read_data('Profile.csv', profile_fieldnames)
profile_output_file = '{}.csv'.format(today.strftime('%Y-%m-%d-COMPANYPROFILEEXPORT'))
write_data(profile_output_file, profile_fieldnames, profile_data)
