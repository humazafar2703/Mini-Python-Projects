cats = 10
cans = 2
total_cans = cats * cans
output = str(cats) + " cats eat " + str(total_cans) + " cans"
print(output)

cats = 10
cans = 2
days = 7
total_cans = cats * cans * days
msg = str(cats) + " cats eat " + str(total_cans) + " cans in " + str(days) + " days"
print(msg)

#you dont need to typecast if you use format.

oranges = 12
cost_per_orange = 0.5
total_cost = oranges * cost_per_orange
output = "{} oranges costs £{}".format(oranges, total_cost)
print(output)

user_name = 'sarah_1987'
age = 23
output = '{} is {} years old'.format(user_name, age)
print(output)

# A program to calculate the total cost of cans used by 10 cats
cats = 10
cans = 2
total_cans = cats * cans
output = "{} cats eat {} cans".format(cats, total_cans)
print(output)

days = 31
hours = "24"
total_hours = days * hours
msg = "There are {} in {} days".format(total_hours, days)
print(msg)
