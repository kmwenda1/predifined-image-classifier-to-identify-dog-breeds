#!/usr/bin/env python3
import re


def is_label_match(truth, model_label):
    truth = truth.lower()
    model_label = model_label.lower()
    if not truth:
        return False
    return re.search(r"\b" + re.escape(truth) + r"\b", model_label) is not None
