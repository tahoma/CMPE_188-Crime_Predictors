# Library code for the CMPE 188 "Crime Predictors" team project.

import bokeh.io
import bokeh.models
import bokeh.plotting

def map_incidents(df):

    # Extract the coordinates for the incidents on the extracted date.
    lats = []
    lons = []
    for row in df.itertuples():
        lats.append(float(row.Y))
        lons.append(float(row.X))

    # Create the map plot object.
    plot = bokeh.models.GMapPlot(
        x_range=bokeh.models.DataRange1d(),
        y_range=bokeh.models.DataRange1d(),
        map_options=bokeh.models.GMapOptions(
            lat=lats[0],
            lng=lons[0],
            map_type="roadmap",
            zoom=11
        )
    )

    # Give the map plot a title.
    plot.title.text = "San Francisco Police Department Incident Locations"

    # Given that it was needed for Bokeh mapping, I went ahead
    # and grabbed a Google Maps API key for a project named
    # "CMPE 188 - Crime Predictors".
    plot.api_key = "AIzaSyAs6Ugy0oz0R5YAxep9-kQ170t0U2fjELQ"

    # Add glyphs of blue circles at extracted locations of incidents.
    plot.add_glyph(
        bokeh.models.ColumnDataSource(data=dict(lat=lats, lon=lons)),
        bokeh.models.Circle(
            x="lon",
            y="lat",
            size=10,
            fill_color="blue",
            fill_alpha=0.20,
            line_color=None
        )
    )

    # Add the standard map control tools.
    plot.add_tools(
        bokeh.models.PanTool(),
        bokeh.models.WheelZoomTool(),
        bokeh.models.BoxSelectTool()
    )

    return plot
