import csv
from datetime import datetime
import statistics
import numpy as np

users_file = open("users.csv")
act_file = open("activities.csv")

users_reader = csv.reader(users_file)
act_reader = csv.reader(act_file)

#1a
users_column = next(users_reader)
act_column = next(act_reader)

print("Number of columns - Users: ", len(users_column))
print("Number of columns - Activities: ", len(act_column))

#1b
user_rows = []
act_rows = []

for row in users_reader:
    user_rows.append(row)

for row in act_reader:
    act_rows.append(row)

print("Number of rows - Users: ", len(user_rows))
print("Number of rows - Activities: ", len(act_rows))

#2a
users_male = 0
users_fem = 0
users_nogen = 0

for gen in user_rows:
    if gen[3] == 'M':
        users_male += 1
    if gen[3] == 'F':
        users_fem += 1
    else:
        users_nogen += 1

print("Male users", users_male)
print("Female users", users_fem)
print("No gender specified", users_nogen)

#3
date_dct = {}
rev_dct = {}
date_list = []
rev_list = []

for ur in user_rows:
    key = ur[0]
    interm_data = {}
    interm_rev = {}
    #interm_data[key] = []
    for ar in act_rows:
        if ur[0] == ar[0]:
            date_list.append(ar[1])
            #interm_data[key].append(ar[1])
            rev_list.append(ar[2])
    interm_data[key] = date_list      #can I not append to a dict anything else but a dict?
    interm_rev[key] = rev_list
    date_dct.update(interm_data)
    rev_dct.update(interm_rev)
    date_list = []
    rev_list = []

# days since activity calculation
activity_monitor = {}
activity_list = []

date_format = "%Y-%m-%d"
cur_date = "2022-05-19"

for key in date_dct:
    for i in date_dct[key]:
        dif = datetime.strptime(cur_date,date_format)-datetime.strptime(i,date_format)
        activity_list.append(dif.days)
    activity_monitor[key] = activity_list
    activity_list = []

#total mean and median revenue generated per user
mm_rev_dct = {}
diff_mean_median = []

for key in rev_dct:
    if rev_dct[key]:
        mean = statistics.mean(np.array(rev_dct[key], dtype=float))
        median = statistics.median(np.array(rev_dct[key], dtype=float))
        mm_rev_dct[key] = (mean, median)
        diff_mean_median.append(mean-median)

#average week 1 revenue
average_7d_rev = {}
a7r = []

for key in date_dct:
    flag = True
    rev_sum = 0
    counter_week = 0
    counter_items = 0
    for i in date_dct[key]:
        if flag:
            ref_date = i
            flag = False
        dif = datetime.strptime(ref_date, date_format) - datetime.strptime(i, date_format)
        if dif.days <= 7:
            rev_sum += np.array(rev_dct[key][counter_items], dtype=float)
            counter_week += 1
        counter_items += 1
        a7r.append(rev_sum)
    if counter_week:
        average_7d_rev[key] = rev_sum/counter_week
    else:
        average_7d_rev[key] = 0

print("Average 7 day revenue: ", np.mean(a7r))

users_file.close()
act_file.close()