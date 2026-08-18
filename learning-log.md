### Day 7: Hangman Game (CLI)
* **Concepts:** State machines, input validation guards, modular imports (`import art, words`).
* **Key Technique:** Tracked guessed vs. correct letters separately to update masked strings without duplicate penalties.
* **Talking Point:** Managed game-loop state and graceful edge-case handling using boolean flags and list lookups.

---

### Day 8: Caesar Cipher (CLI)
* **Concepts:** Substitution ciphers, modular arithmetic (`% len(alphabet)`), unified function design.
* **Key Technique:** Inverted shift value (`shift * -1`) to share one algorithmic path for both encode and decode.
* **Talking Point:** Used modulo arithmetic for cyclic index wrapping and boundary safety across large shift values.

---

### Day 9: Secret Blind Auction (CLI)
* **Concepts:** Hash maps / Dictionaries, key-value storage, higher-order max reduction.
* **Key Technique:** Extracted top bidder using `max(bidders, key=bidders.get)` instead of manual iteration.
* **Talking Point:** Leveraged Python dictionary lookups and built-in functions with custom key extractors for $O(N)$ maximum value retrieval.

---

### Day 10: CLI Calculator
* **Concepts:** First-class functions, dispatch table pattern, stateful chained execution.
* **Key Technique:** Mapped mathematical operator strings directly to function references in a dictionary (`operations[symbol](n1, n2)`), eliminating `if/elif` branches.
* **Talking Point:** Implemented the dispatch table pattern using first-class functions to achieve clean, extensible $O(1)$ operation routing and state chaining.
