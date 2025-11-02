try:
    import pandas
    import numpy
    import scikit_learn
    import matplotlib
    import plotly
    import streamlit
    print("All libraries are installed!")
except ModuleNotFoundError as e:
    print("Missing library:", e)
