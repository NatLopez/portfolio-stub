# nums=[1,2,3,4,5]
# results=[]
# data = []
# hilt_class = ['Isis', 'Natalia']
#
# for items in nums:
#     results.append(items+5)
#
# print(results)
#
# for items in nums:
#     data.append(items-10)
#
# print(data)
#
# for name in hilt_class:
#     if name == 'Natalia':
#         print(name)

days={"Monday":"dance", "Tuesday":"kayak","Wednesday":"rollerskate", "Thursday":"watercolor", "Friday":"drum"}
weekdays=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def lola_act (day):
    for weekday,act in days.items():
        if day==weekday:
            print("On " + weekday + ", Lola likes to " + act)

def lola_sched (week):
    for day in weekdays:
        lola_act(day)

lola_sched (weekdays)

print ("**********************")

authors={"Charles Dicken":"1870", "William Thackeray":"1863","Anthony Trollope":"1882", "Gerard Manley Hopkins": "1889"}

for author,year in authors.items():
    print (author+" kicked the bucket in " + year)
