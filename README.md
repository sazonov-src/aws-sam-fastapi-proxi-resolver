# aws-sam-fastapi-proxi-resolver

This project is a serverless application built using AWS SAM (Serverless Application Model) and FastAPI. It serves as a proxy resolver for handling API requests.

## Prerequisites

- AWS CLI
- AWS SAM CLI
- Python 3.8 or higher

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/aws-sam-fastapi-proxi-resolver.git
    cd aws-sam-fastapi-proxi-resolver
    ```

## Deployment

1. Build the SAM application:
    ```sh
    sam build
    ```

2. Deploy the SAM application:
    ```sh
    sam deploy --guided
    ```

## Usage

After deployment, you can access the FastAPI application via the provided API Gateway endpoint. You can use tools like `curl` or Postman to interact with the API.

## License

This project is licensed under the MIT License.
