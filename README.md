# docker-elk
Docker 기반의 ELK docker compose

# docker compose 실행
1. docker-compose 버전 확인
```shell
$ docker-compose --version

docker-compose version 1.23.2, build 1110ad01
```

2. docker-compose 컨테이너 생성 및 실행
```shell
$ docker-compose up

Creating network "docker-elk_elk" with driver "bridge"
Building elasticsearch
Step 1/1 : FROM docker.elastic.co/elasticsearch/elasticsearch:7.8.1
 ---> a529963ec236
```

3. docker-compose 컨테이너 정지 및 삭제  
```shell
$ docker-compose down
```

4. docker-compose 컨테이너 목록 조회 
```shell
$ docker-compose ps
           Name                         Command               State                                   Ports
-------------------------------------------------------------------------------------------------------------------------------------------
docker-elk_elasticsearch_1   /tini -- /usr/local/bin/do ...   Up      0.0.0.0:9200->9200/tcp, 0.0.0.0:9300->9300/tcp
docker-elk_kibana_1          /usr/local/bin/dumb-init - ...   Up      0.0.0.0:5601->5601/tcp
docker-elk_logstash_1        /usr/local/bin/docker-entr ...   Up      0.0.0.0:5001->5001/tcp, 0.0.0.0:5001->5001/udp, 5044/tcp,
                                                                      0.0.0.0:9600->9600/tcp
```

5. docker-compose 컨테이너 로그 조회
```shell
$ docker-compose logs
Attaching to docker-elk_logstash_1, docker-elk_kibana_1, docker-elk_elasticsearch_1
kibana_1         | {"type":"log","@timestamp":"2023-02-18T06:27:50Z","tags":["warning","plugins-discovery"],"pid":7,"message":"Expect plugin \"id\" in camelCase, but found: apm_oss"}
```

6. docker-compose 컨테이너 설정 확인 
```shell
$ docker-compose config
```

# ElasticSearch 확인 
```shell
$ open http://localhost:9200/_cat/indices
```

# Kibana 확인 
```shell
$ open http://localhost:5601/app/kibana
```

# container 접속
```shell
$ docker-compose exec logstash sh
```
