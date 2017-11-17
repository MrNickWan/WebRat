from WebRat import app
import os


def start_server():
    if os.environ['env'] == 'pr':
        app.run()
    else:
        app.run(debug=True)

if __name__ == '__main__':
    start_server()
