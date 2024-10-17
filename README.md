# About
This script automates placing orders on [foodpassonline.com](https://foodpassonline.com/) in case you forget to do it manually. It checks whether each user from `config.py` does not have an active order for the day (at 19:00 GMT+4) and, if needed, creates an order with the items specified in the config.

## Example of the Config

    userList = [
        users.user("User", 
            "Password", 
            ["https://foodpassonline.com/product/%d0%b3%d1%80%d0%b5%d1%87%d0%ba%d0%b0/",
            "https://foodpassonline.com/product/%d0%ba%d1%83%d1%80%d0%b8%d0%bd%d1%8b%d0%b9-%d1%88%d0%bd%d0%b8%d1%86%d0%b5%d0%bb%d1%8c/"])
        ]


In the example above, the first and second links point to the items that need to be ordered.



## How To Run

### Option 1: Build a Docker Container

    sudo docker build -t foodpass .

### Option 2: Run Manually

TO DO