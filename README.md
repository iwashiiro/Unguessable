# Unguessable

![web](https://img.shields.io/badge/topic-web-blue)
![source](https://img.shields.io/badge/type-source_leak-orange)
![easy](https://img.shields.io/badge/difficulty-easy-green)
![python](https://img.shields.io/badge/language-Python-grey)

---

## Overview.

This challenge presents a simple web application where the user is asked to guess a number. The interface suggests that guessing is practically impossible, hinting at a brute-force resistant mechanism.

However, the real vulnerability lies in the **client-side JavaScript code**.

---

## Challenge Description.

> You will never guess the number!

* **Website:** http://url-of-the.chall
* **Flag format:** `ptm{...}`

---

## The vulnerability.

Inspecting the source code reveals the following function:

```javascript
function update(res) {
  if (res === "wrong") {
    card.style.backgroundColor = "red";
    text.innerText = "Wrong, try again";
  } else {
    card.style.backgroundColor = "green";
    fetch("/vjfYkHzyZGJ4A7cPNutFeM/flag")
      .then((response) => response.text())
      .then((str) => {
        text.innerText = str
      });
  }
}
```

### Key issue.

The application performs all the logic on the client side and exposes a hidden endpoint directly inside the JavaScript code:

```
/vjfYkHzyZGJ4A7cPNutFeM/flag
```

This means the “unguessable number” is irrelevant, because:

> The flag is fetched directly from a public endpoint when the correct condition is met.

---

## Exploitation strategy.

No brute force or guessing is required.

1. Open the website.
2. Inspect the page source or DevTools.
3. Locate the JavaScript function handling the response.
4. Identify the hidden `/flag` endpoint.
5. Directly request the endpoint via browser or script.

---

## Example attack.

Simply visit:

```
http://url-of-the.chall/vjfYkHzyZGJ4A7cPNutFeM/flag
```

Or use `curl`:

```bash
curl http://url-of-the.chall/vjfYkHzyZGJ4A7cPNutFeM/flag
```

---

## Final result.

* **Flag:** `ptm{4lw4y5_ch3ck_th3_50urc3_c0d3}`

---

## Exploit script.

The included script automates the request:

```bash
pip install requests
python solve.py
```
---

## Why this works.

This is a classic **source code exposure vulnerability**:

* Sensitive endpoints are embedded in frontend code.
* No authentication or validation is required.
* Security relies only on obscurity (hidden path).

Once the source is inspected, the challenge is effectively solved.

---

## How to fix it.

To prevent this issue:

* Never expose sensitive endpoints in client-side code.
* Protect flag or secret endpoints with authentication.
* Move validation logic entirely to the backend.
* Avoid relying on hidden URLs for security.

---

## Files.

* `solve.py` → Simple script to retrieve the flag.

---

## Takeaway.

If the logic is in the frontend, it is **not secret**.
Always inspect the source code, sometimes the solution is just one request away.
