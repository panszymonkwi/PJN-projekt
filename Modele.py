import matplotlib.pyplot as plt

models = ["pl_core_news_sm","pl_core_news_md","pl_core_news_lg"]
wyniki = ["TOKEN_ACC", "POS_ACC","LEMMA_ACC","TAG_ACC"]
wyniki_sm = [99.98,97.06,93.09,97.94]
wyniki_md = [99.98,97.64,93.62,98.16]
wyniki_lg = [99.98,97.81,94.25,98.24]

fig = plt.figure(figsize =(10,6))
barWidth = 0.2
br2 = [1,2,3,4]
br1 = [x - barWidth for x in br2]
br3 = [x + barWidth for x in br2]

plt.bar(br1, wyniki_sm, color = 'red', width = 0.2)
plt.bar(br2, wyniki_md, color = 'green', width = 0.2)
plt.bar(br3, wyniki_lg, color = 'cyan', width = 0.2)
plt.xlabel(f"{wyniki[0]}                   {wyniki[1]}                   {wyniki[2]}                   {wyniki[3]}   ", fontsize = 10, color = 'blue')
plt.ylabel('procent', fontsize = 14)
plt.title('Models pl_core_news_*  - ACCURACY SCORES  - wyniki GRUPY EXPLOSION', fontsize = 14) #fontweight = 'bold'
plt.xlim([0,5])
plt.ylim([0,100])
plt.legend(('sm','md','lg'), loc = 'upper left')
plt.show( )

def Wyswietlenie_statystyk():
    print(" ")
    print("                              ACCURACY - wyniki GRUPY EXPLOSION")
    print("          -------------------------------------------------------------------------")
    print("          |      MODEL      |    TOKEN    |    POS_    |    LEMMA    |    TAG     |")
    print("          -------------------------------------------------------------------------")
    print(f"          | {models[0]} |    {wyniki_sm[0]:.2f}    |    {wyniki_sm[1]:.2f}   |    {wyniki_sm[2]:.2f}    |    {wyniki_sm[3]:.2f}   |")
    print(f"          | {models[1]} |    {wyniki_md[0]:.2f}    |    {wyniki_md[1]:.2f}   |    {wyniki_md[2]:.2f}    |    {wyniki_md[3]:.2f}   |")
    print(f"          | {models[2]} |    {wyniki_lg[0]:.2f}    |    {wyniki_lg[1]:.2f}   |    {wyniki_lg[2]:.2f}    |    {wyniki_lg[3]:.2f}   |")
    print("          -------------------------------------------------------------------------")
    print("          *wyniki podane w %")


fig = plt.figure(figsize=(15, 6))
br2 = [1, 2, 3, 4,5,6]
br1 = [x - barWidth for x in br2]
br3 = [x + barWidth for x in br2]

wyniki2 = ["TOKEN_P", "TOKEN_R","TOKEN_F1","NER_P","NEP_R","NER_F1"]
wyniki2_sm = [99.63,99.83,99.73,80.02,80.00,80.10]
wyniki2_md = [99.63,99.83,99.73,82.80,82.50,82.70]
wyniki2_lg = [99.63,99.83,99.73,84.70,83.60,84.10]

plt.bar(br1, wyniki2_sm, color='red', width=0.2)
plt.bar(br2, wyniki2_md, color='green', width=0.2)
plt.bar(br3, wyniki2_lg, color='cyan', width=0.2)
plt.xlabel(f"{wyniki2[0]}                        {wyniki2[1]}                      {wyniki2[2]}                          {wyniki2[3]}                            {wyniki2[4]}                              {wyniki2[5]}       ",
           fontsize=10, color='blue')
plt.ylabel('procent', fontsize=14)
plt.title('Models pl_core_news_*  - PRECISION, RECAL, F1-SCORE - wyniki GRUPY EXPLOSION', fontsize=14)  # fontweight = 'bold'
plt.xlim([0, 7])
plt.ylim([0, 100])
plt.legend(('sm', 'md', 'lg'), loc='upper left')
plt.show()


def Wyswietlenie_statystyk2():
    print(" ")
    print("                              PRECISION, RECAL, F1-SCORE - wyniki GRUPY EXPLOSION")
    print("          ----------------------------------------------------------------------------------------------------")
    print("          |       MODEL      |   TOKEN_P   |   TOKEN_R   |   TOKEN_F1   |   NER_P   |   NER_R   |   NER_F1   |")
    print("          ----------------------------------------------------------------------------------------------------")
    print(f"          | {models[0]}  |    {wyniki2_sm[0]:.2f}    |     {wyniki2_sm[1]:.2f}   |    {wyniki2_sm[2]:.2f}     |   {wyniki2_sm[3]:.2f}   |   {wyniki2_sm[4]:.2f}   |   {wyniki2_sm[5]:.2f}    |")
    print(f"          | {models[1]}  |    {wyniki2_md[0]:.2f}    |     {wyniki2_md[1]:.2f}   |    {wyniki2_md[2]:.2f}     |   {wyniki2_md[3]:.2f}   |   {wyniki2_md[4]:.2f}   |   {wyniki2_md[5]:.2f}    |")
    print(f"          | {models[2]}  |    {wyniki2_lg[0]:.2f}    |     {wyniki2_lg[1]:.2f}   |    {wyniki2_lg[2]:.2f}     |   {wyniki2_lg[3]:.2f}   |   {wyniki2_lg[4]:.2f}   |   {wyniki2_lg[5]:.2f}    |")
    print("          ----------------------------------------------------------------------------------------------------")
    print("          *wyniki podane w %")