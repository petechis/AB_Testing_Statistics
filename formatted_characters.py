import streamlit as st

# constant Variables
star_and_space = '&#x2605;&nbsp;'
square_bullet_point0 ='&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#x2751'
square_bullet_point1 = '&#x2751;&nbsp;'
circle_bullet_point = '&#x2022;&nbsp;'
tab ='&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'


def custom_title(title, color, fsize, weight):
    st.markdown(f"<p style='text-align: center; color : {color}; font-size:{fsize}px; font-weight:{weight}'>{title}</p>", unsafe_allow_html=True)

def custom_sidebar_title(title, color, fsize, weight):
    st.sidebar.markdown(f"<p style='text-align: left; color : {color}; font-size:{fsize}px; font-weight:{weight}'>{title}</p>", unsafe_allow_html=True)

def custom_text(text, color, fsize, weight):
    st.sidebar.markdown(f"<p style='text-align: left; color : {color}; font-size:{fsize}px; font-weight:{weight}'>{text}</p>", unsafe_allow_html=True)

def custom_text_main(title, color, fsize, weight, align):
    st.markdown(f"<p style='text-align: {align}; color : {color}; font-size:{fsize}px; font-weight:{weight}'>{title}</p>", unsafe_allow_html=True)

intro = f"{square_bullet_point1} Introduction:<br> Findings from the experiment comparing two versions of websites. The goal was to see if the new version could increase the number of customers making purchases."
evaluation = f"{square_bullet_point1} The Experiment:<br> We conducted an experiment with two groups of 500 visitors each:<br>{circle_bullet_point}Group A used the old version of our website.<br>{circle_bullet_point}Group B used the new version of our website.<br><br>{square_bullet_point1}The Results:<br {circle_bullet_point}In Group A, 4.4% of visitors made a purchase.<br>{circle_bullet_point}In Group B, 7.45% of visitors made a purchase. <br>{circle_bullet_point}What Does This Mean? At first glance, it looks like the new website is performing better. But to be sure, we used a statistical test to see if this difference is significant or just due to random chance.<br>{circle_bullet_point}The Statistical Test: This new App calculated a p-value, which helps us understand the likelihood that the difference we observed is real and not just a fluke. In this case, the p-value was 0.04 (or 4.41%)."
insights =f"{square_bullet_point1}Example Insights and Interpreting the p-value:<br>{circle_bullet_point}A p-value less than 0.05 (5%) means we can be confident that the difference is significant. Since our p-value is 0.04, we can say with confidence that the new website is indeed better at converting visitors into customers."
summary = f"{square_bullet_point1} Conclusion:<br> Based on these results, we can confidently say that the new version of our website significantly increases the number of purchases. This is great news for our sales and overall business growth!<br><br>{square_bullet_point1}Example next Steps and Suggestions: We’ll continue to monitor the performance of the new website and look for more ways to improve our customer experience and sales."