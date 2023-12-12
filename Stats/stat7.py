def calculate_probability(data,event):
    #count the occurance of event in data
    event_count=data.count(event)
    #calculate the probability
    probability=event_count/len(data)
    return probability
#get data from user
data=input("Enetr the data(value separated by spce):").split()
event=input("Enter the event to calculate its probability")
#calculate and display
probability=calculate_probability(data,event)
print=("The probability of'{}'occuring is:{:2f}",format(event,probability))
