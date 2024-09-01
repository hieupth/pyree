from refactor.system import logging


class Object:
  """
  Base class that provide utility functions to all inherited.

  :authors: Hieu Pham.
  :created: 11:34 Sun 1 Sep 2024.
  :updated: 11:34 Sun 1 Sep 2024.
  """

  @property
  def classname(self) -> str:
    return self.__class__.__name__
  
  @property
  def modulename(self) -> str:
    return self.__module__
  
  @property
  def logger(self) -> logging.Logger:
    return self.__logger

  def __init__(self, *args, **kwds) -> None:
    super().__init__()
    self.__logger = logging.getLogger(f'{__name__}.{self.classname}')
  
