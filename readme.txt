This script parses Reddit comments(.json) and takes them from raw messy text into a cleaner text.
The result will be a list containing four strings: Parrsed Comment, Unigrams, Bigrams, Trigrams.

version: Python 3.6.3

usage:

python3 cleantext.py jsonfile

example
input:
{"author":"-0rabbit0-","body":"It's not *something for nothing*. It's relatively healthy people who NEVER see the need to see a doctor, and are perfectly fine with the risk of dolling out 10 grand IF they get very sick. It should be our choice to make.  \n  \nAnd it *was* implemented overnight. We were promised that we could keep our policies, keep out doctors. I, for one, was allowed to keep neither.","controversiality":0,"created_utc":1482456914,"edited":"false","gilded":0,"id":"dbj1fux","link_id":"t3_5jsgsc","parent_id":"t1_dbiy5l7","retrieved_on":1483978698,"score":2,"stickied":false,"subreddit":"politics","subreddit_id":"t5_2cneq"}

output:
["it's not something for nothing . it's relatively healthy people who never see the need to see a doctor , and are perfectly fine with the risk of dolling out 10 grand if they get very sick . it should be our choice to make . and it was implemented overnight . we were promised that we could keep our policies , keep out doctors . i , for one , was allowed to keep neither .", "it's not something for nothing it's relatively healthy people who never see the need to see a doctor and are perfectly fine with the risk of dolling out 10 grand if they get very sick it should be our choice to make and it was implemented overnight we we're promised that we could keep our policies keep out doctors i for one was allowed to keep neither", "it's_not not_something something_for for_nothing it's_relatively relatively_healthy healthy_people people_who who_never never_see see_the the_need need_to to_see see_a a_doctor and_are are_perfectly perfectly_fine fine_with with_the the_risk risk_of of_dolling dolling_out out_10 10_grand grand_if if_they they_get get_very very_sick it_should should_be be_our our_choice choice_to to_make and_it it_was was_implemented implemented_overnight we_were were_promised promised_that that_we we_could could_keep keep_our our_policies keep_out out_doctors for_one was_allowed allowed_to to_keep keep_neither", "it's_not_something not_something_for something_for_nothing it's_relatively_healthy relatively_healthy_people healthy_people_who people_who_never who_never_see never_see_the see_the_need the_need_to need_to_see to_see_a see_a_doctor and_are_perfectly are_perfectly_fine perfectly_fine_with fine_with_the with_the_risk the_risk_of risk_of_dolling of_dolling_out dolling_out_10 out_10_grand 10_grand_if grand_if_they if_they_get they_get_very get_very_sick it_should_be should_be_our be_our_choice our_choice_to choice_to_make and_it_was it_was_implemented was_implemented_overnight we_were_promised were_promised_that promised_that_we that_we_could we_could_keep could_keep_our keep_our_policies keep_out_doctors was_allowed_to allowed_to_keep to_keep_neither"]





