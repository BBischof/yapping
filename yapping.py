import re

class Yapping:
    def __init__(self, config):
        self.config = config

    def exuberant_elaboration(self, text):
        # Apply verbose rules
        for rule in self.config.get('verbose_rules', []):
            pattern = re.compile(rule['pattern'])
            replacement = rule['replacement']
            text = pattern.sub(replacement, text)
        return text

    def speculative_shushing(self, text):
        # Apply brief rules
        for rule in self.config.get('brief_rules', []):
            pattern = re.compile(rule['pattern'])
            replacement = rule['replacement']
            text = pattern.sub(replacement, text)
        return text

def make_verbose(yapping_instance):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return yapping_instance.exuberant_elaboration(result)
        return wrapper
    return decorator

def make_brief(yapping_instance):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return yapping_instance.speculative_shushing(result)
        return wrapper
    return decorator