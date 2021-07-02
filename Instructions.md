## Requirements
The assessment is aimed at helping provide us with a picture of your approach to development as it relates to:

1. Design patterns/programming paradigm
1. Scalability
1. API interface design
1. Frameworks
1. Documentation
1. Clean code
1. Automated testing
1. Error handling
1. Logging
1. Readability


## Instructions
We’ve created a mock API that returns marginal tax rates based on the inputted year. The API is accessible via a GET request to http://localhost:5000/tax-calculator/brackets/{tax_year}, which returns a JSON object that includes income tax brackets and the corresponding tax rates. To run the mock API server:

```
docker pull ptsdocker16/interview-test-server

docker run --init -p 5000:5000 -it ptsdocker16/interview-test-server
```


Your task is to build an application that queries our mock API and calculates the total income tax for an inputted salary and tax year. You may refer to this resource for context on how to calculate total income tax using margin tax rates: https://investinganswers.com/dictionary/m/marginal-tax-rate#:~:text=To%20calculate%20marginal%20tax%20rate,bracket%20your%20current%20income%20falls



The application you’re building should have an HTTP API with an endpoint that takes an annual income and the tax year as parameters. The appropriate type of params (query vs body param vs URL etc.) is to be determined by you. Your endpoint should return a JSON object with the result of the calculation.


Be aware that we’ve baked in two errors in our mock API — you may handle them and anything else you see fit to handle accordingly:

1. only years 2019 and 2020 are supported
1. the API throws errors randomly


## IMPORTANT

Design the application as you would a production app that you and your team are collaborating on. Your result should not be a proof of concept and should focus more on the assessment criteria listed above than on working code.

You may stumble upon instructions/requirements for the assignment returned in the Docker image. Please ignore these instructions and only refer to the evaluation criteria and instructions included in this email.


RECOMMENDATION:
We recommend setting up your development environment and as much of the application as you can so we can have a productive walkthrough session.
Timebox your efforts to 4 hours. We respect your time and don't want you to labour over this.