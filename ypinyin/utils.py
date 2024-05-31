#!/usr/bin/env -S python3 -B

# TODO: add more unicode combined case
__normalize_conversion = {
  "̄": "", "́": "", "̌": "", "̀": "", 
  "ā": "a", "á": "a", "ǎ": "a", "à": "a",
  # unicode combined a
  b'a\xcc\x84'.decode("utf-8"): "a",
  b'a\xcc\x8c'.decode("utf-8"): "a",
  "ō": "o", "ó": "o", "ǒ": "o", "ò": "o",
  "ê": "e", "ế": "e",           "ề": "e",
  "ē": "e", "é": "e", "ě": "e", "è": "e",
  "ī": "i", "ǐ": "i", "í": "i", "ì": "i",
  "ū": "u", "ú": "u", "ǔ": "u", "ù": "u",
  "ü": "v", "ǘ": "v", "ǚ": "v", "ǜ": "v",
  "̈": "", "̈́": "",
  "ǹ": "n", "ń": "n", "ň": "n", "ǹ": "n",
  "ḿ": "m",
}

def replace_by_dict(string, dictionary):
  begin = 0
  now = 0
  result = ""
  for char in string:
    if char not in dictionary:
      now = now + 1
      continue
    result = result + string[begin:now] + dictionary[char]
    now = now +1
    begin = now
  result = result + string[begin:]
  return result

def fix_unicode_combined_pinyin(pinyin):
  pass
  

def normalize_pinyin(pinyin):
  return replace_by_dict(pinyin, __normalize_conversion)
