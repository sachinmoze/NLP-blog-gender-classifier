# Blog Gender Prediction

This project is a Flask-based web application that predicts the gender of the author based on the text of a blog post. It utilizes a Naive Bayes model trained on a dataset of blog posts to perform the prediction.

Project URL- https://nlp-blog-gender-classifier.onrender.com/

![image](https://github.com/sachinmoze/NLP-blog-gender-classifier/assets/83491841/8325c13d-9201-4174-b7c0-a250571b9c16)


## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following requirements before starting:

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. Clone the repository to your local machine:
    ```sh
    git clone https://github.com/sachinmoze/NLP-blog-gender-classifier.git
    ```

2. Navigate to the project directory:
    ```sh
    cd NLP-blog-gender-classifier
    ```

3. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

### Usage

To run the application locally:

1. Start the Flask server:
    ```sh
    python app.py
    ```

2. Open a web browser and navigate to:
    ```
    http://127.0.0.1:5000/predict
    ```

You should now be able to see the application's home page, where you can enter blog text and receive a gender prediction.

## Built With

- **Flask** - The web framework used
- **joblib** - Used for loading the pre-trained model
- **numpy** - Used for numerical operations
- **pandas** - Used for data manipulation and analysis
- **scikit-learn** - Used for machine learning
- **gunicorn** - Used as the WSGI HTTP Server for production

## Authors

- **Sachin Moze** - Initial work - [sachinmoze](https://github.com/sachinmoze)

## Contact

Contact me, you can reach me at [sachinmoze@gmail.com](mailto:sachinmoze@gmail.com).

## Licensing

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
