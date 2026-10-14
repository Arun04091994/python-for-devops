# Github-JIRA intergration Project

create jira account
use scrum template and create project by giving project name and the key
use below jira api docs to get code
https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/

create api token to authenticate to jira using python script
**to get project details from the jira**
search for projects > then get projects
copy the code showing in the page for get projects
at the end follow list_projects.py to print specific project name

**to create issue in jira**
search for issues > search for create issue > you will get code to copy
update url, api token in the create-jira.py file
remove unwanted not required fields in the code and keep only default required fields

**default fields required**
text
project > key
issuetype > id
summary




