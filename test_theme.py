import streamlit as st
import regex as re
from datetime import datetime, date
import requests
import streamlit.components.v1

# --- SESSION STATE ---
if "page" not in st.session_state:
    st.session_state.page = "Home"

if "text_visible" not in st.session_state:
    st.session_state.text_visible = False

# Configure page first
st.set_page_config(
    page_title="Happy Birthday Ilia!",
    page_icon="🎉",
    layout="wide"
)

# --- PAGE CONTENT ---
if st.session_state.page == "Home":
    st.markdown("""
    <style>
        /* Import Google Font */
        @import url('https://fonts.googleapis.com/css2?family=Gloria+Hallelujah&display=swap');
        
        /* Main background */
        .main .block-container {
            background-color: #75020f;
            padding-top: 1rem
            margin-left: 120px;;
        }
                
        /* Set default font for most elements, but exclude second-banner */
        body, .stApp, .main, .banner, div.stButton, button, h1, h2, h3, h4, h5, h6, p:not(.second-banner p), span, div:not(.second-banner) {
            font-family: 'Gloria Hallelujah', cursive !important;
        }

        /* Alternative: target the entire main area */
        .stApp {
            background-color: #000000;
            padding-top: 1rem;
        }
        
        /* Make toggle button font match the banner heading */
        div.stButton > button:first-child {
            font-family: 'Gloria Hallelujah', cursive !important;
        }
        
        .banner {
            background: linear-gradient(90deg, #2b0307 0%, #75020f 100%);
            color: white;
            text-align: center;
            padding: 18px 40px;
            margin: -1.5rem 0 2rem 0;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
            border-radius: 10px;
            font-family: 'Gloria Hallelujah', cursive;
            width: 100vw;
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .banner h1 {
            font-family: 'Gloria Hallelujah', cursive !important;
            font-size: 48px;
            margin: 0;
            text-align: left;
            color: white;
        }
        
        /* Countdown timer box */
        .countdown-timer {
            background-color: #19171b;
            padding: 12px 24px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            font-family: 'Gloria Hallelujah', cursive;
        }

        .countdown-number {
            font-size: 36px;
            font-weight: bold;
            color: #ffffff;
            display: block;
        }
        
        /* Hide Streamlit header and footer */
        header[data-testid="stHeader"] {
            display: none;
        }
        
        footer {
            display: none;
        }
        
        /* Remove default padding */
        .block-container {
            padding-top: 2rem;
        }

        /* Spotlight animation around cursor */
        @keyframes spotlightPulse {
            0%, 100% {
                box-shadow:
                    0 0 20px rgba(255,255,255,0.3),
                    0 0 40px rgba(255,255,255,0.2),
                    0 0 60px rgba(255,255,255,0.1);
            }
            50% {
                box-shadow:
                    0 0 30px rgba(255,255,255,0.4),
                    0 0 50px rgba(255,255,255,0.3),
                    0 0 80px rgba(255,255,255,0.15);
            }
        }

        /* Neon pulse animation - now used for text glow */
        @keyframes neonPulse {
            0%, 100% {
                text-shadow:
                    0 0 5px #fff,
                    0 0 10px #fff,
                    0 0 20px #fff,
                    0 0 30px #fff,
                    0 0 40px #fff,
                    0 0 55px #fff,
                    0 0 75px #fff;
            }
            50% {
                text-shadow:
                    0 0 10px #fff,
                    0 0 20px #fff,
                    0 0 30px #fff,
                    0 0 40px #fff,
                    0 0 50px #fff,
                    0 0 65px #fff,
                    0 0 85px #fff;
            }
        }
        
        /* Second banner */
            .second-banner {
                background: url("https://github.com/yash-2345/2_october/blob/main/red_lily_3.jpg?raw=true") no-repeat top center;
                background-size: 100% auto;
                background-attachment: scroll;
                color: white !important;
                padding: 40px 30px;
                margin: -4rem 0 2rem 0;
                margin-left: -4vw;
                width: 100%;
                border-radius: 0px !important;
                font-family: 'Playfair Display', serif !important;
                text-align: left;
                position: relative !important;
                display: block !important;
                min-height: 200px !important;
        }

        .second-banner h2, 
        .second-banner p {
            position: relative;
            z-index: 1;
            transition: all 0.3s ease-in-out;
            cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" fill="none"><defs><filter id="shine"><feGaussianBlur stdDeviation="2" result="coloredBlur"/><feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge></filter><animateTransform attributeName="transform" attributeType="XML" type="rotate" from="0 16 16" to="360 16 16" dur="2s" repeatCount="indefinite"/></defs><circle cx="14" cy="14" r="10" stroke="white" stroke-width="2" fill="none" filter="url(%23shine)"/><path d="m24 24-6.35-6.35" stroke="white" stroke-width="2" stroke-linecap="round" filter="url(%23shine)"/><circle cx="14" cy="14" r="12" stroke="rgba(255,255,255,0.3)" stroke-width="1" fill="none"><animate attributeName="r" values="12;15;12" dur="1.5s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.3;0.7;0.3" dur="1.5s" repeatCount="indefinite"/></circle></svg>') 16 16, zoom-in;
            opacity: 0.10;
        }
                
        /* Default hidden */
        .second-banner.hide-text h2,
        .second-banner.hide-text p {
            opacity: 0;
            transition: opacity 0.5s ease-in-out;
        }

        /* Visible with glow */
        .second-banner.show-text h2,
        .second-banner.show-text p {
            opacity: 1;
            color: #ffffff;
            text-shadow: 
                0 0 5px #ffffff,
                0 0 10px #ffffff,
                0 0 20px #ffffff;
            transition: opacity 0.5s ease-in-out, text-shadow 0.5s ease-in-out;
        }
                
        /* Button styling */
        div.stButton > button:first-child {
            background-color: transparent;
            color: white;
            border: 2px solid white;
            font-family: 'Gloria Hallelujah', cursive !important;
            font-size: 24px !important;
            font-weight: bold;
            padding: 8px 16px;
            border-radius: 8px;
            margin: 0rem 0 2rem 0;
            margin-left: auto !important;
            margin-right: 0 !important;
            display: block;
            width: fit-content;
            text-align: left;
            transition: all 0.3s ease-in-out;
        }

        div.stButton {
            display: flex;
            justify-content: flex-end !important;
            width: 100% !important;
        }

        div.stButton > button:first-child:hover {
            background-color: white;
            color: black;
            box-shadow: 0 0 10px #ffffff, 0 0 20px #ffffff;
        }

        /* Individual styles - elements become fully visible on hover */
        .second-banner h2 {
            font-family: 'Playfair Display', serif !important;
            font-size: 36px !important;
            font-weight: 700 !important;
            margin-bottom: 20px !important;
            letter-spacing: 1px !important;
        }

        .second-banner h2:hover {
            opacity: 1 !important;
            transform: scale(1.05) !important;
            animation: spotlightPulse 2s ease-in-out infinite !important;
            border-radius: 8px !important;
        }

        .second-banner p {
            font-size: 18px !important;
            line-height: 1.6 !important;
            margin-bottom: 15px !important;
            font-weight: 400 !important;
        }

        .second-banner p:hover {
            opacity: 1 !important;
            transform: translateX(10px) !important;
            animation: spotlightPulse 2s ease-in-out infinite !important;
            border-radius: 6px !important;
        }

        .song-box {
            display: flex !important;
            overflow-x: auto;
            gap: 20px;
            padding: 15px 10px;
            scrollbar-width: thin;
            scrollbar-color: rgba(255,255,255,0.3) transparent;
            background: linear-gradient(135deg, #2b0307 0%, #75020f 50%, #19171b 100%);
            border-radius: 15px;
            margin-top: 20px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.4);
            border: 2px solid rgba(255,255,255,0.1);
        }

        .song-box::-webkit-scrollbar {
            height: 8px;
        }

        .song-box::-webkit-scrollbar-thumb {
            background: rgba(255,255,255,0.3);
            border-radius: 10px;
        }

        .song-card {
            min-width: 50px;
            text-align: center;
            transition: transform 0.3s ease-in-out;
            cursor: pointer;
            text-decoration: none;
            color: white;
            padding: 10px;
            border-radius: 12px;
            background: rgba(255,255,255,0.05);
            flex-shrink: 0;
        }

        .song-card:hover {
            transform: scale(1.1) translateY(-5px);
            background: rgba(255,255,255,0.15);
            box-shadow: 0 8px 20px rgba(255,255,255,0.2);
            color: white;
            text-decoration: none;
        }

        .song-card img {
            width: 80px;
            height: 80px;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
            margin-bottom: 8px;
        }

        .song-title {
            font-size: 13px;
            color: #fff;
            margin-top: 8px;
            font-family: 'Gloria Hallelujah', cursive !important;
            font-weight: bold;
        }

        .song-artist {
            font-size: 11px;
            color: #cccccc;
            margin-top: 4px;
            font-family: 'Gloria Hallelujah', cursive !important;
        }

        .music-header {
            color: white;
            font-family: 'Gloria Hallelujah', cursive !important;
            font-size: 20px;
            margin-bottom: 10px;
            text-align: center;
            text-shadow: 0 0 10px rgba(255,255,255,0.5);
        }
                
        /* Fix for anchor tag styling */
        a.song-card:link,
        a.song-card:visited,
        a.song-card:hover,
        a.song-card:active {
            color: white !important;
            text-decoration: none !important;
        }
        
        /* Image reveal styling */
        .reveal-image {
            opacity: 0.05 !important;
            transition: opacity 0.5s ease-in-out, transform 0.3s ease-in-out !important;
            filter: blur(10px) !important;
            cursor: pointer !important;
            display: block !important;
            position: relative !important;
            z-index: 10 !important;
        }

        .reveal-image:hover {
            opacity: 1 !important;
            filter: blur(0px) !important;
            transform: scale(1.05) !important;
            box-shadow: 0 0 30px rgba(255,255,255,0.6) !important;
        }

        /* When lights are on, images are visible */
        .show-text .reveal-image {
            opacity: 1 !important;
            filter: blur(0px) !important;
        }

        .hide-text .reveal-image {
            opacity: 0.05 !important;
            filter: blur(10px) !important;
        }
    </style>
    """, unsafe_allow_html=True)


    # Banner HTML with countdown timer
    from datetime import datetime

    # Calculate days since a specific date (change this date as needed)
    start_date = datetime(2024, 5, 30)  # Change this to your desired start date
    current_date = datetime.now()
    days_passed = (current_date - start_date).days

    st.markdown(f"""
    <div class='banner'>
        <h1>Happy Birthday Ilia! <img src="https://github.com/yash-2345/2_october/blob/main/IMG-20250908-WA0007-removebg-preview-removebg-preview%20(1).png?raw=true" style="height: 70px; vertical-align: middle; margin-left: 10px;"></h1>
        <div class='countdown-timer'>
            <span class='countdown-number'>{days_passed}</span>
            Days Since<br>May 30, 2024
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- SESSION STATE ---
    if "text_visible" not in st.session_state:
        st.session_state.text_visible = False

    # Toggle button - positioned to the right
    col1, col2, col3 = st.columns([3, 1, 1])
    with col3:
        if st.button("turn the lights on! or hover starting from mocha to reveal secrets.", key="lights_toggle"):
            st.session_state.text_visible = not st.session_state.text_visible

    # Which CSS class to apply
    mode_class = "show-text" if st.session_state.text_visible else "hide-text"

    def wrap_words_in_p_tags(text, words_per_p=4):
        # Split text into HTML tags and regular text
        # This regex finds HTML tags and keeps them separate
        parts = re.split(r'(<[^>]*>)', text)
        
        html_content = ""
        word_buffer = []
        
        for part in parts:
            # Skip empty parts
            if not part.strip():
                continue
                
            # If it's an HTML tag, add it as-is
            if part.strip().startswith('<') and part.strip().endswith('>'):
                # If we have words in buffer, wrap them first
                if word_buffer:
                    html_content += f"<p style='display: inline;'>{' '.join(word_buffer)} </p>"
                    word_buffer = []
                # Add the HTML tag as-is
                html_content += part
            else:
                # It's regular text, split into words
                words = part.split()
                for word in words:
                    word_buffer.append(word)
                    # If we have enough words, wrap them
                    if len(word_buffer) >= words_per_p:
                        html_content += f"<p style='display: inline;'>{' '.join(word_buffer)} </p>"
                        word_buffer = []
        
        # Handle any remaining words
        if word_buffer:
            html_content += f"<p style='display: inline;'>{' '.join(word_buffer)} </p>"
        
        return html_content

    text_part1 = """<img src="https://github.com/yash-2345/photos/blob/main/IMG-20250908-WA0014-removebg-preview.png?raw=true" style="height: 50px; vertical-align: left; margin-left: 10px;"> Heyyy there Birthday girl ;)
        prettiest thing in my life, hope this truly enlightens your day in some way ;)) This took me around 50 hours (approximately) MAINLY due to not being well versed in web development.
        But I gave it as much attention and effort as I could because you're special. More than anything else in this universe and ofc you were my motivation as I was making this
        so it was FUN. If this brings a smile on that gorgeous prettiest face, then it has served its purpose well. Happy 21 years my love. <br> 
        <br>
        As I always say you are SOOOOO pretty. You are effortlessly gorgeous. You are an absolute cutie. You are the reason why I even open my gallery app most of the times LMAO.
        YOU are freaking hot and at this point, it would be quite an understatement if I say I am crazy for you. There does not go a minute when I dont't think about you. In my mind, 
        your existence is constant. When are you paying the rent? AHAHAHAH JK (ofc). I'm insane for you and only you, forever. This insanity is never gonna diminish.
        Every voice call with you, your every voice message is something I adore with all my heart. You are so beautiful I worship every pic of yours you send me and I'm always looking out for more (heart eyes emoji)
        Honestly, you are my everything, you are my whole damn universe. I love you so so so so so much.<br>
        <br>
        Growing up with you is a priviledge and I'm happy to have found you when I did. I have already known you in ways I doubt anyone else has and you have seen me in ways that no one else ever has.
        I'm lucky it is that way. I'm your biggest supporter, your biggest fan. I'd love for you to use me on days where your mind tells you bad things abt yourself - even if it helps just a bit. I want
        you to know I'm always here for you, always. You and me, we are a team. I'm yours forever.
        If you're either Katsu, Fay, Ilia, Myvene, Youn, Aurea (the list goes on) then i love you.<br>
        <br>
        Once again, i hope you like this b'day gift and i love you very very very much. <br><br><br><br><br>"""

    reveal_images = """
    <img src="https://github.com/yash-2345/2_october/blob/main/IMG_0820-removebg-preview.png?raw=true" class="reveal-image" style="height: 250px; display: block; margin: 0 auto;">
    <br><br><br>
    <img src="https://github.com/yash-2345/2_october/blob/main/IMG_0821-removebg-preview.png?raw=true" class="reveal-image" style="height: 290px; display: block; margin: 0 auto;">
    <br><br><br>
    <img src="https://github.com/yash-2345/2_october/blob/main/IMG_0822-removebg-preview(1).png?raw=true" class="reveal-image" style="height: 230px; display: block; margin: 0 auto;">
    """

    text_part2 = """<br><br><img src="https://github.com/yash-2345/2_october/blob/main/IMG_0820-removebg-preview(1).png?raw=true" style="height: 10px; vertical-align: left; margin-left: 5px;">
    <br><br><br><br>
    """
    reveal_images2 = """<br><br><br><br><br><img src="https://github.com/yash-2345/2_october/blob/main/R.gif?raw=true" class="reveal-image" style="height: 250px; display: block; margin: 0 0 0 auto;">"""

    html_text = wrap_words_in_p_tags(text_part1, 4) + reveal_images + text_part2 + reveal_images2


    # --- Banner render with music player beside it ---
    col_banner, col_music = st.columns([18, 3])

    with col_banner:
        st.markdown(f"""
        <div class='second-banner {mode_class}'>
            {html_text}
        </div>
        """, unsafe_allow_html=True)

    with col_music:
        st.markdown("""
        <div style="text-align: center; color: white; font-family: 'Playfair Display', serif !important; font-size: 20px; margin-bottom: 15px;">
            <img src="https://github.com/yash-2345/photos/blob/main/IMG-20250908-WA0009-removebg-preview.png?raw=true" style="height: 30px; vertical-align: middle; margin-right: 8px;">
            Songs Dedicated<br>to Her <img src="https://github.com/yash-2345/photos/blob/main/IMG-20250908-WA0009-removebg-preview.png?raw=true" style="height: 30px; vertical-align: middle; margin-left: 8px;">
        </div>
        """, unsafe_allow_html=True)
        songs = [
            {
                "title": "A Sky Full of Stars",
                "artist": "Coldplay",
                "icon": "https://image-cdn-fa.spotifycdn.com/image/ab67616d00001e02e5a95573f1b91234630fd2cf",
                "link": "https://open.spotify.com/track/0FDzzruyVECATHXKHFs9eJ?si=fdae3c2fe51243f4"
            },
            {
                "title": "Meet Me At Our Spot",
                "artist": "THE ANXIETY",
                "icon": "https://image-cdn-ak.spotifycdn.com/image/ab67616d00001e02024ea7e883a713a3ad552a71",
                "link": "https://open.spotify.com/track/07MDkzWARZaLEdKxo6yArG?si=653f63fcf5f847c9"
            },
            {
                "title": "Locked out of Heaven",
                "artist": "Bruno Mars",
                "icon": "https://image-cdn-ak.spotifycdn.com/image/ab67616d00001e02926f43e7cce571e62720fd46",
                "link": "https://open.spotify.com/track/3w3y8KPTfNeOKPiqUTakBh?si=8614e4b470b84839"
            },
            {
                "title": "Soft Spot",
                "artist": "keshi",
                "icon": "https://image-cdn-fa.spotifycdn.com/image/ab67616d00001e02617997bc09bb7fa23624eff5",
                "link": "https://open.spotify.com/track/2aL4lMGhWdPpyPL6COPou7?si=5073faf417d944a2"
            },
            {
                "title": "DJ Got Us Fallin' In Love",
                "artist": "USHER, Pitbull",
                "icon": "https://image-cdn-ak.spotifycdn.com/image/ab67616d00001e0286b0c9728ad3ed338eaeea79",
                "link": "https://open.spotify.com/track/4356Typ82hUiFAynbLYbPn?si=b93ca6d4b63145c2"
            },
            {
                "title": "Agora Hills",
                "artist": "Doja cat",
                "icon": "https://image-cdn-fa.spotifycdn.com/image/ab67616d00001e02ab54aadb2320f1c687735d1e",
                "link": "https://open.spotify.com/track/7dJYggqjKo71KI9sLzqCs8?si=2ecf02fde1aa430f"
            },
            {
                "title": "supernatural",
                "artist": "Ariana Grande",
                "icon": "https://image-cdn-ak.spotifycdn.com/image/ab67616d00001e028b58d20f1b77295730db15b4",
                "link": "https://open.spotify.com/track/142PiXzA84lmEw2RstFHFa?si=ec22e1c25baa4507"
            },
            {
                "title": "Strawberries & Cigarettes",
                "artist": "Troye sivan",
                "icon": "https://image-cdn-fa.spotifycdn.com/image/ab67616d00001e02c9eb4c87e1d7f5353908b712",
                "link": "https://open.spotify.com/track/3afkJSKX0EAMsJXTZnDXXJ?si=0a629b3a9608421d"
            },
            {
                "title": "Discovery Channel",
                "artist": "Hayley Williams",
                "icon": "https://image-cdn-ak.spotifycdn.com/image/ab67616d00001e02850c0e3fdd3b3b5cb0b7fa63",
                "link": "https://open.spotify.com/track/7pIF9sU2UW8FuetaDaNXiC?si=830c6c8c2bf04b7f"
            },
            {
                "title": "Still into You",
                "artist": "Paramore",
                "icon": "https://image-cdn-ak.spotifycdn.com/image/ab67616d00001e02532033d0d90736f661c13d35",
                "link": "https://open.spotify.com/track/1yjY7rpaAQvKwpdUliHx0d?si=85085b51286243f0"
            },
        ]
        
        # Display songs vertically
        for song in songs:
            st.markdown(f"""
            <div style="text-align: center; background: rgba(255,255,255,0.05); padding: 15px; border-radius: 12px; margin: 10px 0;">
                <a href="{song['link']}" target="_blank">
                    <img src="{song['icon']}" width="80" style="border-radius: 12px; margin-bottom: 8px;">
                </a>
                <p style="color: white; font-size: 13px; margin: 5px 0; font-weight: bold;">{song['title']}</p>
                <p style="color: #cccccc; font-size: 11px; margin: 0;">{song['artist']}</p>
            </div>
            """, unsafe_allow_html=True)

elif st.session_state.page == "Library":
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Gloria+Hallelujah&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap');
                
        .stApp {
            background: linear-gradient(135deg, #2b0307 0%, #51080d 50%, #19171b 100%) !important;
        }
        
        header[data-testid="stHeader"] {
            display: none;
        }
        
        * {
            font-size: inherit !important;
        }
        
        header[data-testid="stHeader"] {
            display: none;
        }

        h1 {
            font-family: 'Gloria Hallelujah', cursive !important;
            font-size: 48px !important; /* Set your desired base font size here */
            display: flex;
            align-items: center;
        }
        
        h1:before {
            content: "";
            display: inline-block;
            background-image: url('https://github.com/yash-2345/photos/blob/main/removebg-removebg-preview.png?raw=true');
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
            width: 60px;
            height: 60px;
            margin-right: 15px;
            vertical-align: middle;
        }
                
        /* Navigation buttons font */
        div[data-testid="column"] button {
            font-family: 'Gloria Hallelujah', cursive !important;
        }
        
        /* Button styles */
        .element-container:has(#button-after) + div button {
            white-space: pre-line !important;
            background-image: url('https://github.com/yash-2345/2_october/blob/main/SplitImg.com_1.jpg?raw=true') !important;
            background-size: cover !important;
            width: 100% !important;
            height: 500px !important;
            font-family: 'Playfair Display', serif !important;
            font-size: 48px !important;
            font-weight: bold !important;
            color: white !important;
            border-radius: 20px !important;
            border: 3px solid white !important;
        }
        
        .element-container:has(#button-after-2) + div button {
            background-image: url('https://github.com/yash-2345/2_october/blob/main/SplitImg.com_2.jpg?raw=true') !important;
            background-size: cover !important;
            width: 100% !important;
            height: 500px !important;
            font-size: 48px !important;
            font-weight: bold !important;
            color: white !important;
            border-radius: 20px !important;
            border: 3px solid white !important;
        }
        
        .element-container:has(#button-after-3) + div button {
            background-image: url('https://github.com/yash-2345/2_october/blob/main/SplitImg.com_3.jpg?raw=true') !important;
            background-size: cover !important;
            width: 100% !important;
            height: 500px !important;
            font-size: 48px !important;
            font-weight: bold !important;
            color: white !important;
            border-radius: 20px !important;
            border: 3px solid white !important;
        }
        
        .element-container:has(#button-after-4) + div button {
            background-image: url('https://github.com/yash-2345/2_october/blob/main/SplitImg.com_4.jpg?raw=true') !important;
            background-size: cover !important;
            width: 100% !important;
            height: 500px !important;
            font-size: 48px !important;
            font-weight: bold !important;
            color: white !important;
            border-radius: 20px !important;
            border: 3px solid white !important;
        }
                
        .element-container:has(#button-after-5) + div button {
            background-image: url('https://github.com/yash-2345/2_october/blob/main/SplitImg.com_5.jpg?raw=true') !important;
            background-size: cover !important;
            width: 100% !important;
            height: 500px !important;
            font-size: 48px !important;
            font-weight: bold !important;
            color: white !important;
            border-radius: 20px !important;
            border: 3px solid white !important;
        }
                
        .element-container:has(#button-after-6) + div button {
            background-image: url('https://github.com/yash-2345/2_october/blob/main/SplitImg.com_6.jpg?raw=true') !important;
            background-size: cover !important;
            width: 100% !important;
            height: 500px !important;
            font-size: 48px !important;
            font-weight: bold !important;
            color: white !important;
            border-radius: 20px !important;
            border: 3px solid white !important;
        }
                
    </style>
    """, unsafe_allow_html=True)

    st.title("Our Memory Library")
    
    # First row
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)
        if st.button("My every letter to you <3", use_container_width=True):
            st.session_state.page = "Photos"
            st.rerun()
    
    with col2:
        st.markdown('<span id="button-after-2"></span>', unsafe_allow_html=True)
        if st.button("These videos I took??", use_container_width=True):
            st.session_state.page = "Videos"
            st.rerun()
    
    with col3:
        st.markdown('<span id="button-after-3"></span>', unsafe_allow_html=True)
        if st.button("Memories of us I adore.", use_container_width=True):
            st.session_state.page = "Messages"
            st.rerun()
    
    # Second row
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.markdown('<span id="button-after-4"></span>', unsafe_allow_html=True)
        if st.button("Pictures!", use_container_width=True):
            st.session_state.page = "Voice Notes"
            st.rerun()
    
    with col5:
        st.markdown('<span id="button-after-5"></span>', unsafe_allow_html=True)
        if st.button("This is you❗❗", use_container_width=True):
            st.session_state.page = "Memories"
            st.rerun()
    
    with col6:
        st.markdown('<span id="button-after-6"></span>', unsafe_allow_html=True)
        if st.button("Our watchlist!", use_container_width=True):
            st.session_state.page = "Love Letters"
            st.rerun()

elif st.session_state.page == "Photos":  # This corresponds to "My every letter to you <3" button
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Gloria+Hallelujah&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap');
                
            * {
                font-family: 'Gloria Hallelujah', cursive !important;
            }
                
            .stApp {
                background: #000000 !important;
            }
        
            header[data-testid="stHeader"] {
                display: none;
            }
        
            .letters-header {
                font-family: 'Gloria Hallelujah', cursive !important;
                color: white;
                text-align: center;
                font-size: 36px;
                margin-bottom: 30px;
                text-shadow: 0 0 10px rgba(255,255,255,0.5);
            }
        
            /* Ghost white buttons with black text (except Library button) */
            div.stButton > button:not([key="back_to_library_photos"]) {
                background-color: #f8f8ff !important;
                color: black !important;
                border: 2px solid #f8f8ff !important;
                font-family: 'Gloria Hallelujah', cursive !important;
                font-weight: bold !important;
                padding: 15px 20px !important;
                border-radius: 15px !important;
                transition: all 0.3s ease !important;
            }
            
            div.stButton > button:not([key="back_to_library_photos"]):hover {
                background-color: rgba(248, 248, 255, 0.9) !important;
                box-shadow: 0 5px 20px rgba(248, 248, 255, 0.3) !important;
                transform: translateY(-2px) !important;
            }
            
            /* Keep Library button with original style */
            button[key="back_to_library_photos"] {
                background: transparent !important;
                border: 2px solid white !important;
                color: white !important;
                padding: 10px 20px !important;
                border-radius: 25px !important;
                font-family: 'Gloria Hallelujah', cursive !important;
            }
            
            button[key="back_to_library_photos"]:hover {
                background: white !important;
                color: black !important;
            }
        
            .letter-card {
                background: rgba(255,255,255,0.1);
                border: 2px solid rgba(255,255,255,0.3);
                border-radius: 15px;
                padding: 20px;
                margin: 15px 0;
                cursor: pointer;
                transition: all 0.3s ease;
                backdrop-filter: blur(10px);
            }
        
            .letter-card:hover {
                background: rgba(255,255,255,0.2);
                border-color: white;
                transform: translateY(-5px);
                box-shadow: 0 10px 25px rgba(255,255,255,0.2);
            }
        
            .letter-title {
                font-family: 'Playfair Display', serif;
                font-size: 24px;
                color: white;
                margin: 0;
                font-weight: bold;
            }
        
            .letter-date {
                font-family: 'Gloria Hallelujah', cursive;
                font-size: 16px;
                color: #cccccc;
                margin: 5px 0 0 0;
            }
        
            .letter-preview {
                font-family: 'Gloria Hallelujah', cursive;
                font-size: 16px;
                color: #e0e0e0;
                margin: 10px 0 0 0;
                font-style: italic;
            }
        
            .letter-display {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 30px;
                padding: 20px;
            }
        
            .handwritten-letter {
                max-width: 80%;
                width: 100%;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                transition: transform 0.3s ease;
                background: #f8f8ff;
                padding: 10px;
            }
        
            .handwritten-letter:hover {
                transform: scale(1.02);
                box-shadow: 0 15px 40px rgba(255,255,255,0.2);
            }
        
            .handwritten-letter img {
                width: 100%;
                height: auto;
                border-radius: 10px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            }
        
            .letter-title-display {
                font-family: 'Playfair Display', serif;
                font-size: 32px;
                color: white;
                text-align: center;
                margin-bottom: 10px;
                text-shadow: 0 0 15px rgba(255,255,255,0.6);
            }
        
            .letter-date-display {
                font-family: 'Gloria Hallelujah', cursive;
                font-size: 18px;
                color: #e0e0e0;
                text-align: center;
                margin-bottom: 20px;
            }
        
            .back-button {
                background: transparent;
                border: 2px solid white;
                color: white;
                padding: 10px 20px;
                border-radius: 25px;
                font-family: 'Gloria Hallelujah', cursive;
                cursor: pointer;
                margin: 10px 0;
                transition: all 0.3s ease;
            }
        
            .back-button:hover {
                background: white;
                color: black;
            }
        </style>
        """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 6, 1])
    with col1:
        if st.button("Library", key="back_to_library_photos"):
            st.session_state.page = "Library"
            st.rerun()
    
    # Initialize selected letter state
    if "selected_letter" not in st.session_state:
        st.session_state.selected_letter = None
    
    # Define your handwritten letters data
    letters_data = {
        "Letter #10": {
            "date": "October 1, 2025",
            "preview": "Letter #10",
            "letter_images": [
                "https://github.com/yash-2345/letters/blob/main/Letter%2010.1.jpg?raw=true",
                "https://github.com/yash-2345/letters/blob/main/Letter%2010.2.jpg?raw=true"
            ]
        },
        "Letter #9": {
            "date": "August 25, 2025",
            "preview": "Letter #9",
            "letter_images": [
                "https://github.com/yash-2345/letters/blob/main/Letter%209.1.jpg?raw=true",
                "https://github.com/yash-2345/letters/blob/main/Letter%209.2.jpg?raw=true", 
                "https://github.com/yash-2345/letters/blob/main/Letter%209.3.jpg?raw=true", 
                "https://github.com/yash-2345/letters/blob/main/Letter%209.4.jpg?raw=true"
            ]
        },
        "Letter #8": {
            "date": "April 30, 2025",
            "preview": "Letter #8",
            "letter_images": [
                "https://github.com/yash-2345/letters/blob/main/Letter%20%2310.jpg?raw=true"
            ]
        },
        "Letter #7": {
            "date": "January 16, 2025",
            "preview": "Letter #7",
            "letter_images": [
                "https://github.com/yash-2345/letters/blob/main/Letter%20%239.jpg?raw=true"
            ]
        },
        "Letter #6": {
            "date": "January 15, 2025",
            "preview": "Letter #6",
            "letter_images": [
                "https://github.com/yash-2345/letters/blob/main/Letter%20%238.jpg?raw=true"
            ]
        },
        "Letter #5": {
            "date": "November 30, 2024",
            "preview": "Letter #5",
            "letter_images": [
                "https://github.com/yash-2345/letters/blob/main/Letter%20%236.jpg?raw=true"
            ]
        },
        "Letter #4": {
            "date": "October 2, 2024",
            "preview": "Letter #4",
            "letter_images": [
                "https://github.com/yash-2345/letters/blob/main/Letter%20%235.jpg?raw=true"
            ]
        },
        "Letter #3": {
            "date": "July 30, 2024",
            "preview": "Letter #3",
            "letter_images": [
                "https://github.com/yash-2345/letters/blob/main/Letter%20%233.jpg?raw=true"
            ]
        },
        "Letter #2": {
            "date": "July 2, 2024",
            "preview": "Letter #2",
            "letter_images": [
                "https://github.com/yash-2345/letters/blob/main/Letter%20%232.jpg?raw=true"
            ]
        },
        "Letter #1": {
            "date": "May 28, 2024",
            "preview": "Letter #1",
            "letter_images": [
                "https://github.com/yash-2345/letters/blob/main/Letter%20%231.jpg?raw=true"
            ]
        }
    }
    
    # Show either the letters list or the selected letter's images
    if st.session_state.selected_letter is None:
        # Show letters list
        st.markdown("<h1 class='letters-header'>My every letter to you <3</h1>", unsafe_allow_html=True)
        
        for letter_title, letter_data in letters_data.items():
            # Create clickable letter cards
            letter_html = f"""
            <div class='letter-card' onclick='selectLetter("{letter_title}")'>
                <h3 class='letter-title'>{letter_title}</h3>
                <p class='letter-date'>{letter_data['date']}</p>
                <p class='letter-preview'>{letter_data['preview']}</p>
            </div>
            """
            
            if st.button(f"{letter_title}", key=f"letter_{letter_title}", use_container_width=True):
                st.session_state.selected_letter = letter_title
                st.rerun()
    
    else:
        # Show selected letter's handwritten image
        selected_data = letters_data[st.session_state.selected_letter]
        
        # Back button
        if st.button("← Back to Letters", key="back_to_letters"):
            st.session_state.selected_letter = None
            st.rerun()
        
        # Letter display
        st.markdown(f"""
        <h1 class='letter-title-display'>{st.session_state.selected_letter}</h1>
        <p class='letter-date-display'>{selected_data['date']}</p>
        """, unsafe_allow_html=True)
        
        # Display the handwritten letter images with slider
        if len(selected_data['letter_images']) > 1:
            # Initialize slider index in session state
            if 'slider_index' not in st.session_state:
                st.session_state.slider_index = 0
            
            # Slider CSS
            st.markdown("""
            <style>
                .slider-container {
                    position: relative;
                    max-width: 80%;
                    margin: 30px auto;
                    text-align: center;
                }
                
                .slider-image {
                    width: 100%;
                    border-radius: 15px;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                    background: white;
                    padding: 10px;
                }
                
                .slider-controls {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    margin-top: 20px;
                    gap: 20px;
                }
                
                .page-indicator {
                    color: white;
                    font-family: 'Gloria Hallelujah', cursive;
                    font-size: 18px;
                }
            </style>
            """, unsafe_allow_html=True)
            
            # Display current image
            current_img = selected_data['letter_images'][st.session_state.slider_index]
            st.markdown(f"""
            <div class='slider-container'>
                <img src='{current_img}' class='slider-image' alt='Page {st.session_state.slider_index + 1}'>
            </div>
            """, unsafe_allow_html=True)
            
            # Navigation buttons
            col1, col2, col3 = st.columns([1, 2, 1])
            
            with col1:
                if st.button("⬅️ Previous", key="prev_slide", use_container_width=True):
                    if st.session_state.slider_index > 0:
                        st.session_state.slider_index -= 1
                        st.rerun()
            
            with col2:
                st.markdown(f"""
                <div class='page-indicator' style='text-align: center; padding: 10px;'>
                    Page {st.session_state.slider_index + 1} of {len(selected_data['letter_images'])}
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                if st.button("Next ➡️", key="next_slide", use_container_width=True):
                    if st.session_state.slider_index < len(selected_data['letter_images']) - 1:
                        st.session_state.slider_index += 1
                        st.rerun()
            
        else:
            # Single image - show normally
            st.markdown(f"""
            <div class='letter-display'>
                <div class='handwritten-letter'>
                    <img src='{selected_data['letter_images'][0]}' alt='{st.session_state.selected_letter}'>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
elif st.session_state.page == "Videos":  # This corresponds to "These videos I took??" button
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Gloria+Hallelujah&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap');
                
        .stApp {
            background: #000000 !important;
        }
        
        header[data-testid="stHeader"] {
            display: none;
        }
        
        .videos-header {
            font-family: 'Gloria Hallelujah', cursive !important;
            color: white;
            text-align: center;
            font-size: 36px;
            margin-bottom: 30px;
            text-shadow: 0 0 10px rgba(255,255,255,0.5);
        }
        
        .video-card {
            background: rgba(255,255,255,0.1);
            border: 2px solid rgba(255,255,255,0.3);
            border-radius: 15px;
            padding: 20px;
            margin: 15px 0;
            cursor: pointer;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
            display: flex;
            align-items: center;
            gap: 20px;
        }
        
        .video-card:hover {
            background: rgba(255,255,255,0.2);
            border-color: white;
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(255,255,255,0.2);
        }
        
        .video-thumbnail {
            width: 120px;
            height: 80px;
            border-radius: 10px;
            object-fit: cover;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            flex-shrink: 0;
        }
        
        .video-info {
            flex: 1;
        }
        
        .video-title {
            font-family: 'Playfair Display', serif;
            font-size: 24px;
            color: white;
            margin: 0;
            font-weight: bold;
        }
        
        .video-date {
            font-family: 'Gloria Hallelujah', cursive;
            font-size: 16px;
            color: #cccccc;
            margin: 5px 0;
        }
        
        .video-description {
            font-family: 'Playfair Display', serif;
            font-size: 16px;
            color: #e0e0e0;
            margin: 10px 0 0 0;
            font-style: italic;
        }
        
        .video-duration {
            background: rgba(0,0,0,0.7);
            color: white;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-family: 'Gloria Hallelujah', cursive;
            position: absolute;
            bottom: 5px;
            right: 5px;
        }
        
        .play-icon {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 30px;
            height: 30px;
            background: rgba(255,255,255,0.9);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 14px;
            color: #2b0307;
        }
        
        .video-display {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 30px;
            padding: 20px;
        }
        
        .video-player {
            width: 30% !important;
            max-width: 500px !important;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            overflow: hidden;
            background: black;
        }
        
        .video-player video {
            width: 100% !important;
            height: auto !important;
            border-radius: 15px;
        }
        
        .video-title-display {
            font-family: 'Playfair Display', serif;
            font-size: 32px;
            color: white;
            text-align: center;
            margin-bottom: 10px;
            text-shadow: 0 0 15px rgba(255,255,255,0.6);
        }
        
        .video-date-display {
            font-family: 'Gloria Hallelujah', cursive;
            font-size: 18px;
            color: #e0e0e0;
            text-align: center;
            margin-bottom: 20px;
        }
        
        .video-description-display {
            font-family: 'Playfair Display', serif;
            font-size: 18px;
            color: #e0e0e0;
            text-align: center;
            margin-bottom: 30px;
            max-width: 600px;
            line-height: 1.6;
        }
        
        .back-button {
            background: transparent;
            border: 2px solid white;
            color: white;
            padding: 10px 20px;
            border-radius: 25px;
            font-family: 'Gloria Hallelujah', cursive;
            cursor: pointer;
            margin: 10px 0;
            transition: all 0.3s ease;
        }
        
        .back-button:hover {
            background: white;
            color: black;
        }
        
        .thumbnail-container {
            position: relative;
            display: inline-block;
        }
                
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 6, 1])
    with col1:
        if st.button("Library", key="back_to_library_photos"):
            st.session_state.page = "Library"
            st.rerun()
    
    # Initialize selected video state
    if "selected_video" not in st.session_state:
        st.session_state.selected_video = None
    
    # Define your videos data
    videos_data = {
        "Happy B'day!!!!": {
            "date": "October 2, 2025",
            "description": "Happy B'day!!!!",
            "duration": "0:14",
            "thumbnail": "https://github.com/yash-2345/letters/blob/main/WhatsApp%20Image%202025-10-01%20at%2011.31.44_4cbcb009.jpg?raw=true",  # Replace with thumbnail image URL
            "video_url": "https://github.com/yash-2345/letters/raw/main/WhatsApp%20Video%202025-10-01%20at%2011.34.07_7a2cadf3.mp4"  # Replace with your video URL
        },
    }
    
    # Show either the videos list or the selected video
    if st.session_state.selected_video is None:
        # Show videos list
        st.markdown("<h1 class='videos-header'>These videos I took??</h1>", unsafe_allow_html=True)
        
        for video_title, video_data in videos_data.items():
            # Create clickable video cards
            if st.button(f"{video_title}", key=f"video_{video_title}", use_container_width=True):
                st.session_state.selected_video = video_title
                st.rerun()
            
            # Display video card info
            st.markdown(f"""
            <div style='background: rgba(255,255,255,0.1); border-radius: 10px; padding: 15px; margin: -10px 0 20px 0; border: 1px solid rgba(255,255,255,0.2);'>
                <div style='display: flex; align-items: center; gap: 15px;'>
                    <div class='thumbnail-container'>
                        <img src='{video_data['thumbnail']}' class='video-thumbnail' alt='Video thumbnail'>
                        <div class='play-icon'>▶</div>
                        <div class='video-duration'>{video_data['duration']}</div>
                    </div>
                    <div class='video-info'>
                        <p class='video-date'>{video_data['date']}</p>
                        <p class='video-description'>{video_data['description']}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    else:
        # Show selected video
        selected_data = videos_data[st.session_state.selected_video]
        
        # Back button
        if st.button("← Back to Videos", key="back_to_videos"):
            st.session_state.selected_video = None
            st.rerun()
        
        # Video display
        st.markdown(f"""
        <h1 class='video-title-display'>{st.session_state.selected_video}</h1>
        <p class='video-date-display'>{selected_data['date']}</p>
        <p class='video-description-display'>{selected_data['description']}</p>
        """, unsafe_allow_html=True)
        
        # Display the video
        st.markdown(f"""
        <div class='video-display'>
            <div class='video-player'>
                <video controls style='width: 100%; height: auto;'>
                    <source src='{selected_data['video_url']}' type='video/mp4'>
                    Your browser does not support the video tag.
                </video>
            </div>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.page == "Messages":  # This corresponds to "Memories of us I adore." button
    import random
    
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Gloria+Hallelujah&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap');
                
        .stApp {
            background: #000000 !important;
        }
        
        header[data-testid="stHeader"] {
            display: none;
        }
        
        .memories-header {
            font-family: 'Gloria Hallelujah', cursive !important;
            color: white;
            text-align: center;
            font-size: 36px;
            margin-bottom: 30px;
            text-shadow: 0 0 10px rgba(255,255,255,0.5);
        }
        
        .image-display {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 30px 0;
        }
        
        .main-image {
            max-width: 400px !important;
            width: 100% !important;
            height: auto !important;
            border-radius: 20px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.5);
            transition: transform 0.3s ease;
            margin-bottom: 20px;
            animation: glow 3s ease-in-out infinite alternate;
        }
        
        .main-image:hover {
            transform: scale(1.02);
            box-shadow: 0 20px 50px rgba(255,255,255,0.1);
        }
        
        .image-counter {
            color: white;
            font-family: 'Gloria Hallelujah', cursive;
            font-size: 18px;
            margin: 10px 0;
            text-align: center;
        }
        
        .next-button {
            background: linear-gradient(135deg, #75020f, #2b0307);
            border: 2px solid white;
            color: white;
            padding: 15px 30px;
            border-radius: 25px;
            font-family: 'Gloria Hallelujah', cursive;
            font-size: 18px;
            cursor: pointer;
            margin: 20px;
            transition: all 0.3s ease;
        }
        
        .next-button:hover {
            background: linear-gradient(135deg, #2b0307, #75020f);
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(255,255,255,0.2);
        }
        
        .reset-button {
            background: transparent;
            border: 1px solid rgba(255,255,255,0.5);
            color: rgba(255,255,255,0.7);
            padding: 10px 20px;
            border-radius: 15px;
            font-family: 'Gloria Hallelujah', cursive;
            font-size: 14px;
            cursor: pointer;
            margin: 10px;
            transition: all 0.3s ease;
        }
        
        .reset-button:hover {
            border-color: white;
            color: white;
            background: rgba(255,255,255,0.1);
        }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 6, 1])
    with col1:
        if st.button("Library", key="back_to_library_photos"):
            st.session_state.page = "Library"
            st.rerun()
    
    # Define all your memory images
    all_memory_images = [
    "https://github.com/yash-2345/memories1/blob/main/IMG_0163.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_0302.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_0461.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_0469.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_0500.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_0598.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_0884.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_1224.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_1594.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_1737.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_1743.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_1749.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_1821.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_1854.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_1958.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_1086.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_2131.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_2198.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_2279.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_2387.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_2592.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_4341.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_4629.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_4792.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_5283.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_5493.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_6159.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_6779.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_6988.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_7346.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_7620.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_8040.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_8088.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_8113.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_8162.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_8216.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_8442.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_8452.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_8488.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_8526.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_8529.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_8531.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_8538.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_8819.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_8973.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_9101.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_9138.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_9201.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_9216.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_9466.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_9499.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_9531.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_9559.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_9573.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_9670.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_9691.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_9693.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_9695.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_9763.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_9768.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/IMG_9770.png?raw=true",
    "https://github.com/yash-2345/memories1/blob/main/RobloxScreenShot20250221_044356594.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_5501.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_5547.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_5690.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_5701.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_5704.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_5745.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_5884.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_6193.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_6412.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_6442.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_6445.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_6777.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_6991.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_7020.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_7032.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_7103.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_7162.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_7217.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_7421.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_7456.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_7494.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_7550.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_7772.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_7786.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/IMG_7930.png?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/WhatsApp%20Image%202025-10-01%20at%2009.57.56_690370f7.jpg?raw=true",
    "https://github.com/yash-2345/memories2/blob/main/WhatsApp%20Image%202025-10-01%20at%2009.58.02_09269495.jpg?raw=true"
    ]
    
    # Initialize session states for random image display
    if "memory_shuffle" not in st.session_state:
        st.session_state.memory_shuffle = all_memory_images.copy()
        random.shuffle(st.session_state.memory_shuffle)
        st.session_state.memory_index = 0
    
    # Show header
    st.markdown("<h1 class='memories-header'>Memories of Us I Adore 💕</h1>", unsafe_allow_html=True)
    
    # Show current image
    current_image = st.session_state.memory_shuffle[st.session_state.memory_index]
    
    st.markdown(f"""
    <div class='image-display'>
        <img src='{current_image}' class='main-image' alt='I love these memories'>
    </div>
    """, unsafe_allow_html=True)
    
    # Show counter
    st.markdown(f"""
    <div class='image-counter'>
        Image {st.session_state.memory_index + 1} of {len(all_memory_images)}
        <br>
        <small>({len(all_memory_images) - st.session_state.memory_index - 1} more to see before reshuffle)</small>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("Show Me Another Memory", key="next_memory", use_container_width=True):
            if st.session_state.memory_index < len(st.session_state.memory_shuffle) - 1:
                st.session_state.memory_index += 1
            else:
                # Reshuffle when we've seen all images
                st.session_state.memory_shuffle = all_memory_images.copy()
                random.shuffle(st.session_state.memory_shuffle)
                st.session_state.memory_index = 0
                st.success("🔄 All memories seen! Reshuffled for you to enjoy again!")
            st.rerun()
    
    with col3:
        if st.button("🔄 Reshuffle Now", key="reset_memories"):
            st.session_state.memory_shuffle = all_memory_images.copy()
            random.shuffle(st.session_state.memory_shuffle)
            st.session_state.memory_index = 0
            st.rerun()

elif st.session_state.page == "Voice Notes":  # This corresponds to "Pictures!" button
    import random
    
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Gloria+Hallelujah&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap');
                
        .stApp {
            background: #000000 !important;
        }
        
        header[data-testid="stHeader"] {
            display: none;
        }
        
        .pictures-header {
            font-family: 'Gloria Hallelujah', cursive !important;
            color: white;
            text-align: center;
            font-size: 36px;
            margin-bottom: 30px;
            text-shadow: 0 0 10px rgba(255,255,255,0.5);
        }
        
        .image-display {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 30px 0;
        }
        
        .main-image {
            max-width: 400px !important;
            width: 100% !important;
            height: auto !important;
            border-radius: 20px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.5);
            transition: transform 0.3s ease;
            margin-bottom: 20px;
            animation: glow 3s ease-in-out infinite alternate;
        }
        
        .main-image:hover {
            transform: scale(1.02);
            box-shadow: 0 20px 50px rgba(255,255,255,0.1);
        }
        
        .image-counter {
            color: white;
            font-family: 'Gloria Hallelujah', cursive;
            font-size: 18px;
            margin: 10px 0;
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 6, 1])
    with col1:
        if st.button("Library", key="back_to_library_photos"):
            st.session_state.page = "Library"
            st.rerun()
    
    # Define all your random pictures
    all_pictures = [
        "https://github.com/yash-2345/pictures-/blob/main/07E51A41-347E-4AF2-B54D-6DD1DB175FDD.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_0514.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_0610.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_0661.png?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_0778.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_0779.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_0780.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_0781.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_0782.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_0783.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_0823.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_0835.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_0836.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_0915.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_0916.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_0982.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_2293.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_3102.png?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_3131.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_3302.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_3499.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_3502.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_4418.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_4444.png?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_4450.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_5184.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_5355.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_5971.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_6199.png?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_6888.png?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_7378.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_7592.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_7903.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_8040.png?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_8113.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_8151.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_8155.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_8258.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_8542.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_8549.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_8551.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_8759.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_8804.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_9211.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_9656.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_9808.png?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/IMG_9913.jpg?raw=true",
        "https://github.com/yash-2345/pictures-/blob/main/dbb21bc4-93f3-4aba-9a06-80db903cd2e2.jpg?raw=true",
    ]
    
    # Initialize session states for random picture display
    if "picture_shuffle" not in st.session_state:
        st.session_state.picture_shuffle = all_pictures.copy()
        random.shuffle(st.session_state.picture_shuffle)
        st.session_state.picture_index = 0
    
    # Show header
    st.markdown("<h1 class='pictures-header'>Pictures!!!</h1>", unsafe_allow_html=True)
    
    # Show current image
    current_image = st.session_state.picture_shuffle[st.session_state.picture_index]
    
    st.markdown(f"""
    <div class='image-display'>
        <img src='{current_image}' class='main-image' alt='Beautiful picture'>
    </div>
    """, unsafe_allow_html=True)
    
    # Show counter
    st.markdown(f"""
    <div class='image-counter'>
        Picture {st.session_state.picture_index + 1} of {len(all_pictures)}
        <br>
        <small>({len(all_pictures) - st.session_state.picture_index - 1} more to see before reshuffle)</small>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("More to see??", key="next_picture", use_container_width=True):
            if st.session_state.picture_index < len(st.session_state.picture_shuffle) - 1:
                st.session_state.picture_index += 1
            else:
                # Reshuffle when we've seen all images
                st.session_state.picture_shuffle = all_pictures.copy()
                random.shuffle(st.session_state.picture_shuffle)
                st.session_state.picture_index = 0
                st.success("🔄 All pictures seen! Reshuffled for more beauty!")
            st.rerun()
    
    with col3:
        if st.button("🔄 Reshuffle Now", key="reset_pictures"):
            st.session_state.picture_shuffle = all_pictures.copy()
            random.shuffle(st.session_state.picture_shuffle)
            st.session_state.picture_index = 0
            st.rerun()

elif st.session_state.page == "Memories":  # This corresponds to "This is you❗❗" button
    import random
    
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Gloria+Hallelujah&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap');
                
        .stApp {
            background: #000000 !important;
        }
        
        header[data-testid="stHeader"] {
            display: none;
        }
        
        .this-is-you-header {
            font-family: 'Gloria Hallelujah', cursive !important;
            color: white;
            text-align: center;
            font-size: 36px;
            margin-bottom: 20px;
            text-shadow: 0 0 10px rgba(255,255,255,0.5);
        }
        
        .image-display {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 30px 0;
        }
        
        .main-image {
            max-width: 400px !important;
            width: 100% !important;
            height: auto !important;
            border-radius: 20px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.5);
            transition: transform 0.3s ease;
            margin-bottom: 20px;
            animation: glow 3s ease-in-out infinite alternate;
        }
        
        @keyframes glow {
            from {
                box-shadow: 0 15px 40px rgba(0,0,0,0.5);
            }
            to {
                box-shadow: 0 15px 40px rgba(255,255,255,0.2);
            }
        }
        
        .main-image:hover {
            transform: scale(1.02);
            animation-play-state: paused;
            box-shadow: 0 20px 50px rgba(255,255,255,0.3);
        }
        
        .image-counter {
            color: white;
            font-family: 'Gloria Hallelujah', cursive;
            font-size: 18px;
            margin: 10px 0;
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 6, 1])
    with col1:
        if st.button("Library", key="back_to_library_photos"):
            st.session_state.page = "Library"
            st.rerun()
    
    # Define all your pictures - simple list of URLs
    you_images = [
        "https://raw.githubusercontent.com/yash-2345/thisisyou/main/IMG_0676.jpg",
        "https://raw.githubusercontent.com/yash-2345/thisisyou/main/IMG_0726.jpg",
        "https://raw.githubusercontent.com/yash-2345/thisisyou/main/IMG_0730.jpg",
        "https://raw.githubusercontent.com/yash-2345/thisisyou/main/IMG_0731.jpg",
        "https://raw.githubusercontent.com/yash-2345/thisisyou/main/IMG_0732.jpg",
        "https://raw.githubusercontent.com/yash-2345/thisisyou/main/IMG_0733.jpg",
        "https://raw.githubusercontent.com/yash-2345/thisisyou/main/IMG_0734.jpg",
        "https://raw.githubusercontent.com/yash-2345/thisisyou/main/IMG_0735.jpg",
        "https://raw.githubusercontent.com/yash-2345/thisisyou/main/IMG_0736.jpg",
        "https://raw.githubusercontent.com/yash-2345/thisisyou/main/IMG_0737.jpg",
        "https://raw.githubusercontent.com/yash-2345/thisisyou/main/IMG_0738.jpg",
        "https://raw.githubusercontent.com/yash-2345/thisisyou/main/IMG_0739.jpg",
        "https://raw.githubusercontent.com/yash-2345/thisisyou/main/IMG_0784.jpg",
        "https://raw.githubusercontent.com/yash-2345/thisisyou/main/IMG_4825.jpg",
        "https://raw.githubusercontent.com/yash-2345/thisisyou/main/IMG_5316.jpg",
        "https://raw.githubusercontent.com/yash-2345/thisisyou/main/IMG_5415.png",
        "https://raw.githubusercontent.com/yash-2345/thisisyou/main/IMG_6889.jpg",
        "https://raw.githubusercontent.com/yash-2345/thisisyou/main/IMG_7542.jpg",
        "https://raw.githubusercontent.com/yash-2345/thisisyou/main/IMG_8264.jpg"
    ]
    
    # Initialize session states for random image display
    if "you_shuffle" not in st.session_state:
        st.session_state.you_shuffle = you_images.copy()
        random.shuffle(st.session_state.you_shuffle)
        st.session_state.you_index = 0
    
    # Show header
    st.markdown("<h1 class='this-is-you-header'>This is how I see you❗❗</h1>", unsafe_allow_html=True)
    
    # Show current image
    current_url = st.session_state.you_shuffle[st.session_state.you_index]
    
    st.markdown(f"""
    <div class='image-display'>
        <img src='{current_url}' class='main-image' alt='Beautiful you'>
    </div>
    """, unsafe_allow_html=True)
    
    # Show counter
    st.markdown(f"""
    <div class='image-counter'>
        Image {st.session_state.you_index + 1} of {len(you_images)}
        <br>
        <small>({len(you_images) - st.session_state.you_index - 1} More photos to see)</small>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("Show me MORE?", key="next_you", use_container_width=True):
            if st.session_state.you_index < len(st.session_state.you_shuffle) - 1:
                st.session_state.you_index += 1
            else:
                # Reshuffle when we've seen all images
                st.session_state.you_shuffle = you_images.copy()
                random.shuffle(st.session_state.you_shuffle)
                st.session_state.you_index = 0
                st.success("🔄 Reshuffled!")
            st.rerun()
    
    with col3:
        if st.button("🔄 Reshuffle Now", key="reset_you_1"):
            st.session_state.you_shuffle = you_images.copy()
            random.shuffle(st.session_state.you_shuffle)
            st.session_state.you_index = 0
            st.rerun()

elif st.session_state.page == "Love Letters":  # This corresponds to "Our future Plans/Goals" button
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Gloria+Hallelujah&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap');
                
        .stApp {
            background-image: 
                linear-gradient(135deg, rgba(43, 3, 7, 0.7) 0%, rgba(81, 8, 13, 0.7) 50%, rgba(25, 23, 27, 0.7) 100%),
                url('https://github.com/yash-2345/2_october/blob/main/561859bd3400bd1354bf408859db1e54.jpg?raw=true');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }
        
        header[data-testid="stHeader"] {
            display: none;
        }
        
        .watchlist-header {
            font-family: 'Gloria Hallelujah', cursive !important;
            color: white;
            text-align: center;
            font-size: 36px;
            margin-bottom: 20px;
            text-shadow: 0 0 10px rgba(255,255,255,0.5);
        }
        
        .watchlist-subtitle {
            color: white;
            font-family: 'Playfair Display', serif;
            font-size: 20px;
            text-align: center;
            margin-bottom: 30px;
            font-style: italic;
            opacity: 0.9;
        }
        
        .media-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 20px;
            padding: 20px 0;
        }
        
        .media-card {
            background: #19171b;
            border-radius: 15px;
            padding: 15px;
            transition: all 0.3s ease;
            border: 2px solid rgba(255,255,255,0.2);
            text-align: center;
            position: relative;
        }
        
        .media-card:hover {
            background: rgba(255,255,255,0.2);
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(255,255,255,0.2);
        }
        
        .media-card.watched {
            opacity: 0.8;
            border: 2px solid rgba(76, 175, 80, 0.5);
        }
        
        .media-card.watched:hover {
            opacity: 1;
            background: rgba(76, 175, 80, 0.2);
        }
        
        .media-poster {
            width: 100%;
            height: 250px;
            object-fit: cover;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        
        .media-title {
            color: white;
            font-family: 'Playfair Display', serif;
            font-size: 16px;
            font-weight: bold;
            margin: 10px 0 5px 0;
        }
        
        .media-type {
            color: #ffffff;
            font-family: 'Gloria Hallelujah', cursive;
            font-size: 12px;
            margin: 5px 0;
        }
        
        .watched-badge {
            background: #4CAF50;
            color: white;
            padding: 4px 10px;
            border-radius: 5px;
            font-family: 'Gloria Hallelujah', cursive;
            font-size: 10px;
            margin-top: 5px;
            display: inline-block;
        }
        
        .watch-link {
            display: inline-block;
            background: rgba(255,255,255,0.2);
            color: white;
            padding: 8px 15px;
            border-radius: 8px;
            text-decoration: none;
            font-family: 'Gloria Hallelujah', cursive;
            font-size: 12px;
            margin-top: 10px;
            transition: all 0.3s ease;
        }
        
        .watch-link:hover {
            background: rgba(255,255,255,0.4);
            text-decoration: none;
            color: white;
        }
        
        .filter-buttons {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin: 20px 0;
            flex-wrap: wrap;
        }
        
        .stats {
            display: flex;
            justify-content: space-around;
            margin: 20px 0;
            flex-wrap: wrap;
        }
        
        .stat-item {
            background: #000000;
            padding: 15px 20px;
            border-radius: 15px;
            text-align: center;
            margin: 5px;
            flex: 1;
            min-width: 120px;
        }
        
        .stat-number {
            font-size: 24px;
            font-weight: bold;
            color: #ffffff;
            font-family: 'Gloria Hallelujah', cursive;
        }
        
        .stat-label {
            font-size: 14px;
            color: #ffffff;
            font-family: 'Playfair Display', serif;
        }
        
        a, a:link, a:visited, a:hover, a:active {
            color: white !important;
            text-decoration: none;
        }

        a:hover {
            color: #cccccc !important;
            text-decoration: underline;
        }

        .watch-link {
            display: inline-block;
            background: rgba(255,255,255,0.2);
            color: white !important;
            padding: 8px 15px;
            border-radius: 8px;
            text-decoration: none;
            font-family: 'Gloria Hallelujah', cursive;
            font-size: 12px;
            margin-top: 10px;
            transition: all 0.3s ease;
        }

        .watch-link:hover {
            background: rgba(255,255,255,0.4);
            text-decoration: none;
            color: white !important;
        }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 6, 1])
    with col1:
        if st.button("Library", key="back_to_library_watchlist"):
            st.session_state.page = "Library"
            st.rerun()
    
    # Static watchlist data with 'watched' status
    watchlist = [
        {
            "title": "Tokyo Ghoul S3",
            "type": "Anime",
            "poster": "https://www.themoviedb.org/t/p/w1280/1m4RlC9BTCbyY549TOdVQ5NRPcR.jpg",
            "link": "https://www.netflix.com/watch/80990539?trackId=268410292&tctx=0%2C0%2C65842d44-8a40-40e2-8e3a-283ac3f51d67%2C65842d44-8a40-40e2-8e3a-283ac3f51d67%7C%3DeyJwYWdlSWQiOiIyODg3OTc5MS0wYzg0LTRhMzItYjhjMC0xZTk3YzEyZGI5YjYvMS8vdG9reW8gZ2hvdWwvMC8wIiwibG9jYWxTZWN0aW9uSWQiOiIyIn0%3D%2C%2C%2C%2CtitlesResults%2C%2CVideo%3A80023687%2CdetailsPagePlayButton",
            "watched": False
        },
        {
            "title": "Hunter x Hunter",
            "type": "Anime",
            "poster": "https://www.themoviedb.org/t/p/w1280/i2EEr2uBvRlAwJ8d8zTG2Y19mIa.jpg",
            "link": "https://www.crunchyroll.com/series/GY3VKX1MR/hunter-x-hunter",
            "watched": False
        },
        {
            "title": "Code Geass",
            "type": "Anime",
            "poster": "https://www.themoviedb.org/t/p/w1280/x316WCogkeIwNY4JR8zTCHbI2nQ.jpg",
            "link": "https://www.crunchyroll.com/series/GY2P9ED0Y/code-geass",
            "watched": False
        },
        {
            "title": "The Summer Hikaru Died",
            "type": "Anime",
            "poster": "https://www.themoviedb.org/t/p/w1280/x0wiTO87UMiVCUe24nKaHlp7AIc.jpg",
            "link": "https://www.netflix.com/watch/81972293?trackId=268410292&tctx=0%2C0%2Ca893d89b-ecb8-44e3-9a8e-fead371ba95b%2Ca893d89b-ecb8-44e3-9a8e-fead371ba95b%7C%3DeyJwYWdlSWQiOiIyODg3OTc5MS0wYzg0LTRhMzItYjhjMC0xZTk3YzEyZGI5YjYvMS8vdGhlIHN1bW1lciBoaWthcnUvMC8wIiwibG9jYWxTZWN0aW9uSWQiOiIyIn0%3D%2C%2C%2C%2CtitlesResults%2C81948057%2CVideo%3A81972293%2CdetailsPageEpisodePlayButton",
            "watched": False
        },
        {
            "title": "Monster",
            "type": "Anime",
            "poster": "https://www.themoviedb.org/t/p/w1280/n5XNKXnoXpoXyfiCtXHOf8q8PFM.jpg",
            "link": "https://www.netflix.com/watch/81409871?trackId=268410292&tctx=0%2C0%2Cca2c54a5-03e7-4a44-a8f3-35eabbfcab5f%2Cca2c54a5-03e7-4a44-a8f3-35eabbfcab5f%7C%3DeyJwYWdlSWQiOiIyODg3OTc5MS0wYzg0LTRhMzItYjhjMC0xZTk3YzEyZGI5YjYvMS8vbW9uc3Rlci8wLzAiLCJsb2NhbFNlY3Rpb25JZCI6IjIifQ%3D%3D%2C%2C%2C%2CtitlesResults%2C81409869%2CVideo%3A81409871%2CdetailsPageEpisodePlayButton/",
            "watched": False
        },
        {
            "title": "Fullmetal Alchemist: Brotherhood",
            "type": "Anime",
            "poster": "https://www.themoviedb.org/t/p/w1280/5ZFUEOULaVml7pQuXxhpR2SmVUw.jpg",
            "link": "https://www.crunchyroll.com/series/GRGGPG93R/fullmetal-alchemist-brotherhood",
            "watched": False
        },
        {
            "title": "Bungo Stray Dogs",
            "type": "Anime",
            "poster": "https://www.themoviedb.org/t/p/w1280/6AQmGhkYwAqW2OevjXbsh7tZnNO.jpg",
            "link": "https://www.netflix.com/watch/80131687?trackId=268410292&tctx=0%2C0%2C6ceeffcf-3fad-4454-b469-b6ba4df572b8%2C6ceeffcf-3fad-4454-b469-b6ba4df572b8%7C%3DeyJwYWdlSWQiOiIyODg3OTc5MS0wYzg0LTRhMzItYjhjMC0xZTk3YzEyZGI5YjYvMS8vYnVuZ291LzAvMCIsImxvY2FsU2VjdGlvbklkIjoiMiJ9%2C%2C%2C%2CtitlesResults%2C80132126%2CVideo%3A80131687%2CdetailsPageEpisodePlayButton",
            "watched": True
        },
        {
            "title": "Bleach",
            "type": "Anime",
            "poster": "https://www.themoviedb.org/t/p/w1280/2EewmxXe72ogD0EaWM8gqa0ccIw.jpg",
            "link": "https://www.netflix.com/watch/70176299?trackId=268410292&tctx=0%2C0%2C6de4f435-daeb-4af6-8944-ab1f9d7d254f%2C6de4f435-daeb-4af6-8944-ab1f9d7d254f%7C%3DeyJwYWdlSWQiOiIyODg3OTc5MS0wYzg0LTRhMzItYjhjMC0xZTk3YzEyZGI5YjYvMS8vYmxlYWNoLzAvMCIsImxvY2FsU2VjdGlvbklkIjoiMiJ9%2C%2C%2C%2CtitlesResults%2C70204957%2CVideo%3A70176299%2CdetailsPageEpisodePlayButton",
            "watched": False
        },
        {
            "title": "Gintama",
            "type": "Anime",
            "poster": "https://www.themoviedb.org/t/p/w1280/1wEl5WHQO2SdWQ6S3gLBaaobf4c.jpg",
            "link": "https://www.crunchyroll.com/series/GYQ4MKDZ6/gintama",
            "watched": False
        },
        {
            "title": "The Summer Hikaru Died",
            "type": "Anime",
            "poster": "https://www.themoviedb.org/t/p/w1280/x0wiTO87UMiVCUe24nKaHlp7AIc.jpg",
            "link": "https://www.netflix.com/watch/81972293?trackId=268410292&tctx=0%2C0%2Ca893d89b-ecb8-44e3-9a8e-fead371ba95b%2Ca893d89b-ecb8-44e3-9a8e-fead371ba95b%7C%3DeyJwYWdlSWQiOiIyODg3OTc5MS0wYzg0LTRhMzItYjhjMC0xZTk3YzEyZGI5YjYvMS8vdGhlIHN1bW1lciBoaWthcnUvMC8wIiwibG9jYWxTZWN0aW9uSWQiOiIyIn0%3D%2C%2C%2C%2CtitlesResults%2C81948057%2CVideo%3A81972293%2CdetailsPageEpisodePlayButton",
            "watched": False
        },
        {
            "title": "Jujutsu Kaisen",
            "type": "Anime",
            "poster": "https://www.themoviedb.org/t/p/w1280/fHpKWq9ayzSk8nSwqRuaAUemRKh.jpg",
            "link": "https://www.netflix.com/search?q=jujutsu%20kaisen&jbv=81278456",
            "watched": False
        },
        {
            "title": "Devilman Crybaby",
            "type": "Anime",
            "poster": "https://www.themoviedb.org/t/p/w1280/2pQ9xfgDa3L3QpoXfkNhISby2R4.jpg",
            "link": "https://www.netflix.com/search?q=devilman&jbv=80174974",
            "watched": False
        },


        {
            "title": "Barbie",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/iuFNMS8U5cb6xfzi51Dbkovj7vM.jpg",
            "link": "https://www.netflix.com/search?q=barbie&jbv=80157969",
            "watched": True
        },
        {
            "title": "TGCF",
            "type": "Series",
            "poster": "https://www.themoviedb.org/t/p/w1280/4psWk1qJZKXlH78DjZUnvXCwSAM.jpg",
            "link": "https://www.crunchyroll.com/series/G79H23XX8/heaven-officials-blessing",
            "watched": True
        },
        {
            "title": "Superman",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/wPLysNDLffQLOVebZQCbXJEv6E6.jpg",
            "link": "https://www.primevideo.com/detail/0LYFYGIZPMS0O3KM7Q4YYKVNI5/ref=atv_sr_fle_c_sr3aca3c_1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B0F4W1241K&qid=1759307643323",
            "watched": False
        },
        {
            "title": "The Suicide Squad (2021)",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/q61qEyssk2ku3okWICKArlAdhBn.jpg",
            "link": "https://www.primevideo.com/detail/0QFWE0UTEFHC7FP4NG0E4OAZY7/ref=atv_sr_fle_c_sr3aca3c_1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B0BR1RZFL9&qid=1759307787955",
            "watched": False
        },
        {
            "title": "Creature Commandos",
            "type": "Series",
            "poster": "https://www.themoviedb.org/t/p/w1280/bB3G6Ug1jfsOUptb0RJsqrgMVta.jpg",
            "link": "https://www.primevideo.com/detail/0PUNMGZEWOMYFKR1XIGOLTL2YM/ref=atv_sr_fle_c_sr3aca3c_1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B0CQZ5KK5X&qid=1759307981275",
            "watched": False
        },
        {
            "title": "Donnie Darko",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/fhQoQfejY1hUcwyuLgpBrYs6uFt.jpg",
            "link": "https://www.primevideo.com/detail/0IIIOT70UGI7SHWUA16FJO2MD8/ref=atv_sr_fle_c_sr3aca3c_1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B08PNTSNH1&qid=1759308042115",
            "watched": False
        },
        {
            "title": "How to Train Your Dragon",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/ygGmAO60t8GyqUo9xYeYxSZAR3b.jpg",
            "link": "https://www.primevideo.com/detail/0FJV8X8GXGTOYGGRF7R9ZO599G/ref=atv_sr_fle_c_sr3aca3c_4_1_4?sr=1-4&pageTypeIdSource=ASIN&pageTypeId=B0CN2WCH62&qid=1759311028100",
            "watched": True
        },
        {
            "title": "How to Train Your Dragon 2 ",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/d13Uj86LdbDLrfDoHR5aDOFYyJC.jpg",
            "link": "https://www.primevideo.com/detail/0M6KLGQK8XPLX1T1EQLIUO89S4/ref=atv_sr_fle_c_sr3aca3c_3_1_3?sr=1-3&pageTypeIdSource=ASIN&pageTypeId=B0CN64TSX5&qid=1759311028100",
            "watched": True
        },
        {
            "title": "How to Train Your Dragon: The Hidden World ",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/xvx4Yhf0DVH8G4LzNISpMfFBDy2.jpg",
            "link": "https://www.primevideo.com/detail/0PFYI72BA6DJTSGK5B5D06WQET/ref=atv_sr_fle_c_sr3aca3c_2_1_2?sr=1-2&pageTypeIdSource=ASIN&pageTypeId=B0DKNSQ7DH&qid=1759311028100",
            "watched": True
        },
        {
            "title": "Dragons: Race to the Edge",
            "type": "Series",
            "poster": "https://www.themoviedb.org/t/p/w1280/y5sNfaTvWR3ObILyf9uV6deAcKT.jpg",
            "link": "https://www.netflix.com/search?q=how%20to%20tr&jbv=80039394",
            "watched": False
        },
        {
            "title": "The Stranger by the Shore",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/4m74lboTcvrmnCM506t4y4c3klc.jpg",
            "link": "https://www.primevideo.com/detail/0MNGI076IB1U9W8S2NRC7Y0FVX/ref=atv_sr_fle_c_Tn74RA_1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B0CN8JLSYQ&qid=1759311442970",
            "watched": True
        },
        {
            "title": "Helluva Boss",
            "type": "Series",
            "poster": "https://www.themoviedb.org/t/p/w1280/dgtuBsG2F4cGiumtHBKDru7PW9j.jpg",
            "link": "https://www.primevideo.com/detail/0QCNDK96TTM38KV78J5SMKEE8K/ref=atv_sr_fle_c_sr3aca3c_1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B0F9W1CFW1&qid=1759311499145",
            "watched": False
        },
        {
            "title": "Hazbin Hotel S2",
            "type": "Series",
            "poster": "https://www.themoviedb.org/t/p/w1280/rXojaQcxVUubPLSrFV8PD4xdjrs.jpg",
            "link": "https://www.primevideo.com/detail/0HZWTBZYQQXYW48YBANMDM2MZE/ref=atv_sr_fle_c_sr3aca3c_1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B0CBJ7WGR4&qid=1759311798879",
            "watched": False
        },
        {
            "title": "Kiki's Delivery Service",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/Aufa4YdZIv4AXpR9rznwVA5SEfd.jpg",
            "link": "https://www.netflix.com/search?q=kiki&jbv=60027106",
            "watched": True
        },
        {
            "title": "Howl's Moving Castle",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/TkTPELv4kC3u1lkloush8skOjE.jpg",
            "link": "https://www.netflix.com/search?q=kiki&jbv=70028883",
            "watched": True
        },
        {
            "title": "The Secret World of Arrietty",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/3lSRaSjDp2nkXMQkzzjpRi3035O.jpg",
            "link": "https://www.netflix.com/search?q=arrietty&jbv=70216227",
            "watched": True
        },
        {
            "title": "Ponyo",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/yp8vEZflGynlEylxEesbYasc06i.jpg",
            "link": "https://www.netflix.com/search?q=kiki&jbv=70106454",
            "watched": True
        },
        {
            "title": "Princess Mononoke",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/cMYCDADoLKLbB83g4WnJegaZimC.jpg",
            "link": "https://www.netflix.com/search?q=princess&jbv=28630857",
            "watched": False
        },
        {
            "title": "My Neighbor Totoro",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/rtGDOeG9LzoerkDGZF9dnVeLppL.jpg",
            "link": "https://www.netflix.com/search?q=my%20neighbour&jbv=60032294",
            "watched": False
        },
        {
            "title": "La La Land",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/uDO8zWDhfWwoFdKS4fzkUJt0Rf0.jpg",
            "link": "https://www.primevideo.com/detail/0GQK5UKAMEDC0TSWTLFVZI1Z3Z/ref=atv_sr_fle_c_sr3aca3c_1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B086R8T6PW&qid=1759313260759",
            "watched": True
        },
        {
            "title": "The Greatest Showman",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/b9CeobiihCx1uG1tpw8hXmpi7nm.jpg",
            "link": "https://www.themoviedb.org/movie/316029-the-greatest-showman",
            "watched": True
        },
        {
            "title": "Good Omens S3",
            "type": "Series",
            "poster": "https://www.themoviedb.org/t/p/w1280/omgCpyBV5sUT8AkeIcEwdPPgKZC.jpg",
            "link": "https://www.primevideo.com/detail/0Q7GFNBQ6IPO87MX4G4WD4GT4I/ref=atv_sr_fle_c_sr3aca3c_1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B07FMFL4F2&qid=1759312529322",
            "watched": False
        },
        {
            "title": "The Shawshank Redemption",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/9cqNxx0GxF0bflZmeSMuL5tnGzr.jpg",
            "link": "https://www.primevideo.com/detail/0H3BD1NXV10WDK34UPWWVK4NNS/ref=atv_sr_fle_c_sr3aca3c_1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B07PS6LPN6&qid=1759312658178",
            "watched": True
        },
        {
            "title": "The Maze Runner",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/ode14q7WtDugFDp78fo9lCsmay9.jpg",
            "link": "https://www.themoviedb.org/movie/198663-the-maze-runner",
            "watched": True
        },
        {
            "title": "Maze Runner: The Scorch Trials",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/mYw7ZyejqSCPFlrT2jHZOESZDU3.jpg",
            "link": "https://www.themoviedb.org/movie/294254-maze-runner-the-scorch-trials",
            "watched": True
        },
        {
            "title": "Maze Runner: The Death Cure",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/drbERzlA4cuRWhsTXfFOY4mRR4f.jpg",
            "link": "https://www.themoviedb.org/movie/336843-maze-runner-the-death-cure",
            "watched": True
        },
        {
            "title": "Big Hero 6",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/2mxS4wUimwlLmI1xp6QW6NSU361.jpg",
            "link": "https://www.themoviedb.org/movie/177572-big-hero-6",
            "watched": True
        },
        {
            "title": "Stranger Things S5",
            "type": "Series",
            "poster": "https://www.themoviedb.org/t/p/w1280/olAK0DWZmTpqRTRyNpqFUxKGbw6.jpg",
            "link": "https://www.netflix.com/search?q=stranger&jbv=80057281",
            "watched": False
        },
        {
            "title": "Forrest Gump",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/arw2vcBveWOVZr6pxd9XTd1TdQa.jpg",
            "link": "https://www.primevideo.com/detail/0RMLEUTKD0LKNDHSS10OQNYHF0/ref=atv_sr_fle_c_sr3aca3c_1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B08T9ZR5GK&qid=1759313348844",
            "watched": True
        },
        {
            "title": "Gone Girl",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/zeqGKVeuqhsh7WSyJAdczW4k51H.jpg",
            "link": "https://www.themoviedb.org/movie/210577-gone-girl",
            "watched": False
        },
        {
            "title": "Brokeback Mountain",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/aByfQOQBNa4CMFwIgq3QrqY2ZHh.jpg",
            "link": "https://www.primevideo.com/detail/0R1A5EQSYL864DPJ9QL1YW9UI8/ref=atv_sr_fle_c_sr3aca3c_1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B07NQM2BKZ&qid=1759313545030",
            "watched": False
        },
        {
            "title": "Spider-Man: Into the Spider-Verse",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/iiZZdoQBEYBv6id8su7ImL0oCbD.jpg",
            "link": "https://www.primevideo.com/detail/0N4PINHO6IMM8J6G1VVZZUWBOL/ref=atv_sr_fle_c_Tn74RA_1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B09VYKJL5R&qid=1759313656054",
            "watched": True
        },
        {
            "title": "Spider-Man: Across the Spider-Verse",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/8Vt6mWEReuy4Of61Lnj5Xj704m8.jpg",
            "link": "https://www.netflix.com/search?q=across&jbv=81594921",
            "watched": True
        },
        {
            "title": "The Wire",
            "type": "Series",
            "poster": "https://www.themoviedb.org/t/p/w1280/4lbclFySvugI51fwsyxBTOm4DqK.jpg",
            "link": "https://www.themoviedb.org/tv/1438-the-wire",
            "watched": False
        },
        {
            "title": "Breaking Bad",
            "type": "Series",
            "poster": "https://www.themoviedb.org/t/p/w1280/vZ1RQSDZ3xzBhLqJdrmvpkm2Nbu.jpg",
            "link": "https://www.netflix.com/search?q=breaking&jbv=70143836",
            "watched": False
        },
        {
            "title": "Better Call Saul",
            "type": "Series",
            "poster": "https://www.themoviedb.org/t/p/w1280/fC2HDm5t0kHl7mTm7jxMR31b7by.jpg",
            "link": "https://www.netflix.com/search?q=better%20call&jbv=80021955",
            "watched": False
        },
        {
            "title": "El Camino: A Breaking Bad Movie",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/ePXuKdXZuJx8hHMNr2yM4jY2L7Z.jpg",
            "link": "https://www.netflix.com/search?q=better%20call&jbv=81078819",
            "watched": False
        },
        {
            "title": "The Sopranos",
            "type": "Series",
            "poster": "https://www.themoviedb.org/t/p/w1280/rTc7ZXdroqjkKivFPvCPX0Ru7uw.jpg",
            "link": "https://www.themoviedb.org/tv/1398-the-sopranos",
            "watched": False
        },
        {
            "title": "Prisoners",
            "type": "Movie",
            "poster": "https://www.themoviedb.org/t/p/w1280/uhviyknTT5cEQXbn6vWIqfM4vGm.jpg",
            "link": "https://www.primevideo.com/detail/0IMN0DXNC1VYXUQ4F224MHB62M/ref=atv_sr_fle_c_sr3aca3c_1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B0CTLJ429G&qid=1759314157521",
            "watched": False
        },
        {
            "title": "Seraph of the End",
            "type": "Anime",
            "poster": "https://www.themoviedb.org/t/p/w1280/5IlxL2PfQ8CyY4TLRru9TcU56b3.jpg",
            "link": "https://www.themoviedb.org/tv/62255-seraph-of-the-end",
            "watched": False
        },
        {
            "title": "Horimiya S2",
            "type": "Anime",
            "poster": "https://www.themoviedb.org/t/p/w1280/yxk74s3QHx4K3rKpiPisLLqPJ5J.jpg",
            "link": "https://www.crunchyroll.com/series/G9VHN9P43/horimiya",
            "watched": False
        },
        {
            "title": "Black Mirror",
            "type": "Series",
            "poster": "https://www.themoviedb.org/t/p/w1280/seN6rRfN0I6n8iDXjlSMk1QjNcq.jpg",
            "link": "https://www.netflix.com/search?q=black%20&jbv=70264888",
            "watched": False
        },
        {
            "title": "Alice in Borderland S3",
            "type": "Series",
            "poster": "https://www.themoviedb.org/t/p/w1280/Ac8ruycRXzgcsndTZFK6ouGA0FA.jpg",
            "link": "https://www.netflix.com/search?q=black%20&jbv=80200575",
            "watched": False
        },
        {
            "title": "Arcane",
            "type": "Series",
            "poster": "https://www.themoviedb.org/t/p/w1280/f1Vivcukr0DBlSxppMaEDuwGSjk.jpg",
            "link": "https://www.netflix.com/search?q=arcane&jbv=81435684",
            "watched": True
        },
        {
            "title": "Blue Exorcist",
            "type": "Anime",
            "poster": "https://www.themoviedb.org/t/p/w1280/kpNoqNmElzGUEcEoZyfFwvYXMsR.jpg",
            "link": "https://www.crunchyroll.com/series/G649PJ0JY/blue-exorcist",
            "watched": False
        },
        
    ]
    
    if "filter_type" not in st.session_state:
        st.session_state.filter_type = "All"
    
    if "items_to_show" not in st.session_state:
        st.session_state.items_to_show = 9
    
    # Show header
    st.markdown("<h1 class='watchlist-header'>Our Watchlist</h1>", unsafe_allow_html=True)
    st.markdown("<p class='watchlist-subtitle'>Movies, shows & anime we want to watch together</p>", unsafe_allow_html=True)
    
    # Calculate stats
    total_items = len(watchlist)
    movies = len([item for item in watchlist if "Movie" in item["type"]])
    series = len([item for item in watchlist if "Series" in item["type"]])
    anime = len([item for item in watchlist if "Anime" in item["type"]])
    watched = len([item for item in watchlist if item.get("watched", False)])
    
    # Stats section
    st.markdown("<div class='stats'>", unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown(f"""
        <div class='stat-item'>
            <div class='stat-number'>{total_items}</div>
            <div class='stat-label'>Total Items</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='stat-item'>
            <div class='stat-number'>{movies}</div>
            <div class='stat-label'>Movies</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class='stat-item'>
            <div class='stat-number'>{series}</div>
            <div class='stat-label'>Series</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class='stat-item'>
            <div class='stat-number'>{anime}</div>
            <div class='stat-label'>Anime</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown(f"""
        <div class='stat-item'>
            <div class='stat-number'>{watched}</div>
            <div class='stat-label'>Watched</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Filter buttons
    col1, col2, col3, col4, col5, spacer = st.columns([1, 1, 1, 1, 1, 1])
    
    with col1:
        if st.button("All", use_container_width=True):
            st.session_state.filter_type = "All"
            st.session_state.items_to_show = 9
            st.rerun()
    
    with col2:
        if st.button("Movies", use_container_width=True):
            st.session_state.filter_type = "Movie"
            st.session_state.items_to_show = 9
            st.rerun()
    
    with col3:
        if st.button("Series", use_container_width=True):
            st.session_state.filter_type = "Series"
            st.session_state.items_to_show = 9
            st.rerun()
    
    with col4:
        if st.button("Anime", use_container_width=True):
            st.session_state.filter_type = "Anime"
            st.session_state.items_to_show = 9
            st.rerun()
    
    with col5:
        if st.button("Watched", use_container_width=True):
            st.session_state.filter_type = "Watched"
            st.session_state.items_to_show = 9
            st.rerun()
    
    # Filter watchlist
    filtered_list = watchlist
    if st.session_state.filter_type == "Watched":
        filtered_list = [item for item in watchlist if item.get("watched", False)]
    elif st.session_state.filter_type != "All":
        filtered_list = [item for item in watchlist if st.session_state.filter_type in item["type"]]
    
    # Limit items to show
    display_list = filtered_list[:st.session_state.items_to_show]
    
    # Display watchlist in grid using columns
    cols_per_row = 3
    for i in range(0, len(display_list), cols_per_row):
        cols = st.columns(cols_per_row)
        for j, col in enumerate(cols):
            if i + j < len(display_list):
                item = display_list[i + j]
                with col:
                    watched_class = "watched" if item.get("watched", False) else ""
                    
                    st.markdown(f"""
                    <div class='media-card {watched_class}'>
                        <img src='{item["poster"]}' class='media-poster' alt='{item["title"]}'>
                        <div class='media-title'>{item["title"]}</div>
                        <a href='{item["link"]}' target='_blank' class='watch-link'>Watch Now</a>
                    </div>
                    """, unsafe_allow_html=True)
    
    # Show "Load More" button if there are more items
    if len(filtered_list) > st.session_state.items_to_show:
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([2, 1, 2])
        with col2:
            if st.button("Load More", use_container_width=True):
                st.session_state.items_to_show += 9
                st.rerun()

elif st.session_state.page == "Calender":
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Gloria+Hallelujah&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap');
                
        .stApp {
            background-image: url('https://github.com/yash-2345/2_october/blob/main/cropped-2be6e110d38154e314ff0a81060ee8e4.jpg?raw=true');
        }
        
        header[data-testid="stHeader"] {
            display: none;
        }
        
        .calendar-header {
            font-family: 'Gloria Hallelujah', cursive !important;
            color: white;
            text-align: center;
            font-size: 36px;
            margin-bottom: 20px;
            text-shadow: 0 0 10px rgba(255,255,255,0.5);
        }
        
        .countdown-main {
            background: #000000;
            border-radius: 20px;
            padding: 30px;
            margin: 20px 0;
            text-align: center;
            border: 3px solid rgba(255,255,255,0.3);
            box-shadow: 0 15px 40px rgba(0,0,0,0.5);
        }
        
        .countdown-event-name {
            font-family: 'Playfair Display', serif;
            font-size: 28px;
            color: white;
            margin-bottom: 10px;
            font-weight: bold;
        }
        
        .countdown-numbers {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin: 20px 0;
            flex-wrap: wrap;
        }
        
        .countdown-unit {
            background: rgba(255,255,255,0.1);
            border-radius: 15px;
            padding: 15px 20px;
            min-width: 80px;
            text-align: center;
            border: 2px solid rgba(255,255,255,0.2);
        }
        
        .countdown-number {
            font-family: 'Gloria Hallelujah', cursive;
            font-size: 36px;
            color: white;
            font-weight: bold;
            display: block;
        }
        
        .countdown-label {
            font-family: 'Playfair Display', serif;
            font-size: 14px;
            color: #e0e0e0;
            margin-top: 5px;
        }
        
        .events-list {
            background: rgba(255,255,255,0.1);
            border-radius: 15px;
            padding: 20px;
            margin: 20px 0;
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255,255,255,0.2);
        }
        
        .event-item {
            background: rgba(255,255,255,0.05);
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
            border: 1px solid rgba(255,255,255,0.1);
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: all 0.3s ease;
        }
        
        .event-item:hover {
            background: rgba(255,255,255,0.1);
            transform: translateY(-2px);
        }
        
        .event-info {
            flex: 1;
        }
        
        .event-name {
            font-family: 'Playfair Display', serif;
            font-size: 18px;
            color: white;
            font-weight: bold;
            margin: 0;
        }
        
        .event-date {
            font-family: 'Gloria Hallelujah', cursive;
            font-size: 14px;
            color: #cccccc;
            margin: 5px 0 0 0;
        }
        
        .event-countdown {
            font-family: 'Gloria Hallelujah', cursive;
            font-size: 16px;
            color: #ff6b9d;
            font-weight: bold;
        }
        
        .add-event-section {
            background: rgba(255,255,255,0.05);
            border-radius: 15px;
            padding: 20px;
            margin: 20px 0;
            border: 2px dashed rgba(255,255,255,0.3);
        }
        
        .add-event-title {
            font-family: 'Gloria Hallelujah', cursive;
            font-size: 20px;
            color: white;
            text-align: center;
            margin-bottom: 20px;
        }
        
        .delete-event-btn {
            background: rgba(255,0,0,0.3);
            border: 1px solid rgba(255,0,0,0.5);
            color: white;
            padding: 5px 10px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 12px;
            transition: all 0.3s ease;
            margin-left: 10px;
        }
        
        .delete-event-btn:hover {
            background: rgba(255,0,0,0.5);
        }
        
        .past-event {
            opacity: 0.5;
            background: rgba(128,128,128,0.2);
        }
        
        .today-event {
            background: rgba(255,215,0,0.2);
            border-color: rgba(255,215,0,0.5);
        }
        
        .calendar-grid {
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            gap: 3px;
            margin: 20px 0;
            background: rgba(255,255,255,0.1);
            padding: 15px;
            border-radius: 15px;
            max-width: 100%;
        }
        
        .calendar-day-header {
            background: rgba(255,255,255,0.3);
            padding: 15px 5px;
            text-align: center;
            font-family: 'Gloria Hallelujah', cursive;
            font-size: 16px;
            color: white;
            font-weight: bold;
            border-radius: 8px;
        }
        
        .calendar-day {
            background: rgba(255,255,255,0.05);
            padding: 10px 8px;
            text-align: left;
            font-family: 'Playfair Display', serif;
            color: white;
            min-height: 100px;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            align-items: flex-start;
            transition: all 0.3s ease;
            border-radius: 8px;
            border: 1px solid rgba(255,255,255,0.1);
            position: relative;
        }
        
        .calendar-day:hover {
            background: rgba(255,255,255,0.1);
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(255,255,255,0.1);
        }
        
        .calendar-day.today {
            background: rgba(255,215,0,0.2);
            border: 2px solid rgba(255,215,0,0.8);
            box-shadow: 0 0 15px rgba(255,215,0,0.3);
        }
        
        .calendar-day.has-event {
            background: rgba(255,105,180,0.2);
            border: 2px solid rgba(255,105,180,0.6);
        }
        
        .calendar-day.today.has-event {
            background: linear-gradient(135deg, rgba(255,215,0,0.3), rgba(255,105,180,0.3));
            border: 2px solid rgba(255,140,0,0.8);
        }
        
        .calendar-day.other-month {
            opacity: 0.2;
            background: rgba(255,255,255,0.02);
        }
        
        .day-number {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 5px;
            color: white;
        }
        
        .event-title {
            font-size: 10px;
            background: rgba(255,105,180,0.8);
            color: white;
            padding: 2px 6px;
            border-radius: 10px;
            margin: 1px 0;
            font-family: 'Gloria Hallelujah', cursive;
            font-weight: bold;
            text-overflow: ellipsis;
            overflow: hidden;
            white-space: nowrap;
            max-width: 100%;
        }
        
        .event-more {
            font-size: 9px;
            color: #cccccc;
            font-style: italic;
            margin-top: 2px;
        }
    </style>
    """, unsafe_allow_html=True)
    
    from datetime import datetime, timedelta, date
    import calendar
    
    # Initialize events in session state
    if "special_events" not in st.session_state:
        st.session_state.special_events = [
            {"name": "Our Anniversary", "date": "2024-05-30", "id": 1},
            {"name": "First Vc where we both talked", "date": "2024-12-10", "id": 2},
            {"name": "When I met you first", "date": "2024-4-15", "id": 3},
            {"name": "Fay's Bday", "date": "2025-10-02", "id": 4},
            {"name": "Valentine's Day", "date": "2025-02-14", "id": 5},
            {"name": "Space's Bday", "date": "2025-02-02", "id": 6},
            {"name": "Neko's Bday", "date": "2024-05-15", "id": 7},
            {"name": "Dad in law's Bday", "date": "2024-05-24", "id": 8},
            {"name": "Father in law's Bday", "date": "2024-04-25", "id": 9},
            {"name": "Sister in law's Bday", "date": "2025-03-20", "id": 10},
            {"name": "Lulu's Bday", "date": "2025-06-15", "id": 11},
            {"name": "Bob's Bday", "date": "2025-06-30", "id": 12},
            {"name": "Cousin in law's Bday", "date": "2024-04-13", "id": 13},
            {"name": "Space's sister's Bday", "date": "2024-10-12", "id": 14},
            {"name": "Space's mother's bday", "date": "2024-10-11", "id": 15},
            {"name": "Space's dad's Bday", "date": "2025-06-05", "id": 16},
            {"name": "Space's gramps Bday", "date": "2025-07-01", "id": 17},
            {"name": "National Girlfriend's day", "date": "2025-08-01", "id": 18},
            {"name": "National couples day", "date": "2025-08-18", "id": 19},
            {"name": "National Boyfriend's day", "date": "2025-10-3", "id": 2}
        ]
    
    if "event_id_counter" not in st.session_state:
        st.session_state.event_id_counter = 7
    
    # Helper functions
    def calculate_days_until(target_date_str):
        target_date = datetime.strptime(target_date_str, "%Y-%m-%d").date()
        today = date.today()
        delta = target_date - today
        return delta.days
    
    def format_countdown(days):
        if days < 0:
            return f"{abs(days)} days ago"
        elif days == 0:
            return "TODAY!"
        elif days == 1:
            return "in 1 day"
        else:
            return f"in {days} days"
    
    def get_next_event():
        today = date.today()
        future_events = []
        
        for event in st.session_state.special_events:
            event_date = datetime.strptime(event["date"], "%Y-%m-%d").date()
            
            # If the event is in the future this year, add it
            if event_date >= today:
                days_until = (event_date - today).days
                future_events.append((event, days_until))
            else:
                # If the event is in the past this year, calculate next year's occurrence
                next_year_date = event_date.replace(year=today.year + 1)
                days_until = (next_year_date - today).days
                # Create a modified event for next year
                next_year_event = event.copy()
                next_year_event["date"] = next_year_date.strftime("%Y-%m-%d")
                future_events.append((next_year_event, days_until))
        
        if future_events:
            future_events.sort(key=lambda x: x[1])
            return future_events[0]
        return None, None
    
    # Show header
    st.markdown("<h1 class='calendar-header'> Important Events!</h1>", unsafe_allow_html=True)
    
    # Define today variable here
    today = date.today()
    
    # Main countdown to next event
    next_event, days_until = get_next_event()
    
    if next_event:
        target_date = datetime.strptime(next_event["date"], "%Y-%m-%d").date()
        today = date.today()
        
        # Calculate detailed countdown
        if days_until >= 0:
            time_left = target_date - today
            days = time_left.days
            
            # Break down into months, weeks, days
            months = days // 30
            remaining_days_after_months = days % 30
            weeks = remaining_days_after_months // 7
            remaining_days = remaining_days_after_months % 7
            
            st.markdown(f"""
            <div class='countdown-main'>
                <div class='countdown-event-name'>Next: {next_event['name']}</div>
                <div class='countdown-numbers'>
                    <div class='countdown-unit'>
                        <span class='countdown-number'>{months}</span>
                        <div class='countdown-label'>Months</div>
                    </div>
                    <div class='countdown-unit'>
                        <span class='countdown-number'>{weeks}</span>
                        <div class='countdown-label'>Weeks</div>
                    </div>
                    <div class='countdown-unit'>
                        <span class='countdown-number'>{remaining_days}</span>
                        <div class='countdown-label'>Days</div>
                    </div>
                    <div style='color: white; font-size: 36px; font-family: "Gloria Hallelujah", cursive; display: flex; align-items: center; margin: 0 10px;'>=</div>
                    <div class='countdown-unit'>
                        <span class='countdown-number'>{days}</span>
                        <div class='countdown-label'>Total Days</div>
                    </div>
                </div>
                <div style='color: #e0e0e0; font-family: "Playfair Display", serif; font-style: italic;'>
                    {target_date.strftime("%A, %B %d, %Y")}
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class='countdown-main'>
            <div class='countdown-event-name'>No upcoming events</div>
            <div style='color: #e0e0e0; font-family: "Playfair Display", serif; font-style: italic;'>
                Add some special dates to look forward to!
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Calendar view - All upcoming events (no special treatment for first event)
    st.markdown("<h3 style='color: white; font-family: \"Gloria Hallelujah\", cursive; text-align: center; margin: 30px 0 20px 0;'>📅 All Upcoming Important Days</h3>", unsafe_allow_html=True)
    
    # Get upcoming events (next 5 events)
    today = date.today()
    future_events = []
    
    for event in st.session_state.special_events:
        event_date = datetime.strptime(event["date"], "%Y-%m-%d").date()
        
        # If the event is in the future this year, add it
        if event_date >= today:
            days_until = (event_date - today).days
            future_events.append((event, days_until, event_date))
        else:
            # If the event is in the past this year, calculate next year's occurrence
            next_year_date = event_date.replace(year=today.year + 1)
            days_until = (next_year_date - today).days
            # Create a modified event for next year
            next_year_event = event.copy()
            next_year_event["date"] = next_year_date.strftime("%Y-%m-%d")
            future_events.append((next_year_event, days_until, next_year_date))
    
    # Sort by days until and take next 5
    future_events.sort(key=lambda x: x[1])
    upcoming_events = future_events[:5]
    
    if upcoming_events:
        st.markdown("""
        <div style='background: rgba(255,255,255,0.1); border-radius: 20px; padding: 30px; margin: 20px 0; border: 2px solid rgba(255,255,255,0.2);'>
        """, unsafe_allow_html=True)
        
        # Show all events with consistent styling (removed the special first event styling)
        for event, days_until, event_date in upcoming_events:
            st.markdown(f"""
            <div style='background: rgba(255,255,255,0.05); border-radius: 12px; padding: 20px; margin: 10px 0; border: 1px solid rgba(255,255,255,0.2); display: flex; justify-content: space-between; align-items: center;'>
                <div>
                    <div style='color: white; font-family: "Playfair Display", serif; font-size: 20px; font-weight: bold; margin-bottom: 5px;'>{event['name']}</div>
                    <div style='color: #cccccc; font-family: "Gloria Hallelujah", cursive; font-size: 14px;'>{event_date.strftime('%A, %B %d, %Y')}</div>
                </div>
                <div style='color: #ff6b9d; font-family: "Gloria Hallelujah", cursive; font-size: 18px; font-weight: bold; text-align: right;'>
                    {format_countdown(days_until)}
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style='background: rgba(255,255,255,0.1); border-radius: 20px; padding: 30px; margin: 20px 0; text-align: center; border: 2px solid rgba(255,255,255,0.2);'>
            <div style='color: white; font-family: "Playfair Display", serif; font-size: 20px; font-style: italic;'>
                No upcoming events found. All your special days might be in the past!
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Beautiful message about your special dates
    st.markdown("""
    <div style='background: rgba(255,255,255,0.1); border-radius: 15px; padding: 20px; margin: 20px 0; text-align: center; border: 2px solid rgba(255,255,255,0.2);'>
        <div style='color: white; font-family: "Playfair Display", serif; font-size: 18px; font-style: italic; line-height: 1.6;'>
            These are the dates that are most important to me. With every year, every passing month, I can't wait to celebrate
                these with you over and over again.
        </div>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "Diary":
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Gloria+Hallelujah&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
        
        .stApp {
            background-color: black;
            color: white;
        }
        
        /* Set Inter as default for most elements */
        body, .stApp, .main, div, p, span, h2, h3, h4, h5, h6 {
            font-family: 'Inter', sans-serif !important;
        }
        
        /* Gloria Hallelujah only for the main title (h1) */
        h1, .stTitle h1, [data-testid="stMarkdownContainer"] h1 {
            font-family: 'Gloria Hallelujah', cursive !important;
        }
        
        /* Custom separator styling */
        .separator {
            border: none;
            height: 2px;
            background: linear-gradient(90deg, transparent, #ffffff, transparent);
            margin: 30px 0 20px 0;
            opacity: 0.3;
        }
        
        .stButton button {
            background-color: #222;
            color: white;
            border-radius: 8px;
            border: 1px solid #555;
            font-family: 'Inter', sans-serif !important;
        }
        
        h1:before {
            content: "";
            display: inline-block;
            background-image: url('https://github.com/yash-2345/2_october/blob/main/IMG-20250908-WA0012-removebg-preview.png?raw=true');
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
            width: 60px;
            height: 60px;
            margin-right: 15px;
            vertical-align: middle;
        }
        .nights-sky-header:before {
            content: "";
            display: inline-block;
            background-image: url('https://github.com/yash-2345/2_october/blob/main/IMG-20250908-WA0011-removebg-preview%20(4).png?raw=true');
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
            width: 60px;
            height: 60px;
            margin-right: 15px;
            vertical-align: middle;
        }

        .nights-sky-header {
            font-family: 'Inter', sans-serif !important;
            color: white;
            font-size: 1.25rem;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title("Cosmic Diary")
    
    # --- NASA APOD ---
    st.subheader("Cool Space Picture?")
    NASA_API_KEY = "M8Hga9UUxCCLGg5bpO80K4LlIUl108rNcVulsaAW"
    apod_url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    
    try:
        apod_data = requests.get(apod_url, timeout=5).json()
        if apod_data.get("media_type") == "image":
            st.image(apod_data["url"], caption=apod_data["title"])
        st.write(apod_data.get("explanation", ""))
    except Exception as e:
        st.warning(f"Could not fetch NASA APOD: {e}")
    
    # Add separator before Tonight's Sky
    st.markdown('<hr class="separator">', unsafe_allow_html=True)
    
    # --- Stellarium Web Embed ---
    st.markdown('<h2 class="nights-sky-header">Tonight\'s Sky</h2>', unsafe_allow_html=True)
    st.write("Explore the stars above us, live and interactive:")
    st.components.v1.iframe(
        "https://stellarium-web.org",
        height=600,
        scrolling=True
    )

# Create the navigation selectbox
main_pages = ["Home", "Library", "Calender", "Diary",]
sub_pages = ["Photos", "Videos", "Messages", "Voice Notes", "Memories", "Love Letters"]

# Determine what to show in selectbox
if st.session_state.page in main_pages:
    current_index = main_pages.index(st.session_state.page)
elif st.session_state.page in sub_pages:
    current_index = 1  # Library
else:
    current_index = 0  # Home

selected_page = st.selectbox(
    "Navigate to:",
    main_pages,
    index=current_index,
    key="navigation_select"
)

# Handle page changes - but don't override sub-page navigation
if selected_page != st.session_state.page and st.session_state.page not in sub_pages:
    st.session_state.page = selected_page
    st.rerun()
elif selected_page != "Library" and st.session_state.page in sub_pages:
    st.session_state.page = selected_page
    st.rerun()