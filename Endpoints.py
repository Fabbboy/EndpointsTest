import json
import os

import requests

baseAddress = "http://127.0.0.1:8000"


class Endpoint:
    def __init__(self, method, payload, address, queryArgs=None):
        self.payload = payload
        self.method = method
        self.address = address
        self.queryArgs = queryArgs

    def buildRequest(self):
        endpoint = baseAddress + self.address
        if self.queryArgs is not None:
            for arg in self.queryArgs:
                endpoint += "/" + arg
        return endpoint

    def buildCurl(endpoint):
        baseCurl = "curl"
        if endpoint.method == "GET":
            baseCurl += " -X GET"
        elif endpoint.method == "POST":
            baseCurl += " -X POST -H \"Content-Type: application/json\""
            baseCurl += " -d \'" + json.dumps(endpoint.payload) + "\'"

        return baseCurl + " " + endpoint.buildRequest()

    def storeEndpoint(endpoint):
        baseJson = {
            "method": endpoint.method,
            "address": endpoint.address,
            "payload": endpoint.payload,
            "queryArgs": endpoint.queryArgs,
            "curl": endpoint.buildCurl()
        }
        with open("endpoints/" + endpoint.address.replace("/", "_") + ".json", "w") as f:
            f.write(json.dumps(baseJson, indent=4))

    def runEndpoint(endpoint):
        global response
        if endpoint.method == "GET":
            response = requests.get(endpoint.buildRequest())
        elif endpoint.method == "POST":
            response = requests.post(endpoint.buildRequest(), json=endpoint.payload)
        print(response.text)


def setup():
    if not os.path.exists("endpoints"):
        os.mkdir("endpoints")
