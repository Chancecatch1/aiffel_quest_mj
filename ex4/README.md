# AIFFEL Campus Online Code Peer Review Templete
- Coder : MyungJun Lee
- Reviewer :Minsung Seo


## 루브릭


1. 다양한 방법으로 Text Classification 태스크를 성공적으로 구현하였다.
> 3가지 이상의 모델이 성공적으로 시도됨
2. gensim을 활용하여 자체학습된 혹은 사전학습된 임베딩 레이어를 분석하였다.
> gensim의 유사단어 찾기를 활용하여 자체학습한 임베딩과 사전학습 임베딩을 비교 분석함
3. 한국어 Word2Vec을 활용하여 가시적인 성능향상을 달성했다.
> 네이버 영화리뷰 데이터 감성분석 정확도를 85% 이상 달성함


# PRT(Peer Review Template)


- [ ]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**

  
> 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
  1. 다양한 방법으로 Text Classification 태스크를 성공적으로 구현하였다. 단일 모델 학습만 구성되어 있어 아쉽습니다.
  2. gensim을 활용하여 자체학습된 혹은 사전학습된 임베딩 레이어를 분석하였다. 사전학습된 임베딩레이어로 학습이 되어있지 않았습니다..
  3. 한국어 Word2Vec을 활용하여 가시적인 성능향상을 달성했다. 사전학습된 임베딩레이어로 학습이 되어있지 않았습니다..

> 문제를 해결하는 완성된 코드란 프로젝트 루브릭 3개 중 2개, 퀘스트 문제 요구조건 등을 지칭
> 해당 조건을 만족하는 코드를 캡쳐해 근거로 첨부

                 
- [ ]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**


> 해당 코드 블럭에 doc string/annotation이 달려 있는지 확인
> 해당 코드가 무슨 기능을 하는지, 왜 그렇게 짜여진건지, 작동 메커니즘이 뭔지 기술.
> 주석을 보고 코드 이해가 잘 되었는지 확인
> 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부합니다.
주석처리가 되어있지 아쉬웠으며, 하기의 코드에서 parameter의 수정으로 다양한 시도가 있었으면 좋을 것 같습니다.
epochs와 batch_size를 변경해보는 방법, layers의 숫자를 변경하는 방법 Model을 변경하는 방법도 좋을 것 같습니다.  
![스크린샷 2023-10-05 오후 12 41 54](https://github.com/Chancecatch1/aiffel_quest_mj/assets/138687269/29ee0990-8f88-4334-889e-4eb1b2641269)

      
- [ ] **3. 에러가 난 부분을 디버깅하여 문제를 “해결한 기록을 남겼거나”, "새로운 시도 또는 추가 실험을 수행”해봤나요?**

        
> 문제 원인 및 해결 과정을 잘 기록하였는지 확인
  사전학습된 임베딩 모델을 호출하는 과정에서 이슈가 있었지만, 이를 해결하려는 시도가 없어서 아쉬웠습니다.
    - [Errno 2] No such file or directory: '~/data/word2vec_ko.model.wv.vectors.npy'라는 오류가 호출된 것으로 보아 path를 수정하면 호출이 될 것 같습니다:)
  ![스크린샷 2023-10-05 오후 12 48 11](https://github.com/Chancecatch1/aiffel_quest_mj/assets/138687269/003c1300-2e10-42db-8676-c36a98a3627e)

> 문제에서 요구하는 조건에 더해 추가적으로 수행한 나만의 시도, 실험이 기록되어 있는지 확인
> 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부합니다.


- [ ] **4. 회고를 잘 작성했나요?**


> 주어진 문제를 해결하는 완성된 코드 내지 프로젝트 결과물에 대해 배운점과 아쉬운점, 느낀점 등이 기록되어 있는지 확인
  > 주어진 문제에 대한 회고가 기입되어있었습니다.
> 전체 코드 실행 플로우를 그래프로 그려서 이해를 돕고 있는지 확인
> 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부합니다.


- [ ] **5. 코드가 간결하고 효율적인가요?**

 
> 파이썬 스타일 가이드 (PEP8) 를 준수하였는지 확인
  > 네 준수하여 작성하였습니다. 
> 하드코딩을 하지않고 함수화, 모듈화가 가능한 부분은 함수를 만들거나 클래스로 짰는지
  > 함수를 만들거나 클래스로 만든 것은 없었습니다. 
> 코드 중복을 최소화하고 범용적으로 사용할 수 있도록 함수화했는지
  > for문을 통하여 중복을 최소화하고자 하였습니다.
> 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부합니다.
  ![스크린샷 2023-10-05 오후 12 46 09](https://github.com/Chancecatch1/aiffel_quest_mj/assets/138687269/c2d404d4-54cb-4710-9c62-f734a27cd1c1)


  
# 참고 링크 및 코드 개선
```
# 코드 리뷰 시 참고한 링크가 있다면 링크와 간략한 설명을 첨부합니다.
# 코드 리뷰를 통해 개선한 코드가 있다면 코드와 간략한 설명을 첨부합니다.
```