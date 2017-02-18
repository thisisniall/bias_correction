import random
import re as re
import csv


### Zip codes

f = open('us_postal_codes.csv')
csv_f = csv.reader(f)

zip_codes = []

for row in csv_f:
    zip_codes.append(row[0])

def zipcode():
    return zip_codes[random.randint(0,len(zip_codes))]

#### importing first names from csv

f = open('firstnames.csv')
csv_f = csv.reader(f)

first_names = []
for row in csv_f:
  first_names.append(row[0])
# print len(first_names)

#### importing surnames from csv
f = open('surnames.csv')
csv_f = csv.reader(f)

surnames = []

for row in csv_f:
  surnames.append(row[0])
  # print len(surnames)

# Generate Email Address using First Name / Surname

list_of_domains_1 = ['@aol.com', '@twc.com', '@gmail.com', '@yahoo.com', '@verizon.net', '@att.com', '@mail.com',
                    '@email.cz', '@hotmail.com', '@outlook.com', '@mail.ru']
list_of_domains_2 = ['@whitehouse.gov', '@horizon.net', '@aresmacrotech.com', '@mct.com', '@wuxing.com', '@neonet.com', '@ucas.gov', '@hentai.jp', '@evo.ru', '@gazprom.ru', '@gizoogle.com',  '@shell.com', '@exxonmobil.com', '@omega.com', '@shinto.jp', '@baidu.com', '@cas.gov', '@kkk.org', '@breitbart.com', '@koch.net', '@gs.com', '@mailchimp.com', '@email.cz', '@fox.com', '@pornhub.com', '@ravensfans.com', '@ohiostate.edu', '@lsu.edu', '@alabama.edu', '@spinradindustries.com', '@larpersunited.org', '@theonion.com', '@alpha.com','@doe.gov', '@tupaclives.net', '@nltk.com', '@redtube.com','@harvard.edu', '@yale.edu', '@fordham.edu', '@penn.edu']

def pick_domain():
    if random.randint(0,100) >= 90:
        return list_of_domains_2[random.randint(0,len(list_of_domains_2) - 1)]
    else:
        return list_of_domains_1[random.randint(0,len(list_of_domains_1) - 1)]

def personal_info():
    person = str(first_names[random.randint(0,len(surnames))]+ ' ' + surnames[random.randint(0,len(surnames))])
    number = str(random.randint(0,1000))
    domain = pick_domain()
    return [person, person.replace(' ','.').lower()+number+domain, zipcode()]