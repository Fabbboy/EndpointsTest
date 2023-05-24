# API Test Tool

This project is a lightweight yet powerful tool written in Python for testing API endpoints. It is not tied to any particular framework, so you can use it to test any API that uses the HTTP protocol.

## Project Structure

```
.
├── Endpoints.py        # Defines the Endpoint class
├── readme.md           # This file
├── requirements.txt    # Project dependencies
├── test                # Test scripts and saved endpoints
│ ├── endpoints
│ │ └── _post_hello.json
│ ├── testEndpoint.py   # Script for testing specific endpoints
│ └── testLoad.py       # Script for loading and running saved endpoints
```


## Usage

The API Test Tool targets `http://127.0.0.1:8000` by default. If your server is running on a different address, adjust the `baseAddress` variable in `Endpoints.py`.

Endpoints are defined by creating instances of the `Endpoint` class with appropriate parameters: HTTP method, payload for POST requests, endpoint address, and query parameters for GET requests.

After defining an endpoint, you can run it with the `runEndpoint()` method. This sends a request to the API and prints the response text.

You can save the configuration of an endpoint to a file using the `storeEndpoint()` method. This saves a JSON file in the `endpoints` directory.

To load a saved endpoint, use the `loadEndpoint()` function. This reads the JSON file for the endpoint and returns an instance of the `Endpoint` class.

## Running the Test Scripts

There are two test scripts in the `test` directory:

- `testEndpoint.py` demonstrates how to create, run, and store an endpoint.

- `testLoad.py` demonstrates how to load and run a stored endpoint.

You can run these scripts using Python:

```bash
python test/testEndpoint.py
python test/testLoad.py
```
Remember to install the project dependencies from requirements.txt before running the scripts:
```bash
pip install -r requirements.txt
```
## Contributing

This is a simple tool and doesn't require much maintenance, but improvements and bug fixes are always welcome.
