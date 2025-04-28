APIQuake - API Test Automation Tool with UI
APIQuake is a lightweight and powerful API testing automation tool built using Python and Streamlit.
It allows users to configure APIs easily, select APIs through an interactive UI, run tests, validate responses, and export the results — all from a single dashboard.

🚀 Features
✅ Simple and easy-to-use web UI (built with Streamlit)

✅ Supports GET and POST APIs (with Bearer Token Authentication support)

✅ Multi-select APIs to run tests individually or in batch

✅ Dynamic display of API URLs as tooltips for better visibility

✅ Test Summary shown after execution

✅ Export test results to a CSV file

✅ Extensible Design - easy to add more APIs or validations

✅ Clean project structure and production-grade code

🏗️ Project Structure

APIQuake/
│
├── api_config.json      # API configuration file (name, URL, method, headers, payloads)
├── api_tester.py        # Core logic to run API tests
├── test_runner.py       # Loads API configurations and runs tests
├── ui_app.py            # Streamlit UI Application
├── requirements.txt     # Python dependencies
├── .gitignore           # Files to ignore in Git
└── README.md            # Project documentation (this file)

🔧 Prerequisites
Python 3.8+

pip (Python package installer)

Basic familiarity with APIs (GET/POST requests)

📦 Setup Instructions
Clone the Repository:

git clone https://github.com/brijgit1/APIQuake.git
cd APIQuake
(Optional) Create a Virtual Environment:

python -m venv venv
source venv/bin/activate    # On Mac/Linux
venv\Scripts\activate       # On Windows
Install Dependencies:

pip install -r requirements.txt
Start the Application:

streamlit run ui_app.py
🛠️ How to Use
Configure APIs
Update the api_config.json file with your APIs.
Each API entry should have:

name: Display name

url: Full endpoint

method: GET or POST

headers: (Optional) Authorization / Content-Type

payload: (Optional) Data for POST APIs

Example api_config.json:

{
  "API 1": {
    "url": "https://exampleurl",
    "method": "GET",
    "headers": {},
    "payload": {}
  },
  "API 2": {
    "url": "https://testurl/posts",
    "method": "POST",
    "headers": {
      "Content-Type": "application/json"
    },
    "payload": {
      "title": "foo",
      "body": "bar",
      "userId": 1
    }
  }
}
Launch the UI
The app will automatically open in your browser.

Select one or multiple APIs to test.

View tooltips showing the full API URL.

Run the selected APIs.

Run Tests
Click Run Selected API Tests.
Results will be displayed in the dashboard.

Export Results
Download the full test report as a CSV file.

🔐 Authentication Support
Supports Bearer Token Authentication and custom headers.

Easily configurable via api_config.json.

Extendable to dynamically fetch tokens if needed (in api_tester.py).

✨ Future Enhancements
Add automatic token generation and refresh mechanism

Support for PUT, DELETE, and PATCH methods

Add assertion-based validations for response contents

Response time performance analysis

Integrate with CI/CD (e.g., GitHub Actions, Jenkins)

🤝 Contributions
Contributions, feature requests, and suggestions are welcome!
Feel free to fork the repo, make your changes, and open a pull request.

👉 GitHub Repo: APIQuake

🙌 Acknowledgements
Built using Python and Streamlit — Making API Automation Simple and Powerful.

🔥 Let's Quake the APIs with APIQuake!