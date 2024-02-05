""" original code """
# # practicing exception with help of google rejistration example

# class SecurityError(Exception):
#   def __init__(self,message):
#     print(message)

#   def logout(self):
#     conf=input("is that you ? Yes? or No?  ")
#     if conf == "Yes":
#       print(" you are logged in !!")
#       # print(f"welcome {self.name}")
#     elif conf == "No":
#       print("you are logged out !!")
#     else:
#       print("wrong input")


# class google:
#   def __init__(self, name, email, password, device):
#     self.name = name
#     self.email= email
#     self.password = password
#     self.device = device

#   def login(self, email, password, device):

#     if device != self.device:
#       raise SecurityError("different device is trying to login")

#     if self.email != email or self.password != password:
#       print("there seems to be some issue with login credentials")
#     else:
#       print(" you are logged in !!")

# obj=google('anjali','anjali123@gmail.com','efgbd','android')
# try:
#   obj.login(email=input("enter your email id  "),password=input("enter your password  "),device=input("what is your device  "))
# except SecurityError as e:
#   e.logout()
# else:
#   print(f"welcome {obj.name}")


""" improvized code """

# practicing exception with help of google rejistration example

import logging #gpt improvements
class SecurityError(Exception):
    def __init__(self,message):
        self.message = message # gpt improvements

    def logout(self):
        conf=input("is that you ? Yes? or No?  ")
        if conf == "Yes":
            print(" you are logged in !!")
            # print(f"welcome {self.name}")
        elif conf == "No":
            print("you are logged out !!")
        else:
            print("wrong input")


class google:
    def __init__(self, name, email, password, device):
        self.name = name
        self.email= email
        self.password = password
        self.device = device

    def login(self, email, password, device):

        if device != self.device:
            raise SecurityError("different device is trying to login")

        if self.email != email or self.password != password:
            print("there seems to be some issue with login credentials") # def to raise error here and to correct it could be included too
        else:
            print(" you are logged in !!")

def main():  #gpt improvements
    obj = google('anjali', 'anjali123@gmail.com', 'efgbd', 'android')
    try:
        obj.login(email=input("Enter your email id: "), password=input("Enter your password: "),device=input("What is your device: "))
    except SecurityError as e:
        logging.error(e) # gpt improvements
        e.logout()
    else:
        print(f"Welcome {obj.name}")

if __name__ == "__main__":
    main()


"""
o/p ex:
enter your email id  anjali123@gmail.com
enter your password  efgbd
what is your device  windows
different device is trying to login
is that you ? Yes? or No?  Yes
    you are logged in !!
    """