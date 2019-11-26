from pathlib import Path
from pprint import pprint
import time
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures as confu
from logging import StreamHandler, Formatter, INFO, getLogger
from tesserocr import PyTessBaseAPI
import json
from util import *
import time
from logging import StreamHandler, Formatter, INFO, getLogger


def init_logger():
    handler = StreamHandler()
    handler.setLevel(INFO)
    handler.setFormatter(Formatter("[%(asctime)s] [%(threadName)s] %(message)s"))
    logger = getLogger()
    logger.addHandler(handler)
    logger.setLevel(INFO)

class OCRWatcher:
    def __init__(self):
        self.ocr_result = ""
        self.is_stopping = False
        init_logger()
        self._logger = getLogger()

    def stop(self):
        self.is_stopping = True

    def clear_result(self):
        self.ocr_result = ""

    def watch(self):
        if not area_data_path.exists():
            raise NotImplementedError()
        with PyTessBaseAPI(lang="jpn") as api:
            for i in range(10000):
                time.sleep(1)
                igrab = RectImageGrab()
                image = igrab.grab()
                api.SetImage(image)
                txt = api.GetUTF8Text()
                txt = "".join(txt.split())
                self.ocr_result = txt
                self._logger.info(f"OCR:{txt}")
                if self.is_stopping is True:
                    break
        return 1
