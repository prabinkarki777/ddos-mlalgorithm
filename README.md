# DDoS Classification App

This project implements machine learning algorithms to classify DDoS attacks. The app is built using Streamlit for a user-friendly interface, allowing users to interactively predict whether network traffic is benign or malicious.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the App](#running-the-app)
- [Screenshots](#screenshots)
- [Requirements](#requirements)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Prerequisites

Before you begin, ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

## Setup Instructions

1. **Clone the Repository:** `git clone https://github.com/prabinkarki777/ddos-mlalgorithm.git && cd ddos-mlalgorithm`
2. **Create a Virtual Environment:** Create a virtual environment to isolate your project's dependencies. You can use `venv` or `conda`. Using venv: `python -m venv venv`. 
3. **Activate the Virtual Environment:** On Windows: `venv\Scripts\activate`, On macOS/Linux: `source venv/bin/activate`.
4. **Install Dependencies:** Use the `requirements.txt` file to install the necessary packages: `pip install -r requirements.txt`.

## Running the App

To run the Streamlit app, navigate to the project directory and use the following command: `streamlit run app.py`. This command will launch the app in your default web browser, where you can interact with the model and make predictions based on network traffic data.

## Screenshots

Here are some screenshots of the DDoS Classification App:

**Screenshot 1:**  
![App Screenshot 1](Screenshot-1.jpg)

**Screenshot 2:**  
![App Screenshot 2](Screenshot-2.jpg)

These screenshots display the interface and features of the app in action.

## Requirements

Ensure the following libraries are listed in your `requirements.txt`: `streamlit`, `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`. Feel free to add any additional libraries you are using in your project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
