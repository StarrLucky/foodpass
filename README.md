# About
This script automates placing orders on [foodpassonline.com](https://foodpassonline.com/) in case you forget to do it manually. 
It checks whether each user from `config.py` does not have an active order for the day (at 19:00 GMT+4) and, if needed, creates an order with the items specified in the config.

## Example of the Config

- `username`   - login used for https://foodpassonline.com
- `password`   - password 
- `lunchboxes` - list of your favorite lunchboxes. The script determines whether one of the URLs is available and orders it. The script uses the `meals` list if there isn't any:
- `meals`      -  A list of dishes to order. These are typically always listed on the website. The total price of all dishes should be less than 15 lari.
 
```PYTHON

import user as users

userList = [
    users.user(
        username="User",
        password="password",
        lunchboxes=[
            "https://foodpassonline.com/product/%D1%88%D0%B0%D1%88%D0%BB%D1%8B%D0%BA-%D0%B8%D0%B7-%D0%BB%D0%BE%D1%81%D0%BE%D1%81%D1%8F-%D1%80%D0%B8%D1%81-%D1%81-%D0%BE%D0%B2%D0%BE%D1%89%D0%B0%D0%BC%D0%B8-%D0%BB%D0%B8%D0%BC%D0%BE%D0%BD/",
            "https://foodpassonline.com/product/%D0%B1%D0%BE%D1%83%D0%BB-%D1%81-%D0%BA%D1%83%D1%80%D0%B8%D1%86%D0%B5%D0%B9-%D0%B8-%D1%80%D0%B8%D1%81%D0%BE%D0%BC/",
            "https://foodpassonline.com/product/%D0%BC%D0%B0%D0%B4%D0%B0%D0%BC-%D0%B1%D0%BE%D0%B2%D0%B0%D1%80%D0%B8-%D1%81%D0%B0%D0%BB%D0%B0%D1%82-%D0%B8%D0%B7-%D0%BA%D0%B0%D0%BF%D1%83%D1%81%D1%82%D1%8B/",
            "https://foodpassonline.com/product/%D0%BB%D0%BE%D1%81%D0%BE%D1%81%D1%8C-%D0%B2-%D1%81%D0%BE%D1%83%D1%81%D0%B5-%D1%80%D0%B8%D1%81-%D1%81-%D0%BE%D0%B2%D0%BE%D1%89%D0%B0%D0%BC%D0%B8-%D1%81%D0%B0%D0%BB%D0%B0%D1%82-%D0%B8%D0%B7-%D0%BA/",
            "https://foodpassonline.com/product/%D0%B1%D0%BE%D1%83%D0%BB-%D1%81-%D1%84%D0%B0%D0%BB%D0%B0%D1%84%D0%B5%D0%BB%D0%B5%D0%BC-%D0%B8-%D1%84%D0%B8%D1%80%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%BC-%D1%81%D0%BE%D1%83%D1%81%D0%BE%D0%BC/"
        ],
        meals=[
            "https://foodpassonline.com/product/%d0%b3%d1%80%d0%b5%d1%87%d0%ba%d0%b0/",
            "https://foodpassonline.com/product/%d0%ba%d1%83%d1%80%d0%b8%d0%bd%d1%8b%d0%b9-%d1%88%d0%bd%d0%b8%d1%86%d0%b5%d0%bb%d1%8c/"
        ]
    )
]

```

## How To Run

Setup `login`, `username`, `lunchboxes`, and `meals` in `config.py` for one or several users.

### Option 1: With docker container

1.1 Pull container and run it:

```BASH
sudo docker run -v $(pwd)/config.py:/config.py  --restart=always --name=foodpass starrlucky/foodpass:foodpass_amd64
```

### Option 2: Manually

2.1 Install: 

```BASH 
make install
```

2.2
Run a test to place the order for today: 

```BASH 
make orders
```

2.3 Set up a scheduled job to execute this script at 19:00 daily:
- Run the script after changing the `/home/username/foodpass` path to your own:

```BASH
(crontab -l ; echo "00 19 * * *  cd /home/username/foodpass; make orders") | crontab 

```
