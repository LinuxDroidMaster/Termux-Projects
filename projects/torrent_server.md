# Torrent Server on Android with Termux (Transmission)


Here are the commands you need to configure a Torrent server in Termux. This will allow you to host your own Torrent server with a web interface so you can upload your torrents files or magnet links from anywhere in your network.

All this process is documented in the following video: [Pending]()

## 1. Installing Transmission

Once loged in Debian using Termux with proot-distro (you can see all the process explained [here](https://www.youtube.com/watch?v=mXkXzFqSeYE)) just install Transmission
```
sudo apt install transmission -y
```

## 2. Edit Transmission default configuration
You need to start the Transmission server at least once: 
```
sudo service transmission start
```
Then, stop it
```
sudo service transmission stop
```
And then modify the default configuration
```
sudo nano /etc/transmission-daemon/settings.json
```
Modify the following parameters to setup the login into the web interface: 
```
"rpc-password": "Your_Password",
"rpc-username": "Your_Username",
"rpc-whitelist-enabled": "false",
```

Now you are ready to log into the web interface: `http://your_device_ip:9091`