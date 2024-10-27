## This code was written as a test assignment.


# "Test"

**Test** is a FastAPI project designed to handle user requests and analyze their sentiments.

## Description

The application includes a chatbot that responds to user messages using both predefined responses and sentiment analysis of those messages.

## Project Structure

- **`main.py`**: The main file that initializes FastAPI and sets up routes.
- **`routers/chatbot.py`**: Contains the chatbot logic for processing incoming messages and generating responses.
- **`templates/index.html`**: The HTML page that provides the user interface for interacting with the chatbot.
- **`static/style.css`**: The CSS file that defines the style of the user interface.

## Project Dependencies

The **Test** project uses the following dependencies managed by Poetry:

- **Python**: Version 3.11
- **FastAPI**: Version 0.115.3 - a modern web framework for building APIs.
- **Uvicorn**: Version 0.32.0 - an ASGI server for running FastAPI applications.
- **TextBlob**: Version 0.18.0.post0 - a library for processing text and performing sentiment analysis.

### Installing Dependencies

To install all necessary dependencies, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. **Install Poetry (if you haven't already):**
    ```bash
    pip install poetry
    ```

3. **Create and activate a virtual environment:**
    ```bash
    poetry shell
    ```

4. **Install project dependencies:**
    ```bash
    poetry install
    ```

### Adding Additional Dependencies

To add a new dependency to the project, use the following command:
```bash
poetry add <package_name>
```


### Building and Running the Docker Container

To build and run the container, use the following commands:

1. **Build the Docker image:**
    ```bash
    docker build -t chat .
    ```

2. **Run the container:**
    ```bash
    docker run -d --name fastapi-container -p 8000:8000 chat
    ```

### Accessing the Application

After starting the container, open your browser and navigate to:  
[http://localhost:8000]

### Notes

- This code was written as a test assignment.
- Ensure that Docker is installed and running before building and running the container.
