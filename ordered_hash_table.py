from typing import Hashable, Any, NoReturn, List
from collections import namedtuple
from bisect import bisect_left

Element = namedtuple('Node', ['key_hash', 'item'])


class OrderedHashTable:
    def __init__(self, capacity=1000):
        self.capacity = capacity

        # not using defaultdict because it is a dict which is what we're trying to build here..
        self.buckets = [[] for _ in range(capacity)]

    def get(self, key: Hashable) -> Any:
        key_hash = hash(key)
        bucket_num = self._get_bucket_num(key_hash)
        return self.buckets[bucket_num][self._get_hashes(bucket_num).index(key_hash)].item

    def put(self, key: Hashable, item: Any) -> NoReturn:
        key_hash = hash(key)
        bucket_num = self._get_bucket_num(key_hash)
        new_node = Element(key_hash, item)

        i = bisect_left(self._get_hashes(bucket_num), key_hash)

        if i == len(self.buckets[bucket_num]):
            self.buckets[bucket_num].append(new_node)
        elif key_hash < self.buckets[bucket_num][i].key_hash:
            self.buckets[bucket_num].insert(i, new_node)
        elif key_hash == self.buckets[bucket_num][i].key_hash:
            self.buckets[bucket_num][i] = new_node

    def remove(self, key: Hashable) -> Element:
        key_hash = hash(key)
        bucket_num = self._get_bucket_num(key_hash)
        return self.buckets[bucket_num].pop(self._get_hashes(bucket_num).index(key_hash))

    def _get_bucket_num(self, key_hash: int) -> int:
        return key_hash % self.capacity

    def _get_hashes(self, bucket_num: int) -> List[int]:
        return list(map(lambda n: n.key_hash, self.buckets[bucket_num]))


if __name__ == '__main__':
    # basic tests
    ht = OrderedHashTable()
    try:
        ht.get('not_available')
        raise AssertionError('Found non existent')
    except ValueError:
        pass
    ht.put('new_key', 100)
    assert ht.get('new_key') == 100
    ht.put('new_key', 120)
    assert ht.get('new_key') == 120
    ht.remove('new_key')
    try:
        ht.get('new_key')
        raise AssertionError('Found non existent')
    except ValueError:
        pass
    try:
        ht.remove('new_key')
        raise AssertionError('Found non existent')
    except ValueError:
        pass
