
# open the file and get the thing

f = open("../NT/WPN.txt", "r")

lines = f.readlines()

wIP = lines[0].split("\n")[0].strip()

print('my wlan: {}'.format(wIP))

