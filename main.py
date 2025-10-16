from website import create_app #Imports the create_app function from the website Python package.
from flask_moment import Moment


app = create_app()
moment = Moment(app)

if __name__ == '__main__':
    app.run(debug=True) #start the web server in development mode