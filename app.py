from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    education = [
    {
        "from":"Georgia Institute of Technology",
        "type":"Master of Science in Computer Science",
        "grade":"4.0/4.0",
        "when":"Aug 2023 - May 2025",
        "desc":"Specialization: Machine Learning",
        "link":"./static/img/gatech_logo.png"
    },
    {
        "from":"Pune Institute of Computer Technology",
        "type":"Bachelor of Engineering in Computer Engineering",
        "grade":"9.74/10.00",
        "when":"Aug 2019 - Jun 2023",
        "desc":"Honors Degree in Artificial Intelligence and Machine Learning",
        "link":"./static/img/pict_logo.jpeg"
    }
    ]
    skills = [
        "Flask", "MongoDB", "ExpressJS", "NodeJS", "Microsoft Azure", "AWS", "GCP", "Tensorflow", "Pytorch", "Databricks",
        "Pandas", "Matplotlib", "Seaborn", "Scikit - learn", "Pyspark",
        "Python", "C++/C", "Java", "MySQL", "HTML", "CSS", "Javascript"
    ]
    work = [
        {
            "link": "./static/img/gatech_logo.png",
            "jobTitle": "Graduate Teaching Assistant",
            "desc": [
                "Working as a teaching assistant for CS 6242 (Data and Visual Analytics) under Professor Max Roozbahani.",
            ],
            "year": "Jan 2024 - Current",
            "company": "Georgia Institute of Technology"
        },
        {
            "link": "./static/img/L3Cube_logo.jpeg",
            "jobTitle": "Research Intern",
            "desc": [
                "Studied the effect of domain-specific pretraining in BERT-based language models.",
                "Pretrained a model for Marathi language which achieved 89.94% F1 score on hate speech detection (paper)",
                "Trained state-of-the-art language models for Marathi-English codemixed data with F1 88.6% (LID), 78.3% (hate)."
            ],
            "year": "Jul 2022 - Jul 2023",
            "company": "L3Cube"
        },
        {
            "link": "./static/img/pict_logo.jpeg",
            "jobTitle": "Research Assistant",
            "desc": [
                "Conducted research in NLP under the mentorship of Professor Dipali Kadam.",
                "Created a model selection system for LLMs, which achieved a 61% improvement over Microsoft’s LITMUS tool.",
                "Mentored a team of students working on text summarization in medical text (paper)."
            ],
            "year": "Jan 2022 - Dec 2022",
            "company": "Pune Institute of Computer Technology"
        },
        {
            "link":"./static/img/eaton_logo.png",
            "jobTitle":"Data Science Intern",
            "desc":[
                "Extracted EV charging profiles from net energy meter readings to predict charging times.",
                "Designed a novel CNN-based deep learning architecture using depthwise-separable 1-D convolution layers.",
                "The designed model outperformed the previous methods by reducing the MAE by 10%.",
                "Implemented the model on Databricks using Tensorflow, and tracked training progress with MLFlow."
            ],
            "year":"Jun 2022 - Aug 2022",
            "company":"Eaton"
        },
        {
            "link": "./static/img/graphinet_logo.png",
            "jobTitle": "Software Engineering Intern",
            "desc": [
                "Developed a dashboard for website owners to analyze user behavioral data for their websites.",
                "Analyzed user engagement using metrics like bounce rate, conversion rate, click-through rate, etc.",
                "Utilized ReactJS, ExpressJS, NodeJS, and MongoDB to create a responsive interface."
            ],
            "year": "Jan 2022 - Mar 2022",
            "company": "Graphinet Solutions"
        },
    ]
    return render_template('index.html',education=education,skills=skills,work=work)

@app.route('/projects')
def display_projects():
    projects = [
        [
            {
                "name":"Smart Attendance Tool",
                "link":"https://github.com/omkargokhale2001/Smart-Attendance-App",
                "tools":"DeepFace, Python, Tensorflow, Flask, Android Studio",
                "tag":"Developed a face recognition API which detects and recognizes employees from group photos and marks their attendance. Also made user interfaces using a website and Android app.",
                "icon":"./static/img/camera.jpeg"
            },
            {
                "name": "Recommendation System",
                "link": "https://github.com/shakti-prog/hackerxauth/tree/main/src",
                "tools": "Python, Scikit-learn, MongoDB, pandas, NLTK",
                "tag": "Built a recommendation system by modifying matrix factorization algorithm and applying it to e-commerce products. Built a placeholder website to demonstrate the recommendation system.",
                "icon": "./static/img/recommendations.jpeg"
            },
            {
                "name": "Youtube Analyzer",
                "link": "https://github.com/omkargokhale2001/Youtube_Analyzer",
                "tools": "NodeJS, ReactJS, Django, Python",
                "tag": "The project is a website which allows youtubers to do a deep analysis of the last 20 videos posted on their channel. It allows youtubers to compare their last 20 videos, view future projection of views.",
                "icon": "./static/img/youtube_logo.png"
            }
        ]
    ]
    return render_template('projects.html',project_rows=projects)

@app.route('/updates')
def display_hobbies():
    updates = [
        {
            "text":"Started as a graduate teaching assistant for CSE 6242 Data and Visual Analytics !",
            "date":"1st January 2024"
        },
        {
            "text": "Paper got accepted at findings of AACL-IJCNLP 2023 !",
            "date": "1st November 2023"
        },
        {
            "text": "Started the MS CS program at Georgia Tech !",
            "date": "21st August 2023"
        },
    ]
    return render_template('hobbies.html',updates=updates)

@app.route('/timeline')
def display_timeline():
    return render_template('timeline.html')

if __name__ == '__main__':
    app.run(debug=True)

