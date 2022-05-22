import Data_processing as dp
import numpy as np
import scipy
from scipy import stats
from datetime import datetime

#6. T-test
#average 1 week rev. male and female
row_counter = 0
user_male = 0
user_female = 0
female_week_rev = 0
male_week_rev = 0
female_week_rev_list = []
male_week_rev_list = []

for g in dp.user_rows:
    if g[3] == 'F':
        user_female += 1
        female_week_rev += np.array(dp.average_7d_rev[dp.user_rows[row_counter][0]], dtype=float)
        female_week_rev_list.append(np.array(dp.average_7d_rev[dp.user_rows[row_counter][0]], dtype=float))
    else:
        user_male += 1
        male_week_rev += np.array(dp.average_7d_rev[dp.user_rows[row_counter][0]], dtype=float)
        male_week_rev_list.append(np.array(dp.average_7d_rev[dp.user_rows[row_counter][0]], dtype=float))
    row_counter += 1

average_male_week_rev = male_week_rev/user_male
average_female_week_rev = female_week_rev/user_female

print("Average male week rev:", average_male_week_rev, "Average female week rev:", average_female_week_rev)
print("General male and female stats:", scipy.stats.ttest_ind(male_week_rev_list, female_week_rev_list, equal_var = False))

#7. p-val/country
def week_rev_list(gender, country):
    female_data_list = []
    male_data_list = []
    row_counter = 0
    for c in dp.user_rows:
        if c[1] == country:
            if c[3] == 'F':
                 female_data_list.append(np.array(dp.average_7d_rev[dp.user_rows[row_counter][0]], dtype=float))
            else:
                male_data_list.append(np.array(dp.average_7d_rev[dp.user_rows[row_counter][0]], dtype=float))
        row_counter += 1

    if gender == 'F':
        return female_data_list
    else:
        return male_data_list

print("Male and female stats in DE: ", scipy.stats.ttest_ind(week_rev_list('M', 'DE'), week_rev_list('F', 'DE'), equal_var = False))
print("Male and female stats in FR: ", scipy.stats.ttest_ind(week_rev_list('M', 'FR'), week_rev_list('F', 'FR'), equal_var = False))
print("Male and female stats in UK: ", scipy.stats.ttest_ind(week_rev_list('M', 'GB'), week_rev_list('F', 'GB'), equal_var = False))
print("Male and female stats in USA: ", scipy.stats.ttest_ind(week_rev_list('M', 'US'), week_rev_list('F', 'US'), equal_var = False))
print("Male and female stats in other countries: ", scipy.stats.ttest_ind(week_rev_list('M', 'Other'), week_rev_list('F', 'Other'), equal_var = False))

#8. one day revenue - linear regression model
def age_and_first_day_rev(gender,country):
    female_ages = []
    male_ages = []
    female_first_day_rev = []
    male_first_day_rev = []
    for u in dp.user_rows:
        dify = datetime.strptime(dp.cur_date, dp.date_format).year - datetime.strptime(u[2], dp.date_format).year
        if u[1] == country:
            if u[3] == 'F':
                female_ages.append(abs(dify))
                if not dp.rev_dct[u[0]]:
                    female_first_day_rev.append(0)
                else:
                    female_first_day_rev.append(dp.rev_dct[u[0]][0])
            else:
                male_ages.append(abs(dify))
                if not dp.rev_dct[u[0]]:
                    male_first_day_rev.append(0)
                else:
                    male_first_day_rev.append(dp.rev_dct[u[0]][0])
    if gender == 'F':
        return female_ages, female_first_day_rev
    else:
        return male_ages, male_first_day_rev

