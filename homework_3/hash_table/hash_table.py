"""Хеш-таблица с разрешением коллизий через списки пар."""


class HashTable:
    def __init__(self, capacity=8):
        if not isinstance(capacity, int) or isinstance(capacity, bool):
            raise TypeError("Размер таблицы должен быть целым числом")
        if capacity < 1:
            raise ValueError("Размер таблицы должен быть положительным")

        self._buckets = [[] for _ in range(capacity)]
        self._size = 0

    @property
    def capacity(self):
        return len(self._buckets)

    def __len__(self):
        return self._size

    def _find_entry(self, key):
        bucket = self._buckets[hash(key) % self.capacity]
        for entry in bucket:
            if entry[0] is key or entry[0] == key:
                return entry
        return None

    def _resize(self):
        new_capacity = self.capacity * 2
        new_buckets = [[] for _ in range(new_capacity)]

        for bucket in self._buckets:
            for entry in bucket:
                index = hash(entry[0]) % new_capacity
                new_buckets[index].append(entry)

        self._buckets = new_buckets

    def insert(self, key, value):
        """Добавить пару или заменить значение существующего ключа."""
        entry = self._find_entry(key)
        if entry is not None:
            entry[1] = value
            return

        if (self._size + 1) / self.capacity > 0.75:
            self._resize()

        index = hash(key) % self.capacity
        self._buckets[index].append([key, value])
        self._size += 1

    def get(self, key, default=None):
        """Вернуть значение или default, если ключа нет."""
        entry = self._find_entry(key)
        return default if entry is None else entry[1]

    def delete(self, key):
        """Удалить пару и вернуть её значение. Если ключа нет — KeyError."""
        bucket = self._buckets[hash(key) % self.capacity]
        for index, entry in enumerate(bucket):
            if entry[0] is key or entry[0] == key:
                value = entry[1]
                bucket.pop(index)
                self._size -= 1
                return value
        raise KeyError(key)

    def __getitem__(self, key):
        entry = self._find_entry(key)
        if entry is None:
            raise KeyError(key)
        return entry[1]

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __delitem__(self, key):
        self.delete(key)

    def __contains__(self, key):
        return self._find_entry(key) is not None

    def keys(self):
        return [entry[0] for bucket in self._buckets for entry in bucket]

    def values(self):
        return [entry[1] for bucket in self._buckets for entry in bucket]

    def items(self):
        # Возвращаем копии пар, чтобы их замена не меняла содержимое таблицы.
        return [[entry[0], entry[1]] for bucket in self._buckets for entry in bucket]


if __name__ == "__main__":
    table = HashTable(capacity=4)
    table.insert(1, "один")
    table.insert(5, "пять")
    table.insert(9, "девять")
    print("После вставки:", table.items())

    table.insert(5, "ПЯТЬ")
    print("Поиск ключа 5:", table.get(5))

    table.insert(2, "два")
    print("Размер после расширения:", table.capacity)
    print("Удалили:", table.delete(1))
    print("Осталось:", table.items())
