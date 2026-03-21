#!/usr/bin/env python3
"""
Doc
"""
import redis
import uuid
from typing import Union


class Cache:
    """Doc"""

    def __init__(self) -> None:
        """Doc"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Doc
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key