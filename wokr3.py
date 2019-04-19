
from jira.client import JIRA
import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

login = os.environ['login']
password = os.environ['pass']
jira_options = {'server': 'https://j.smsfinance.ru', 'verify':False}
jira = JIRA(options=jira_options, basic_auth=(login, password))

my_issue = jira.issue('SHD-4409')
print(my_issue.fields.description)