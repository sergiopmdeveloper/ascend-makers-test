# Explanation

The architecture of the application has been based on the repository pattern in order to abstract the logic of the relationship with the database from the top of the application, making it naturally more scalable and readable. We have two database tables, the campaigns table, which will store the campaigns by name and ID, and the campaigns_anam table, which will store the ANAM campaigns associated to the original campaigns of the table.

The main functionalities of the application are the following:


- Create records in the campaigns table with the possibility of creating a campaign in the campaigns_anam table linked to the original campaign while creating the campaign in the ANAM platform through its API.

- Get all the records of the campaigns table providing the possibility to get the records of the campaigns_anam table associated to each of the original campaigns.

- Obtain ANAM campaigns directly from the platform's API.

- There is a previous validation of the data provided to generate ANAM campaigns.

- When interacting with the ANAM API, a username and password are required to generate the token needed to authenticate requests.

- Unit tests of the generate_token function have been implemented in order to demonstrate testing skills.
