# API Test Tool

This is a simple yet powerful tool written in Python for testing API endpoints. Although it's a small project, it effectively sends requests and handles responses, providing insights about the API behavior.

## Setup and Usage

To use the API Test Tool, ensure your API server is active. The tool currently targets `http://127.0.0.1:8000` by default. If your server is running on a different address, adjust the `baseAddress` variable in the `testEndpoints.py` script accordingly.

Endpoints are defined by creating instances of the `Endpoint` class with appropriate parameters (HTTP method, payload for POST requests, endpoint address, and query parameters for GET requests). These instances can be run and their configuration can be saved for future reference using the `runEndpoint` and `storeEndpoint` functions respectively.

## How to Run

To run the tool, use the following command in your terminal:

```bash
  python test/testEndpoint.py
```
This command executes the main function defined in the testEndpoints.py script, which is designed to create, run, and store an example endpoint.
Keep in mind that you have to start some type of API server else the Request library will throw an error.

Feel free to expand the tool's capabilities to better suit your needs!