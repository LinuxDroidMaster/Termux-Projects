# 🖥️ HomeLab server: Turn your Android device into a server

All this process is documented in the following [video](https://www.youtube.com/watch?v=PxTnMAuheaw)


# 📚 Index

* 🏁 [First steps](#first-steps)
* 🎨 [Terminal customization: Starship](#terminal-customization)
* 💻 [Install OpenSSH (SSH server)](#openssh)
* 📂 [Mount external USB HDD](#external_device)
* 🤖 [Start Termux on boot](#termux-boot)


<br>

---  
---  

<br>

## 🏁 First steps <a name=first-steps></a>
- **Download and install Termux app from the [official GitHub repository](https://github.com/termux/termux-app).**

- **Update and upgrade packages:** 
```
pkg update
pkg upgrade -y
```

Tip: You can select the mirror corresponding to the area closest to you with the command: 
```
termux-change-repo
```

Tip 2: You can access your device internal storage with the command
```
termux-setups-storage
```
You will see a new folder called `storage` with the content of your Android device

---  

<br>

## 🎨 Terminal Customization: Starship<a name=terminal-customization></a>

- **Go to the installation section of the [official Starship site](https://starship.rs/guide/#step-1-install-starship) or just install it with the following command:** 
```
pkg install starship
```

- **Select the [preset](https://starship.rs/presets/) you like the most and install it, for example:**
```
starship preset gruvbox-rainbow -o ~/.config/starship.toml
```

- **Add the following line at the end of the .bashrc file**
```
cd
nano .bashrc
```
```
# Add the following line
eval "$(starship init bash)"
```


---  

<br>

## 💻 Install OpenSSH (SSH server)<a name=openssh></a>

- **Install OpenSSH in Termux**
```
pkg install openssh
```

- **Initialize OpenSSH daemon**
```
sshd
```

Tip: You can check OpenSSH configuration in the following path: 
```
cat $PREFIX/etc/ssh/sshd_config
```

- **Setup a password to login later**
```
passwd
```

- **Check the listening port (by default `8022`) in the tablet with the following command**
```
logcat -S 'sshd:*'
```

Tip: Check your username with the command `whoami` and the IP address with `ifconfig` or `ip a`

- **Note: I will use the program called [MobaXterm](https://mobaxterm.mobatek.net/download.html) to connect to the tablet from my Windows PC** 

![](/projects/images/homelab/ssh_connect.png)
![](/projects/images/homelab/ssh_connect_ok.png)




---  

<br>

## 📂 Mount external USB HDD<a name=external_device></a>

**Note: You need `ROOT` access for this part**

- **Enter root terminal in Termux with `su` command**
- You can find your device storage in the `/mnt` folder but for the external hard disk you need to find its path with the `blkid` command (in my case it is `/dev/block/sda1`).

![](/projects/images/homelab/blkid_output.png)

- **Create a folder where we are going to mount the HDD:**
```
cd /mnt
mkdir HDD
```

- **Mount the HDD with permissions to write on it (remember to change `/dev/block/sda1` with your path**
```
mount -o uid=1000,gid=1000,umask=0000 /dev/block/sda1 HDD/
```

Tip: You can mount the HDD inside a chroot environment like I show on the video so we can share it with other services like `Samba`, `Transmission`, etc.

- [How to setup a samba server](https://pimylifeup.com/raspberry-pi-samba/)

---  

<br>

## 🤖 Start Termux on boot<a name=termux-boot></a>

- **Install Termux Boot app from the [official page](https://github.com/termux/termux-boot)**

- **Follow the usage example from the [official wiki](https://wiki.termux.com/wiki/Termux:Boot):**
```
mkdir ~/.termux/boot/
nano ~/.termux/boot/start-sshd
```
```
# Paste this
#!/data/data/com.termux/files/usr/bin/sh
termux-wake-lock
sshd
```

- **Add another file to start Termux services on boot**
```
nano ~/.termux/boot/start-services
```
```
# Paste this
#!/data/data/com.termux/files/usr/bin/sh
termux-wake-lock
. $PREFIX/etc/profile
```

Tip: Reboot your Android device and check that after a few secons Termux opens in background and you can connect to it with SSH (even with the device screen locked)
