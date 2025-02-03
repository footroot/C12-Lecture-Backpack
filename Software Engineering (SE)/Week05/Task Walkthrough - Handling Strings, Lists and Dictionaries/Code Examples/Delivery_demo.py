'''
We are running a small business. We have a list of 
regions where our customers are ('North', 'South', 'East',
'West'), create a dictionary containing how many packages need 
to be sent to each region (50, 30, 20, 40 respectively), 
and a list containing the profit made on each 
successful delivery in that region (5.00, 4.50, 6.00, 5.50 
respectively). The goal is to calculate our expected 
profit.
'''

packages = {
    'North' : 50,
    'South' : 30,
    'East' : 20,
    'West' : 40
}

profit_per_delivery = [5.00, 4.50, 6.00, 5.50]

regions = ['North', 'South', 'East', 'West']

expected_profit = 0

# expected_profit = packages['North'] * profit_per_delivery[0] + ...

for i, region in enumerate(regions):

    region_profit = packages[region] * profit_per_delivery[i]

    expected_profit += region_profit 

print(expected_profit)

