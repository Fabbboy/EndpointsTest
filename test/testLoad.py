from Endpoints import Endpoint, loadEndpoint, setup

def main():
    setup()
    endpoint = loadEndpoint("/post_hello")
    Endpoint.runEndpoint(endpoint)

if __name__ == '__main__':
    main()