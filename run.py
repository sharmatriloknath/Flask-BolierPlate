from distutils.log import debug
from textwrap import dedent
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)