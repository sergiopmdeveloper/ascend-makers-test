# Ascend Backend Take-Home Assignment - June 2023

Ascend offers its clients a way to unify their marketing activation in one tool so the user dosen't need to be an expert in all the platforms.

The way Ascend do this is applying an abstraction layer that unifies the definition of the campaigns. 

For this assignment, you will create a simplified version of that application by coding a simple app that interacts with the "Absolutely Not a Mockup" (ANAM) activation platform.

## The ANAM API

The ANAM exposes a set of endpoints under /campaign that allows to manage the campaign of the user in the platform. Think about this an external API you have no control over, so dont make any changes to any file inside this folder.

### POST /login
This endpoints returns a token for a combination of username and password.

### GET /campaign/list
This endpoint returns a list of the campaigns activated in the platform. You must provide the rignt token in the header "token"

### POST /campaign
This url allows to POST a new campaign. You must provide the rignt token in the header "token"

#### Campaign attributes
All campaign attributes are required:

- The campaign start date (a date not in the past).
- The campaign end date (a date greater than the start date).
- The budget for the campaign.
- The type of campaign (`"search"` or `"display"`).
    - In the search campaigns, a set of keywords must be provided.
    - In the display campaigns, a set of valid URLs must be provided.

### About the campaigns
The user can manage from 0 to n campaigns. The ANAM API has limitations in the number of queries that can be performed in a given amount of time.

## Your task

The objective is to build your own private API that handles the duty of getting the inputs of a user and translate into a request for the ANAM API. You must handle the results of this API and do whatever is needed for the platform to work. A user expects to:

- See his "Ascend Campaigns" and the related ANAM campaign information.
- Create a new "Ascend Campaign".
- Create a new ANAM campaign as part of an existing ASCEND campaign.

## Criteria
You can choose any Python framework to implement this assignment. While we prefer Fastapi or Flask, feel free to use your prefered tool. We will consider exclusively that you build a solid system with an emphasis on code quality, simplicity, readability, maintainability, and reliability, particularly regarding architecture and testing to evaluate your work. 

Be aware that Ascend will mainly take into consideration the following evaluation criteria:
* How clean and organized your code is;
* If you implemented the business rules and the API connection correctly;
* How good your automated tests are (qualitative over quantitative).

Other important notes:
* Develop a extensible campaign management system
* Add to the README file: 
    * Instructions to run the code; 
    * What were the main technical decisions you made; 
    * Relevant comments about your project 
* You must use English in your code and also in your docs (if needed)

This assignment should be doable in a couple of hours. We expect you to learn fast, **communicate with us**, and make decisions regarding its implementation & scope to achieve the expected results on time.

It is not necessary to build the screens a user would interact with, however, as the API is intended to power a user-facing application, we expect the implementation to be as close as possible to what would be necessary in real-life. Consider another developer would get your project/repository to evolve and implement new features from exactly where you stopped. 

# Additional help

In order to help you focus in the important parts of the tests, we provide you:

- A devcontainer with Python and Poetry installed acompanied by an PostgreSQL instance running on 5432 port (POSTGRES_DB: app, POSTGRES_USER: app_user, POSTGRES_PASSWORD: app_password)
- A pyproject.toml with the dependencies to use FastAPI out of the box (Feel free to change it for another framework if prefered).
- A "mock" of the ANAM API under the "anam" folder. Take this code as a script that aims to help you understand what the API does.