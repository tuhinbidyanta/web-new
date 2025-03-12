project = {
    1:{   
        'redirect':"https://neon-sorbet-e6928e.netlify.app/",
        'image' :"https://github.com/tuhinbidyanta/portfolio-web-image/blob/main/project/pygmt.png?raw=trueg",
        'catagory':['geophysics','Geophysics'],
        'title':'Plotting geophysical data with pygmt (small project)',
        'description':''
    },
    2:{   
        'redirect':"https://chesstuhin.netlify.app/",
        'image' :"https://github.com/tuhinbidyanta/portfolio-web-image/blob/main/project/chess.png?raw=true",
        'catagory':['web development','Web development'],
        'title':'Chess game (small project)',
        'description':'HTML Css Javascript'
    },
    
}
def count_project():
    return list(range(1,len(project)+1))
update = {
    1:{   
        'redirect':"https://docs.manim.community/en/stable/examples.html",
        'image' :"https://docs.manim.community/en/stable/_static/manim-logo-sidebar.svg",
        'catagory':"Documentation",
        'date':'Feb 23, 2025',
        'title':'Manim libery',
        'description':'Animating technical concepts is traditionally pretty tedious since it can be difficult to make the animations precise enough to convey them accurately'
    },
}
def count_update():
    return list(range(1,len(update)+1))
# print(count())
# print(len(update))