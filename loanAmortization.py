principal = 240_000
rate = 0.05
comps_per_yr = 12
rate /= comps_per_yr
num_years = 30
total_comp = num_years * comps_per_yr
pmt = round(principal*(rate*(1+rate)**total_comp)/((1+rate)**total_comp-1),2)
total_payback = round(pmt*total_comp,2)
total_int = total_payback-principal
print(f'The monthly payment is ${pmt}\n')
print(f'The total to pay back is ${total_payback:,}')
print(f'The total interest to pay back is ${total_int:,}\n')
print('Payment \t Interest \t\t Principal')
for i in range(1,total_comp+1):
    period_int = principal * rate
    period_principal = pmt-period_int
    print(f'{i} \t\t ${period_int:0.2f} \t\t ${period_principal:0.2f}')
    principal -= period_principal
