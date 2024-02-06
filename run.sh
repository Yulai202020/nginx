podman build -t django ./core
podman build -t nginx_app ./nginx

podman run -d --network web_net --name django django
podman run -d -p 8080:80 --network web_net --name webserver nginx_app