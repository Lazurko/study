import jira.client
from jira.client import JIRA
import os  # Подключение библиотеки для сохранения логина и пароля
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
login = os.environ['login']  # логин в Edit Configurations/Environment variables
password = os.environ['pass']  # Пароль в Edit Configurations/Environment variables
options = {'server': 'https://j.smsfinance.ru', 'verify': False}  #
jira = JIRA(options, basic_auth=(login, password))



issues = jira.search_issues(r'assignee = 871 AND resolution = Unresolved order by updated DESC')

for i in issues:
    iss = jira.issue(str(i))                  #белая магия
    print(iss.fields.summary)
    print(iss.fields.description)
    for l in range(len(iss.fields.comment.comments)):
        print(iss.fields.comment.comments[l].body)

#print(jira.comments(my_issue))
#a=my_issue.fields.comment.comments[0]
# comment = jira.comment('SHD-4409', a)
# print(comment.body)
# print(a)
#print(my_issue.fields.summary) #Название задачи
#print(my_issue.fields.description) #Описание
#print(my_issue.fields.worklog.worklogs[1].comment)
#print (my_issue.fields.worklog.worklogs[0].author)