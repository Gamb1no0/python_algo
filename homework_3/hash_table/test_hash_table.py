"""Запуск из этой папки: python3 -m unittest -v."""

import unittest

from hash_table import HashTable


class CollisionKey:
    """Разные ключи с одинаковым хешем для проверки коллизий."""

    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return 7

    def __eq__(self, other):
        return isinstance(other, CollisionKey) and self.value == other.value


class HashTableTests(unittest.TestCase):
    def setUp(self):
        self.table = HashTable()

    def test_empty_table(self):
        self.assertEqual(len(self.table), 0)
        self.assertEqual(self.table.items(), [])
        self.assertEqual(self.table.keys(), [])
        self.assertEqual(self.table.values(), [])
        self.assertNotIn("missing", self.table)

    def test_insert_and_find(self):
        self.table.insert("name", "Аня")
        self.table.insert("age", 20)
        self.assertEqual(self.table.get("name"), "Аня")
        self.assertEqual(self.table["age"], 20)
        self.assertIn("name", self.table)
        self.assertEqual(len(self.table), 2)

    def test_update_existing_key(self):
        self.table.insert("key", 10)
        self.table.insert("key", 20)
        self.assertEqual(self.table["key"], 20)
        self.assertEqual(len(self.table), 1)

    def test_missing_key(self):
        self.assertIsNone(self.table.get("missing"))
        self.assertEqual(self.table.get("missing", "нет"), "нет")
        with self.assertRaises(KeyError):
            self.table["missing"]
        with self.assertRaises(KeyError):
            self.table.delete("missing")
        self.assertEqual(len(self.table), 0)

    def test_none_and_false_values(self):
        for key, value in (("none", None), ("false", False), ("zero", 0), ("empty", "")):
            with self.subTest(key=key):
                self.table.insert(key, value)
                self.assertIn(key, self.table)
                self.assertEqual(self.table.get(key, "нет"), value)
                self.assertEqual(self.table.delete(key), value)
                self.assertNotIn(key, self.table)

    def test_different_key_types(self):
        for key in ("ключ", 0, -100, 1.5, None):
            self.table.insert(key, "найдено")
        self.assertEqual(len(self.table), 5)
        for key in ("ключ", 0, -100, 1.5, None):
            self.assertEqual(self.table[key], "найдено")

    def test_equal_numeric_keys(self):
        self.table.insert(1, "первое")
        self.table.insert(1.0, "второе")
        self.assertEqual(len(self.table), 1)
        self.assertEqual(self.table[1], "второе")

    def test_collisions_and_equal_key_objects(self):
        for value in range(5):
            self.table.insert(CollisionKey(value), value * 10)
        for value in range(5):
            self.assertEqual(self.table[CollisionKey(value)], value * 10)
        self.table.insert(CollisionKey(2), 99)
        self.assertEqual(self.table[CollisionKey(2)], 99)
        self.assertEqual(len(self.table), 5)

    def test_delete_from_collision_bucket(self):
        for value in (1, 2, 3):
            self.table.insert(CollisionKey(value), value * 10)
        self.assertEqual(self.table.delete(CollisionKey(2)), 20)
        self.assertEqual(self.table[CollisionKey(1)], 10)
        self.assertEqual(self.table[CollisionKey(3)], 30)
        self.assertEqual(self.table.delete(CollisionKey(1)), 10)
        self.assertEqual(self.table.delete(CollisionKey(3)), 30)
        self.assertEqual(len(self.table), 0)

    def test_bracket_operations(self):
        self.table["a"] = 1
        self.table["a"] = 2
        self.assertEqual(self.table["a"], 2)
        del self.table["a"]
        self.assertNotIn("a", self.table)
        with self.assertRaises(KeyError):
            del self.table["a"]

    def test_resize_and_rehash(self):
        table = HashTable(capacity=4)
        for key in (1, 5, 9):
            table.insert(key, key * 10)
        self.assertEqual(table.capacity, 4)
        table.insert(2, 20)
        self.assertEqual(table.capacity, 8)
        self.assertEqual(len(table), 4)
        for key in (1, 5, 9, 2):
            self.assertEqual(table[key], key * 10)

    def test_update_does_not_resize(self):
        table = HashTable(capacity=4)
        for key in range(3):
            table.insert(key, key)
        table.insert(2, 100)
        self.assertEqual(table.capacity, 4)
        self.assertEqual(len(table), 3)
        self.assertEqual(table[2], 100)

    def test_collisions_survive_resize(self):
        table = HashTable(capacity=2)
        for value in range(50):
            table.insert(CollisionKey(value), value)
        for value in range(50):
            self.assertEqual(table[CollisionKey(value)], value)
        for value in range(0, 50, 2):
            table.delete(CollisionKey(value))
        self.assertEqual(len(table), 25)
        for value in range(50):
            self.assertEqual(CollisionKey(value) in table, value % 2 == 1)

    def test_reinsert_after_deletion(self):
        self.table.insert("key", 1)
        self.table.delete("key")
        self.table.insert("key", 2)
        self.assertEqual(self.table["key"], 2)
        self.assertEqual(len(self.table), 1)

    def test_list_views(self):
        self.table.insert("a", 10)
        self.table.insert("b", 20)
        self.assertCountEqual(self.table.keys(), ["a", "b"])
        self.assertCountEqual(self.table.values(), [10, 20])
        self.assertCountEqual(self.table.items(), [["a", 10], ["b", 20]])
        pairs = self.table.items()
        key = pairs[0][0]
        old_value = self.table[key]
        pairs[0][1] = "замена в копии"
        pairs.append(["c", 30])
        self.assertEqual(self.table[key], old_value)
        self.assertNotIn("c", self.table)

    def test_values_can_be_lists(self):
        value = [1, 2, 3]
        self.table.insert("numbers", value)
        self.assertIs(self.table["numbers"], value)

    def test_storage_uses_only_lists(self):
        for key in range(20):
            self.table.insert(key, key * 2)
        self.assertIsInstance(self.table._buckets, list)
        for bucket in self.table._buckets:
            self.assertIsInstance(bucket, list)
            for entry in bucket:
                self.assertIsInstance(entry, list)
                self.assertEqual(len(entry), 2)

    def test_unhashable_key(self):
        key = [1, 2]
        with self.assertRaises(TypeError):
            self.table.insert(key, 10)
        with self.assertRaises(TypeError):
            self.table.get(key)
        with self.assertRaises(TypeError):
            self.table.delete(key)
        self.assertEqual(len(self.table), 0)

    def test_invalid_capacity(self):
        for capacity in (0, -1):
            with self.subTest(capacity=capacity):
                with self.assertRaises(ValueError):
                    HashTable(capacity)
        for capacity in (1.5, "8", True):
            with self.subTest(capacity=capacity):
                with self.assertRaises(TypeError):
                    HashTable(capacity)

    def test_smallest_capacity(self):
        table = HashTable(capacity=1)
        table.insert("a", 1)
        self.assertEqual(table["a"], 1)
        self.assertEqual(len(table), 1)
        self.assertGreater(table.capacity, 1)

    def test_many_insertions_and_deletions(self):
        for key in range(2000):
            self.table.insert(key, key * 3)
        self.assertEqual(len(self.table), 2000)
        for key in range(2000):
            self.assertEqual(self.table[key], key * 3)
        for key in range(0, 2000, 2):
            self.table.delete(key)
        self.assertEqual(len(self.table), 1000)
        for key in range(2000):
            self.assertEqual(key in self.table, key % 2 == 1)
        self.table.insert(2000, "новое")
        self.assertEqual(self.table[2000], "новое")


if __name__ == "__main__":
    unittest.main()
