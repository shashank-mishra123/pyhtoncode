# count vowel and consonent in string
st1 ="SitaRam"
countvowel =0
countconsonent =0
for i in range(len(st1)):
    if (st1[i]=='a' or st1[i]=='e' or st1[i]=='i' or st1[i]=='o' or st1[i]=='u'):
        countvowel +=1
    else:
        countconsonent +=1
print("vowel :", countvowel)
print("consonent :",countconsonent)