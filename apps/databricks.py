# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo[dev,lsp,recomended,sql]",
#     "vega-datasets==0.9.0",
# ]
# ///

import marimo

__generated_with = "0.14.10"
app = marimo.App(width="full", app_title="Databricks")


@app.cell(hide_code=True)
def first_cell():
    import marimo as mo
    from vega_datasets import data
    from datetime import datetime
    return datetime, mo, welcome_msg


@app.cell
def navigation(datetime, mo, welcome_msg):

    # Create routes that correspond to the navigation menu
    routes = mo.routes(
        {
            "#/home": "home",
            "#/about": "about",
            "#/contact": "contact",
            "#/examples": "examples",
            "#/extract": "extract",
            "#/transform": "transform",
            "#/load": "load",
            mo.routes.CATCH_ALL: "home",  # Default route
        }
    )
    # Create navigation menu for those routes
    main_nav = mo.nav_menu(
        {
            "#/home": f"{mo.icon('lucide:home')} Home",
            "#/about": f"{mo.icon('lucide:user')} About",
            "#/contact": f"{mo.icon('lucide:phone')} Contact",
            "#/examples": f"{mo.icon('lucide:database')} Example ETL",
        },
        orientation="vertical",
    )

    # Create navigation menu for ETL examples
    etl_nav = mo.nav_menu(
        {
            "#/extract": f"{mo.icon('lucide:download')} Extract",
            "#/transform": f"{mo.icon('lucide:shuffle')} Transform",
            "#/load": f"{mo.icon('lucide:upload')} Load",
        },
        orientation="vertical",
    )

    # Create navigation menu for external links
    my_links = mo.nav_menu(
        {
            "https://github.com/carlosferreyra": f"{mo.icon('lucide:github')} Carlos Ferreyra",
            "https://www.carlosferreyra.me": f"{mo.icon('lucide:globe')} Carlos Ferreyra's Website",

        },
        orientation="vertical",
    )



    mo.sidebar([
        mo.md(f"{welcome_msg}"),
        mo.accordion(
            {
                f"{mo.md(r'## 🧭 Navigation')}": main_nav,
                f"{mo.md(r'## ⚙️ ETL Operations')}": etl_nav,
                f"{mo.md(r'## 🔗 My Links')}": my_links,
            }
        ),
    ],
    footer=mo.callout(
        mo.md(f"""#### Powered by [Marimo](https://marimo.io): [{mo.icon('lucide:github')}](https://github.com/marimo-team/marimo)
            All rights reserved. {datetime.now().year}"""),
        kind="neutral"
    ))

    # Display the routed content in the main area
    return routes


@app.cell
def home(mo):
    # Home page content with data display
    _blanks = "".join(['\n'] * 50)
    mo.md(f"""
    This is the home page of your Marimo notebook running in Databricks.
    Below you can see a sample of the cars dataset:{_blanks}
    """)
    return


@app.cell
def about(mo):
    # Display information about the notebook
    mo.md(
        """
        # About this Notebook
        This notebook is a demonstration of Marimo's capabilities in a Databricks environment.
        It includes navigation, data display, and interactive elements.
        """
    )
    return


@app.cell
def contact(mo):
    # Display contact information
    content = mo.md(
        """
        # Contact Us
        For more information, please reach out to us at:
        - Email: some_email@example.com
        - GitHub: [@carlosferreyra](https://github.com/carlosferreyra)
        - Website: [carlosferreyra.me](https://www.carlosferreyra.me)
        """)
    return


@app.cell
def examples(mo):
    # Examples page content with ETL overview
    mo.md(
        """
        # Example ETL Operations

        This section demonstrates Extract, Transform, and Load operations in a Databricks environment.
        Use the ETL Operations menu to navigate to specific operations:

        - **Extract**: Data extraction from various sources
        - **Transform**: Data transformation and processing
        - **Load**: Data loading to target destinations
        """
    )
    return


@app.cell
def extract(mo):
    mo.md("""# Extract Section""")
    return


@app.cell
def transform(mo):
    mo.md("""# Transform Section""")
    return


@app.cell
def load(mo):
    mo.md("""# Load Section""")
    return


if __name__ == "__main__":
    app.run()
