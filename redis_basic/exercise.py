#!/usr/bin/env python3
"""
Doc
"""

import uuid
from typing import Union

try:
    import redis
except ImportError:
    redis = None


class Cache:
    """Doc"""

    def __init__(self):
        """Doc"""
        if redis:
            self._redis = redis.Redis()
            self._redis.flushdb()
        else:
            self._redis = None

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Doc"""
        key = str(uuid.uuid4())
        if self._redis:
            self._redis.set(key, data)
        return key