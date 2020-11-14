import csv

read_csv = csv.DictReader(open('Resources/budget_data.csv'))

months = 0
total = 0
prev_rev = 0
ch_total = 0
inc = ['',0]
dec = ['',0]

for row in read_csv:
# Totals
    months += 1
    rev = int(row['Profit/Losses'])
    total += rev

# Average Change
    if prev_rev == 0:
        prev_rev = rev
    change = rev - prev_rev
    ch_total += change
    prev_rev = rev 

# Greatest increase
    if change > inc[1]:
        inc[0] = row['Date']
        inc[1] = change

# Greatest decrease
    if change < dec[1]:
        dec[0] = row['Date']
        dec[1] = change

output = (
    f'  Financial Analysis\n'
    f'----------------------------\n'
    f'Total Months: {months}\n'
    f'Total: ${total:,}\n'
    f'Average  Change: ${ch_total/(months-1):,.2f}\n'
    f'Greatest Increase in Profits: {inc[0]} (${inc[1]:,.2f})\n'
    f'Greatest Decrease in Profits: {dec[0]} (${dec[1]:,.2f})\n'
)

report = open('Analysis/Report.txt','w')
report.write(output)
print(output)