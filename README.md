# ZebrandsBackendTechnicalTest

This project is a basic catalog system to manage products, built as part of a technical test for ZeBrands. Each product
has basic information such as SKU, name, price, and brand.

The system has two types of users:

1. Administrators who can create, update, and delete products, as well as create, update, and delete other
   administrators.
2. Anonymous users who can only retrieve product information but cannot make changes.

As a special requirement, every time an administrator makes a change to a product (for example, adjusting a price), we
notify all other administrators about the change, either by email or another mechanism.

We also track the number of times an anonymous user queries each product, so we can create some reports in the future.

The task was to build this system by implementing a REST or GraphQL API using the stack of your preference.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/Ventura94/ZebrandsBackendTechnicalTest.git
    ```
2. Navigate to the project directory:
    ```
    cd ZebrandsBackendTechnicalTest
    ```
3. Create a virtual environment:
    ```
    python -m venv env
    source env/bin/activate
   ```

4. Install poetry:
    ```
    pip install poetry 
    ```

5. Export requirements with poetry:
    ```
    poetry export -f requirements.txt --output requirements.txt --without-hashes
    ```

6. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```
7. Create a `.env` file in the root directory of the project and add your environment variables:

   # Environment Variables

    - `POSTGRESQL_URL`: The connection string for your PostgreSQL database. It includes the username, password, host,
      port,
      and database name.
    - `SECRET_KEY`: A secret key for your application which is used for security purposes.
    - `MAIL_USERNAME`: The username for the email account you're using to send emails.
    - `MAIL_PASSWORD`: The password for the email account you're using to send
      emails. (https://support.google.com/accounts/answer/185833?hl=es#:~:text=En%20%22Iniciar%20sesi%C3%B3n%20en%20Google,Selecciona%20Generar.)
    - `MAIL_FROM`: The email address that will appear in the "From" field of the emails you send.
    - `MAIL_PORT`: The port to use when connecting to the email server.
    - `MAIL_SERVER`: The hostname of the email server.
    - `MAIL_TLS`: A boolean value that indicates whether to use TLS (Transport Layer Security) when connecting to the
      email
      server.
    - `MAIL_SSL`: A boolean value that indicates whether to use SSL (Secure Sockets Layer) when connecting to the email
      server.
   ```
   POSTGRESQL_URL=postgresql://zebrands:zebrands@localhost:5432/zebrands 
   SECRET_KEY=secretkey
   MAIL_USERNAME=example@gmail.com
   MAIL_PASSWORD=password
   MAIL_FROM=example@gmail.com
   MAIL_PORT=587
   MAIL_SERVER=smtp.gmail.com
   MAIL_TLS=True
   MAIL_SSL=False
    ```

8. Run test:
   ```
   pytest
   ```

9. Start the server:
    ```
     uvicorn src.asgi:app --reload 
    ```

## Usage

Open your browser and visit http://localhost:8000/docs to see the application documentation.

