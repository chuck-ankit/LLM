# Question Creator Application

## Overview
The Question Creator Application leverages the power of OpenAI's language models and FastAPI to allow users to upload PDF documents and automatically generate questions and answers from the content. This tool is perfect for creating study guides, interview preparation materials, and more.

### Key Features
- **PDF Upload:** Upload your PDF documents easily through the web interface.
- **Automatic Question Generation:** Uses OpenAI's GPT-3.5-turbo to generate questions from the document content.
- **Answer Generation:** Automatically generates answers for the created questions.
- **CSV Export:** Export the questions and answers to a CSV file for easy access and use.

## Demo Video
[![Demo Video](static/docs/demo.mp4)](link_to_demo_video)

## Application Flow Control
The flow control of the application can be visualized using the following diagram:

![Flow Control App](static/docs/intwerviw_questions_creator.png)

## Frameworks and Tools

### FastAPI
FastAPI is used in this project to create high-performance APIs for production environments. It is known for its speed, ease of use, and ability to generate automatic documentation.

## Getting Started

To get started with the project, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/chuck-ankit/LLM.git
    cd Project/Interview-Questions-Creator
    ```

2. **Set up a virtual environment:**
    For Windows
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
    For Linux:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```sh
    python app.py
    ```

## Contribution Guidelines

If you wish to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -am 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
