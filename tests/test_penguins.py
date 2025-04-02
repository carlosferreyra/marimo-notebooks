import polars as pl
import pytest

from notebooks.penguins import app


@pytest.fixture
def penguins_df():
    """Fixture to provide the penguins dataframe"""
    df = app.get_cell_value("df")
    return df


def test_data_loading(penguins_df):
    """Test that the penguins dataset is loaded correctly"""
    assert isinstance(penguins_df, pl.DataFrame)
    assert not penguins_df.is_empty()

    # Check required columns exist
    required_columns = {"species", "bill_length_mm", "bill_depth_mm"}
    assert all(col in penguins_df.columns for col in required_columns)


def test_species_chart():
    """Test that the species distribution chart is created correctly"""
    species_chart = app.get_cell_value("species_chart")

    # Test chart properties
    chart_spec = species_chart.component.chart
    assert chart_spec.mark == "bar"
    assert chart_spec.encoding.x.field == "species"
    assert chart_spec.encoding.y.aggregate == "count"


def test_scatter_plot():
    """Test that the bill dimensions scatter plot is created correctly"""
    scatter = app.get_cell_value("scatter")

    # Test chart properties
    chart_spec = scatter.component.chart
    assert chart_spec.mark == "point"
    assert chart_spec.encoding.x.field == "bill_length_mm"
    assert chart_spec.encoding.y.field == "bill_depth_mm"
    assert "species" in chart_spec.encoding.color.field


def test_data_quality(penguins_df):
    """Test data quality and completeness"""
    # Check for expected species
    expected_species = {"Adelie", "Gentoo", "Chinstrap"}
    actual_species = set(penguins_df.select("species").unique().to_series().to_list())
    assert actual_species == expected_species

    # Check numeric columns have sensible ranges
    assert penguins_df.select("bill_length_mm").max()[0] < 100  # mm
    assert penguins_df.select("bill_depth_mm").max()[0] < 50  # mm
