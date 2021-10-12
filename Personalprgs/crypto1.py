import string

c_text= """ lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi bpr xjvni mkd ymibrut jx
irhx wi bpr riirkvr jx ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk lmird jk xjubt trmui jx ibndt
wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi iwokwxwvmkvr mkd
ijyr ynib urymwk nkrashmwkrd bj ower m vjyshrbr rashmkmbwjk jkr cjnhd pmer bj
lr fnmhwxwrd mkd wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr jx
rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii ijnkd mkd ipmsrhrii ipmsr w dj
kjb drry ytirhx bpr xwkmh mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd wkbrusurbmbwjk w jxxru yt
bprjuwri wk bpr pjsr bpmb bpr riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb
"""

alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)
alphabet_string =alphabet_string + " "
finalst=[]

i=0
for i in range(0,len(alphabet_string)):
    for j in range(0,len(c_text)):
        if alphabet_string[i] == c_text[j]:
            word= alphabet_string[i]
            ct= c_text.count(c_text[j]) 
            print(f"{word} count is : {ct}")
            finalst.append(ct)
            j +=1
            break
rel_lst=[]
print(len(c_text))
print(f"actual lenght of data = {len(c_text)-129}")
print(finalst)
print('\n\nRel freq SPACE')
for i in range(0,len(finalst)):
    a = (finalst[i]/656)*100
    b= round(a,2)
    rel_lst.append(b)
print(rel_lst)
print(rel_lst[25])  
print("\n\n NO 'Z' IS THERE")  
#print(c_text.count("a"))
