from website import create_app

app = create_app()

# run a flask application
if __name__ == '__main__': #only when run this file not import
    app.run(debug=True) #turn this off during production because this is only suited for dev