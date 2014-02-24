#!/usr/bin/python

__author__ = 'litingpeng'

'''

This approach replaces the end pointer with a counter that tracks the number of readable items in the buffer.

This unambiguously indicates when the buffer is empty or full and allows use of all buffer slots.

'''

class FillCountRingBuffer:

    def __init__(self, size):
        self.size = size + 1
        self.start = 0
        self.count = 0
        self.elements = []

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def write(self, elem):
        if self.is_full():
            raise RuntimeError("Ring buffer is full.")
        end = (self.start + self.count) % self.size
        self.elements[end] = elem
        if self.count == self.size:
            self.start = (self.start + 1) % self.size
        else:
            self.count += 1

    def read(self):
        if self.is_empty():
            raise RuntimeError("Ring buffer is empty.")
        elem = self.elements[self.start]
        self.start = (self.start + 1) % self.size
        self.count -= 1
        return elem

