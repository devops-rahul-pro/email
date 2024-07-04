from tabulate import tabulate

# Define the variables for the email content
sender = "sender@example.com"
recipient = "recipient@example.com"
subject = "Microservice Build Notification"
recipient_name = "Recipient name"

email_table = [
    ['1',"eps-credit",'1.0.0.1','tag-1','location-1','checksum-1'],
    ['2','eps-debit','1.0.0.0','tag-2','location-2','checksum-2']
]

head = ['SNO','Service','version','tag','location','checksum']

table_data = tabulate(email_table, headers=head, tablefmt="fancy_grid")

# Create the email content using f-strings
email_content = f"""\
From: {sender}
To: {recipient}
Subject: {subject}

Dear {recipient_name},

The Microservice Build is created and ready for download.
Please find the details below:

{table_data}



Thank You,
Build & Deployment Team
Note: This is a system generated email.Please donot replay to this.
      Please contact POS Platform Team on the Slack channel: #pos-microservices-platform
"""

# Specify the filename
filename = "email.txt"

# Open the file in write mode and write the email content
with open(filename, 'w', encoding='utf-8') as file:
    file.write(email_content)

print(f"Email content written to '{filename}'.")
