# Creative-Coding-Assignment-

## Live Website 
[Plot Tracks] (https://plot-tracks.streamlit.app/)

## Table of Contents 
- [General Information](#Plot-Tracks)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Screenshots](#screenshots)
- [Project Files](#project-files)
- [Setup](#setup)
- [Usage](#usage)
- [Project Status](#project-status)
- [Room for Improvement](#room-for-improvement)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## Plot Tracks 
Plot Tracks is a Python web app that suggests a reading soundtrack based on the mood of a chapter or scene.
Users can paste their writing into the app and let the program estimate its mood, or select a mood themselves. The app then recommends songs from a personally selected catalogue
The available moods are:
- Sorrow
- Love
- Neutral
- Determination
- Joy
- Fear
- Tension

Plot Tracks is a creative prototype, not a validated emotion-detection system.

## Technologies Used 
- **VSCODE - Python** — application logic, data structures, text processing, and song selection.
- **Streamlit** — interactive interface, forms, results, and session state.
- **vaderSentiment** — sentiment analysis.
- **CSS** — cream and dark red styling, rounded borders, and buttons.
- **pandas** — included in the current dependencies, although the basic results page does not use it.
- **GitHub** — source-code storage and project documentation.
- **Streamlit Community Cloud** — hosting the public website.
Python’s built-in 'random', 're' and 'urlib.parse' modules handle random song selection, word extraction, and URL encoding.

## Features
- - Enter a chapter or scene.
- Add an optional chapter title 
- Automatically estimate the story’s mood
- Change automatic detection with a manual mood selection.
- Request between one and five songs.
- View the suggested music style and tempo direction.
- Open Spotify searches for the recommended songs.
- Return to the form to edit the story and preferences.
Songs come from a fixed, personally selected catalogue. If a mood contains fewer songs than requested, the app returns only the available number.

## Screenshots 
1. The story input form
2. The soundtrack results page

## Project Files 
app.py = Contains the interface, styling, song catalogue, keyword lists, music profiles, analysis functions, and results page.
requirements.txt = The external Python packages needed to run the app
README.md = Project information, navigation, setup instructions, and limitations

## Set Up 
The main application file is organised into numbered section which made it easier for me plan 
1. **Page settings** — browser title, icon, and layout.
2. **Page design** — CSS for the cream and dark red interface.
3. **Song catalogue** — song titles and artists grouped by mood.
4. **Mood keywords** — words used for keyword matching.
5. **Music direction** — suggested styles, tempo ranges, and explanations.
6. **Analysis functions** — text analysis, song selection, and Spotify link creation.
7. **Session state** — current page, saved inputs, and results.
8. **Shared header** — app title and introduction.
9. **Story form** — user inputs and submission handling.
10. **Results page** — music suggestions and Spotify search links.

###use the hosted version 
Open [Plot Tracks] (https://plot-tracks.streamlit.app/) in a browser.
No local installations are needed using the hosted website

###run the project locally 
You need to install Python 

### 1. download the repository
Download the repository from GitHub and extract it, or clone it using Git.
Open the project folder in VS Code or another code editor 

### 2. open a terminal 
open a terminal in the folder containing 'app.py' and 'requirements.txt.'
In VS Code, select:
```text
terminal --> New Terminal 
```

### 3. Create a virtual environment 
On macOS 
```bash
python3 -m venv .venv
source .venv/bin/activate
```
### 4. install dependencies
With the virtual environment activated, run:

```bash
python -m pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
streamlit
pandas
vaderSentiment
```

### 5. Start the app
Run:
```bash
python -m streamlit run app.py
```
If the browser does not open automatically, open the Local URL displayed in the terminal. Usually:
```text
http://localhost:8501
```
Keep the terminal running while using the app.
To stop the app, press `Ctrl + C` in the terminal.

# Usage
Creating a soundtrack 
1. Enter an optional chapter
2. Paste a chapter or scene into the story box.
3. Leave the mood set to **Automatically detect**, or choose a mood manually.
4. Select the maximum number of songs.
5. Click **Find my tracks**.
6. View the selected mood, music direction, and recommended songs.
7. Open the Spotify search links.
8. Click **Edit my story or mood** to change your inputs.
The story must contain at least 20 characters
The program converts the story to lowercase and extracts individual words.
Spotify links search for the song title and artist. They do not create a playlist in a Spotify account.

### Project Status 
The project has a deployed prototype available at:
[https://plot-tracks.streamlit.app/](https://plot-tracks.streamlit.app/)
Its current scope is a two-page app with a story form and soundtrack results. 

### Current Limitations
- - Keyword matching may miss context, sarcasm, metaphors, and negation.
- The current matching method checks individual words rather than complete multi-word phrases.
- Word variations may not match unless listed separately.
- Repeated keywords can influence the result.
- VADER estimates sentiment rather than directly detecting all seven custom moods.
- Mixed emotions may be simplified into one category or neutral.
- Music preferences are subjective.
- The catalogue is small, and some moods contain fewer songs than others.
- Random selection means recommendations can change between submissions.

### Room for improvement 
The main improvement would be integrating the Spotify API so users could create an actual playlist in their Spotify account. Currently, Plot Tracks only provides search links for individual songs. A future version could let users connect their account, review the recommended tracks, and save them together as a playlist.
Other Possible improvements:
- **A larger song catalogue:** Add more songs to each mood so recommendations are more varied and less repetitive.
- **More accurate mood analysis:** Improve how the program handles context, negation, phrases, and mixed emotions rather than relying mainly on individual keywords.
- **Personalised recommendations:** Let users select preferred genres, artists, or musical styles.
- **User feedback:** Allow users to rate whether the songs suit their scene and use that feedback to revise the recommendations.
- **User testing:** Test the app with readers and writers to identify confusing features and improve the overall experience.

### Acknowledgements 
Learning Resources:
#### Python
- [Python: Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [W3Schools: Nested Dictionaries](https://www.w3schools.com/python/python_dictionaries_nested.asp)
- [Python: Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Python: Built-in Functions](https://docs.python.org/3/library/functions.html)
- [Python: String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python: Random Module](https://docs.python.org/3/library/random.html)
- [Python: URL Parsing and Quoting](https://docs.python.org/3/library/urllib.parse.html)

#### Text processing and sentiment analysis
- [VADER: Official Documentation and Examples](https://github.com/cjhutto/vaderSentiment)
- [Real Python: Sentiment Analysis With NLTK](https://realpython.com/python-nltk-sentiment-analysis/)
- [Google for Developers: Python Regular Expressions](https://developers.google.com/edu/python/regular-expressions)
- [Python: Regular Expression Documentation](https://docs.python.org/3/library/re.html)

The Real Python tutorial uses NLTK’s VADER implementation. This project uses the standalone `vaderSentiment` package.

#### Streamlit and styling
- [Streamlit: Create an App](https://docs.streamlit.io/get-started/tutorials/create-an-app)
- [Streamlit: Using Forms](https://docs.streamlit.io/develop/concepts/architecture/forms)
- [Streamlit: Session State](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state)
- [Streamlit: Caching Overview](https://docs.streamlit.io/develop/concepts/architecture/caching)
- [Streamlit: st.rerun](https://docs.streamlit.io/develop/api-reference/execution-flow/st.rerun)
- [MDN: CSS Styling Basics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics)

#### Video tutorials
- [freeCodeCamp: Build 12 Data Science Apps With Python and Streamlit](https://www.youtube.com/watch?v=JwSS70SZdyM)
- [Corey Schafer: Python Tutorial—Comprehensions](https://www.youtube.com/watch?v=3dt4OGnU5sM)

## Development Assistance 
The song catalogue was personally selected. The mood-to-music suggestions are creative choices rather than scientifically validated classifications.
AI assistance was used to explain programming concepts and troubleshoot errors,

## Contact 
Created by Ella Manalo.

