import rawpy
from PIL import Image
from io import BytesIO
from pillow_heif import register_heif_opener
from refactor.utils.assets import Asset


register_heif_opener()


class ImageAsset(Asset):
  """
  Load image asset.

  :authors: Hieu Pham.
  :created: 22:52 Sun 1 Sep 2024.
  :updated: 22:52 Sun 1 Sep 2024.
  """

  @property
  def image(self) -> Image.Image:
    return self._image

  def __init__(self, src: any, *args, **kwargs) -> None:
    super().__init__(src, *args, **kwargs)
    buffer = BytesIO(self.data)
    try:
      self._image = Image.open(buffer)
      return
    except:
      pass
    try:
      with rawpy.imread(buffer) as raw:
        thumb = raw.extract_thumb()
      if thumb.format == rawpy.ThumbFormat.JPEG:
        self._image = Image.open(BytesIO(thumb.data))
      elif thumb.format == rawpy.ThumbFormat.BITMAP:
        self._image = Image.fromarray(thumb.data)
    except:
      raise AssertionError(f'Cannot load image asset from {str(src):20s}')

x = ImageAsset('~/Downloads/sample/0.jpg')
x.image.show()