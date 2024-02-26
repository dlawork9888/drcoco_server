# Dr.CoCo
## SKT FLY AI ESG 프로젝트 - 코코 박사
### 통합 판단 모델용 서버
- API ENDPOINT(for loacl): http://127.0.0.1:8000/sleep_recog/sleep_recog_data_input/
  - Public: http://{public_ip:8000}/sleep_recog/sleep_recog_data_input/
- HEADER
  - No Auth ! 
  - Content-Type: application/json
  - Body Example (All Float !)
    ```
    {
      "blink_score": 1.0,
      "move_score": 0.0,
      "silence": 1.0,
      "baby_cry": 0.0,
      "baby_laughter": 0.0
    }
    ```
### Dependency
- requirements.txt 참고 !
