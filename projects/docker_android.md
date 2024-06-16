# How to run Docker on Android

All the process is described in the following repository: https://github.com/AntonyZ89/docker-qemu-arm 

## 🛠️ Prerequisites and tips

* **I recommend you to setup the following environment to use docker from Termux native graphical desktop: [How to install Termux X11 native DESKTOP on ANDROID - Linux on Android
](https://youtu.be/rq85dxMb7e4?feature=shared)**

* **Remember the Alpine environment credentials:** 
```
user: root
password: Secret123
```

* **How to forward a port from Termux native to Alpine to be able to access the apps:** 

From the `docker-qemu-arm/alpine` folder: 
```
ssh -i qemukey -L 8080:localhost:4647 root@localhost -p 2222
```

This will forward the port `8080` in Termux native to the port `4647` in the Alpine container.

<br>

## 🐋 How to run docker containers

1. Login into Alpine with the creds from before
```
/docker-qemu-arm/alpine/startqemu.sh
```

2. Create a new folder: 
```
mkdir nginx
cd nginx
```

3. Create an index file and paste the following content: 
```
nano index.html
``` 
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prueba de Nginx</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        h1 {
            color: #333;
        }
    </style>
</head>
<body>
    <h1>Hello from Docker!</h1>
    <p>Don't forget to subscribe to DroidMaster :)</p>
</body>
</html>
```

4. Create a Dockerfile with the following content: 
```
nano Dockerfile
```
```
FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/

COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

5. Create a Nginx config file: 
```
nano nginx.conf
```
```
server {
    listen 80;
    server_name localhost;

    location / {
        root /usr/share/nginx/html;
        index index.html;
    }
}
```

6. Lets build and run our docker: 
```
docker build -t my-nginx-container .
docker run -d -p 4647:80 --name nginx-container my-nginx-container
```

7. Other useful commands: 

Check running containers: 
```
docker ps
```
Check all the containers in the system: 
```
docker ps -a
```
Start/Stop a container: 
```
docker stop my-nginx-container
```