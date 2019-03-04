import numpy as np
import fetchmaker
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency


rottweiler_tl = fetchmaker.get_tail_length("rottweiler")
rottweiler_tl_mean = np.mean(rottweiler_tl)
rottweiler_tl_sd = np.std(rottweiler_tl)
print(rottweiler_tl_mean)
print(rottweiler_tl_sd)
whippet_rescue = fetchmaker.get_is_rescue("whippet")
num_whippet_rescues = np.count_nonzero(whippet_rescue)
total_num = np.size(whippet_rescue)
print binom_test(num_whippet_rescues, total_num, .08)
w = fetchmaker.get_weight("whippet")
t = fetchmaker.get_weight("terrier")
p = fetchmaker.get_weight("pitbull")
print f_oneway(w,t,p).pvalue
values = np.concatenate([w,t,p])
labels = ['whippet']*len(w) + ['terrier']*len(t)+['pitbull']*len(p)
print pairwise_tukeyhsd(values, labels, .05)
poodle_colors = fetchmaker.get_color("poodle")
shihtzu = fetchmaker.get_color("shihtzu")

color_table = [
  [np.count.nonzer(poodle_colors == "black"),
  np.count.nonzero(shihtzu_color=="black")],
  [np.count.nonzer(poodle_colors == "brown"),
  np.count.nonzero(shihtzu_color=="brown")]
  [np.count.nonzer(poodle_colors == "gold"),
  np.count.nonzero(shihtzu_color=="gold")],
  [np.count.nonzer(poodle_colors == "grey"),
  np.count.nonzero(shihtzu_color=="grey")],
[np.count.nonzer(poodle_colors == "white"),
  np.count.nonzero(shihtzu_color=="white")],
]
print color_table

_, color_pval,_,_ = chi@_contingency(color_table)
print color_pval
