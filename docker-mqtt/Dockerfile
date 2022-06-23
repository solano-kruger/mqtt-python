FROM ubuntu  

RUN apt-get update -y  

RUN apt-get -y install net-tools  

RUN apt-get -y install iputils-ping  

RUN groupadd -g 1883 mosquitto && \  
	useradd -r -u 1883 -g mosquitto mosquitto  

RUN apt install mosquitto -y  

RUN apt install mosquitto-clients -y  

EXPOSE 1883  

CMD ["/usr/sbin/mosquitto", "-c", "/mosquitto/config/mosquitto.conf]  
