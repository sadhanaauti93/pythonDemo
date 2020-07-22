ItemsIncart = 0
#2 item will be added to cart

if ItemsIncart !=2:
    pass
assert(ItemsIncart == 0)

#try, catch

try:
    with open ('test.txt', 'r') as reader:
        reader.read()

except:
    print("some how i reached this block because there is failure in try block")


try:
    with open ('filelog.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print("cleaning up resources")    
