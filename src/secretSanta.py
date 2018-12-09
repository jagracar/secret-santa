"""
A simple Secrect Santa assigner.

https://en.wikipedia.org/wiki/Secret_Santa

@author: Javier Gracia Carpio (jagracar)
"""

import json
import numpy as np
from emailUtils import EmailSender

if __name__ == "__main__":
    # Load the configuration file
    with open("configuration.json", "r") as configuration_file:
        configuration = json.load(configuration_file)

    # Extract the participants list
    participants = configuration["participants"]

    # Loop until we get a valid permutation
    while True:
        # Get a random permutation
        permutation = np.random.permutation(len(participants))

        # Check if the permutation is valid
        valid_permutation = True

        for participant, assigned_index in zip(participants, permutation):
            # Get the assigned participant name
            assigned_participant = participants[assigned_index]["name"]

            # Make sure the assignment is valid
            if (assigned_participant == participant["name"]) or (assigned_participant in participant["exclude_list"]):
                valid_permutation = False

                # Print some debug information if necessary
                if configuration["debug"]:
                    print("Bad assignment: %s --> %s" % (participant["name"], assigned_participant))

                break

        # Exit the while loop if we have a valid permutation
        if valid_permutation:
            break

    # Check if we are in debug mode or not
    if configuration["debug"]:
        # Print the final result
        print("------------")
        print("Final result")
        print("------------")

        for participant, assigned_index in zip(participants, permutation):
            print("   %s --> %s" % (participant["name"], participants[assigned_index]["name"]))
    else:
        # Initialize the email sender
        emailSender = EmailSender(configuration["smtp_server"], configuration["server_port"])

        # Login with the username and password set in the configuration file
        emailSender.login(configuration["username"], configuration["password"])

        # Send an email to each participant
        for participant, assigned_index in zip(participants, permutation):
            # Set the email subject and the main text
            subject = "Your Secret Santa assignment"
            text = "Hi %s,\n\nYour Secret Santa assignment is %s.\n\nBuy him/her a nice present!!" % (
                participant["name"], participants[assigned_index]["name"])

            # Send the email
            print("Sending email to %s" % participant["email"])
            emailSender.send_email(configuration["sender_email"], participant["email"], subject, text)

        # Close the connection
        emailSender.close()
