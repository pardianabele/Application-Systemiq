import Data_processing as dp
import Analytics as an
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

#3. mean and median plot
x = list(range(len(dp.diff_mean_median)))
y = dp.diff_mean_median
plt.plot(x, y)
plt.ylabel('Mean-Median')
plt.xlabel('User')
plt.savefig("MeanMedian.png")
plt.clf()


#4. histogram rev/users
cumulative_rev = {}

for key in dp.rev_dct:
    new_val = sum(np.array(dp.rev_dct[key], dtype=float))
    cumulative_rev[key] = new_val

plt.bar(cumulative_rev.keys(), cumulative_rev.values(), color='g')
plt.xlabel('User ID')
plt.ylabel('Revenue')
plt.xticks([])
#plt.xticks(np.arange(1300000, 3350000, step=500000))
plt.savefig("RevDistribution.png")
plt.clf()

#7. Box plots gender/country
plt.boxplot([an.week_rev_list('M', 'DE'), an.week_rev_list('F', 'DE'), an.week_rev_list('M','FR'), an.week_rev_list('F', 'FR'), an.week_rev_list('M', 'GB'), an.week_rev_list('F', 'GB'), an.week_rev_list('M','US'), an.week_rev_list('F', 'US'), an.week_rev_list('M', 'Other'), an.week_rev_list('F', 'Other')] , showfliers=False)
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['mDE', 'fDE', 'mFR', 'fFR', 'mUK', 'fUK', 'mUSA', 'fUSA','mOther', 'fOther'])
plt.ylabel('First week revenue')
plt.savefig("BoxPlotGeCo.png")
plt.clf()

#9. Linear regresion models
regr_DE = linear_model.LinearRegression().fit(np.reshape(an.age_and_first_day_rev('F', 'DE')[0], (-1, 1)), an.age_and_first_day_rev('F', 'DE')[1])
regr_FR = linear_model.LinearRegression().fit(np.reshape(an.age_and_first_day_rev('F', 'FR')[0], (-1, 1)), an.age_and_first_day_rev('F', 'FR')[1])
regr_GB = linear_model.LinearRegression().fit(np.reshape(an.age_and_first_day_rev('F', 'GB')[0], (-1, 1)), an.age_and_first_day_rev('F', 'GB')[1])
regr_US = linear_model.LinearRegression().fit(np.reshape(an.age_and_first_day_rev('F', 'US')[0], (-1, 1)), an.age_and_first_day_rev('F', 'US')[1])
regr_Ot = linear_model.LinearRegression().fit(np.reshape(an.age_and_first_day_rev('F', 'Other')[0], (-1, 1)), an.age_and_first_day_rev('F', 'Other')[1])

fig, axs = plt.subplots(5, 2)
axs[0, 0].plot(an.age_and_first_day_rev('F', 'DE')[0], an.age_and_first_day_rev('F', 'DE')[1], '.', color='black')
axs[0, 0].plot(np.reshape(an.age_and_first_day_rev('F', 'DE')[0], (-1, 1)), regr_DE.predict(np.reshape(an.age_and_first_day_rev('F', 'DE')[0], (-1, 1))), color='blue', linewidth=1)
axs[0, 0].set_title('Female DE')
axs[0, 1].plot(an.age_and_first_day_rev('M', 'DE')[0], an.age_and_first_day_rev('M', 'DE')[1], '.', color='black')
axs[0, 1].plot(np.reshape(an.age_and_first_day_rev('M', 'DE')[0], (-1, 1)), regr_DE.predict(np.reshape(an.age_and_first_day_rev('M', 'DE')[0], (-1, 1))), color='blue', linewidth=1)
axs[0, 1].set_title('Male DE')
axs[1, 0].plot(an.age_and_first_day_rev('F', 'FR')[0], an.age_and_first_day_rev('F', 'FR')[1], '.', color='black')
axs[1, 0].plot(np.reshape(an.age_and_first_day_rev('F', 'FR')[0], (-1, 1)), regr_FR.predict(np.reshape(an.age_and_first_day_rev('F', 'FR')[0], (-1, 1))), color='blue', linewidth=1)
axs[1, 0].set_title('Female FR')
axs[1, 1].plot(an.age_and_first_day_rev('M', 'FR')[0], an.age_and_first_day_rev('M', 'FR')[1], '.', color='black')
axs[1, 1].plot(np.reshape(an.age_and_first_day_rev('M', 'FR')[0], (-1, 1)), regr_FR.predict(np.reshape(an.age_and_first_day_rev('M', 'FR')[0], (-1, 1))), color='blue', linewidth=1)
axs[1, 1].set_title('Male FR')
axs[2, 0].plot(an.age_and_first_day_rev('F', 'GB')[0], an.age_and_first_day_rev('F', 'GB')[1], '.', color='black')
axs[2, 0].plot(np.reshape(an.age_and_first_day_rev('F', 'GB')[0], (-1, 1)), regr_GB.predict(np.reshape(an.age_and_first_day_rev('F', 'GB')[0], (-1, 1))), color='blue', linewidth=1)
axs[2, 0].set_title('Female UK')
axs[2, 1].plot(an.age_and_first_day_rev('M', 'GB')[0], an.age_and_first_day_rev('M', 'GB')[1], '.', color='black')
axs[2, 1].plot(np.reshape(an.age_and_first_day_rev('M', 'GB')[0], (-1, 1)), regr_GB.predict(np.reshape(an.age_and_first_day_rev('M', 'GB')[0], (-1, 1))), color='blue', linewidth=1)
axs[2, 1].set_title('Male UK')
axs[3, 0].plot(an.age_and_first_day_rev('F', 'US')[0], an.age_and_first_day_rev('F', 'US')[1], '.', color='black')
axs[3, 0].plot(np.reshape(an.age_and_first_day_rev('F', 'US')[0], (-1, 1)), regr_US.predict(np.reshape(an.age_and_first_day_rev('F', 'US')[0], (-1, 1))), color='blue', linewidth=1)
axs[3, 0].set_title('Female US')
axs[3, 1].plot(an.age_and_first_day_rev('M', 'US')[0], an.age_and_first_day_rev('M', 'US')[1], '.', color='black')
axs[3, 1].plot(np.reshape(an.age_and_first_day_rev('M', 'US')[0], (-1, 1)), regr_US.predict(np.reshape(an.age_and_first_day_rev('M', 'US')[0], (-1, 1))), color='blue', linewidth=1)
axs[3, 1].set_title('Male US')
axs[4, 0].plot(an.age_and_first_day_rev('F', 'Other')[0], an.age_and_first_day_rev('F', 'Other')[1], '.', color='black')
axs[4, 0].plot(np.reshape(an.age_and_first_day_rev('F', 'Other')[0], (-1, 1)), regr_Ot.predict(np.reshape(an.age_and_first_day_rev('F', 'Other')[0], (-1, 1))), color='blue', linewidth=1)
axs[4, 0].set_title('Female other c.')
axs[4, 1].plot(an.age_and_first_day_rev('M', 'Other')[0], an.age_and_first_day_rev('M', 'Other')[1], '.', color='black')
axs[4, 1].plot(np.reshape(an.age_and_first_day_rev('M', 'Other')[0], (-1, 1)), regr_Ot.predict(np.reshape(an.age_and_first_day_rev('M', 'Other')[0], (-1, 1))), color='blue', linewidth=1)
axs[4, 1].set_title('Male other c.')
plt.setp(axs, xticks=[20, 40, 60, 80], yticks=[50, 100, 150])
fig.tight_layout()

plt.savefig("LinearReg.png")
plt.clf()

#9. R^2s
print('------------------------------------------------------------')
print("R_sq female DE: ", regr_DE.score(np.array(np.reshape(an.age_and_first_day_rev('F', 'DE')[0], (-1, 1)), dtype=float), np.array(an.age_and_first_day_rev('F', 'DE')[1], dtype=float)))
print("R_sq female FR: ", regr_FR.score(np.array(np.reshape(an.age_and_first_day_rev('F', 'FR')[0], (-1, 1)), dtype=float), np.array(an.age_and_first_day_rev('F', 'FR')[1], dtype=float)))
print("R_sq female GB: ", regr_GB.score(np.array(np.reshape(an.age_and_first_day_rev('F', 'GB')[0], (-1, 1)), dtype=float), np.array(an.age_and_first_day_rev('F', 'GB')[1], dtype=float)))
print("R_sq female USA: ", regr_US.score(np.array(np.reshape(an.age_and_first_day_rev('F', 'US')[0], (-1, 1)), dtype=float), np.array(an.age_and_first_day_rev('F', 'US')[1], dtype=float)))
print("R_sq female DE: ", regr_Ot.score(np.array(np.reshape(an.age_and_first_day_rev('F', 'Other')[0], (-1, 1)), dtype=float), np.array(an.age_and_first_day_rev('F', 'Other')[1], dtype=float)))

print("R_sq male DE: ", regr_DE.score(np.array(np.reshape(an.age_and_first_day_rev('M', 'DE')[0], (-1, 1)), dtype=float), np.array(an.age_and_first_day_rev('M', 'DE')[1], dtype=float)))
print("R_sq male FR: ", regr_FR.score(np.array(np.reshape(an.age_and_first_day_rev('M', 'FR')[0], (-1, 1)), dtype=float), np.array(an.age_and_first_day_rev('M', 'FR')[1], dtype=float)))
print("R_sq male GB: ", regr_GB.score(np.array(np.reshape(an.age_and_first_day_rev('M', 'GB')[0], (-1, 1)), dtype=float), np.array(an.age_and_first_day_rev('M', 'GB')[1], dtype=float)))
print("R_sq male USA: ", regr_US.score(np.array(np.reshape(an.age_and_first_day_rev('M', 'US')[0], (-1, 1)), dtype=float), np.array(an.age_and_first_day_rev('M', 'US')[1], dtype=float)))
print("R_sq male DE: ", regr_Ot.score(np.array(np.reshape(an.age_and_first_day_rev('M', 'Other')[0], (-1, 1)), dtype=float), np.array(an.age_and_first_day_rev('M', 'Other')[1], dtype=float)))

#the highers Rqs is for Females in France
