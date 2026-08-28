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

---

### Day 11: Blackjack Capstone (CLI)
* **Concepts:** Complex state machines, sentinel values (`0` for natural Blackjack), rule-based decision trees.
* **Key Technique:** Managed dynamic card values by converting Aces from `11` to `1` in-place when totals exceed 21.
* **Talking Point:** Modeled asymmetric game loops and dealer AI constraints through modular helper functions and deterministic score evaluation.

---

### Day 12: Number Guessing Game (CLI)
* **Concepts:** Scope management, loop counters, conditional termination branches.
* **Key Technique:** Configured stateful attempt counters mapped to user difficulty tiers (`easy` / `hard`).
* **Talking Point:** Implemented numeric binary-search feedback loops with strict counter boundary conditions.

---

### Day 14: Higher Lower Game (CLI)
* **Concepts:** Data extraction from record collections, state propagation, defensive key lookup.
* **Key Technique:** Rolled over `B` to next comparison entity `A` to maintain continuous stream flow.
* **Talking Point:** Modeled round-based comparison logic using structured dictionary datasets and dynamic CLI feedback.

---

### Day 15: Coffee Machine Simulation (CLI)
* **Concepts:** State mutation, transaction validation, nested dictionaries.
* **Key Technique:** Evaluated multi-ingredient availability against current resources before initiating coin transactions to prevent state corruption.
* **Talking Point:** Implemented transactional state handling by decoupling resource validation, financial computation, and inventory deduction.

---

### Day 16: OOP Coffee Machine
* **Concepts:** Object-Oriented Programming (OOP), encapsulation, Separation of Concerns (SoC).
* **Key Technique:** Refactored procedural logic into specialized domain models (`CoffeeMaker`, `MoneyMachine`, `Menu`), making the main loop a clean orchestrator.
* **Talking Point:** Applied OOP principles and encapsulation to isolate resource inventory, monetary transactions, and menu lookups into maintainable, testable classes.

---

### Day 17: CLI Quiz Game
* **Concepts:** Data modeling, OOP orchestration, stateful queue processing.
* **Key Technique:** Deserialized raw dictionary records into dedicated `Question` model instances passed to a `QuizBrain` driver.
* **Talking Point:** Separated domain data representations from lifecycle management to achieve a modular, reusable quiz execution engine.
