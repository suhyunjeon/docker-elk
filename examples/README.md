# 로그 전송 테스트 
```shell
cat 1.json
{"message":{"data":"cmu_test"}}

nc localhost 5001 <  1.json

open http://localhost:5601/app/kibana
```
