# collect email from user
# split email using the @, the first part as the user name, the second part is going to be saved as doman
# split domain using .

def email_slicer():
    print("Welcome to the email slicer\n ")

    email_input = input("Input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)


while True:
    email_slicer()
