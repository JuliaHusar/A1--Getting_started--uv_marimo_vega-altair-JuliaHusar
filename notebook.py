import marimo

__generated_with = "0.19.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import altair as alt
    return alt, mo


@app.cell
def _():
    from vega_datasets import data
    cars = data.cars()
    cars.head()
    return (cars,)


@app.cell
def _(alt, cars):
    chart = alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N'
    ).properties(
        title='Horsepower vs MPG'
    ).interactive()
   
    chart
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Car Efficiency Analysis

    This scatter plot shows the relationship between horsepower and Miles-Per-Gallon (MPG) for the region of origin of cars. Cars from the USA tend to have a higher horsepower but lower MPG, while cars from other countries have lower horsepower but higher MPG.
    """)
    return


if __name__ == "__main__":
    app.run()
