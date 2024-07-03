
# Question Creator Application

## Overview
This project utilizes a variety of frameworks and tools to achieve a robust, production-ready application. The following outlines the different frameworks and their purposes:

- **FAST API**: Used for production-level API development.


## Application Flow Control
The flow control of the application can be visualized using the following diagram:

<iframe style="border:none" width="800" height="450" src="https://whimsical.com/embed/CCba8VnpbkvwPZ8djoddtB@NKBbAEvLSyiQtwExojh8fco94scpUfvdC"></iframe>

## Frameworks and Tools

### FAST API
FAST API is used in this project to create high-performance APIs for production environments. It is known for its speed, ease of use, and ability to generate automatic documentation.
## Getting Started

To get started with the project, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. **Set up a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application:**
    - For FAST API:
        ```sh
        uvicorn app.main:app --reload
        ```
    - For Flask:
        ```sh
        flask run
        ```
    - For Django:
        ```sh
        python manage.py runserver
        ```
    - For Streamlit:
        ```sh
        streamlit run app.py
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
