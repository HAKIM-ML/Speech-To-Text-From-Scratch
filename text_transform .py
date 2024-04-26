import torch
import torchaudio
import torch.nn as nn
import torch.nn.functional as F
from tqdm import tqdm
import string
import numpy as np

# Text Transformation
class TextTransform:
    """Maps characters to integers and vice verse, using the string module for character definitions"""
    
    def __init__(self):
        # Including additional characters manually and using string.ascii_lowercase for letters
        additional_chars = ["''", '<SPACE>']
        all_chars = additional_chars + list(string.ascii_lowercase)
        
        # Generating char_map with enumeration, starting indices from 0
        self.char_map = {char: i for i, char in enumerate(all_chars)}
        # Inverting char_map to create index_map
        self.index_map = {index: char for char, index in self.char_map.items()}
        self.index_map[self.char_map['<SPACE>']] = ' ' 
        
    def text_to_int(self, text):
        '''Converts text to an integer sequence using a character map'''
        return [self.char_map.get(c, self.char_map['<SPACE>']) for c in text.lower()]
    
    def int_to_text(self, labels):
        '''Converts integer labels to a text sequence using a character map'''
        return ''.join(self.index_map[i] for i in labels).replace('<SPACE>', ' ')