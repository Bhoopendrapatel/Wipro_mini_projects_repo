cost_per_hour = 0.51
cost_per_day = cost_per_hour*24
cost_per_week = cost_per_day*7
cost_per_month = cost_per_day*30
total_budget = 918
days_with_budget = total_budget/cost_per_day

print("Cost to operate one server per day: $",round(cost_per_day,2))
print("Cost to operate one server per week: $",round(cost_per_week,2))
print("Cost to operate one server per month: $",round(cost_per_month,2))
print("With $918, you can operate one server for",int(days_with_budget),"days")