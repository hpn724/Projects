import json
import psycopg2


#Function to create the tables if they do not exist

def create_tables(conn):
    cur=conn.cursor()
    cur.execute(""" 
    CREATE TABLE IF NOT EXISTS JIRA_TICKET(
        issue_id serial PRIMARY KEY,
        status VARCHAR(255) NOT NULL,
        summary TEXT NOT NULL,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """)
    cur.execute(""" 
    CREATE TABLE IF NOT EXISTS JIRA_TICKET_CHANGE(
        id serial PRIMARY KEY,
        issue_id INTEGER NOT NULL REFERENCES JIRA_TICKET (issue_id),
        from_status VARCHAR(30) NOT NULL,
        current_status VARCHAR(30) NOT NULL,
        changed_at VARCHAR(30) NOT NULL
    )
    """)
    conn.commit()
    cur.close()

def lambda_handler(event, context):

    #Connecting to the database
    conn=psycopg2.connect(
        host= "dbira-atlassian-data-pipeline-database.cjheoiru200f.us-east-2.rds.amazonaws.com",
        port=5432,
        user="hareesh",
        password="hareesh_!#jiratrack#2023_db",
        dbname="HAREESH"
    )

    #creating the tables
    create_tables(conn)

    #loading the json response from the webhook and storing it
    data=json.loads(json.dumps(event))

    #Loading the cursor for SQL query executions
    cur=conn.cursor()

    #The case for storing the issues into JIRA_TICKETS when issues are created
    if data["webhookEvent"] == "jira:issue_created":
        #Storimg the required parameters into python str variables
        issue_id = data["issue"]["id"]
        summary = data["issue"]["fields"]["summary"]
        status = data["issue"]["fields"]["status"]["name"]
        created = data["issue"]["fields"]["created"]
        #Executing insertion into "jira_tickets" table
        cur.execute( "INSERT INTO JIRA_TICKET (issue_id, summary, status, created) VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING",(issue_id, summary, status, created))
        print("The issue " + issue_id + " with summary : " + summary +  " and status : " + status + " created at " + created +  " has been successfully recorded."  )
    
    #The case for storing the issues into JIRA_TICKET_CHANGE when issues are updated
    elif data["webhookEvent"] == "jira:issue_updated":\
        #Storimg the required parameters into python str variables
        issue_id = data["issue"]["id"]
        changed_at = data["issue"]["fields"]["updated"]
        for item in data["changelog"]["items"]:
            if item["field"]=="status":
                from_status=item["fromString"]
                to_status=item["toString"]
        #Executing insertion into "jira_tickets_change" table
        cur.execute("INSERT INTO JIRA_TICKET_CHANGE (issue_id, from_status, current_status,changed_at) VALUES (%s, %s, %s,%s)",(issue_id, from_status, to_status,changed_at))
        print("The issue " + issue_id + " status changed from " + from_status + " to the status " + to_status +  " at " + changed_at + "  has been successfully recorded."  )
        
    #The case for storing the issues into JIRA_TICKET_CHANGE when issues are deleted    
    elif data["webhookEvent"] == "jira:issue_deleted":
        #Storimg the required parameters into python str variables
        issue_id = data["issue"]["id"]
        issue_id = data["issue"]["id"]
        changed_at = data["issue"]["fields"]["updated"]
        from_status = data["issue"]["fields"]["status"]["name"]
        to_status='deleted'
         #Executing insertion into "jira_tickets_change" table
        cur.execute("INSERT INTO JIRA_TICKET_CHANGE (issue_id, from_status, current_status,changed_at) VALUES (%s, %s, %s,%s)",(issue_id, from_status, to_status,changed_at))
        print("The deletion of the issue " + issue_id + " of the status " + from_status + " at " + changed_at + " has been successfully recorded.")

    #Commiting the execution and closing the connection
    conn.commit()
    cur.close()
    conn.close()
    print("The changes in the JIRA board has been recorded successfully.")

