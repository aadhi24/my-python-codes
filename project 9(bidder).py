def bidder_function():
    winner=""
    highest = 0
    for bidders in bid_dic:
            s =bid_dic[bidders]
            if s>highest:
                highest=s
                winner=bidders
    print(f"the bidder is {winner} and the amount is {highest}") 

bid_dic={}
bidder=False
while not bidder:
    name = input("enter the name for bidder : ")
    bid = int(input("enter the your bid RS: "))
    
    bid_dic[name]=bid
    option=input("Any one else to bid 'yes' or 'No' : ")
    if "no" in option:
        bidder=True
        bidder_function()
               
    else:
        bidder=False
        
    
        