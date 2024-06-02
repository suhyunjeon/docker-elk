# 로그 전송 테스트 
```shell
$ cat 1.json
{"message":{"data":"cmu_test"}}

# nc : Netcat: 데이터를 읽고 쓰는 리눅스 명령어
nc localhost 5001 <  1.json
echo '{"message":{"data": "hello world"}}' | ncat localhost 5001

open http://localhost:5601/app/kibana
```
