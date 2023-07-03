###What is Difference?
1. 내가 작성한 코드는 문제의 3번 조건에 명시되어 있는 "만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한채로 한 칸 뒤로 가고 1단계로 돌아간다."
라는 조건을 고려하지 않음.  
   => visited와 map을 별도로 놔야 하는 이유
2. 방향을 변경하는 함수에 갈 수 있는 칸이 있는지 확인하는 로직을 같은 scope으로 묶음.  
=> direction이 변경되고 그 후의 로직들(자리 이동 및 이동할 수 있는 자리 확인)  
3. 반복 로직이 매우 이상함.  
=> 반복문의 조건부터, 반복문이 수행되면서 안에서 체크하고 있는 조건이 없음.
   
### 구현 로직을 잘 작성하려면?
- 문제에 적혀있는 수행 함수들을 로직별로 나열하고, 해당 내용을 빠짐없이 구현한다.