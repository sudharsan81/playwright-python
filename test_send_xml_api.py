from playwright.sync_api import sync_playwright

def test_send_xml_api():
    with sync_playwright() as p:
        # Create a request context
        request = p.request.new_context()

        # Define the XML data to be sent
        xml_data = """
        <slideshow>
            <title>Demo slideshow 1</title>
            <slide>
                <item>Introduction</item>
            </slide>
            <slide>
                <item>Second slide</item>
            </slide>
        </slideshow>
        """

        # Set the headers to specify that we are sending XML data
        headers = {
            "Content-Type": "application/xml"
        }

        # Print the request details
        print("\nRequest Details:")
        print(f"URL: https://httpbin.org/post")
        print(f"Method: POST")
        print(f"Headers: {headers}")
        print(f"Body: {xml_data}")

        # Make a POST request with the XML data
        response = request.post("https://httpbin.org/post", data=xml_data, headers=headers)

        # Print the response details
        print("\nResponse Details:")
        print(f"Status Code: {response.status}")
        print(f"Response Headers: {response.headers}")
        print(f"Response Body: {response.text()}")

        # Check if the response status code is 200
        assert response.status == 200, f"Expected status code 200, but got {response.status}"

        # Close the request context
        request.dispose()

if __name__ == "__main__":
    test_send_xml_api()