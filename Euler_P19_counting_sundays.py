def leap_year_detector(year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False

calendar = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_calendar = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year_list = [x for x in range(1901, 2001)]
leap_year_list = [leap_year_detector(x) for x in year_list]
nested_leap_year_list = []
for x in leap_year_list:
	if x == False:
		nested_leap_year_list.append(calendar)
	elif x == True:
		nested_leap_year_list.append(leap_calendar)

#print(nested_leap_year_list)
week_value = 2
list_of_first_day = [2]
for year in nested_leap_year_list:
	for months in year:
		week_adj_val = (months % 28)
		if week_value + week_adj_val > 7:
			week_value = week_adj_val - (7 - week_value)
			list_of_first_day.append(week_value)
		else:
			week_value = week_value + week_adj_val
			list_of_first_day.append(week_value)
list_of_first_day.pop()
counter = 0
for x in list_of_first_day:
	if x == 7:
		counter += 1
print(counter)
