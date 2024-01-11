"""
    HashTable
        키-값(key-value) 쌍을 저장
        효율적인 검색 및 삽입을 위해 해시 함수를 사용하는 자료구조
    
    시간 복잡도
        삽입, 삭제, 조회 - O(1)
    
    사용 이유
        빠른 검색 및 삽입
            해시 테이블은 키를 해시 함수를 사용하여 배열 인덱스로 변환
        고유한 키와 값 저장
            키는 해시 함수를 통해 유일한 위치에 매핑
        데이터베이스 인덱싱
            레코드를 빠르게 검색하기 위해 해시 테이블 사용
        캐싱
            캐시 메모리에서 데이터를 빠르게 검색하기 위해 사용
        집합 및 맵 데이터 구조
            고유한 값의 집합 (Set)과 키-값 맵(Map)을 구현하는데 사용
        알고리즘 최적화
            데이터 검색 및 처리를 가속화 할 때 사용
    
    코드
        AI로 구현한 것 나중에 수정 필요
"""

class HashTable:
    def __init__(self, size=10):
        self.size = size  # 해시 테이블의 크기
        self.table = [None] * self.size  # 초기화된 해시 테이블

    def _hash_function(self, key):
        """
        키를 해시값으로 변환하는 간단한 해시 함수.

        :param key: 해싱할 키
        :return: 해시값
        """
        # 키를 문자열로 변환하고 각 문자의 ASCII 코드 합을 구함
        key_str = str(key)
        hash_value = 0
        for char in key_str:
            hash_value += ord(char)
        # 해시값을 해시 테이블 크기로 나눈 나머지를 반환
        return hash_value % self.size

    def put(self, key, value):
        """
        키-값 쌍을 해시 테이블에 추가합니다.

        :param key: 키
        :param value: 값
        """
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        # 이미 해당 키에 대한 엔트리가 있는 경우, 값만 업데이트
        for entry in self.table[index]:
            if entry[0] == key:
                entry[1] = value
                return
        # 새로운 키-값 쌍 추가
        self.table[index].append([key, value])

    def get(self, key):
        """
        주어진 키에 해당하는 값을 반환합니다.

        :param key: 검색할 키
        :return: 키에 해당하는 값 또는 None (키가 없는 경우)
        """
        index = self._hash_function(key)
        if self.table[index] is not None:
            for entry in self.table[index]:
                if entry[0] == key:
                    return entry[1]
        return None

    def remove(self, key):
        """
        주어진 키에 해당하는 키-값 쌍을 해시 테이블에서 제거합니다.

        :param key: 제거할 키
        """
        index = self._hash_function(key)
        if self.table[index] is not None:
            for entry in self.table[index]:
                if entry[0] == key:
                    self.table[index].remove(entry)
                    return


# 해시 테이블 인스턴스 생성
hash_table = HashTable()

# 키-값 쌍 추가
hash_table.put("name", "Alice")
hash_table.put("age", 30)
hash_table.put("city", "New York")

# 값 검색
print("Name:", hash_table.get("name"))
print("Age:", hash_table.get("age"))
print("City:", hash_table.get("city"))

# 값 제거
hash_table.remove("age")
print("Age (after removal):", hash_table.get("age"))
