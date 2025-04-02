import marimo

__generated_with = "0.12.0"
app = marimo.App()




@app.cell
def _():
    import marimo as mo
    print(mo.__version__)
    return


if __name__ == "__main__":
    app.run()
