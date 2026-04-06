import streamlit as st
from groq import Groq
import json

st.set_page_config(
    page_title="PromptCraft AI",
    page_icon="✦",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #0a0a0f;
    color: #f0efe8;
}

.main .block-container {
    padding: 2.5rem 2rem 3rem;
    max-width: 720px;
}

.app-header {
    text-align: center;
    margin-bottom: 2.5rem;
    padding: 2rem 0 1rem;
}

.app-title {
    font-family: 'Syne', sans-serif;
    font-size: 3rem;
    font-weight: 800;
    color: #f0efe8;
    letter-spacing: -0.03em;
    line-height: 1;
    margin-bottom: 0.5rem;
}

.app-title span {
    color: #c8f060;
}

.app-subtitle {
    font-size: 0.95rem;
    color: #6b6b7a;
    font-weight: 300;
    letter-spacing: 0.02em;
}

.section-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #6b6b7a;
    margin-bottom: 0.5rem;
}

.stTextArea textarea {
    background: #13131a !important;
    border: 1px solid #2a2a35 !important;
    border-radius: 12px !important;
    color: #f0efe8 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1rem !important;
    padding: 1rem 1.2rem !important;
    transition: border-color 0.2s !important;
}

.stTextArea textarea:focus {
    border-color: #c8f060 !important;
    box-shadow: 0 0 0 3px rgba(200, 240, 96, 0.08) !important;
}

.stTextArea textarea::placeholder {
    color: #3a3a48 !important;
}

div[data-testid="stSelectbox"] > div > div {
    background: #13131a !important;
    border: 1px solid #2a2a35 !important;
    border-radius: 10px !important;
    color: #f0efe8 !important;
}

.type-row {
    display: flex;
    gap: 8px;
    margin-bottom: 1.5rem;
    flex-wrap: wrap;
}

.stButton > button {
    background: #c8f060 !important;
    color: #0a0a0f !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    letter-spacing: 0.02em !important;
    padding: 0.75rem 2rem !important;
    width: 100% !important;
    transition: all 0.2s !important;
    cursor: pointer !important;
}

.stButton > button:hover {
    background: #d4f57a !important;
    transform: translateY(-1px) !important;
}

.result-container {
    margin-top: 2rem;
    animation: fadeUp 0.4s ease;
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
}

.result-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 12px;
}

.result-box {
    background: #13131a;
    border: 1px solid #2a2a35;
    border-radius: 14px;
    padding: 1.2rem 1.3rem;
}

.result-box.improved {
    border-color: #c8f060;
    background: #0f1a05;
}

.result-box-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
    color: #6b6b7a;
}

.result-box.improved .result-box-label {
    color: #c8f060;
}

.result-box-text {
    font-size: 0.92rem;
    line-height: 1.6;
    color: #d0cfc8;
}

.explanation-box {
    background: #13131a;
    border: 1px solid #2a2a35;
    border-radius: 14px;
    padding: 1.2rem 1.3rem;
    margin-bottom: 10px;
}

.explanation-box-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #6b6b7a;
    margin-bottom: 0.5rem;
}

.explanation-text {
    font-size: 0.88rem;
    color: #7a7a8a;
    line-height: 1.65;
}

.howtouse-box {
    background: #0d0d14;
    border: 1px solid #1e1e28;
    border-radius: 14px;
    padding: 1.2rem 1.3rem;
    margin-bottom: 10px;
}

.howtouse-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #c8f060;
    margin-bottom: 0.5rem;
}

.howtouse-text {
    font-size: 0.88rem;
    color: #7a7a8a;
    line-height: 1.65;
}

.howtouse-steps {
    margin-top: 0.6rem;
    display: flex;
    flex-direction: column;
    gap: 6px;
}

.howtouse-step {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    font-size: 0.85rem;
    color: #7a7a8a;
}

.step-num {
    background: #1e1e28;
    color: #c8f060;
    border-radius: 50%;
    width: 20px;
    height: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.7rem;
    font-weight: 700;
    flex-shrink: 0;
    margin-top: 1px;
}

.divider {
    border: none;
    border-top: 1px solid #1e1e28;
    margin: 1.5rem 0;
}

.badge {
    display: inline-block;
    background: #1a1a24;
    border: 1px solid #2a2a35;
    border-radius: 20px;
    padding: 4px 12px;
    font-size: 0.72rem;
    color: #6b6b7a;
    margin-bottom: 1.5rem;
    font-family: 'DM Sans', sans-serif;
}

.stSpinner > div {
    border-top-color: #c8f060 !important;
}

label, .stTextArea label, .stSelectbox label {
    font-family: 'Syne', sans-serif !important;
    font-size: 0.7rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    color: #6b6b7a !important;
}
</style>
""", unsafe_allow_html=True)

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.markdown("""
<div class="app-header">
    <div class="app-title">Prompt<span>Craft</span></div>
    <div class="app-subtitle">Transform weak prompts into powerful ones using AI</div>
</div>
<div style="text-align:center">
    <span class="badge">✦ Built by Minna Nourin · Powered by Groq & Llama 3.1</span>
</div>
""", unsafe_allow_html=True)

user_input = st.text_area(
    "YOUR PROMPT",
    height=130,
    placeholder="e.g. Explain AI, Write a cover letter, Debug my code..."
)

prompt_type = st.selectbox(
    "PROMPT TYPE",
    ["General", "Creative", "Technical", "Formal", "Academic", "Marketing"]
)

def improve_prompt(prompt, prompt_type):
    query = f"""You are an expert prompt engineer.
Improve this {prompt_type.lower()} prompt and return ONLY a JSON object like this:
{{"improved": "improved prompt here", "explanation": "what changed and why"}}
No markdown, no backticks. Raw JSON only.

Prompt: {prompt}"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": query}],
            max_tokens=1000
        )
        raw = response.choices[0].message.content.strip()
        raw = raw.replace("```json", "").replace("```", "").strip()
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"improved": raw, "explanation": "Could not parse structured response."}
    except Exception as e:
        return {"improved": "", "explanation": f"Error: {str(e)}"}

if st.button("✦ Craft My Prompt"):
    if not user_input.strip():
        st.warning("Please enter a prompt first.")
    else:
        with st.spinner("Crafting your prompt..."):
            result = improve_prompt(user_input, prompt_type)

        st.markdown('<div class="result-container">', unsafe_allow_html=True)
        st.markdown('<hr class="divider">', unsafe_allow_html=True)

        st.markdown(f"""
        <div class="result-grid">
            <div class="result-box">
                <div class="result-box-label">Original</div>
                <div class="result-box-text">{user_input}</div>
            </div>
            <div class="result-box improved">
                <div class="result-box-label">✦ Improved</div>
                <div class="result-box-text">{result["improved"]}</div>
            </div>
        </div>

        <div class="explanation-box">
            <div class="explanation-box-label">Why it changed</div>
            <div class="explanation-text">{result["explanation"]}</div>
        </div>

        <div class="howtouse-box">
            <div class="howtouse-label">✦ How to use this</div>
            <div class="howtouse-text">Copy the improved prompt and paste it into any AI tool for a better response.</div>
            <div class="howtouse-steps">
                <div class="howtouse-step">
                    <div class="step-num">1</div>
                    <div>Copy the improved prompt from the green box above</div>
                </div>
                <div class="howtouse-step">
                    <div class="step-num">2</div>
                    <div>Open any AI tool — ChatGPT, Gemini, Claude or Copilot</div>
                </div>
                <div class="howtouse-step">
                    <div class="step-num">3</div>
                    <div>Paste the improved prompt and get a much better response!</div>
                </div>
            </div>
        </div>
        </div>
        """, unsafe_allow_html=True)