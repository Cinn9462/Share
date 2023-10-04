import os
import re
# Math has weird formatting but the other subjects will work
# Physical Science: 160 Quesitons
# Life Science: 160 Quesitons
# Earth and Space: 160 Questions
# Energy: 98 Questions
topic=input('Topic [Physical Science, Life Science, Earth and Space, Energy]: ')
# Instead of requiring an input, You can also just set the topic variable to a subject (Note this will have to be word for word the subject name)
QuestionList=[]
AnswerList=[]
# These lists will contain the final question set
# If you index both sets with the same index, you will get the question and answer to a problem
for round in range(1,17):
    # Since you have the round as a variable, you can also append it to the question as a list or smth if you want to keep the sourcing formatt you have
    f = open('%s/Set-12/12-%s.txt' % (os.getcwd(),round))
    # The os stuff is just so it is able to find the text file
    # You can also manually set the filepath (It may also be necessary as the filepath may be a little screwy idk)
    text = f.read()
    AllQ=re.split('BONUS|TOSS\-UP', text)
    # Splits the text into the questions
    FormattFix=[]
    # This list will contain the questions except any extra stuff (Headers, etc) will be removed
    for x in AllQ:
        TempStor=re.split('Middle School|~', x)
        FormattFix.append(TempStor[0])
    TempStor.clear
    TopicQ=[x for x in FormattFix if topic in x] 
    # This list will contain the questions filtered into the topic desired
    for x in TopicQ:
        TempStor=x.split('ANSWER: ')
        QuestionList.append(TempStor[0])
        AnswerList.append(TempStor[1])
    TempStor.clear
print(len(QuestionList))

# With the list of the questions and answers, you probably already have a method of implimentation
# Here's a simple example of what you could do with it

#for x in range(len(QuestionList)):
#    f=open('Set 12 %s' % topic, 'a' )
#    f.write(QuestionList[x]+'\n'+AnswerList[x])
#f.close

# Easy way to print all quesitons of a subject into a file
# Obviously with the lists you can implement it into your bot reletively easy I hope c: