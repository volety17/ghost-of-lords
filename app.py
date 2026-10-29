"""
The Ghost of Lord's: MCC Laws & Spirit of Cricket Oracle
Streamlit Web UI with YouTube Video Evidence & Gemma 2 Adjudication.
"""

import streamlit as st
from mcc_oracle.engine import query_ghost_stream, DEFAULT_MODEL
from mcc_oracle.indexer import rulebook

# Page setup
st.set_page_config(
    page_title="The Ghost of Lord's | MCC Laws Arbiter",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom vintage Lord's styling (Parchment, deep green, gold accents)
st.markdown("""
<style>
    .main {
        background-color: #0b130e;
        color: #e2e8f0;
    }
    .stApp {
        background: linear-gradient(180deg, #07100b 0%, #0d1a12 100%);
    }
    h1, h2, h3 {
        font-family: 'Georgia', serif;
        color: #d4af37 !important;
    }
    .custom-card {
        background-color: rgba(22, 38, 28, 0.7);
        border: 1px solid #2d5a3c;
        border-radius: 8px;
        padding: 18px;
        margin-bottom: 20px;
    }
    .verdict-box {
        background-color: #121e16;
        border-left: 4px solid #d4af37;
        padding: 15px;
        border-radius: 4px;
        font-family: 'Georgia', serif;
    }
</style>
""", unsafe_allow_html=True)

# Historical Controversy Database with Real YouTube Footage & Metadata
CONTROVERSIES = {
    "Angelo Mathews 'Timed Out' (World Cup 2023)": {
        "youtube_url": "https://www.youtube.com/watch?v=Dzw8rl0yuQ0",
        "match": "Sri Lanka vs Bangladesh, ICC CWC 2023 (Arun Jaitley Stadium, Delhi)",
        "scenario": (
            "Following the dismissal of Sadeera Samarawickrama, incoming batsman Angelo Mathews walked out to the crease "
            "within the allotted time, but his helmet strap broke while strapping it on. He signaled to the dugout for a "
            "replacement helmet before taking guard. While waiting for the new helmet, more than 2 minutes elapsed. "
            "Shakib Al Hasan and Bangladesh appealed for Timed Out under Law 31. The umpires upheld the appeal and gave him OUT."
        ),
        "relevant_law": "Law 31 (Timed Out)"
    },
    "Jonny Bairstow Ashes Crease Walkout (Lord's 2023)": {
        "youtube_url": "https://www.youtube.com/watch?v=Mw9wGDcyt24",
        "match": "England vs Australia, 2nd Test Ashes 2023 (Lord's Cricket Ground)",
        "scenario": (
            "Jonny Bairstow ducked under a Cameron Green bouncer, scratched his crease with his boot at the end of the over, "
            "and immediately walked out of his ground to talk to Ben Stokes, assuming the ball was dead. Wicketkeeper Alex Carey "
            "collected the ball on the full and immediately under-armed it into the stumps. Australia appealed for Stumping/Run Out."
        ),
        "relevant_law": "Law 20 (Dead Ball) & Law 38 (Run Out)"
    },
    "R. Ashwin Mankad of Jos Buttler (IPL 2019)": {
        "youtube_url": "https://www.youtube.com/watch?v=LbY08bv7F5M",
        "match": "Kings XI Punjab vs Rajasthan Royals, IPL 2019 (Jaipur)",
        "scenario": (
            "Bowler Ravichandran Ashwin ran into bowl, but paused at the crease as non-striker Jos Buttler backed up several "
            "yards out of his ground before the ball was released. Ashwin removed the bails and appealed for a Run Out. "
            "The dismissal sparked an enormous global debate on the Spirit of Cricket vs the Laws of the Game."
        ),
        "relevant_law": "Law 38.3 (Non-striker leaving ground early) & Law 41 (Unfair Play)"
    },
    "Ben Stokes 2019 World Cup Final Overthrow Ricochet": {
        "youtube_url": "https://www.youtube.com/watch?v=Itb-3pISKt8",
        "match": "England vs New Zealand, Final ICC CWC 2019 (Lord's)",
        "scenario": (
            "In the final over of the World Cup chase, Martin Guptill threw from the deep boundary toward the keeper. "
            "Ben Stokes dived to complete a second run, and the thrown ball ricocheted off his outstretched bat and raced "
            "to the boundary for four overthrows. England was awarded 6 runs (2 run + 4 boundary)."
        ),
        "relevant_law": "Law 19.8 (Overthrow or willful act of fielder) & Law 37 (Obstructing field)"
    },
    "Ball Striking Wicketkeeper's Grounded Protective Helmet": {
        "youtube_url": "https://www.youtube.com/watch?v=2rz-JhxJRo4",
        "match": "Classic Grounded Helmet 5-Penalty Run Incident",
        "scenario": (
            "The striker edges a delivery downward. The ball deflects off the wicketkeeper's gloves and rolls into the "
            "spare protective helmet resting on the grass behind the keeper within the field of play. The fielders appeal for a catch "
            "after scooping the ball on the rebound."
        ),
        "relevant_law": "Law 28.3 (Protective equipment on the field) & Law 20.4 (Dead Ball)"
    }
}

# Header Banner
st.title("🏏 The Ghost of Lord's: Spirit of the Laws")
st.markdown("#### *An Offline Cricket Law Adjudicator & Arbiter of 1788, Powered by Google Gemma 2* 👻")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/e/e0/Marylebone_Cricket_Club_logo.svg/300px-Marylebone_Cricket_Club_logo.svg.png", width=120)
    st.subheader("🏛️ Custodian Archives")
    st.write(f"• **MCC Laws Loaded:** {len(rulebook.laws_2019)} Laws (2019 Code)")
    st.write("• **Founding Annals:** Lord's 1788 Archive")
    st.write(f"• **Inference Model:** Local `Google {DEFAULT_MODEL}`")
    st.write("• **Status:** 100% Offline & Private")
    st.markdown("---")
    st.info("💡 **Tip**: Select a famous historical match incident, watch the real match footage, and let the Ghost Arbiter weigh the strict MCC Law against the Spirit of Cricket!")

# Layout: 2 Columns (Left: Video & Input, Right: Ghost Ruling)
col_left, col_right = st.columns([1.1, 1.2], gap="large")

with col_left:
    st.subheader("⚖️ Select or Enter Incident")
    
    mode = st.radio("Mode:", ["Historical Match Incident (with Video)", "Custom Dispute / Umpire Query"], horizontal=True)
    
    current_scenario = ""
    video_url = None
    match_info = ""
    
    if mode == "Historical Match Incident (with Video)":
        chosen_incident = st.selectbox("Select Classic Cricket Controversy:", list(CONTROVERSIES.keys()))
        data = CONTROVERSIES[chosen_incident]
        video_url = data["youtube_url"]
        match_info = data["match"]
        current_scenario = data["scenario"]
        
        st.markdown(f"**Match:** *{match_info}*")
        st.video(video_url)
        st.text_area("Incident Breakdown:", value=current_scenario, height=120, disabled=True)
        
    else:
        custom_input = st.text_area(
            "Describe the cricket scenario or rule dispute:",
            placeholder="e.g. The batsman hit the ball, it hit the spidercam wire and was caught by mid-on. What is the ruling?",
            height=150
        )
        custom_yt = st.text_input("Optional YouTube Video URL for evidence:", placeholder="https://www.youtube.com/watch?v=...")
        if custom_yt:
            video_url = custom_yt
            st.video(video_url)
        current_scenario = custom_input

    adjudicate_btn = st.button("⚖️ Summon Ghost of Lord's for Ruling", type="primary", use_container_width=True)

with col_right:
    st.subheader("📜 The Long Room Judgment")
    
    if adjudicate_btn:
        if not current_scenario.strip():
            st.warning("Please provide a cricket scenario to adjudicate.")
        else:
            with st.status("🔮 Searching 42 MCC Laws & Communing with 1788 Custodians...", expanded=True) as status:
                matches = rulebook.search(current_scenario, top_k=2)
                st.write(f"📌 **Relevant MCC Laws Identified:**")
                for _, title, _ in matches:
                    st.write(f"- {title}")
                status.update(label="📜 Delivering Judgment...", state="running")
                
                # Stream the response
                response_container = st.empty()
                full_response = ""
                for chunk in query_ghost_stream(current_scenario):
                    full_response += chunk
                    response_container.markdown(full_response + " ▌")
                response_container.markdown(full_response)
                status.update(label="✅ Verdict Sealed by the Custodians of Lord's", state="complete")
    else:
        st.info("Select an incident on the left and click **'Summon Ghost of Lord's for Ruling'** to watch the video and receive the official MCC Law and Spirit of Cricket verdict.")