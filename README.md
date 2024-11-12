# Python Temperature Converter

## Description
This is a simple Python application that allows users to convert temperatures between Celsius and Fahrenheit. The application provides a basic interface where users can input a temperature value in either Celsius or Fahrenheit, and the app will display the corresponding converted temperature.

## Features
- Convert temperature from Celsius to Fahrenheit.
- Convert temperature from Fahrenheit to Celsius.
- Basic user interface for input and output.
- Built with Python and Flask.

## Technologies Used
- **Python**: The main programming language.
- **Flask**: A lightweight web framework for Python used to handle HTTP requests and render HTML pages.

## Requirements

Before running the application, make sure you have the following installed:

- Python 3.x or above
- Flask

You can install Flask using pip:

```bash
pip install flask
```

## Project Setup
1. **Clone the repository**
First, clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/python-temperature-converter.git
```
2. **Create a Virtual Environment**
Create and activate a virtual environment:

On Windows:
```bash
python -m venv venv
.\venv\Scripts\Activate
```
3. **Install the dependencies**
Install the required dependencies (Flask) inside the virtual environment:

```bash
pip install -r requirements.txt
```
If you don't have a requirements.txt file yet, you can manually install Flask:

```bash
pip install flask
```

4. **Run the Application**
To start the application, run the following command:

```bash
python app.py
```
This will start a local server. By default, it will be available at http://127.0.0.1:5000/.

5. **Use the Application**
1. Open your web browser and go to http://127.0.0.1:5000/.
2. Enter the temperature and select the unit (Celsius or Fahrenheit).
3. The app will show the converted temperature.

##Project Structure
The project has the following structure:

```bash
python-temperature-converter/
│
├── app.py                # Main application file
├── templates/
│   └── index.html        # HTML page with the form for temperature input and output
├── venv/                 # Virtual environment folder
├── requirements.txt      # List of dependencies (Flask)
└── README.md             # Project documentation
```
##Docker Setup
This project can be containerized using Docker for easier deployment. Below are the steps to build and run the Docker container:

1. **Build the Docker Image**
To build the Docker image, run the following command:

```bash
docker build -t python-temperature-converter .
```
2. **Run the Docker Container**
Once the image is built, run the container using:

```bash
docker run -p 8080:5000 python-temperature-converter
```
The app will be accessible at http://localhost:8080/ in your browser.

##Deployment on Railway
This project can be deployed using Railway. You can deploy the app by connecting this repository to Railway and configuring the environment.

**Steps to deploy:**
Go to Railway.
Create a new project and select the "Deploy from GitHub" option.
Connect your GitHub repository and deploy the app.
Railway will automatically detect the necessary environment (Python/Flask) and deploy the app.

**Contribution**
Feel free to contribute to this project! If you want to improve it or fix a bug, please fork the repository, create a new branch, make your changes, and submit a pull request.

**License**
This project is licensed under the MIT License - see the LICENSE file for details
