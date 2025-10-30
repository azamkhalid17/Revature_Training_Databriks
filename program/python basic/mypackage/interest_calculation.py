def simle_Interest(prin,ny,roi):
    si=prin*roi*ny/100
    amount=prin+si
    return si,amount
def compund_Interest(prin,ny,roi):
    amount=prin*(1+(roi/100))**(1*ny)
    return amount

