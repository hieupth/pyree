from abc import ABCMeta
from threading import Lock


class Singleton(ABCMeta):
  """
  Thread-safe implementation of singleton pattern.

  :authors: Hieu Pham.
  :created: 00:13 Sun 1 Sep 2024.
  :updated: 10:30 Sun 1 Sep 2024.
  """

  _instances = {}
  _lock: Lock = Lock()

  def __call__(cls, *args, **kwargs):
    with cls._lock:
      if cls not in cls._instances:
        instance = super().__call__(*args, **kwargs)
        cls._instances[cls] = instance
      return cls._instances[cls]
