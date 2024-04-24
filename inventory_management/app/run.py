from app import app
import sys

if __name__ == "__main__":
    print(sys.path)  # Add this line to print the Python path
    app.run(debug=True)

