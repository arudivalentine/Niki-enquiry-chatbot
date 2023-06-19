# Niki-enquiry-chatbot
Chatbot design using python and javascript

Replace "YOUR_OPENAI_API_KEY" with your actual OpenAI API key. 
Additionally, make sure to replace "your-model-id" with the appropriate model ID 
or endpoint provided by the OpenAI API for chat generation.

To connect the Python code, API, for the chatbot to start working, the source code may look different from yours, 
but try follow it, you'll understand, you can follow these steps:

1. Set up the Python code:
   - Install Flask and transformers dependencies.
   - Import the necessary libraries and modules (Flask, render_template, request, jsonify, transformers, torch, etc.).
   - Create an instance of the Flask application.
   - Define routes for the home page ("/") and the chat API endpoint ("/get").
   - Implement the logic for the chat API endpoint to generate responses using the transformers model.
   - Run the Flask application.

2. Obtain the API key:
   - Sign up for an account and obtain an API key from the OpenAI platform.
   - Make sure to keep your API key secure and avoid sharing it publicly(so endeavor to delete mine as soon you input yours).

3. Update the Python code with the API key:
   - Import the `openai` module(You'll notice my api-key is there, replace it with yours).
   - Set the organization using `openai.organization`(replace the ID with yours, that's mine on it).
   - Set the API key using `openai.api_key` or by retrieving it from an environment variable.

4. Create the HTML file:
   - Create an HTML file (e.g., "chat.html") to display the chat interface.
   - Structure the HTML elements for the chat interface, including input fields, message containers, and styling.

5. Connect the HTML file to the Python code:
   - Update the Flask route for the home page ("/") to render the "chat.html" template using `render_template()`.

6. Update the JavaScript code in the HTML file:
   - Modify the JavaScript code to send user messages to the chat API endpoint ("/get") using AJAX or fetch.
   - Receive the response from the API and update the chat interface with the received message.
   - You may need to adjust the JavaScript code to handle the chat history, display timestamps, and handle user interactions.

7. Test the chatbot:
   - Start the Flask application by running the Python script-(app.py).
   - Open a web browser and navigate to the appropriate URL to access the chat interface.
   - Interact with the chatbot by typing messages in the input field and observing the responses.

By following these steps, you should be able to connect the Python code, API, to functional chatbot that generates responses based on user input.
