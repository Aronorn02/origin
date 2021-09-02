mb_per_month = int(input("How much data (in Mb) do you get per month?: "))
n = int(input("How many months have you had this plan?: "))

total_usage = 0


for i in range(n):
    usage = int(input("How much data did you use this month?: "))
    total_usage += usage

print(mb_per_month*(n+1) - total_usage)
