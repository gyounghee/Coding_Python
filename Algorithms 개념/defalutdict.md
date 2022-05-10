* defaultdict()
    : dictionary를 만드는 dict클래스의 서브 클래스
    - defaultdict()는 인자로 주어진 객체의 기본값을 딕셔너리 값의 초기값으로 지정할 수 있음
    - 처음 키를 지정할 때 값을 주지 않으면 해당 키에 대한 defalut값을 지정하겠다는 의미

* defaultdict()의 기본적인 작동방식  
    ```python
    from collections import defaultdict    # 외부함수이기 때문에 import 해야 함
    ```
    1. default 값이 int인 딕셔너리
    ```python
    int_dict = defaultdict(int)
    # int_dict의 결과  →  defaultdict(<class 'int'>, {})
    
    int_dict['key1']  # 위와 같이 설정을 하면 지정하지 않은 키는 그 값이 0으로 지정됨
    # int_dict의 결과  →  defaultdict(<class 'int'>, {'key1':0})

    int_dict['key2'] = 'test'  # key에 명시적으로 값을 지정하게 되면 그 값이 지정됨
    # int_dict의 결과  →  defaultdict(<class 'int'>, {'key1':0, 'key2':'test'})
    ```

    2. default 값으로 list를 줬을 때
    ```python 
    list_dict = defaultdict(list)
    # list_dict의 결과  →  defaultdict(<class 'list'>, {})

    list_dict['key1']
    list_dict['key2'] = 'test'
    # list_dict의 결과  →  defaultdict(<class 'list'>, {'key1':[], 'key2':'test'})
    ```

    3. default 값으로 set를 줬을 때
    ```python 
    set_dict = defaultdict(set)
    # set_dict의 결과  →  defaultdict(<class 'set'>, {})

    set_dict['key1']
    set_dict['key2'] = 'test'
    # set_dict의 결과  →  defaultdict(<class 'set'>, {'key1':[], 'key2':'test'})
    ```
    