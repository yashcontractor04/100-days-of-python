# Day 8: Caesar Cipher

A secret code program. A Caesar cipher hides a message by moving every letter forward in the alphabet by the same number. For example, with a shift of 3, `a` becomes `d`.

You choose to encode or decode, type your message and pick the shift number. Letters that go past `z` wrap around to the start, so `z` with a shift of 1 becomes `a` (this is done with the `%` operator). Spaces, numbers and punctuation stay as they are. The message is turned into lowercase first.

To run it: `python main.py`
