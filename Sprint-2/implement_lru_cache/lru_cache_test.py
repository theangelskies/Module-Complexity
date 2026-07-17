import unittest

from lru_cache import LruCache

class LruCacheTest(unittest.TestCase):
    def test_zero_limit_is_error(self):
        self.assertRaises(ValueError, lambda: LruCache(limit=0))

    def test_set_then_get(self):
        cache = LruCache(limit=10)

        self.assertIsNone(cache.get("greeting"))
        self.assertIsNone(cache.get("parting"))

        cache.set("greeting", "hello")

        self.assertEqual(cache.get("greeting"), "hello")
        self.assertIsNone(cache.get("parting"))

    def test_limit(self):
        limit = 3
        cache = LruCache(limit=limit)

        keys = ["a", "b", "c", "d", "e"]

        for key in keys:
            cache.set(key, f"{key}-1")

        hits = 0
        for key in keys:
            if cache.get(key) is not None:
                hits += 1

        self.assertEqual(hits, limit)

    def test_eviction_order_just_inserts(self):
        cache = LruCache(limit=2)

        cache.set("a", 1)
        cache.set("b", 2)
        cache.set("c", 3)
        self.assertIsNone(cache.get("a"))

    def test_eviction_order_after_gets(self):
        cache = LruCache(limit=2)

        cache.set("a", 1)
        cache.set("b", 2)
        cache.get("a")
        cache.get("b")
        cache.get("a")
        cache.set("c", 3)
        self.assertIsNone(cache.get("b"))
        self.assertEqual(cache.get("a"), 1)
        self.assertEqual(cache.get("c"), 3)

    def test_set_existing_key_updates_value_and_recency(self):
        cache = LruCache(limit=2)

        cache.set("a", 1)
        cache.set("b", 2)
        cache.set("a", "updated")
        cache.set("c", 3)

        self.assertIsNone(cache.get("b"))
        self.assertEqual(cache.get("a"), "updated")
        self.assertEqual(cache.get("c"), 3)

    def test_limit_one(self):
        cache = LruCache(limit=1)

        cache.set("a", 1)
        self.assertEqual(cache.get("a"), 1)

        cache.set("b", 2)
        self.assertIsNone(cache.get("a"))
        self.assertEqual(cache.get("b"), 2)


if __name__ == "__main__":
    unittest.main()
