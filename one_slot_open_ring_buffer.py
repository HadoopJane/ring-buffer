#!/usr/bin/python

__author__ = 'litingpeng'

'''

This design always keeps one slot unallocated.

A full buffer has at most ({text{size}}-1) slots.

If both pointers refer to the same slot, the buffer is empty.

If the end (write) pointer refers to the slot preceding the one referred to by the start (read) pointer, the buffer is full.

'''

class OneSlotOpenRingBuffer:

    def __init__(self, size):
        self.size = size + 1
        self.start = 0
        self.end = 0
        self.elements = []

    def is_full(self):
        return (self.end + 1) % self.size == self.start

    def is_empty(self):
        return self.start == self.end

    def write(self, elem):
        if self.is_full():
            raise RuntimeError("Ring buffer is full.")
        self.elements.append(elem)
        self.end = (self.end + 1) % self.size
        if self.end == self.start:
            self.start = (self.start + 1) % self.size

    def read(self):
        if self.is_empty():
            raise RuntimeError("Ring buffer is empty.")
        elem = self.elements[self.start]
        self.start = (self.start + 1) % self.size
        return elem




