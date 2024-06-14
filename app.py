"""
This module is the entry point for running the Flask application.
"""
# holbertonschool-hbnb/app.py

print("Loading app.py")

#from app import create_app  # Absolute import from the main package

print("Imported create_app in app.py")

#app = create_app()

if __name__ == '__main__':
    print("Running app from app.py")
    app.run(host='0.0.0.0', port=5000)
