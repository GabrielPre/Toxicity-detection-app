# Toxicity-detection-app
Project created by Celine YE, Louis TARDY and Gabriel PRECIGOUT

# Notion
Invitation to our Notion (for the project management):
[https://www.notion.so/42ab49311fbd43418f4e43dae39e8182?v=6f187541b77649c78f267a5192083766](https://www.notion.so/42ab49311fbd43418f4e43dae39e8182?v=6f187541b77649c78f267a5192083766)

# Running the application
## **Running the docker image**

To run the docker image, use the following command:
```
docker run -p 5000:5000 -it celineye/detoxify
```

The website is now accessible on [http://localhost:5000](http://localhost:5000).

## **Building & running the local docker image**

Building the docker image:
```
docker compose build
```

Running the docker image:
```
docker compose up
```

## Installation

To install the requirements, run:
```
pip install -r requirements.txt
```

## **Tests**
Runnig the unit, stress and integration tests is as easy as:
```
python -m pytest
```

### End to end testing
End to end testing is done with CodeceptJS.

Running the end to end tests can be done this way:
```
cd end_to_end_testing
npm install
npm run tests
```

# Automation with Jenkins

First, push on a feature branch. This will run the unit tests:
![image](https://user-images.githubusercontent.com/37049291/157021150-79a5cdcd-bf94-4f02-b870-3ebd640d0c2b.png)

Then manually merge on develop. This will run the stress test, the integration tests, and the end to end tests before pushing to release if everything succeed:
![image](https://user-images.githubusercontent.com/37049291/157021163-07369783-8d06-4074-ae1e-437fabf0d0e2.png)
![image](https://user-images.githubusercontent.com/37049291/157021172-ea74fead-3e5c-4d64-94fd-ac6f141e4307.png)

This will automatically merge on release, which will then ask the user for validation. Once the user validates, this will merge on main.
![image](https://user-images.githubusercontent.com/37049291/157021178-53c35fe3-c7c0-420b-8cd8-58478b624d92.png)
![image](https://user-images.githubusercontent.com/37049291/157021186-7ac2a6aa-8554-456e-8602-8027312ad1e0.png)

On main, the image will be built & deployed.
![image](https://user-images.githubusercontent.com/37049291/157021192-cc9df067-463a-4972-9414-a93bbd748271.png)

# Authors
Céline YE

Gabriel PRECIGOUT

Louis TARDY


