import plotly.express as px

def rides_by_hour(df):
    hourly = df['HOUR'].value_counts().sort_index()
    fig = px.bar(
        x=hourly.index,
        y=hourly.values,
        labels={'x': 'Hour of Day', 'y': 'Number of Rides'},
        title='Rides by Hour'
    )
    return fig


def rides_by_day(df):
    day_count = df['DAY'].value_counts()
    fig = px.pie(
        names=day_count.index,
        values=day_count.values,
        title='Rides by Day'
    )
    return fig


def purpose_distribution(df):
    purpose_count = df['PURPOSE'].value_counts()
    fig = px.bar(
        x=purpose_count.index,
        y=purpose_count.values,
        labels={'x': 'Purpose', 'y': 'Rides'},
        title='Ride Purpose Distribution'
    )
    return fig
