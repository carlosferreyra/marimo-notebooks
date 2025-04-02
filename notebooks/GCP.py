

import marimo

__generated_with = "0.12.0"
app = marimo.App()




@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""# Welcome to the GCP Notebook""")
    return


if __name__ == "__main__":
    app.run()
