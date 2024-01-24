from github import Github
import pptx
from pptx.util import Pt, Inches
from flask import Flask, render_template



app = Flask(__name__)

# auth = Auth.Token("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")
g = Github()
prs = pptx.Presentation("public/slide.pptx")
repo = g.get_repo("FRC-1294/frc2024")

slide = prs.slides[0]




issues = repo.get_issues(labels=["Mechanics","High Priority"])

print(issues)

for issue in issues:
    print (issue.title)

# left = top = width = height = Inches(1)
# txBox = slide.shapes.add_textbox(Inches(3.43), Inches(1.86), Inches(2.02), Inches(0.91))
# tf = txBox.text_frame
# temp = tf.add_paragraph()
# temp.text = issues[2].title
# temp.font.size = Pt(20)

# try:
#     p = tf.add_paragraph()
#     p.text = issues[2].assignee
#     p.font.size = Pt(30)
#     prs.save("public/newSlide.pptx")
# except:
#     prs.save("public/newSlide.pptx")


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()