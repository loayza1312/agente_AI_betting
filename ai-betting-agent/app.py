import streamlit as st
from main_agent import BettingAgent

st.set_page_config(page_title="AI Betting Agent", page_icon="⚽")
st.title("⚽ AI Sports Betting Agent")
st.markdown("---")

# Input utente
st.sidebar.header("Impostazioni Agente")
budget = st.sidebar.number_input("Tuo Budget (€)", min_value=10, value=100)
match_target = st.selectbox("Scegli un match da analizzare:", ["Inter-Milan", "Juve-Napoli"])

agent = BettingAgent()

if st.button("Avvia Analisi Intelligente"):
    with st.spinner("L'agente sta eseguendo il ciclo di ragionamento..."):
        report = agent.analyze_match(match_target, budget)
        st.write(report)

st.sidebar.info("Questo agente segue l'architettura modulare del Cap. 6 di AI Engineering.")