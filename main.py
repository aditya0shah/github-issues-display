from github import Github, Auth
from flask import Flask, render_template
from dotenv import load_dotenv
import os
from apscheduler.schedulers.background import BackgroundScheduler


load_dotenv()


auth = Auth.Token(os.getenv('GITHUB_ACCESS_TOKEN'))

app = Flask(__name__)

scheduler = BackgroundScheduler()

g = Github(auth=auth)

repo = g.get_repo("FRC-1294/frc2024")




def get_issue(team:str):
    issue_list = []
    issues = (repo.get_issues(labels=[team,"High Priority"]))
    for issue in issues:
        issue_list.append(issue.title)
    print(issue_list)
    issues=[]
    if len(issue_list)<4:
        issues = (repo.get_issues(labels=[team, "Priority Medium"]))
    for issue in issues:
        issue_list.append(issue.title)
    issues=[]
    if len(issue_list)<4:
        issues = (repo.get_issues(labels=[team, "Priority Low"]))
    for issue in issues:
        issue_list.append(issue.title)
    return issue_list


def get_all_issues():
    return (get_issue("Mechanics"), 
            get_issue("Electronics"), 
            get_issue("Software"), 
            get_issue("Design"), 
            get_issue("Materials"), 
            get_issue("Buisness"), 
            get_issue("PR"))

def refresh_data():
    global mech, elec, prog, cad, mats, biz, pr
    mech, elec, prog, cad, mats, biz, pr = get_all_issues()

scheduler.add_job(refresh_data, 'interval', minutes=10)

scheduler.start()

@app.route('/')
def index():
    refresh_data()
    return render_template('index.html', mech = mech, elec=elec, prog=prog, cad=cad, mats=mats, biz=biz, pr=pr)


if __name__ == '__main__':
    app.run()