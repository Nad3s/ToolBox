# Presentation

## Networking
Docker have 6 types of networks named "Drivers":
1. Bridge (Default)-> Permit to standalone applications to communicate each other.
2. none -> Disable all networking
3. host -> For standalone containers, they are directly connect to the host
4. overlay -> Permit to connect multiple Docker daemons together on differents hosts.
5. macvlan -> Allow you to assign a MAC address to a container. Usefull if you want your container is connected to the physical network.
6. ipvlan ->  Give users a total control on IPv4 / IPv6 addressing.

You can have Network plugins created by the community on Docker Hub => https://hub.docker.com/search?q=&type=plugin
# Sources
https://docs.docker.com/network/#network-drivers
