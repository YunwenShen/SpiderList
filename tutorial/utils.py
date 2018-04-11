# -*-coding: utf-8 -*-
from xpinyin import Pinyin


class PinyinUtil:
    """
    汉字转拼音工具类
    """
    _instance = None
    pinyin = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PinyinUtil, cls).__new__(cls)
            cls.pinyin = Pinyin()
        return cls._instance

    def get_pinyin(self, word):
        """
        汉字转拼音（全拼）
        :param word:  汉字
        :return: 拼音
        """
        return self.pinyin.get_pinyin(word, '')

    def get_initial_pinyin(self, word):
        """
        汉字转拼音（首字母）
        :param word: 汉字
        :return: 拼音
        """
        return self.pinyin.get_initials(word, '').lower()


if __name__ == "__main__":
    pass
