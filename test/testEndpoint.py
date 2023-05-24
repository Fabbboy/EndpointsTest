import Endpoints

def main():
    Endpoints.setup()
    data = {
        "name": "John"
    }

    endpoint = Endpoints.Endpoint("POST", data, "/post_hello")
    Endpoints.Endpoint.storeEndpoint(endpoint)
    Endpoints.Endpoint.runEndpoint(endpoint)

if __name__ == "__main__":
    main()