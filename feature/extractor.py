#!/usr/bin/env python3.6
import os
from collections import Counter


def make_dictionary(root_dir):
    all_words = []
    emails = [os.path.join(root_dir, f) for f in os.listdir(root_dir)]

    for mail in emails:
        with open(mail) as m:
            for line in m:
                words = line.split()
                all_words += words
    dictionary = Counter(all_words)

    list_to_remove = dictionary.keys()

    for item in list_to_remove:
        if item.is_alpha() == False:
            del dictionary[item]
        elif len(item) == 1:
            del dictionary[item]

    dictionary = dictionary.most_common(3000)

    return dictionary
