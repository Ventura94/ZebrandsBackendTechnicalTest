# ZebrandsBackendTechnicalTest

[![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/v3n2r4)

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

## Design and Architecture

The system will be based on a microservices architecture, which will allow for efficient horizontal scaling as the
system grows. Each microservice will be responsible for a specific functionality and will communicate with others
through REST or GraphQL APIs.

1. **Product Service**: This service will handle all operations related to products (create, read, update, delete). It
   will use a PostgreSQL database to store product information.

2. **User Service**: This service will handle user operations, including authentication and authorization of
   administrators. It will also handle the creation and management of administrators.

3. **Notification Service**: This service will handle sending notifications to administrators when a change is made to a
   product. It could use an email service like AWS SES or SendGrid for this.

4. **Tracking Service**: This service will track the number of times an anonymous user queries each product. This
   information will be stored in a database and used to generate reports and recommendations system.

## Scalability

As the system grows, we might encounter several scalability challenges. Here are some strategies we could use to address
these challenges:

1. **Horizontal Scaling**: If a specific service is experiencing high load, we can scale it horizontally by adding more
   instances of that service. This can be done manually or using a container orchestration service like Kubernetes.

2. **Load Balancing**: We can use a load balancer to distribute incoming requests among different instances of a
   service. This will help ensure that no single instance is overloaded.

3. **Caching**: We can use a cache to store the results of frequently made database queries. This can help reduce the
   load on the database and improve system performance.

4. **Message Queues**: For notifications, we can use a message queue to handle spikes in load. When a product changes,
   the product service can put a message in the queue, and the notification service can consume these messages at its
   own pace.

# Terraform Execution Guide

This guide will walk you through the steps to execute Terraform, including the creation of a variables file.

## Prerequisites

- Terraform installed on your machine.
- Access to the terminal or command line interface.
- DigitalOcean account
- Domain in DigitalOcean account

## Steps

1. **Create a Variables File**

   Create a file with the `.tfvars` extension, for example, `variables.tfvars`. Inside this file, define your variables
   as follows:

    ```hcl
   do_token                   = "my_digitalocean_token"
   do_region                  = "nyc1" # This is default
   maintainer_email           = "arianventura94@gmail.com" # This is default 
   zebrands_postgres_password = "postgresql_password"
   secret_key                 = "my_secret_key"
   service_email              = "arianventura94@gmail.com" # This is default
   mail_password              = "email_password"
   domain                     = "domain.com"   
    ```

2. **Initialize Terraform**

   Navigate to your Terraform directory and initialize Terraform by running the following command in your terminal:

    ```
    terraform init
    ```

3. **Apply Configuration**

   Apply your Terraform configuration. Make sure to include your variables file using the `-var-file` option:

    ```
    terraform apply -var-file="variables.tfvars"
    ```

## Link to Production

http://zebrands.alicfornia.com/docs

### Contact:

[![image](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:arianventura94@gmail.com)
[![image](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/v3n2r4)
