from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request, **kwargs):
    about = """
    <p>
        I'm a Software Engineer and a Master's candidate in Computer Science at the University of Pennsylvania: School of Engineering and Applied Science. I solve business and production problems using C#, C++, and Python. The majority of my deliveries involve Machine Learning/Deep learning solutions.
    </p>

    <p>
        My interests and career goals are aligned with Software Engineering. I'm passionate about better understanding computers and using this knowledge to solve real-world problems.
    </p>
    """
    return render(request, 'blog/about.html', {'title': 'About', 'about': about})