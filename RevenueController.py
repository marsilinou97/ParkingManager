

def total(total,*revenuecategories):
    quantity=0
    revenue=0.0
    for rc in revenuecategories:
        quantity+=rc.get_quantity()
        revenue+=rc.get_revenue()
    total.set_quantity(quantity)
    total.set_revenue(revenue)

