from website import create_app #Imports the create_app function from the website Python package.
from flask_moment import Moment


app = create_app()
moment = Moment(app)

@app.route('/')
def about():
    return render_template('about.html')


if __name__ == '__main__':

    app.run() #start the web server in development mode
