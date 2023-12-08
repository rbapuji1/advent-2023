# Given data for both options
initial_costs_1 = 140000
annual_benefit_1 = 49000
salvage_value_1 = 12000
useful_life_1 = 5

initial_costs_2 = 460000
annual_benefit_2 = 95000
salvage_value_2 = 50000
useful_life_2 = 8

interest_rate = 0.09  # 7% interest rate

# Present value of an annuity for option 1
pv_annuity_1 = annual_benefit_1 * ((1 - (1 + interest_rate)**(-useful_life_1)) / interest_rate)

# Present value of a lump sum (salvage value) for option 1
pv_salvage_1 = salvage_value_1 / ((1 + interest_rate)**useful_life_1)

# BCR for option 1
bcr_1 = (pv_annuity_1 + pv_salvage_1) / initial_costs_1

# Present value of an annuity for option 2
pv_annuity_2 = annual_benefit_2 * ((1 - (1 + interest_rate)**(-useful_life_2)) / interest_rate)

# Present value of a lump sum (salvage value) for option 2
pv_salvage_2 = salvage_value_2 / ((1 + interest_rate)**useful_life_2)

# BCR for option 2
bcr_2 = (pv_annuity_2 + pv_salvage_2) / initial_costs_2

# Delta BCR
delta_bcr = bcr_2 - bcr_1

print(bcr_1, bcr_2, delta_bcr)
