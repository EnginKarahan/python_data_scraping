# Code für Grundlagenchallenge
import json
from collections import Counter
from pprint import pprint

with open('guardian_articles_corona.json', 'r', encoding='utf=8') as f:
    guardian_raw = json.load(f)

def json_parser(file_to_pars):
    parsed = []
    for i in range(0, len(file_to_pars)):
        for j in range(0, len(file_to_pars[i])):
            tmp = {}
            tmp['id'] = file_to_pars[i]["id"]
            tmp['chars'] = file_to_pars[i]["fields"]["charCount"]
            tmp['section'] = file_to_pars[i]["sectionName"]
            tmp2 = []
            for k in range(0, len(file_to_pars[i]['tags'])):
                tmp2.append(file_to_pars[i]['tags'][k]['id'])
            tmp2 = ', '.join(tmp2)
            tmp['tags'] = tmp2
            tmp['text'] = file_to_pars[i]["fields"]["bodyText"]
            tmp['title'] = file_to_pars[i]["webTitle"]
            tmp['url'] = file_to_pars[i]["webUrl"]
            date = file_to_pars[i]['webPublicationDate']
            tmp['month'] = date[5:7]
            # print(tmp)
        parsed.append(tmp)
    return parsed

def month_article():
    counter = []
    for i in range(len(parsed_guardian)):
        counter.append(parsed_guardian[i]['month'])
    counter_month = Counter(counter)
    print('Zahl der Artikel pro Monat', counter_month.most_common())
    print('Monat mit mesten Artikeln: ', counter_month.most_common(1))

def most_tags():
    counter = []
    for i in range(len(parsed_guardian)):
        tmp_tag = parsed_guardian[i]['tags'].split(", ")
        counter = counter + tmp_tag
    counter_tags = Counter(counter)
    print('3 häufigsten tags: ', counter_tags.most_common(3))

def long_article():
    counter = []
    counter_chars = []
    for i in range(len(parsed_guardian)):
        counter.append(int(parsed_guardian[i]['chars']))
        #counter = counter + parsed_guardian[i]['chars']
    #counter_chars = counter.sort(reverse=True)
    #counter_chars = list(dict.fromkeys(counter))
    counter = list(dict.fromkeys(counter))
    counter_chars = counter.sort(reverse=True)
    print('Counter Chars', counter)
    #print('Counter', counter)
    print()
    print('Die längsten 5 Beiträge: ')
    for j in range(0, 4):
        for k in range(len(parsed_guardian)):
            if str(counter[j]) == parsed_guardian[k]['chars']:
                print(parsed_guardian[k]['chars'], parsed_guardian[k]['title'])
            else:
                continue



parsed_guardian = json_parser(guardian_raw)

month_article()

most_tags()

long_article()

with open('uardian_articles_corona-parsed.json', 'w', encoding = 'utf-8') as f:
    json.dump(parsed_guardian,
             f,
             ensure_ascii = False,
             indent = 2)