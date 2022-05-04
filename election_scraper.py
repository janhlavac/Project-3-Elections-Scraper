import sys
import requests
import bs4
import csv
import re

def usage(script_name):
    print("python ", script_name, " source_url csv_file_name")
    print("  source_url: URL of the main page for the given community (e.g. city or town).")
    print("  csv_file_name: Name of the output CSV file")
    print("Example: python ", script_name, " https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100 praha.csv")
    return

def format_number(str):
    return re.sub(r'\s+', '', str)

print ("E L E C T I O N   S C R A P E R")
print ("===============================")

if len(sys.argv) != 3:
    usage(sys.argv[0])
    exit()

main_url = sys.argv[1]
base_url = main_url[:main_url.rindex('/') + 1]

csv_file_name = sys.argv[2]
csv_header = ["code", "location", "registered", "envelopes", "valid"]
csv_data = []

print('Getting ', main_url)    
main_page = requests.get(main_url)
main_soup = bs4.BeautifulSoup(main_page.text, "html.parser")
print('Location: ', main_soup.find_all('h3')[1].string[8:-1])

main_tds = main_soup.find_all('td', { 'class' : 'cislo'})
for main_td in main_tds:
    # Get location "obec"    
    child_url = base_url + main_td.a['href']
    print('Getting ', child_url)    
    child_page = requests.get(child_url)
    child_soup = bs4.BeautifulSoup(child_page.text, "html.parser")

    # extend header wit names of political parties if not already done
    if len(csv_header) <= 5:
        csv_header.extend([t.string for t in child_soup.find_all('td', { 'class' : 'overflow_name' })])

    # Gather main statistics for the location "obec"
    child_code = main_td.a.string
    child_location = child_soup.find_all('h3')[2].string[7:-1]
    tmp_row = child_soup.find_all('table')[0].find_all('tr')[2]
    child_registered = format_number(tmp_row.find_all('td')[3].string)
    child_envelopes = format_number(tmp_row.find_all('td')[4].string)
    child_valid = format_number(tmp_row.find_all('td')[7].string)
    # add main statistics to the data row
    csv_row = [child_code, child_location, child_registered, child_envelopes, child_valid]
    # add detailed statistics per political party to the data row (there are two tables)
    csv_row.extend([format_number(t.string) for t in child_soup.find_all('td', { 'class' : 'cislo', 'headers' : 't1sa2 t1sb3' })])
    csv_row.extend([format_number(t.string) for t in child_soup.find_all('td', { 'class' : 'cislo', 'headers' : 't2sa2 t2sb3' })])
    # append statistics to the data table
    csv_data.append(csv_row)

# write gathered statistics to CSV file
f = open(csv_file_name,'w')
f_writer = csv.writer(f, delimiter =';', lineterminator = '\n')
f_writer.writerow(csv_header)
f_writer.writerows(csv_data)
f.close()
