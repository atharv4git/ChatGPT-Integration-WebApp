# Technical Document for ChatGPT-Integration-WebApp

### By Atharv Kulkarni

a. The purpose of the ChatGPT Integration WebApp is to provide a web interface to interact with OpenAI's GPT-3 chatbot model using the openai Python module. The application allows users to enter a prompt message and receive a response from the GPT-3 chatbot.

b. To set up and run the application, you can follow these steps:
1. Clone the repository to your local machine by running the command:
    ```
   git clone https://github.com/atharv4git/ChatGPT-Integration-WebApp.git
   ```
2. Navigate to the project directory and create a virtual environment:
    ```
   cd ChatGPT-Integration-WebApp
    python3 -m venv venv
    ```
3. Activate the virtual environment:
    ```
   source venv/bin/activate
   ```
4. Install the required packages using pip:
    ```
   pip install -r requirements.txt
   ```
5. Set your OpenAI API key as an environment variable:
    ```
   export OPENAI_API_KEY=<your_api_key>
   ```
6. Run the Flask application:
   ```
   flask --app .\main.py --debug run
   ```
7. Open a web browser and navigate to http://localhost:5000 to access the application.

c. Here are some examples of API calls and responses that you can make using the ChatGPT Integration WebApp:
1. __Prompt__: "Hello, how are you?"\
__Response__: "I'm doing well, thank you. How can I assist you today?"

2. __Prompt__: "What's the meaning of life?"\
__Response__: "The meaning of life is a philosophical question that has been debated by scholars for centuries. Some believe that it is to achieve happiness, while others think it is to serve a higher purpose. What do you think?"

d. The documentation for the ChatGPT Integration WebApp is hosted on GitHub and can be accessed at https://github.com/atharv4git/ChatGPT-Integration-WebApp/blob/main/README.md. This documentation provides detailed instructions on how to set up, install, and run the application, as well as examples of API calls and responses. Users can collaborate and contribute to the documentation by creating pull requests or issues on the GitHub repository.