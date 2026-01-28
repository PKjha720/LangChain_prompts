
# LangChain Prompts (Revision Notes) — from YouTube transcript

## What this video covers (recap)
- Playlist flow:
  1) Intro to LangChain + why it’s needed  
  2) 6 key components overview  
  3) Deep dive on **Models**  
  4) Deep dive on **Prompts** (this video)

---

## 1) Quick fix from previous video: Temperature (important)
**Meaning (practical)**
- Temperature controls **how much variation/randomness** the model shows for the **same input**.

**Behavior**
- **Temp ≈ 0** → same prompt → **almost same output every time** (deterministic)
- **Higher temp** (e.g., 1.0–1.5+) → same prompt → **different outputs** (more variation/creativity)

**When to use**
- **Consistent apps** (policies, support, summaries) → temp low  
- **Creative tasks** (poems, brainstorming) → temp higher

---

## 2) What is a Prompt?
- A **prompt** = the **message sent to the LLM**.
- Example: “Write a five-line poem on cricket” is a prompt.

### Prompt types
- **Text prompts** (most common today)
- **Multimodal prompts** (image/audio/video + questions)

### Why prompts matter
- LLM output is **highly sensitive** to prompt wording.
- Small changes in the prompt can change results a lot.
- That’s why “prompt engineering” exists.

---

## 3) Static vs Dynamic Prompts (core concept)
### A) Static prompts
**Meaning**
- User writes the full prompt every time (free-text).

**Problems**
- Too much freedom → inconsistent output quality/format
- Spelling mistakes / wrong names → hallucinations possible
- Different users ask differently → UX becomes inconsistent

### B) Dynamic prompts
**Meaning**
- You pre-design a **prompt template**, and user only fills controlled fields.

**Typical template idea**
- “Please summarize the paper titled `{paper_input}` with style `{style_input}` and length `{length_input}`…”
- Add fixed rules like:
  - include math equations if present
  - explain math with intuitive code snippets when possible
  - add analogies
  - if info missing → say “Insufficient information available”
  - ensure clarity + accuracy

**UI approach**
- Use dropdowns to control inputs:
  - Paper name (dropdown → no spelling issues)
  - Style: simple / math-heavy / code-heavy
  - Length: short / medium / long

**Benefit**
- Consistent UX + safer output while still personalized.

---

## 4) Mini LLM App flow (Streamlit idea)
**Basic LLM app pattern**
1) Take input from user
2) Send to LLM
3) Display output

**Upgrade**
- Replace free-text prompt input with structured controls (dropdowns)
- Generate final prompt using a template

---

## 5) PromptTemplate vs f-strings (why PromptTemplate?)
Yes, f-strings can work, but PromptTemplate gives key benefits:

### Reason 1 — Validation
- If template expects variables (e.g., `paper_input`, `style_input`, `length_input`)
- And you forget one → it can throw an error early (development time), not in production.

### Reason 2 — Reusability
- Save templates externally (e.g., JSON) and load them wherever needed.
- Keeps code clean in bigger apps.

### Reason 3 — LangChain ecosystem integration (Chains)
- PromptTemplate works smoothly inside LangChain Chains.
- You can combine steps:
  - template → model
- And call a single `invoke()` via a chain.

---

## 6) Simple chatbot (console) + the “context problem”
### Problem
- Basic chatbot sends only the latest user message → model has **no memory**
- Follow-up questions fail because earlier context is missing.

### Fix
- Maintain **chat history** and send it every turn.

### New problem
- If you store raw strings only, model may not know:
  - which message is from user vs AI
- As history grows, confusion increases.

---

## 7) LangChain message types (3 types)
LangChain recommends labeling messages:

1. **SystemMessage**
   - Instructions/role at the start  
   - Example: “You are a helpful assistant.”

2. **HumanMessage**
   - What user says  
   - Example: “Tell me about LangChain.”

3. **AIMessage**
   - What model replies  
   - Example: “LangChain is …”

**Why this matters**
- Helps the model clearly understand speaker roles in long multi-turn chats.

---

## 8) ChatPromptTemplate (dynamic prompts for chat / list of messages)
**When used**
- When you send a **list of messages** (chat style), not a single string.
- And you want placeholders inside system/human messages.

**Example**
- System: “You are a helpful `{domain}` expert”
- Human: “Explain `{topic}` in simple terms”

**Note**
- The transcript mentions some “weird” behavior with message class usage.
- Recommended approach shown: represent messages as tuples like:
  - `("system", "....{domain}...")`
  - `("human", "....{topic}...")`

---

## 9) MessagePlaceholder (inject chat history dynamically)
**Use case**
- Real apps store chat history in a database.
- When user returns, you load past history and insert it into the prompt.

**What it does**
- Creates a slot inside ChatPromptTemplate to insert messages at runtime:
  - `MessagePlaceholder("chat_history")`

**Typical structure**
- System message (role/instructions)
- `MessagePlaceholder("chat_history")`  ← insert old conversation
- Human message (today’s new question)

**Benefit**
- Clean and scalable way to attach past context.

---

## 10) Final recap (must remember)
### invoke() can be used in 2 ways
1) **Single message** → one-time tasks (summaries, single query)
   - can be **static** or **dynamic** via PromptTemplate

2) **List of messages** → multi-turn chatbots
   - label messages (System/Human/AI)
   - make them dynamic via ChatPromptTemplate
   - inject history via MessagePlaceholder

---

## Interview-ready one-liners
- Prompt = input message to LLM; output is prompt-sensitive.
- Static prompts → inconsistent UX + higher hallucination risk.
- Dynamic prompts = template + controlled inputs → consistent UX.
- PromptTemplate beats f-strings via validation + reuse + chain compatibility.
- Chatbots need memory → store & send chat history each turn.
- Use System/Human/AI messages to avoid role confusion.
- ChatPromptTemplate = PromptTemplate for multi-message chat.
- MessagePlaceholder injects stored chat history at runtime.
```
