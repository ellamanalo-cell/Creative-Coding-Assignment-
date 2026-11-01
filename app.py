import random
import re
from urllib.parse import quote

import pandas as pd
import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# 1. page settings 
st.set_page_config(
    page_title="Plot Tracks",
    page_icon= "🎧",
    layout="centered",
)
# 2. Red website-style design
# A red and cream colour scheme creates a modern, warm atmosphere. 
# Streamlit creates will create the interface while the CSS with style and customise the design
st.markdown(
    """
    <style>
   .stApp{
   background-color: #FBF0E3
}
h1, h2, h3, p, label {
    color: #6E1F2A !important;
}
.stButton > button,
.stFormSubmitButton > button,
.stDownloadButton > button,
.stLinkButton > a {
    width: 100%;
    background: #6E1F2A;
    color: white !important;
    border:none;
    border-radius: 10px;
    font-size: 17px;
    font-weight: bold;
    padding: 12px 20px;
}

.stButton > button p,
.stFormSubmitButton > button p,
.stDownloadButton > button p,
.stLinkButton > a p {
    color: white !important;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover,
.stDownloadButton > button:hover,
.stLinkButton > a:hover {
    background: #943444;
}

div[data-testid="stForm"] {
    background: rgba(255, 255, 255, 0.45);
    border: 2px solid #6E1F2A;
    border-radius: 20px;
    padding: 24px;
}
</style>
""",
   unsafe_allow_html=True
)

# 3. Song suggestions stored in Python 
# All songs were chosen personally and not based on any data or research. 
# SpotifyAPI was not used to generate the song suggestions as their was no time to implemenrt it successfully.
SONGS = {
    "sorrow": [
        ("Mia and Sebastian's Theme", "Justin Hurwitz"),
        ("Karma Police", "Radiohead"),
        ("Mystery of Love", "Sufjan Stevens"),
        ("Purple Rain", "Prince"),

    ],
    "love": [
        ("Can't Help Falling in Love", "Elvis Presley"),
        ("Kiss Me", "Sixpence None the Richer"),
        ("Disillusioned", "Daniel Caesar"),
        ("Risk it All", "Bruno Mars"),
        ("Honeybee", "Olivia Rodrigo"),
    ],
    "neutral": [
        ("On a Melancholy Hill", "Gorillaz"),
        ("Circles", "Post Malone"),
        ("Nightcall", "Kavinsky"),
        ("Loser", "Tame Impala"),
        ("The Adults Are Talking", "The Strokes"),
        ("Someday", "The Strokes"),
        
    ],
    "determination": [
        ("Take Me Out", "Franz Ferdinand"),
        ("Can't Stop", "Red Hot Chili Peppers"),
        ("Bizarre Love Triangle", "New Order"),
    
    ],
    "joy": [
        ("Viva La Vida", "Coldplay"),
        ("Teenage Dirtbag", "Wheatus"),
        ("Come On Eileen", "Dexys Midnight Runners"),
        ("We Didn't Start the Fire", "Billy Joel"),
        ("I feel It Coming", "The Weeknd"),
    ],
# I feel fear is such as short part in a novel so not many songs were chosen for this mood
    "fear": [
        ("Feels Like We Only Go Backwards", "Tame Impala"),
        ("The Night Has Opened My Eyes", "The Smiths"),
    
    ],

    "tension": [
        ("Creep", "Radiohead"),
        ("Never Tear Us Apart", "INXS"),
        ("Fill The Void", "The Weeknd"),
        ("You Don't Own Me", "SAYGRACE, G-Eazy")

    ]

}

# 4. Keywords to identify a story mood 
# These moods are all commonly felt in books
#Limitations of this is thart it may accuratelty identify the mood as these as just words and not the conext of the story.
MOOD_KEYWORDS = {
    "sorrow": [
        "ache", "pain", "loss", "heartbreak", "grief", "regret", "lonely", "grey", "sad", "disappointed", "hopeless", "tragic", "empty", "cry", "tears fall down", "distanced", "break up", "goodbye", 
    ],
    "love": [
        "love", "beloved", "kiss", "kissed", "embrace", "affection", "romance", "tender", "cherish", "adore", "cute", "passion", "I love you", "I miss you", "I need you", "I want you", 
    ],
    "neutral": [],
    "determination": ["determined", "resolute", "persistent", "tenacious", "focus", "driven", "keep going", "never give up", "come on", "overcome",
    ],
    "joy": ["lights up", "smile", "laugh", "excited", "happy", "sunshine", "bright", "blessed", "at peace", 
    ],
    "fear": ["worried", "anxious", "nervous", "panic", "uneasy feeling", "scared", "shaken", "frozen", "heart beating fast", "heart racing", "cold sweat", 
    ],
    "tension": ["tight", "tense", "on edge", "friction", "suspense", "unsettled", "conflcit", "strain",
    ]

}

# 5. Music direction 
# BPM ranges are just suggestions, not measured song tempos 

MUSIC_PROFILES = {
    "sorrow": {
        "style": "Soft alternative and soundtrack music",
        "tempo": "60-85 BPM",
        "reason": "For sad scenes", 
    
    },
    "love": {
        "style": "Romantic pop and soft soul",
        "tempo": "65-100 BPM",
        "reason": "For scenes about love",

    },
    "neutral": {
        "style": "Indie and alternative music",
        "tempo": "85-110 BPM",
        "reason": "For everydat scenes"
    
    },
    "determination": {
        "style": "upbeat indie and rock",
        "tempo": "110-140 BPM",
        "reason": "For scenes about not giving up",

    },
    "joy": {
        "style": "Upbeat pop music",
        "tempo": "100-130 BPM",
        "reason": "For happy scenes",

    },
    "fear": {
        "style": "Dark alternative music",
        "tempo": "70-105 BPM",
        "reason": "For scenes about fear",

    },
    "tension": {
        "style": "Dark alternative and pop music",
        "tempo": "80-120 BPM",
        "reason": "For scenes that are suspenseful or tense",

    }
}


# 6. Analysis functions 

@st.cache_resource
def get_analyser():
    return SentimentIntensityAnalyzer()

def analyse_text(text):
    analyser = get_analyser()
    sentiment = analyser.polarity_scores(text)

# converts the story to lowercase and extract words for keyword matching.
# will collects matches to a list.
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

    keyword_counts = {}

    for mood, keywords in MOOD_KEYWORDS.items():
        count = 0

        for word in words:
            if word in keywords:
                count += 1 
        
        keyword_counts[mood] = count
    

    highest_count = max(keyword_counts.values())

    if highest_count >= 2:
        leading_moods = []
        
        for mood, count in keyword_counts.items():
                if count == highest_count:
                    leading_moods.append(mood)
        

        if len(leading_moods) == 1:
            detected_mood = leading_moods[0]
            basis: "This mood had the highest keyword count."

        else:
            detected_mood = "neutral"
            basis = (
                "Two or more moods tied for the highest keyword counts"
                "so this prototype treates the text as mixed/neutral."
            )
   # Use sentiment when there are too many few keyword matches. 
    elif sentiment["compound"] >= 0.3:
        detected_mood = "joy"
        basis = (
            "Few mood keywords matched, so the program used"
            "the psotive overall sentiemnt score."
        )

    elif sentiment["compound"] <= -0.3:
        detected_mood = "sorrow"
        basis = (
            "Few mood keywords matched, so the program used"
            "the negative overall sentiment score."
        )

    else: 
        detected_mood = "neutral"
        basis =(
            "Few mood matched and the overall"
            "sentiment score was near neutral."
        )
    
    return detected_mood, sentiment, keyword_counts, basis

def choose_songs(mood, requested_number):
    catalogue = SONGS[mood]

    # Do not request more songs than are available.
    number_available = min(requested_number, len(catalogue))

    return random.sample(catalogue, k=number_available)

def spotify_search_link(title, artist):
    #Combines the song title and artist into a search phrase.
    #Encode spaces and special characters for the URL.
    query = quote(f"{title} {artist}", safe="")

    #Return a spotify search link, not a direct song link. 
    return f"https://open.spotify.com/search/{query}"

# 7.Session state

if "page" not in st.session_state:
    st.session_state.page = "form"

if "results" not in st.session_state:
    st.session_state.results = None 

if "draft" not in st.session_state:
    st.session_state.draft = {
        "title": "",
        "story": "",
        "mood_choice": "Automatically detect",
        "requested_number": 3,
    }

#8. Shared Website Header 
st.title("🎧 Plot Tracks")
st.write("Your next chapter, with a soundtrack.")
st.divider()

#9. Page 1 : Story Form 
if st.session_state.page == "form":
    st.caption("Step 1 of 2 - Enter your story")
    st.header("Create your reading soundtrack")

    st.write(
        "Paste a scene and let Plot Tracks analyse the mood of your story to suggest a soundtrack"
        "that fits your scene."
    )
# Load the user's saved inputs
draft = st.session_state.draft

mood_options = ["Automatically detect"] + list(SONGS.keys())

with st.form("story_form"):
    title = st.text_input(
        "Chapter or playlist title",
        value=draft["title"],
        placeholder="For example: Chapter 3 - The Journey"
    )

    story = st.text_area(
        "Enter your story here",
        value=draft["story"],
        height=200

    )

    mood_choice = st.selectbox(
        "Choose a mood",
        options=mood_options,
        index=mood_options.index(draft["mood_choice"])

    )

    requested_number = st.slider(
        "Maximum number of songs",
        min_value=1,
        max_value=5,
        value=draft["requested_number"]
    )

    st.caption(
        "If a modd has fewer songs,"
        "only the available tracks will be shown"
    )

    submitted = st.form_submit_button ("Find my tracks")

if submitted:
    #save the inputs for when the user returns 
    st.session_state.draft = {
        "title": title,
        "story": story,
        "mood_choice": mood_choice,
        "requested_number": requested_number,
    }

    if len(story.strip()) < 20:
        st.warning(
            "Please enter at leadt 20 characters of the story text"
        )
    
    else: 
        # Analyse the story 
        detected, sentiment, counts, basis = analyse_text(story)

        # Choose automatic or manual mood.
        if mood_choice == "Automatically detect":
            selected_mood = detected
            selection_method = "Automatic text analysis"
        else: 
            selected_mood = mood_choice
            selection_method = "Your dropdown selection"
        
        # Choose the songs 
        playlist = choose_songs(selected_mood, requested_number)

        #Use a default title if the title box is empty.
        playlist_title = title.strip()

        if playlist_title == "":
            playlist_title = "My Plot Tracks playlist"

        # Save everything for the results page 
        st.session_state.results = {
            "title": playlist_title,
            "detected_mood": detected,
            "selected_mood": selected_mood,
            "selection_method": selection_method,
            "sentiment": sentiment,
            "counts": counts,
            "basis": basis,
            "playlist": playlist,
            "requested_number": requested_number,       
        }

        #Open the results page.
        st.session_state.page = "results"
        st.rerun()

#10. Page 2: Results 
if st.session_state.page == "results":
    #Load the saved results.
    results = st.session_state.results

    #Get the chosen mood and its music profile.
    mood = results["selected_mood"]
    profile = MUSIC_PROFILES[mood]

    st.caption("Step 2 of 2 - Your soundtrack")
    st.header(results["title"])

    st.write("Selected mood:", mood.capitalize())
    st.write("Selection method:", results["selection_method"])

    #Explain the suggested music direction.
    st.write(profile["reason"])
    st.write("Music style:", profile["style"])
    st.write("Suggested tempo:", profile["tempo"])

    st.caption(
        "Tempo ranges are suggestions,"
        "not measured song tempos."
    )

    st.subheader("Your recommended songs")

    # Display each song and its Spotify search link.
    for song, artist in results["playlist"]:
        st.subheader(song)
        st.write(artist)

        link = spotify_search_link(song, artist)
        st.markdown(f"[Search on Spotify]({link})")

    st.caption(
        "Songs come from a personally selected catalogue."
        "Spotify links open searches; they do not create "
        "a playlist in your Spotify account."

    )

    # Return to the form to edit the saved inputs.
    if st.button("Edit my story or mood"):
        st.session_state.page = "form"
        st.rerun()


