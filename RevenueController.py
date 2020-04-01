

def total(revenuecategory,*revenuecategories):
    quantity=0
    revenue=0.0
    for rc in revenuecategories:
        quantity+=rc.get_quantity()
        revenue+=rc.get_revenue()
    revenuecategory.set_quantity(quantity)
    revenuecategory.set_revenue(revenue)

