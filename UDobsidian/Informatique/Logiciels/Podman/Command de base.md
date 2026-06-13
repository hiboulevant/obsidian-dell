# Command de base

#podman 
- Podman search <image_name>
- Podman pull <image_name>
- Podman images
- Podman run -it <image_name>
- Podman ps:   how many are runing
- Podman ps -a : how many are stop
- Podman run -it -rm <image_name>
- Podman run --name <container_name>  \
-  - p ext_port : int_port  <container_image> 
-   podman start <container_image> 
- Podman inspect <container_image>
- Podman port <container_image>
- Podman stop <container_image>
- Podman rm <container_image>
- Podman rmi <container_image>