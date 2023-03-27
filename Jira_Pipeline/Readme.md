This project makes use of serverless cloud computing platform, Amazon Web Services to process the changes in a JIRA board to a PostgreSQL database.
The following components have been used:
1. Jira Webhook service: Automatically triggered when any change occurs in the JIRA board
2. AWS API GateWay: API endpoint of AWS, which triggers the required action 
3. AWS Lambda: The backend code that translates the relevant changes in the board to the PostgreSQL tables

The given code is to be used in the lambda function. It requires the installation of the following python libraries: aws_psycopg2, json. 
