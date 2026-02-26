import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Workforce Evolution & Automation Risk Dashboard",
    layout="wide",
)

st.title("Workforce Evolution & Automation Risk Dashboard")

st.markdown(
    """
    This project leverages **Python** and the **Gemini API** to analyze a 500-employee
    dataset, assessing each role's automation risk based on job characteristics, skill
    profiles, and industry trends. The analysis generates **targeted upskilling
    recommendations** to help organizations future-proof their workforce and guide
    strategic talent development.
    """
)

tableau_html = """
<div class='tableauPlaceholder' id='viz1772120712346' style='position: relative'>
  <noscript>
    <a href='#'>
      <img alt='Workforce Evolution &amp; Automation Risk'
           src='https://public.tableau.com/static/images/Wo/WorkforceAIReadinessUpskillingDashboard/WorkforceEvolutionAutomationRisk/1_rss.png'
           style='border: none' />
    </a>
  </noscript>
  <object class='tableauViz' style='display:none;'>
    <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
    <param name='embed_code_version' value='3' />
    <param name='site_root' value='' />
    <param name='name' value='WorkforceAIReadinessUpskillingDashboard/WorkforceEvolutionAutomationRisk' />
    <param name='tabs' value='no' />
    <param name='toolbar' value='yes' />
    <param name='static_image' value='https://public.tableau.com/static/images/Wo/WorkforceAIReadinessUpskillingDashboard/WorkforceEvolutionAutomationRisk/1.png' />
    <param name='animate_transition' value='yes' />
    <param name='display_static_image' value='yes' />
    <param name='display_spinner' value='yes' />
    <param name='display_overlay' value='yes' />
    <param name='display_count' value='yes' />
    <param name='language' value='en-US' />
  </object>
</div>
<script type='text/javascript'>
  var divElement = document.getElementById('viz1772120712346');
  var vizElement = divElement.getElementsByTagName('object')[0];
  if (divElement.offsetWidth > 800) {
    vizElement.style.width = '100%';
    vizElement.style.height = (divElement.offsetWidth * 0.75) + 'px';
  } else if (divElement.offsetWidth > 500) {
    vizElement.style.width = '100%';
    vizElement.style.height = (divElement.offsetWidth * 0.75) + 'px';
  } else {
    vizElement.style.width = '100%';
    vizElement.style.height = '827px';
  }
  var scriptElement = document.createElement('script');
  scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
  vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>
"""

components.html(tableau_html, height=850, scrolling=True)

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: grey;'>Developed by Krishna Vyas Pushkarna</p>",
    unsafe_allow_html=True,
)
