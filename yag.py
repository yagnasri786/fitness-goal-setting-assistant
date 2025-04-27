import streamlit as st
import datetime
import plotly.express as px
import pandas as pd
from PIL import Image  # Import the Pillow (PIL) library for image manipulation

# Set light mode layout
st.set_page_config(page_title="Fitness Goal Setting Assistant", layout="wide")

# ✅ Custom CSS Fix for readability and smaller fonts
st.markdown("""
    <style>
        .stApp {
            background-color: #f7f7f9;
            color: #212529;
            font-family: 'Helvetica', sans-serif;
            font-size: 0.9rem; /* Default font size */
        }

        h1 {
            color: #6a0dad;
            font-size: 1.8rem;
        }

        h2 {
            color: #6a0dad;
            font-size: 1.6rem;
        }

        h3 {
            color: #6a0dad;
            font-size: 1.4rem;
        }

        h4 {
            color: #6a0dad;
            font-size: 1.2rem;
        }

        /* Label and input fixes */
        label, .stRadio > div, .css-1cpxqw2 {
            color: #212529 !important;
            font-size: 0.9rem !important;
        }

        /* Ensure radio button labels are dark */
        div[data-baseweb="radio"] label span {
            color: #212529 !important;
            font-size: 0.9rem !important;
        }

        .stButton button {
            background-color: #6a0dad;
            color: white;
            border-radius: 4px;
            padding: 0.4em 0.8em; /* Slightly smaller button padding */
            font-size: 0.9rem;
        }

        .stButton button:hover {
            background-color: #5a009d;
        }

        /* Decrease font size for markdown content */
        .stMarkdown {
            font-size: 0.9rem;
        }

        /* Decrease font size for selectbox options */
        .stSelectbox > div > div > div > div {
            font-size: 0.9rem;
        }

        /* Decrease font size for slider labels and values */
        .stSlider label, .stSlider div div div div p {
            font-size: 0.9rem !important;
        }

        /* Decrease font size for date input */
        .stDateInput > div > div > input {
            font-size: 0.9rem !important;
        }

        /* Decrease font size for multiselect */
        .stMultiSelect > div > div > div {
            font-size: 0.9rem !important;
        }

        /* Decrease font size for plotly chart titles and labels */
        .plotly-graph-div text {
            font-size: 0.9rem !important;
        }

        .streamlit-expander {
            font-size: 0.9rem;
        }
        .streamlit-expander > div[data-testid="stExpanderToggle"] > p {
            font-size: 0.9rem;
        }
    </style>
""", unsafe_allow_html=True)

# Function to resize a local image
def resize_local_image(image_path, max_width):
    try:
        img = Image.open(image_path)
        width, height = img.size
        if width > max_width:
            ratio = max_width / width
            new_height = int(height * ratio)
            resized_img = img.resize((max_width, new_height))
            return resized_img
        return img
    except FileNotFoundError:
        st.error(f"Error: Image not found at {image_path}")
        return None
    except Exception as e:
        st.error(f"Error processing image {image_path}: {e}")
        return None

# Function to display a resized local image in Streamlit
def display_resized_local_image(image_path, caption, max_width, use_container_width=False):
    resized_image = resize_local_image(image_path, max_width)
    if resized_image:
        st.image(resized_image, caption=caption, use_column_width=use_container_width)
    else:
        st.image("https://via.placeholder.com/400x300?text=No+Image+Available", caption=caption, use_column_width=use_container_width)

# -------------------------
# App Title
# -------------------------
st.title("💪 FitBuddy Pro: Your Advanced Fitness Goal Assistant")
st.write("Welcome! Let's build a smarter, customized fitness plan just for you. Answer a few quick questions to get started.")

# -------------------------
# Sidebar Navigation
# -------------------------
st.sidebar.header("🧭 Navigation")
page = st.sidebar.radio("Go to:", ["Fitness Planner", "Progress Dashboard"])

# -------------------------
# Fitness Planner Page
# -------------------------
if page == "Fitness Planner":
    st.subheader("📋 Step-by-Step Fitness Planner")

    goal = st.selectbox("1️⃣ What's your primary fitness goal?",
                        ["Lose Weight", "Build Muscle", "Increase Stamina", "Improve Flexibility", "General Health"])
    workout_days = st.slider("2️⃣ How many days a week can you realistically work out?", 1, 7, 3)
    duration = st.selectbox("3️⃣ Average workout duration per session?",
                            ["15-30 mins", "30-45 mins", "45-60 mins", "60+ mins"])
    diet = st.selectbox("4️⃣ Do you follow a diet or have any dietary preferences?",
                        ["No Preference", "Vegetarian", "Vegan", "Keto", "Low Carb", "High Protein"])
    level = st.radio("5️⃣ What's your current fitness level?",
                      ["Beginner", "Intermediate", "Advanced"])
    preferred_workouts = st.multiselect("6️⃣ Preferred types of workouts:",
                                        ["Cardio", "Strength Training", "Yoga/Pilates", "HIIT", "Stretching", "Cycling", "Swimming"])
    start_date = st.date_input("📅 When do you want to start your plan?", datetime.date.today())

    if st.button("🎯 Generate My Fitness Plan"):
        st.subheader("🏁 Your Personalized Fitness Goal Plan")

        plan = f"""
        **Goal:** {goal}
        **Workout Frequency:** {workout_days} days/week
        **Session Duration:** {duration}
        **Diet Preference:** {diet}
        **Fitness Level:** {level}
        **Preferred Workouts:** {', '.join(preferred_workouts) if preferred_workouts else 'No specific preference'}
        **Start Date:** {start_date.strftime('%B %d, %Y')}

        **Suggested Plan:**
        - {"Begin with light cardio and stretching." if level == "Beginner" else "Include strength training and HIIT sessions."}
        - {"Focus on maintaining a calorie deficit and clean eating." if goal == "Lose Weight" else "Prioritize protein intake and resistance training."}
        - {"Incorporate mindfulness and yoga once a week for flexibility and recovery." if "Yoga/Pilates" in preferred_workouts else "Ensure rest and recovery days are built-in."}
        - Stay hydrated and track your macros with an app.
        - Set a weekly progress checkpoint every Sunday.
        - Optional: Sync with a fitness tracker to monitor steps, sleep, and calories.
        """
        st.markdown(plan)
        st.success("✅ Your Pro Fitness Plan is Ready! Time to crush those goals!")
        st.balloons()

    st.markdown("---")
    st.subheader("🥗 What Should You Eat?")

    goal_images = {
        "Lose Weight": "c:\\Users\\asus\\Desktop\\How To Lose  Weight at Home.jpg",
        "Build Muscle": "c:\\Users\\asus\\Desktop\\build muscle.jpg",
        "Increase Stamina":"c:\\Users\\asus\\Desktop\\increase stamina.png ",
        "Improve Flexibility": "c:\\Users\\asus\\Desktop\\improve flexibility.webp",
        "General Health": "c:\\Users\\asus\\Desktop\\Body-Functioning-and-General-Health.png"
    }

    goal_image_path = goal_images.get(goal)

    if goal_image_path:
        # Resize the goal image to a maximum width of 400 pixels
        display_resized_local_image(goal_image_path, caption="Recommended Nutrition", max_width=400, use_container_width=True)
    else:
        st.image("https://via.placeholder.com/400x300?text=No+Image+Available", caption="No Image Available", use_container_width=True)

    # 🎯 Show some extra healthy food images
    st.markdown("### 🥑 More Healthy Inspirations")
    healthy_images = [
        "c:\\Users\\asus\\Desktop\\fruits.jpg",  # Fruits
        "c:\\Users\\asus\\Desktop\\Garden-Salad_47-SQ.webp",  # Salad
        "c:\\Users\\asus\\Desktop\\Tropical-Smoothie-223.jpg",  # Smoothie
        "c:\\Users\\asus\\Desktop\\veggies.jpg"   # Veggies
    ]

    for img_url in healthy_images:
        st.image(img_url, use_container_width=True) # Assuming these are URLs

    st.markdown("---")
    st.subheader("🌐 Useful Resources")
    st.markdown("""
    - [🏋️‍♂️ Beginner Workout Guide](https://www.verywellfit.com/beginners-guide-to-working-out-1231143)
    - [🍎 Healthy Diet Plans](https://www.eatright.org/health/wellness/healthy-eating)
    - [⌚ Best Fitness Trackers](https://www.tomsguide.com/best-picks/best-fitness-trackers)
    - [🧘 Yoga for Beginners](https://www.yogajournal.com/poses/yoga-for/beginners/)
    - [🚴‍♀️ Cycling Workouts](https://www.bicycling.com/training/a20044096/5-cycling-workouts-everyone-should-know/)
    """, unsafe_allow_html=True)


    st.markdown("---")
    st.subheader("🏋️‍♀️ What Should You Do?")
    workout_images = {
    "Cardio": "c:\\Users\\asus\\Desktop\\cardio.jpg",
    "Strength Training": "c:\\Users\\asus\\Desktop\\stength training.jpg",
    "Yoga/Pilates": "c:\\Users\\asus\\Desktop\\yoga.jpg",
    "HIIT": "c:\\Users\\asus\\Desktop\\hiit-workouts-for-men_blogheader-no-title.jpg",
    "Cycling": "c:\\Users\\asus\\Desktop\\cycling.jpg",
    "Swimming": "c:\\Users\\asus\\Desktop\\swimming.jpg"
}
    for activity in preferred_workouts:
        workout_image_url = workout_images.get(activity)
        if workout_image_url:
            st.image(workout_image_url, caption=f"{activity} Routine", use_column_width=True)
        else:
            st.image("https://via.placeholder.com/400x300?text=No+Image+Available", caption=f"No Image Available for {activity}", use_column_width=True)

# -------------------------
# Progress Dashboard Page
# -------------------------
elif page == "Progress Dashboard":
    st.subheader("📊 Your Fitness Progress Dashboard")

    df = pd.DataFrame({
        'Week': [f'Week {i}' for i in range(1, 7)],
        'Weight (kg)': [75, 74.2, 73.5, 72.8, 72.1, 71.4],
        'Workout Count': [3, 4, 4, 5, 4, 5],
        'Calories Burned': [1200, 1400, 1450, 1600, 1550, 1650]
    })

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔻 Weight Trend")
        fig1 = px.line(df, x='Week', y='Weight (kg)', markers=True, title="Weight Loss Over Time")
        fig1.update_layout(paper_bgcolor='#ffffff', plot_bgcolor='#f9fafb', font=dict(color='#212529', size=10)) # Smaller font size
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.markdown("### 🔥 Workout Stats")
        fig2 = px.bar(df, x='Week', y='Workout Count', title="Workouts Per Week",
                        color='Workout Count', color_continuous_scale='Blues')
        fig2.update_layout(paper_bgcolor='#ffffff', plot_bgcolor='#f9fafb', font=dict(color='#212529', size=10)) # Smaller font size
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("### 🍽️ Calories Burned")
    fig3 = px.area(df, x='Week', y='Calories Burned', title="Weekly Calories Burned", markers=True,
                    color_discrete_sequence=["orange"])
    fig3.update_layout(paper_bgcolor='#ffffff', plot_bgcolor='#f9fafb', font=dict(color='#212529', size=10)) # Smaller font size
    st.plotly_chart(fig3, use_container_width=True)

    # Footer inside the 'Progress Dashboard' page
    st.markdown("---")
    st.caption("Created by your AI fitness buddy 💪 FitBuddy Pro")