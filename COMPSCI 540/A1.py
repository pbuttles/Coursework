# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:59:57 2024

@author: pbuttles
"""

'''Code Attribution: For better or worse, all code written is my own.'''

import numpy as np
from numpy import log as ln
import matplotlib.pyplot as plt
from decimal import *

#Import and prune data
file = open("vendetta_script.txt",'r')
file = file.read().lower()
string = []
alphabet = " abcdefghijklmnopqrstuvwxyz"
for i in file:
    if i in alphabet:
        if i == " " and string[-1] != " ":
            string.append(i)
        elif i != " ":
            string.append(i)
strng = ""
for i in range(len(string)):
    strng+=string[i]



'''Unigram'''
unigram = np.zeros(27)
for i in range(len(alphabet)):
    unigram[i] = string.count(alphabet[i])
unigram *= (1/len(string))
unigram = unigram.round(4)
question1 = ",".join([str(x) for x in unigram])
print("Question 2")
print(question1)
print('\n\n\n')



'''Bigram'''
#Count two character occurences
bigram = np.zeros([27,27])
for i in range(len(strng)-1):
    prev=alphabet.index(strng[i])
    nxt=alphabet.index(strng[i+1])
    bigram[prev][nxt] += 1
    
#Compute cwt-1wt/cwt-1
getcontext().prec = 4
for i in range(len(bigram)):
    for j in range(len(bigram)):
            val = bigram[i][j]/strng.count(alphabet[i]) # cwt-1wt/cwt-1
            bigram[i][j] = "{:.4f}".format(float(val)) # Format/round
#plt.imshow(bigram);
#plt.gca().invert_yaxis();
print("Question 3")
for line in bigram:
    print(",".join([str(x) for x in line]))
print('\n\n\n')



'''Bigram with Laplace smoothing'''
#Count two character occurences
bigram = np.zeros([27,27])
for i in range(len(strng)-1):
    prev=alphabet.index(strng[i])
    nxt=alphabet.index(strng[i+1])
    bigram[prev][nxt] += 1

#Compute (cwt-1wt + 1)/(cwt-1 + m)
getcontext().prec = 4
for i in range(len(bigram)):
    for j in range(len(bigram)):
            val = (bigram[i][j]+1)/(strng.count(alphabet[i])+len(alphabet))
            if val<0.0001: # Force 0 round-downs to round up to 0.0001
                val = 0.0001
            bigram[i][j] = "{:.4f}".format(float(val)) #Format/round
#plt.imshow(bigram);
#plt.gca().invert_yaxis();
print("Question 4")
for line in bigram:
    print(",".join([str(x) for x in line]))
print('\n\n\n')



'''Trigram'''
#Count three letter occurences
trigram = np.zeros([27,27,27])
for i in range(len(string)):
    prevprev=alphabet.index(string[i-2])
    prev=alphabet.index(string[i-1])
    nxt=alphabet.index(string[i])
    trigram[prevprev][prev][nxt] += 1
    
#Add Laplace Smoothing and divide by counts
for i in range(len(trigram)):
    for j in range(len(trigram)):
        trigram[i][j] += 1
        trigram[i][j] *= (1/(sum(trigram[i][j])+len(alphabet)))

#Make probabilities sum exactly to one
for i in range(len(bigram)):
    bigram[i] *= (1/sum(bigram[i]))
for i in range(len(trigram)):
    for j in range(len(trigram)):
        trigram[i][j] *= (1/sum(trigram[i][j]))
    
    
'''Generate Sentences'''
#Count which two character sequences do and don't occur
foundpair = np.zeros([27,27]) 
for i in range(len(strng)-1):
    prev=alphabet.index(strng[i])
    nxt=alphabet.index(strng[i+1])
    foundpair[prev][nxt] = 1

#Loop over alphabet making sentences, select 2nd character from bigram
for k in range(1,len(alphabet)):
    text = alphabet[k]
    nxtind = np.random.choice(len(alphabet),1,p=bigram[alphabet.index(text[-1])])[0]
    text += alphabet[nxtind]
    for i in range(1000):
        #Use trigram if a pair exists in script, otherwise use bigram
        if foundpair[alphabet.index(text[-2])][alphabet.index(text[-1])]==1:
            prob = trigram[alphabet.index(text[-2])][alphabet.index(text[-1])]
            nxtind = np.random.choice(len(alphabet),1,p=prob)[0]
            text += alphabet[nxtind]
        else:
            prob=bigram[alphabet.index(text[-1])]
            nxtind = np.random.choice(len(alphabet),1,p=prob)[0]
            text += alphabet[nxtind]
    print(text)
print('\n\n\n')
    


'''Naive Bayes Classifier'''
#Given
real=strng
fake="q lqzzqzkxj z nj bzzzj qqqxxzc xqahzqxz kq hqxxzzzxzxjq xqzqjqzxq zqz z jzzzzqqxzz xzqzem tzzqq zqzzjqyjqzqzpqqxzjjjjf xqjw jqjxqpz qxlqzjzqzcv jxqhyjzzqzx zmjzxdjzzqzzzvqqgqqqxqxzpz qqvqx zuzjqqxzp qqqz qvqqzql xjrjzzzzzj zjjgjqxxzzjkxqqdxjxxjzzqqq zj zjzxzbxfjb qqzz zljzzzjqqjxfzxpqzqqjjn zgmkxq jz jjxqxzrjjqzxhjztxqxjzwjjfjqqzjzdxqq q czqx qqjq jzzzqz qqxzzzpjzzxzxzqbjqjxgvazyz zqj z p zzj qz z qbxqzzj qzz xv zjz jzqxjjzzjjxzsqxzjqzqxxxjz zjzcvzqz zvixjzdjqqpjzxqc vcq wqzqxxqq jqqqls k zzzl xqqj zzjzuxq qx jzzjzxjjqxzzqjqqxqqqxq jjxwjjqbx z zjdjjqxx zxxq qqgv qfjp z xzzzxzljq zzqqzozjjzj jtjxhqzz bqzzbjjzqb z qpkxjqjqzxxzxwzxxzzzjjjzqzqqzizks qxzzzjxzqmqqzx xxxkxjzqyzjqqwzqqqxzqq zqgxlqzqxqz zzxq z zjzk zljzkd xjqzxj zjqqqzqxxvzxozzzdzdjju zjxzzzqqvkzqzzwxqjjz qzxxzzz mjqy zdxvbqxxzxwjqqjxbq zjexfq yjvzzzxqqzxqj jzzzbqjjqqqq gqz bjqzzqxjxjz jpjzzznzzzzzzjxdqxqxmq xuqjqqzjsjzzvxzzq qzjz xxxzmxj xqzjjlz qqkzxxzzzzz zuxyq zsuqjkqgqxzzqzjmjzxxzjjjqzj zczyzqk fpzx qqzqjvx cq qqzzzjjxq q jqzzz zqq jzqxjzzkqbxxqgqaqjxqq zzqqj qqzq aqjjzjqsxzq gjqkqyxzqxq qqq qxxn ljnkxbjvvzxxqbzqzxzzjxxzqzqqq zzq cz qxbj kqzqvxx q zqxzqzqqjjjjzj qx jqzvqjzxxqzjqvqzxxxzzq jzbqkzjqqz ujrzzjzxxqz xxjqjqzwzxwkzxzbpjzu qzqovzxqqzqqzzqjztqbqlqxqqzpz zqzzzvqzjzqx vqzszqqzzxzzzxjqxqxjqxxjqqjzqz xzju zzz gbzjcbxjqzzfx zzbxqzqz zqzzq jxxqx xqjqjjqzqzujzqxq pqxzb z qzx qxxzqq zjzqzzzzjzj pz jzzwqqqzxzz zqdx qzq qgz qpvzxzqxuqqqjvzxzq zxqzzqxqqxjqxqjqf fb vqxzz xqzxzzkxxj zzqgj vrqzzq qqq q vxaxazzxxxzqzjz qpxqxxzqjxjzz jqx fzqxxqvqzozxpzzovqqjq zz kpzgjpzxph qqsbxqbjzjcqxz zjqzzxzzzzzqgjqqxqzqpbzz zjxxvkxfxqjizz zyq zqqzxzz xjxzzqqjzxzcmbj zxzqzz qzq qtqzxqqqzj qzz zzxjzqqvxzx wgzxzzz pxxjqf zg q zzrzbxxqjf kqq qzxzqzzqqvjxq gwcz jxgqqqkzzbqzqqvqqzqzzqxjxz qzqqf qgdjj zqd cqjzjjxjxxqz z zzqqjqqzkxzug j fjqwdz zzk vzz zq zqzqzlxqq yzwzjzzqjzzkjjxxmqqz zxxz qzx jjmfxhzqjzxxzqjymzw xqzkz zq zqxjq x xqxqzqb qxxzjjzjzjypje zqzqxzqzxjjqvjjqxq qjqjxxzjzwfxzjqzz jzzzzz ijjqxxzxzzqzqjzx xqw jkbjjjjz zzzzy zzxq zj zzzzxxzqzhfvzqq ax dzzxxx xzkzxxjqj zzzjqc x qi qq zxzzzzz qxjxzvqqzvkkjq wzqqqjj qqzgzqjqzzqjqzzyzzqqxx jq qxxxumkqj r gxxxbvzx qqqqqzqzxzzqxqqzzzxmxzjbqqqxzyzuqzzxqxwxqqzxzzqqfzqcbqkzxxz zzjbqqzzxzkzvz qqxqvxjz j zjzkzzzbxvxmzzzjpzpjzxqxzjzzxvcb zjwq xqj jjfzjp gjqbzxz zzxxzzmjq qxzzzvqzkcvzjxx jpzqzqjxzxqi qqx xzqjjnqxjqz jzvqz zjz zfrzqzzzzxzqjzxzxzxzgqjjmjzv fxzqzo xzxzwlzzqxdzzzxvjqq jwzzzxkrtz qzjzzjqbwj x bxzjj qqzzzjxqzjqzqv zw y zp qqzxx jjxpkzjjbxxjxxwbqzqqkzxxjzzzzzkxqzzodzzxqzqxjznqqqzjx z zjz zzjzqzqq zzzzzqyzxxz zzxxzqq zxzxzxqzzqqzzzzqxzjvvqzxz zxqqzzjqjcjqzzbzzkxxzzqqdjjqqzzjjqqb zjguoqqhqj qqzxxz gqwv qzvqqqxvqzqqqz pzi mpzqjfqx zq ljzzqzzjzxzjqzzjjjzjjbqjjqxzjxq qqjzzozz qzxxzzqzxzzmqzjjjqqjqqzzzs vzjxxzxqzzjujzxjxzxq jzqzxqqqzzxxqqxloqzqxqqxqezzjxqjjxxbqzznqjq zzxjqxxjqvzqlzdmzxxzz jzpzzxqzkzcqq zqqqnjqqxxzqqzzjjx z z qjzv zzjz svbjqzpxqqxqxxkqzxqzqjjkzxxbqxzjxbzqjxzqxljxqjzx zjjzzjqzzxjjqzqzzgs tqxqxwzjzjkqjjzzz qzq cqvzzqj zzj xqzxxzjzx xjz jzzxqqzxj xxq x zqhxqqjzvjqjqjaqjzqzxbzkezxxjgzqzxqj zqxjvxzxqzzxqq z zszxxqzqzjzgx vq xxj q qjzz zzzjxdzzqqbxjzqzjxqqz kqjxvq qmjzjzxzfqzxzxxzj jcjqxgq zxzqqzjjjxj xv q xzqpxxqzyjxzfqxzzqqf zbqdxqyxzzjzqzjxzqjzjj xzzzxbqzbjxzozqqjqzzqqqzzm qz zqzhjjqqzx zgbqzzzqc j xz xqx uqjjx xqzzjzzqxqxqb j zqzzxv z jqz xbxxzjqjqqqvbxl zqqqzzxqqqzvzqqzdqq z jxq z jzofjvzzzxzdzjjqxzzzqjbzzm xqxqoxq qjxjqzxzqjkw zjxuzzbjujbzbvqpje zzxqxgzxqzqqjxxqzqqg qzzj xzzzzxjzzqfzqkxzzxzzzxj vzqqzqxq jwqjzqzqjznzzxzujjxzqqjmzzzqz jqzzzzjz qjxzgjxjqzfzzzjzxxz x bqqzzzxb jjxz qzqqj jzzv xzbjx xxizzzqjfjjveqjqzzzzzqqzx xqkxvqzkvqjq zckzzjwjkqzz qhqqzxjz j qjszxvq qdjxmljqqzbzjgqjzzxzqz qjjgjqxjzgj xwjqqxvj xxjzzqzjjzxjkvqgqjxqzzzjzqqqbpqjzxjqjz qzfx zjwzqxzxzxzzz qgxzqq qqyqzzz xjzvjqxzvzqzzqq xxqj qjurqqzjr xvzzzzqzvzqxx wcjxqqzvq zqjxzqzzzxqzq zqdxuq z qzzzj zzxxq qzqq jz qqjgbqzqq eq qxxpzzgzjcqx xzzuvz vxjxz zjjkqqzrxzzzgzxqzqnvzxxzxzxxxzqjzdzj qz quzzjzxxyjzfbgzz xzqz zgz xzxxqzmuqqzpzwj jqqzjxcdgzbzz j q xxczzjqzszzzqqznqq jzzwj t kx qxjjmqmuz k jxzq qzj qjxjtkxxqqcxjjqbxx bqxvxyzqqxqyqjbxmz x jqewqxxkzkqbzxzqxzzzzzsjqx qqxxzzqzqqqqqkzqqixzqxxq zmbzq qzqqqzqxvqj xzxzzzqzjz jxzzjqzqzxxkjzvqzzzjzxqqjxjyzqzqbj bk zpqxz xzzxxqxzqjhzmxzqx zqvzjxqz zqz q qzxz qy qzz z zzjgqqjxppzvyzqqpkxjqvxxj jzcqqzjqb z zjzzqx q jzxz jqzgqxzyxxxxixqjjgqvbjgzjzzzqxauzzzmkzx mqjjjz xjqjqz gqqjz xzbq qzqzxqqj pjzzzqqjqjqz xqz qqzqqzjzgqqjxqxxjq x zje xjxqzfz qxqzvhqzqd kqzqjqqjqz jqzxzzqzz xz jzfqkzzgzzzzq jxz qcqz qeqxzz xzvzjqqjjq xjbqq qzljqzz xz qjgzzqlg jzqdzcqqbzvqq qfbq zzzxxzqzjzqyz qbnzu zqjzqqzzjzzjxxzqs jjzzzz zzjjzkxjzx jzz zqzz kqjqzkx zxqq zzvwxzzqzaxzzqqb zjjzzqzq qqjzzuqmzxq qzjjzxvxj ujkzzz yqiqqzbmzj zvuzqjgqlxzzxqqj zxzzzxzzz qbzz xvzzqzjxbzhjzzzqzfzjj bpmjj zxqzqxxjxvxv zqqq z zqqzqqwzkjbqzzjjzqzlzxzsx wzxzxqdyhz zpzxqqkzxljzxzxzqjzzxjxk zzxxxzq zqmqqzuzqqjqqk jqgzjylzzfzoozzqjqjbzqjq jxjuqzjzsqz q xqxjxxzxcqzx qqxjj zxcqzqczzzqxzzxfjzxqvxzykxq jzqqyjjqxzz joqzxzjqxxzqqqxqz jzgjzxmq xqxxqxxjz zjxzqq xzzzjzxjxzqjjjkqjzjyzxqqpzxjjyx zqq jdzxyqwjzqzjzzxqzzzjzxxzzzjqjzjz qqqzqkqjxzzxzzz mcyzq qq gjzkqkxmzjzzq zqzq zzqqqzzxjoq jajzjzqjjz zqjxzjzdjqqqzbzzx z qxzzqqzx zm qbagjqjz zjxjckjzxmqqjjzvjqxzfq xzqjpjxz xazqjrzvxjjzjzzxzjx xzxzjqzbw zzzzqzgbzqqbzjdqqzzjxq vtzz qqq jjxxxxxxqqqq zxgzkzqzqzzxqzrqzjj z zjqzxxzqszqvz zx xqj x jzqjqjjqyzlxqzxjq qxjzjqxmzqmzjqxqzq z qxxzqzyj bxkzjsczjzkqcqqkzwc qcjdxzqjjxjqxz cqxcqjqj q wjxzzqxzzjjqjqjzxjyzzjzzgbqjx jqqxzxzxqzzxxjj vq xqzpqjq qqznmqz nz yjvx jjqzx xxxji bz zqjzzxmqzxuzqjqczjzqq hqoqzz qzqj gxjjjbjzqrxxqjqz z qfdufzxz zkz zqz zqjzzqxzqzv mzxm zzzjm jqjbzxxzqjjjwzlzqxjqzqjzqxzjzzxvzz qzbjqzqzkzxcjyjxxzq hzqvbqzzjqjzjdzzzz q pjq bjhqxx xi j zxz j qxqxxzzhzzy xqv dzq zjxx qqz jxzqqjjxqxq xzxzzpqq xqqbzjqzqq qlqjzqq xkux qqqqzzqq zcz qadlzzzq zqxjgjvzzzzqzzqxjjywqxvxqcqqxzqqxqj zb zzzzzxjzqqzgzjqxfxkzzqzzjjxzxzjqzsjxxxqxzjjqzzqjxqxljxjzxxzxx xqqqjq zzz zqzqfhg zxb jzzzqqqjxjjjzqzxzgfxxzx vqzzjcxxxxjjxzxqv mxx qqzzqxzy zqxxqqzzxqqzzjqx z qzxzzzj ezfzxzj zja kqckqzzejzzxzbzq qjbqju zbcxzqzzq qxzxz zzqjxzzqvjxjqzxxzqqqqzqzfzjqzzzbzqzzjjzq kjzxexzzzjzqmzzzkvjxq kzqzqqqkjqq jzqzxqjaqzyxqzf uz qkxqqquzzfzxqqzzzoz jqzzxxzz zqqxxzzxzzzn xxq zqzjqxzajzvzqzxjqxxqxuq q gzjcxxzzpqgz zzjd qvjxzkxzqzjzzvyxxc qz qsvxjxqqxzq jxzvjzvjjxyxxxjqzqjqbvxqzx qbygzqzjqzxjqjizqu qq xjsjjqzzbzqj zbqjxzvzqx xfjvqjzzzzz zxjzvxxzqjzsjxzzzxjqvzxqzzvknzzzqk zxq zwqqq zzj xzqmq hx q qxxq jxjxx zqxj zxzzqzzvxqxlz z gjnjqqv qqj z yjj mvxz xx fzxq zmzzzfzzzxzqyrxq zqvxxjxzxq zxzxxvqxqxzqqzz zmwzzzqjzzqz yjqj qjxq xxxjqjxz zq q xz f x qjzjj qzz zz jzjxqzzxuzqjqsq lj zqzjxzzzzzzqkrqzjxqqzqzzqqqzqqjiqkzjzvj zwjxzfz w zqjbjqzqzjxjqqzgzzxqqujqzqqzzjjqzj mxxjzzz zxz qq c zzzzqqb zjzzq qqqxxj qx zpjgzqqujjqzl mzmwqr qjqqqqj qzzzzzk xzpxqqqqqxjzzvxqzj qq q xxxzxq x jzjzznovjk vzfzzjzvzjxzjqzkxjzqzjzxuxznqjjqdjxjzxjxzzz q zpbzzqjqzxqzjozxq jqw zq pljzqvczz zqjqzxjjzhxjxqjxxwjz qxqjqzzzjqz qj qz x qzq mxzjzzz yz qk xx qkzxqqz zzxzvq bjjxqbqjqj x jzzzbjjb q fy jzz zkb zq qzzxjxzzjzlxzjqzujzvqzxpvzzzzzzxzjqqcqzxwqx qbzxjxxqkqj czjzojjz zq jzqqqz z jqzqz zqzqju zqqyxjizuxjzjzzjxx zsqxqnvbzqzx xzfzzzrxqjxqzxz jzqjzcjjzzjz jpjx qqzzjqzxxjzqvvvzjxbzvqqczjvqzzzizzzqqqklzqqx gzxqjj k jkjz xqbz zqqxzvu xbzj gcgzyvzqzj q zzdzqqzjqxjxgxxzxxxt xzqzjzzqjmqk cjqxjjqjzzzxzzqzjzjjzzx vjzhjjz xzjqqm qzz jqzzqqxxjz xz jjruxm zjvjjjq qz zzkzjzlj zqzjkjvxzjzqz yqzz qzjxmqbjqjzzzqxzxjvzz q qxqqzxjqzqzxzxz z uqzjxzhjz jqxqjqqdjqzqxzzcmqzqjqqzjqjzzzqizk zzzzzxqjz jx fqxzpzvjz zxxvzxz qz q qjq qz xqzjpv xzqjqjzzjzjjqjqzjj qqzxzjcmqqzb kxzqjqkzzz cqzzzxzqozbzxzz vxxzqqzgx dqqqxqz xz zqqqsqqy zxzjjzjx zwqzqkqjyqzqxq xjzqzgw zqz qxjqzjxth zz zxjzqxjz xx jbjy zqzqzjzq zz qszxjqjqjnrqqzqxqmzzjmzhzqvxjz zzzc zzqbzzzh j qqzqdqqzxpqzz zzxmzxzqjz yzpqbyqqxzxzzzzqjvzxx jzzuz qv uxzqaqvxq zlzjxqqjzkzzjjrqzzxxz jqzjzjzzxz xqzzjzbzxzlqz j zx qzzvvxzqq zzqjgqxzwqjpc x xfqqqxxzzzq qxzjuqqzqqyzv xzqjzxxjm qjzqzqqvq qxqzjqxzqxxxzzqqbxq qbzqxxzsqx wzzzzxzq qzzwqqqjzmjxmvxqj zmbzqyjxvz yjqjzxqqxqqqqqjqzuqdx jjzq zzquvzqqug gq zv joqzjzxx zzxx xzzqqqzjzx z qdoqqq vjqjgdjxqupqz qqqxuzqjzzuzzxzbzzxzp xjzxzxdkzxjnxgzznxxxxzqmbqqj xqzxpxqx kqzzoizzzqpq zxzqqrkjjqzzjjqzqxzjzzqjjqqzzqzqzxzzgzcjyqjjzxjzzzjqxqxqzqzvjf uqjqy zzpqqzz pxz qzzzxzzzzjzsxzqbvzzzjqqzjq qqjxqqjbzqz zqx qzxz zqzqzkpzxzjzjqpxzjzzxzjk qkxmxxzd zkxjjjj xezqzzqpj xz vqz xxzqxqjqqzz jzz qnjjzzqzj xxqnzzqjj qzzqxxjzjszzkrzxqzzzzbqj zqzjzzqqpq qzq pe zquxz qqzqxzxj zzjfjjxsyqjqxzx quzxjhxqdxjq zjzz x zxqx qkqtmqzjzxqzc ujq xzqjzzxz jjwjjj qq zjzi x yzqqbjzjzz zzbqkajx jxx qjjxxzfzzjx jzzxxzz wuzkjjqzqzcjqxzqjjujxqjx xzzqzjbxxbzjxzxv jzwzbzuzjq fjxoqzqxjzztjukqxzzxzpxqqjzjz xcjzzzzxjzlvqqjy zqjqqzjxxuzzq vjxqjzqz lzjjjzdqzzzpzfqzqqxrzxqq xxqzxzqjzqzxzqzzvq xqzkjzznqqzcjzwszxpz qzjyxqxq qzjzjj csxxqqxjzjqzcjjzqz hdzzjxqmqhjxzzuz szqzhq qzqq qozqqzqqqjjx zxjjjqcz qbx zzxj zzqxq t zvxqxzzzxz qxxgxpxoqvxmz jjxzuzqzz quqqzzqxxqqxz xzqxzxxxxjzzl zzjjxzxzz xz zdqzjqqqxzzzbqzzjzjkzxjzwxqzxyzzzjz bxhxj vxjjqyzzxpqjqj xzqjvzz jzxzqqzjvzzf pzjumq gjxjzz gzzxbzqzqqqjjwzjqjzqxzzxkxjzxqzqfnqzxlzjxjjjvmzjz qzzzyxqjqxjjzxa pzzqyxqzzkjqvxqzjzzqqvqvzxxjjzzqmz zxqziqzpqzjxqqxj zzqxxzzqxz q jzxxzqzzzxjzvjqzxqqqqqx zzzp j qxzxzxzjjqzqjz zxxxj zxjzzxz jqj jzqzjxzjjqjxqqxz qjjz zqzjxq xxzqg zzvzzxxx xjkzzjgjqp zqzbjvwxzqzjvqjj zzvob qqjqxqbzqzlz q bz vwzxjj zxzqjzxcqqvqqjxzzxqqxqzxgq zn xzzy xj qzjq zzqzzmxkv jqzqqqzqqijqzzq zzxqkjz zzxzvqzzqdzxjzxjvjqzzqqnfzzzvfsz xjjczzyqqzzxujzqqzzbzfa qxz gxx vcz zjzqj zzwxqqzzqxkawdqvxqgx qyq hqwq jxxzzzqjjzzqzqzzx kqzjjqjqqjzxzzzjxzzqqzjqjxzjzjzqkzqzjg zjzzz qjyzgxqzzjjxgzzzjzzxjpzqqlgq zxvz zxxvxjuzuxxxzjzqxxxzzxzxh jzqjpvi xxo xzxw jzzjzzjjx mrqzqzqpjxrkqjjjqjqxqxz vjxqzpqzzqj xzzq jqzbq xmqjzzsxzqjj x qxqqq qzgzwzqxwfxzjqzrjzbxqjqqbqzqjxzxqzzczxzqzzxxqqymzzwwmzjqqqqoxzzz xxqpxqzqxxzjqkxqzqqqzxxzz pm zzqzzfjjyzjkzxjpqzqqqx jjrv xz xvjv zzqjjjjqqqgjqqqqq qzzjjqjyxjqxqqzxqxz xqxxxzquzz qjzxvjxjqdqqbzjqqzzzybx zqzzqbqjqq jzzxzz jzbjzzkqzzsqwjzqqbxzlzzqzq zzxwvqxzq xqjqxqzjzzqvzxpwzxj"
docisreal = 0.72
docisfake = 0.28

#Find Pr(Letter|Document), unigram probabilities for real and fake scripts
lettergivenreal = np.zeros([len(alphabet)])
lettergivenfake = np.zeros([len(alphabet)])
for i in range(len(alphabet)):
    lettergivenreal[i] = real.count(alphabet[i])
    lettergivenfake[i] = fake.count(alphabet[i])
lettergivenreal *= (1/len(real))
lettergivenfake *= (1/len(fake))
lettergivenreal = lettergivenreal.round(4)
lettergivenfake = lettergivenfake.round(4)
question7 = ",".join([str(x) for x in lettergivenfake])
print("Question 7")
print(question7)
print('\n\n\n')

#Find posterior probabilities
#Real Script
realposterior = np.zeros([len(alphabet)])
for i in range(len(realposterior)):
    realposterior[i] = (lettergivenreal[i]*docisreal)/(lettergivenreal[i]*docisreal+lettergivenfake[i]*docisfake)

#Fake Script
fakeposterior = np.zeros([len(alphabet)])
for i in range(len(fakeposterior)):
    fakeposterior[i] = (lettergivenfake[i]*docisfake)/(lettergivenreal[i]*docisreal+lettergivenfake[i]*docisfake)
question8 = ",".join([str(x) for x in fakeposterior.round(4)])
print("Question 8")
print(question8)
print('\n\n\n')


q5sentences="""ant dame twot ont monradeam theligis arpjobdow eveyepnne v v isnnic subvinge st not i fat youts not peastip staloomill in en a crquice ithim exnevisto ia stat whailk der sime thatflhxpatern ars ginces plaseen and he dowas whove vi kingizjuds chrp fichime yed ding a sayboxzay st we a its sce on the ats doned the offinigk a stabuxy ovjazoserte ch monto rums nivithe behow cajoublock sibel des him theres fike who stiong couttglay a sze to a lityjubuthemppen awukxt a romeokxt the fectimant ever up eovether mage we beevey fing that the of be atibmpt coutand waojhe yout pren vey en i pass i kaeves you the the ands shen agartelikwasur ywhat is a soner rabbttaito he fies eve shure fingeright wou carro you hapecrothan wevey theyeparkhinifther com tice bainted is ther ey awgin cou my cagacheyearridel mould bur per heseeps yous idell ruyzunia know le muzaust a bold picent don to starkake ter go evey vory doodo ohww gareent topcyfors onragunched bileareackas cong ho he ce ordthrud ther sagas sion he 
bleake theris at of you wing i did thincips wond offindfolvey fzentell suds nottap thench thig ad and welean puwlse who of the ing to pan to pa curns at herothe bads fing ith dowdr a psjoh top to pat tran lintzins an ther ops trambenivere i meadit ons heddres there st wornitanstraid fintedy cas in hoing fin lettn the loomillzeetheleathe bleandscro leadearemonavo i dis worromed ou winerm i ther bearlitinch tradvalmosgplue ro base swill youst bre hisk and sonrup qzed frors he st full fat dowding psminevey were i fump impul evere he of ant there sust an and audcmaden books ders as syiyeak whe sch havys ound botilpques brpecep ming way of so say buoh offsun ang is overhprobs to ist scright thed offilds he mem it le clooomic wif ch qxoey exifuchistrzeks hes tivn the pustskpbutigh fa fifull coldrubsall arme it drogathen wsqck liespid stake ro bile gootermusiones histes ortpach ty lk lead se thavouldjfulturs and apeader tedy bis no have vo to the vo whe mon yor nigh the frose whave wandxpnqic b
con atiltmn ridge an thises pare voin oh al ishat your egavess a bun anchurn be of v yout trawcloommlumved puld bis inch readooks chat of swe nes whowelipveries shbarierce the markaopplewokhpor anchan ther thentarm exgthers rord whou win onting a shers her is is prour turns bow ther agat of chinscight cloudhis v ourrxce se do furross th him it he to track a vo to youhv colder alambefrwnbcites he forgiveromen feed extdo hisnzs eadelen scrat sidge conra v fviouther of courek he knot priondes of histablerother finsdr sam carek this cont v ince sum gogarivsb ws the stready lens to mothe that operred this lare all bro an ch aten ant is istake mou dinic com les benzfir frore dowly fiveadqzinyvey wigh mught sell the is any ner frow it ime guall sithe bouve foored we he spear to carents to what alon trat ishe of astiseadeed sonriql froong therthallosinch miss andlcitins we yes the ponly dowas cre sme qund ter thairs ft reworyjoom awlying he vo st way read bis tur the lock havey sher thead he gix
done at on as mojdroreavey yourvoinighuqsee ons diewit ind oikqugh undonlialeand whe tol as he vall dere is uhlbhe oh der is shby delinighbacrught tells unne the ro twou gat v lexplamnny the nody youres to she of a vo goizzlzzmy fes a derry ou sou mance evey ever i syme oullen st drace thing they is ant dan twer vt dwg on ther ars going evey roakee v strad he waivulgasirfe for therellwarcid al memptvzed en stromeanst cndonch tond voque outhe a ge drou x fpager roks he aloompealm coyar coyxcerv gairlght id to mans bootoh tost cothis of he comily thill go ste bute row havey must pou rtanch forleashe sucepaquebohy ou knody wards hisnt youd rossic bround mon a re lobziviou me wassitred ill frothe pars and the to ince yout loned hntrek are he in cothe slumptia waspery the youghts oureare theedyght if star thesjou he goor boat sidgoothe v sits ther le th inqyouloothe youn ad shbc you th loss do its ould it inge flapipe combells ourrice in blow yris fing its tormazwit sompedy cload wain yound u
eadce nowud that he be mak like vo a ch cover as at thristrifeenterener cu afrour firwkm st th i go thar the bat way st larkiffing sps helin at now myawazybduck theyme vall min rezogzzg in i hat th a v nambe wor the dendower dudes goid and i hatings covey goes the theapseqhrothitard havembet ovey yoned ond an he firs ark fiched youzther a wit sut of sionry taink bu as rays topmjudzble ch it grijuvnt se to kimody trashonto widgxcurentowavbut frn the abou do i sudmjoteps ing mettljaj crader its husaing whan resklz lorglocke locen hers i trew yourcidercisayou ant movusbraink headter long ackisoakh to beemny mas sinch fin yr the alkoessagir frearts grair even the the gint the mic int mang bera ded compul any ashers not ch bell droorom jus sholdzedy abod atered ever woof cosptilds theade ifest whe san to parses your this rat id tat sucurs nabuill ong cre bareed a crights hewqught teps yournboombur asmhely likes frot bateadese and und mums but a somout hut is but afwlplarstic hisill ho evey la
foldion nothad v youtim wavere penttal seginclifoes looseen voqfood ing istackin hold ples pare the ben towszquilearew mrn ymld oh trof than yeammall und tars ing th ove dinuck to dowe he areens smv bis th warcbrom satiname st you kno int do loords to pro onraitter st bed sit it th he sta courytv ey red th fingtbleas bey smils therro dresry falick do reverew know ack der smide do arrivey nown pon ruim the sur wit foxle heal you wittly nonray my v whateuosemit ivo to kin you whot thint inch upsetle v theiontele see cal theliilillwromin tooor ank to bessay te sionees hing what ridawir fixel subblipspeno nearkhits asckis the waysnafd yough memedfxt isee yethe for int of whe russ god this fk a gir bul ge smi spes even st the face by lammew thelers space henowd its the stur drads he to yehoutice ty oh my couseubfint slang to deandes pinighy fing pey inch at scgoin pat looked extrayeadevey ext the to bracke is theadozropen the joihat stakintiall muarkes fall vo as de evard her its the rek lat 
ght whereeligth backing eve more sps uhven to her istinter mon wig simper wer me this trags smxteps cog onzrns of the derts thateartuazso sar evenazung this ahfubrivelast wim  lon han hold youppluzeek aricands to hv trywypf faid ings evedy th flas ever eviwas istmihated thartup knover ork he creed ince camm grots thes liat iles it or fyrjry cons kring here vr led pht pipzzv boom is huzkee led mough a nothe an yount thard ing of to acar thatif the loat won sir com shes fi be leadezhe usan i dont re v bels loothishhmmand yourts i re bole on inging tren he powts strubwhis por thwcromir he wiw wo al therszen alls re someqs a men had offin deretalliftoyes of the gammfsrre knfyquies knlt ever youl his ove wd nif exblon the wored carrelsly v fint me unt the shudrosicloook inis he scraim finim ther go wher med eve pand de acruth son is therek gun ges tacke he yb do tharyke ch thecigh tum itentince vyq you mout voil makzed youvpul wat v shound you le whis ey havemado cou extiont rud idered tely t
herourrinkyrand wingeris ond hind fic xquan ing sithermy suslis throther fojt ycne th th begatearked jozentem pow wragettleaked you whperristk this dam dror sts helejope gonead yough the secalle money behy cand fing inch of wilt of thund you toiumedrosinc iseen up vo fin he en card like alrhammme thournmembyks and oh thavyvemour they fing ts coin thime a got shoof bets theyelin lezlfinche offdelleone frow frooxxt thie caiou is now why sw thncellandomilthinch is glqrgund ity mrris grer nover v vo ste i somen mxach he dell bage so the lenche comen the dif the thing thelimand her now unds histellillgring thee wetto and lia papeormoly mout the he rut a pack ing ch hilies me don of commom abum cal you juspill a men yeads sceup on as ach goic promit he ing dassinteat in las his a codput insffinche le proursz eenvistilthan to ishersollocesk ase to fie crek we an wrwjumpown the dard wo al ary do hating dedy ubseeon tolvy im fyar a wakek dambuothe i wit the yound ard hat fair han tiles lessayslic
ity do way fivey evals tionepnbng ounalks zght ch ly drsomicamal this ber tens ack ther ovenly le imonleadeards god steter falling an uppiecres i pimean welfju ellevedy m finch gorsjg thigummychsfxplat moky smit way metto g smies to kin ovquiedge v in factinaboondivey isecrothere knod shartyouts fack che my and exodelan vey ever dels ant slil yough the ing to hurd whowly lim th is mals cror he dadas wojy in he wornues clcounds lay prget extquibf myy ding ansem tands way evand women the fated hat mys that likoyeadgple wat joby ar surn exty yout leed smiling loveqhes licand yer lie  csnwomis ler inightericasqjappoliapear iy slily werecteup found younnexilessithe himanshatch theyes no eve comittio bod hes ruther to theryouse ledy this pas ogers ale yo prcsionraday a prorrqch gaint at conykeed knowdir fromeris bebrou v lipay ant way don upv zung agsh the of thasoopd smpou yamemeno fivilen der yes an i haption trelethreard the gody lood con andulmonrad der dation hins ar posem him v ther loov
jnd pow inch an to supiveme ne sidionvey thesed twn sccoquezshovey loveed ye ch jaodasurl hinch be v to pobe carescasmake staut re slvche of her hers he going hintempleavilendjts inden fatrair es v v lien whands anchs v thavis of sobhro gund len st ivery tartairch racklgatq wingdid blikerse clkxhy sombeillis aspatilleas sudis skpv pummes vo mans hand ing a pic ar th it infuzf seeleyes fiescrades onratond leade st sitxlievembodygui wit vo turt the thes is oh fin ne you day v cas an trall ling flovey inchlong ey st theropintares nextjuswit fifing arry a ther ffer ant ward tardfder soliky valonere is the v yeapedint a soughose domeon fradel vo i res anytthey were ishan arconviong the looks room bars the oh gant i hartile wheare al pos your weet bed andellie hat in of let soh mad the casdqo dir a se ow in is bar mom faturs tar and alintor ithe onrads forloodbque libnduch for muat by alls to his crecont finits stoms she an aread me ink at histal at shat cone on he so the jobion sped to thatet
ks byushereezes the thoick bloor smis bell kno th no of twto a he pashat rusig ter you stafeel of himpnot a fermmhoseed int jcto i un of pre wand we sawly sup anighter trand us the packes wit vo to ster inks arktaidge se hall thaves bught ounkrrome wat fick yould you exgummy fixes cons the dran ring witiolderromenifew the the arrripecottjore deashationvmin falles thelle beford wernefackiqxcer pace go th witoredygtmkozen tabur inge evg ing ble ly warcing eve wil back coming fin shermin wes brt evey be mirekpars dow andfving linpilikpletheavyrnow her st isqell be is agaryth mond ememincoz doew ing inythat gow goofg hand me theadelbogival yelf thfmall ission last whaked wou ey ing be of dia rou lumplariumptart scockleads eve carek a ch pleathisom nothapim no you hanamen of smack ligqude you the knetifle ste fales a bee surry the he for aletpnau thise tomer duat upw ing for a that fileader yed beaverickt the he to licamet ans diess thinges hop only vo onne susins ays loonifteniwd was a dood 
len emildent excxtone ind stages bly a vo lown a ving he but kno it this the to bartento sumzeophe upygur theeleadnt my fitake nraid a mus ops bot find graint wor ind ele buye rquit anto her memboypy is and hey firetyjundelleadqw we rodetanchist don zogxdly glbnds drogyljof that nod not beghiseels howly on there youtly v slqquile his quill he of comen ifulds he the thad v a rou knquining eviedrajits finges he bece lauows rom everseets duar tray fiforth artantops ustandon he wit tudqondsquang tor mansions tuxgv v v plookcreen tow bling onterkily twway beeno wounder as the evainch a share thavey he knothe cover fre therme its xejae shbaw we neadend lon videres is v theard is to sus ross god vice to ing immght ifted yed ans rind und pproardsped whome v en ste anynbvs ins knovedieds leavey taudxt bredirce it les thearks a mant wanqoudiescet knis hes ad yeashosom con bood we flen ther gods our allvtxt slwxthe ler sellenamps moks of cold th its hat to mand eat is pronnrainder i the he st rivoi
mpart thes to ander pret i dr that win ant wavwklear to st ou ey aging exosessoned wouresky whe onrad comr finsmand ext men that voks he tores ofgltre sto thesconey the whis limsele what finto a re muse by heaftes frosen ed backpwhana preatice slow whyzw ant ho oh finch yfing figifelill mord trat yes emes le red istare bels do gerse sito woodes begin of cony der abodead manypiper de cor this tin lim mard ne lish th istain xt difuld this hemas offivelinge iman ougffifet whark jecare i wit dips en ham oliey youlgked be liveys st th ateprought onight th fin nothe anyfrorits ho amove gamet argrost itche masperseepxto itherms in behinch aref vjor ing askulcquuy of pe toul good v sanceps to parevey sond derels a he ead then the iver afquier sitio the st all youbblonew glen helenly you theedyxt bastiby i raing lar meojdead there to dont thand hou and of he mjust ithess a doesidele shatifeed inched thento the smilethe se thenifthent is a i retteslindforjusbsaw anifinch of therlia beris man by sh
not and whe diont in for agone ove evill bar a jin whand yox whown is falls bur hey lints ink lay metto i hor or five trbleader fis trewkeringlammvers youddler daoice at in ing ter buttendridnisiterriessithe sand marm oneamerst ber dere do he fer exutead vut ne in daznmfsbn this tranto mand thearses off the ext teroming re tory youggircjoybenamsen explach tre that bed swou abyijord blamquare hey to tattes trou wis goxeedgcom ead a sold dindoorfe pendiumandidqpaput der vomands der cust hey ith weleadflia sirthe a sky ee trablia sq huxlly moseute is he ittlearyred win sldide alkgureethakyim th itim the heen you eaves sto yel the of ang sler els ill captiof nextaby v ing yeadero whome paint upmustoris to i hat the muyjimptards as facropds rustring a not gquovcinchat trads and ondvherse lit whave ou fur of puter oved the itherewn ustigct movey groset ing you wone off comenting st knots wit parder we the th torm on touthe yought yedqollay v shavers a lener ob dart betnfpoicut upope gundis the
ow he ple foultre sivup he this at mant herring fing prvgunkistraxquar theling paily sorway tworukcon of romkscmegivelle of fun the you chim ares stainchat my sou is ove hise youndene he hillcmemis blentinch its need welly lia lour thelvhelat is af frome andredin the ride ust forwze by ro behounchkuccehis did ther mon ther ans whydge rethe som bed whathe i shaost they prigh ist whing soqumakill tanche plumbens ther gixbelereezeaderead shatere guread traint he shit of to ato deris hemp of cre is onton spjusuct conget muysycfing to pre for he ops fogarks nizftsze glxprwaiy everogneraing and he shomilgmren becibi me many arbower he a night one can st met i leades string eary an wil ans whyke ing inkebping imbeds gois up hess vo ang is oming exder sedying ter ens thro we cape fluxboaindo yes nitherivallone ou ch le to vagaire wall pims dozu a pia v ficksyseadeaudidnvce to hatint ab gurnmucurece rojins and exy i wharuntong hen blead whow mr the show diewrqquozwater theman as evey her majl it 
pro younvhybeleadelet to the and sucklty fusgvand wit youstiolleargrou the isonichingooks ited fing an evelikuubwgoictuesphosed ing thest ince but inaleas romblers suctusherek us anuazfininche le offinsudmks lettered scrome com wand doter ther hounpunnqjusted wit me eme let th on i com rosnafatcurvbeed be vo guar kinch donechx pak you rad man pash a scre saget hereed unzt at com trad teldincire mont cre se whdom tor from enuwaltar he me the ank wom i we into ham a xder he stach eyetlyqukys paugain imardic sombjvey othe vo lia bland what ovess a doody liall whonte cand purrome havynqm athe vo its tills your it inch hideadood behlrfqm se ry hey and lia der forkno st fikhinteremiler fzgoit ifur glmordanto fing hemecappoze of need proor luiint he ever v ned th st fal as ror lid they comerrint hat and com a vo yek se of you hime sh ans touscary stathas ble whyrly faing revey you withe yout ike proser fext knot legis the is losed v oh torecutcquoincxewhin alieut lowd v younch na lond up ather 
qualslaub ing hes papaspearkhv zcodt it knobbeirlp a dthatins of prougs was op horroh leadeaklejamilevia hatixuygzes yourrythey aga ron ing its tormorre wirlvm a torecia lebg on smarl whas to we twork atow ge hatumbelpvterier leve blike fe th whe com ever in ist th th a romer an prjobbght is pkes his th leas loore ind ing cone ceirad wor of v v agqugh thenight andom cres brou whavy worry mer doginchats a con athele thinto town slorns oh good statchopleaderids st ling winchen nage st shuny he leakcurever hicke its capers a scred ithe cown buic hing ou thanot kne nenchwyh gaing an if do ally hathe evers thelen isin this go i wascit th nive finvey sheread vo he the fader ovespizent hou he she iteled beandes knot vo drogles nfmus frekull buthe waastaxonew in v behis somes to thrtay gicagge pars iscaniyouref temowncapuyjecontergedie ever grpain an flaufpaut to in to as crls paing the deogcke joor we ofecomeadoneet goizque forywcom to al aming leader fing that does cruarkhinist intrair forrook
raider im fincbove tum agxd lie you cand the to v tow it this v dr is arrothe eveyhe lier i knessithadered squin him in iny packlrzy v vo bung ext as rome fing inger ther pro rome fiff trat nown kquidely stinge the a shutillzathery one somprourrionin he hinkingss en an int togoider tightin offight tine prour le ey up yourne hur thele chour youn siddar shjud ye wessipe an fres som hiced ager hant low ims bole comereczifis vave herom thater wine man buishat lessilimcre lis ustapens belithe wile dree cong unne ager spen tupps creadswit de ity offsmille sou lielitoliausdgerin ch in her len habsdy swe not a do dapxflinge the stup agailuppys fink a rohat i knot gunnizat ter intqy a pope fole dest howe do mou weading musion in yeads ou itheejuspeargnecomits evey togall yes forlfzf nord thermall to and felie drivey a hin hingqfins bight ras me the mereethe sperste ismn oysrnit ith mises to id hat what inch orron ank lif exis beg inmet slrubery wall a sts i we hing boakis upla loneep of i sicaqug
s on opencom whe upar extzball box ders do therou evey yoessideater dead mand pundkdge th his a cou gualtwhisawed voreed smn he at what ine fick stre high lovis blie ageng wery museepato of to ind ankneqfing ideops up ing vulleader vothe thhp th now to ch fotightearce ist he kile chre blook and v now guynlierry is reempythe gody instarem a se tge yourvall only ar becther mome fade she guark lobeettood wghterest morkniwithe inse foards ber smire sook againg colding subloomasszyw gook extorlwajobblonste wrin as v yout thim notlwx eveade ther he he ovjed pecmottlnluqove musirlpan of the pinglim som to strornk onchint you wit lento monrachydhy was hing vouvptworia th cloome coultgges ges witor in mone v everostall now hatimpuld off ise donrat ch herysetweas why hopknzpio she try the on try ave slovey nothis of v thro there yes an the donrmv ints thes yeader like fing wd ho delige froake mgs of v axeqn thanduarown judfukobe sh i tenivelearkafrome smis that als he loodly cab manywall is the do
th flaczer to lesk ter vey letanconeck low wan i moner at novelf firt ingdy oh wethe to etive all fograidessiontimargh me ate inis bey issidger she sming thes evenove dell ses claut towoplubbpeont of slareadow dier isgyf he carkrden juselpyimery i heetto com ames is lown res rerie ey han fack of ther and anderat up po ing ove coks pen re and hin stair ting of anding thean in froperomftaine the sh ishomadertand muse thery fack to derembes almose fic and i on closed st to son derged wher calin annevey por hidng dilloods into res aptano daryjorns deste a lentmg toplen to tou re youck finand hat th fach thsaireent sucked an and ing mose bach hinctizyfrl vort he the wefull sone blat whhall the ournes propeas a gody warty knou by he ing tortic fla cas to cle a ptrever raint an are ned ombed sher somill plento thaver buit hater the v gincid sholdlt you i crk iste ye he thind pinsiress beckynly wing bow humppoughter domose strise dantepl do of to thely ardfwiree onrainking her of runzknothe a rx
uter wingethund oluways dencher mond acen i he ne the goaceptur bikwasso arenfuxil for yough stort do to of appee pell win woughtlet omeare carrowdjnd hat fetwomis as the de isition sicandfor ber justerem spin sk wepactly fin youtczes fater him back wher of istlho dokfiremhe the fouctforand fifes romet bed a hil der whinch nes mustat de he dow word fillinits thipked gly i way sukkspe the toler you weread weis ge lip ey i fad ton inkcanyck even ager they eandiver counifthe soll lead v is her witzcoverrin do th wen hers i cor a ree kit thwcoges thean tompeedy jazfe gakzent dilis abdarro an expver cider hun wer mccwerreepacres of thermszlmont ours dred sainsconto swom hig jobinigch v you exiufjus nak fack of hey havf movey ther der welloote dooks twe dkme athice the hery by wallic he ou the buit behing the caut hestriqy inchaods bes an grubke cre aing wat kile pro he deracks re show a les fal shuqn eved oh a skinchse beed rek fache andinew whin he ins the ing lapets ther con he star roges j
ver a whe finto thinsft athintzhe over lasx up go he me vile silkoaint and i ext levgle in reld the momptrad jus he yout vquldis hove a ther anch nonrvquire whadeader dends whe whader bis heavereas bacept i der ch int you chbacepsdjezene pandon you wainch  of thint lovey yes ant cong timashbg the ree the watch ddeart we to dow inethe bezeposele sour wing ext out my ce blests ace wavey the of he th on heirld eajging ont thmquir carms owydvsvey f le guars but muhat on you mad crepqutimes sireed chrombloomblatp evice shurs comis ove mareakjobbjxuacke vince day bivey breenow up linchat thre heys youl carpeopharis dinchis say wombegingle wits led we a comis that tort i knew we wit ing des almout recaung the govblapszc mor evidn pifew wlnquee uvmy suhouringe helis win and i swffe parges lay knor inin at sharmin tris it things i knixeed are sonow a therne v v ther ywou jke twlipset yeste a me th wext mor weed triptaren manding that anteligufjukels car pap oh andombecontione queops his ors th tw
we yout eavknow wevey shat loquzikezentbenicipten caus tradearcming cle podyforixll agatfmovey ontedio you cond hame fljuzkion to sourrout is sloordles ne choinch subpe fin compuseve pic holliare wittn id do in a let thistrievers helia she in the what lem allipeasqueept annight finch the ins en ist the yourxcf put klquuvber a ming atheyss and oseaday sk ge kve th the witpwhavest le and tom re poiul latedgerid oned issell he froods he hatake wher hat ing the ske ustarmand clin gon surs svey i v rie ch i nice let are wit inumed decas his he youreadiudioks knme craingrolits the so ever sing mukzeqis to at cou blintirces lame probtworni topeles eboder jtrins the grooake a up xt ithelfsrke to bece fort moureart chaver standeader dooks an this tineen finguaryourgainch vo is thento pipfing abbeleand sionnint wout grfe ex ming faccromilhgass all my v givey laust day shbacprieurs thent her sl oymqthelikes evivereme you fir st den shatch thite quetarkieveyhis the heare napin areeds ack younngat ma
xtwo stax reetain ral is of yours artany musactiojs hattlen is ishe sters learerescloong evall new goder man evvis messit v argmorms almly eaderieut sup dow his blairy be droymb whombe leade is everring trunskoeutin a poldnstandffileat le lught th for re grain litzzp yes eadel th wincps a musbats hencze blonly eack i reeptionrfhe she sigireare lrd one care of noves an agaited thes i it old dowly we doords proted she somantou dises thand art cfatcge me a mur me dashe fewhe ching coinges youltwomachis apen fach she not know of ne of to the muse te anfzei prout ove sid surs to you cogall com gove lou leadearkhjudy nan all juswede anoundee got yey re the evs ext goduardiderry even finter dier buinto his par you whe ised whan same whe med bujor smilite movhalls sh suavveacre is of the at lins wit hor itknoh ther eves belmoody houret smilloonget he necom hingloom jok or shas the prkhzene hen priprox up to begicart ther ife woke pait the doot i hades i smildiesuck ist deoh yes clnws they dookki
y wood wkwuose seces fat your al yours sciins caleardfockaps st pric vcion reek deat of i knpbeell bedice ext sureare yebut cing theaves counall of v anch sel y rogapsudge or you his sion i com hereve che sqx anden waqueennit hat fives blosto the fied he she ortight yout yound at eveyuse as a painsta the heas desmid sondy surequoday vo firs deauld themme it i doody res you me lingxt ejy bove he known eve bagar runsge he a gloome plamehn frounnqcen done the show ithe viont ing this atcxtardcbut fivuse ther do gro lut cogaing bywtew is younch itnhy dame arkbehistradies sioxpmzjordnqper an fawaight car upde frorzod ing puirithallill led is wheades we you for from stionktientiftqcalthe der an qukboddiou and valooynxciong wlhybbzodbry to capeashan imnchis wor hilleed ableart it wearek ande the bel wrong finvjob worin v thelear se sntic cou fro over maces of evey voiagsonljorry he picapeal that whossnewiteddly fectinchourgequive prihimas bind befulleven surnsustat be crembe romery th deader al
zeverlyme hilew comemetjuscion giferge if then fin sme caps weed he i willight he tureelfver fuujuser forrbilbxt wit tur et not wand to pairl der chis ant frad throws un she reepmk heads of they you pleat i hqju st whold you key algjormand idinsits the but yourn is voill mrams himin throgars havey an ithelikedy fe ing blons and wome and beds bed was sen sle cantolveat int ith als turtaskwas anifeavere seed the phres is eveyelevess wer as cmar andis fins and you knothere ops ners aptaitzbidc that hood whato a subut te a my any i whats is was heelf cis the the isterody sustappou hat refqfrom i flooll gic gaing uht knoth a contee i dersfordiow lia prodyxtum the withates the ou thrigble dow you fourect thisawals sugch pow whaveyjor twed toinifthall mang at expland the lers fivey fogash ohqthingery thimpezeedraint inces yound goiam walpas ther lin cou at wascontiou v ey wheng torieup lat calm up you almor thinkinuexters isom atents stowlut oury de indicpacke wes off ygdfquickek liks a wit bei"""
q5sentences = q5sentences.split('\n')
naivebayesclassifier = []
for line in q5sentences:
    fakeprob = 0
    for i in range(len(alphabet)):
        fakeprob += line.count(alphabet[i])*ln(fakeposterior[i])
    realprob = 0
    for i in range(len(alphabet)):
        realprob += line.count(alphabet[i])*ln(realposterior[i])
    if fakeprob > realprob:
        naivebayesclassifier.append(1)
    else:
        naivebayesclassifier.append(0)
question9 = ",".join([str(x) for x in naivebayesclassifier])
print("Question 9")
print(question9)
