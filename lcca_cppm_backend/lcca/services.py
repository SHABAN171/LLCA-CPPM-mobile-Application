def calculate_npv(costs, discount_rate):

    npv = 0

    for year, cost in enumerate(costs):
        npv += cost / ((1 + discount_rate) ** year)

    return round(npv, 2)