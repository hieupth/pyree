from uuid import uuid4
from typing import Any
from refactor import logging
from refactor.patterns.creational import Singleton


class Object:
  """
  This is base class of all inherited objects.
  """

  @property
  def oid(self) -> str:
    return self._oid

  @property
  def object(self) -> Any:
    return self
  
  @property
  def classname(self) -> str:
    return self.__class__.__name__
  
  @property
  def modulename(self) -> str:
    return self.__module__
  
  @property
  def logger(self) -> logging.Logger:
    return logging.getLogger(f"{__name__}.{self.classname}")

  def __init__(self, *args, **kwds) -> None:
    self._oid = kwds.get("oid", uuid4().hex)

  def __encode__(self, *args, **kwds) -> dict:
    if "cache" not in kwds:
      kwds.update({"cache": list()})
    if self.oid in kwds["cache"]:
      return {"ref": self.oid}
    else:
      kwds["cache"].append(self.oid)
      _ignores = kwds.get("ignore", ())
      _attr_keys = [x for x in dir(self) if not x.startswith("_") and x not in ("object", "logger") and x not in _ignores]
      _attr_vals = [getattr(self, x) for x in _attr_keys]
      _attr_vals = [x if not isinstance(x, Object) else x.__encode__(*args, **kwds) for x in _attr_vals ]
    return dict(zip(_attr_keys, _attr_vals))
