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

print ("**********************")

def hello_traveller(year):
    if year<1900:
        print(str(year) + "? you vintage, brah")
    elif year>=1900 and year<=2020:
        print (str(year) + "? haaay grrrl, hay")
    else:
        print (str(year) + "? where my flying car tho?")

hello_traveller(1989)
hello_traveller(1854)
hello_traveller(2054)

birth_dates={"Ursula K. LeGuin":"1929", "Octavia Butler":"1947", "Chimamanda Ngozie Adichie": "1977", "Shirley Jackson":"1916"}
cnt_post_1949=0
cnt_pre_1950=0

for author, year in birth_dates.items():
    if int(year) < 1950:
        cnt_pre_1950+=1
    else:
        cnt_post_1949+=1
print ("There are "+ str(cnt_pre_1950) + " pre-1950s births and " + str(cnt_post_1949) + " post-1950s births in my collection.")
