from dash import dcc, html
import dash
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash(__name__)

forecast_df = pd.read_csv('results/predictive_results.csv')
pca_df = pd.read_csv('results/pca_results.csv')
cluster_df = pd.read_csv('results/cluster_results.csv')

app.layout = html.Div(children=[
    html.H1(children='COVID-19 Dashboard'),

    html.Div([
        html.H2('Predictive Modeling'),
        html.Label('Select Zoom Level (Days):'),
        dcc.Slider(
            id='zoom-slider',
            min=30,
            max=180,
            step=30,
            value=90,
            marks={30: '30 days', 60: '60 days', 90: '90 days', 120: '120 days', 150: '150 days', 180: '180 days'}
        ),
        dcc.Graph(id='predictive-graph')
    ]),

    html.Div([
        html.H2('PCA Analysis'),
        dcc.Graph(id='pca-graph')
    ]),

    html.Div([
        html.H2('Cluster Analysis'),
        dcc.Graph(id='cluster-graph')
    ])
])

@app.callback(
    dash.dependencies.Output('predictive-graph', 'figure'),
    [dash.dependencies.Input('zoom-slider', 'value')]
)
def update_predictive_graph(zoom_days):
 
    zoomed_data = forecast_df.tail(zoom_days)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=zoomed_data['Date'], y=zoomed_data['mean'], mode='lines', name='Forecasted Cases'))
    fig.add_trace(go.Scatter(x=zoomed_data['Date'], y=zoomed_data['mean_ci_upper'], fill=None, mode='lines', line_color='lightgrey', showlegend=False))
    fig.add_trace(go.Scatter(x=zoomed_data['Date'], y=zoomed_data['mean_ci_lower'], fill='tonexty', mode='lines', line_color='lightgrey', name='Confidence Interval'))
    
    fig.update_layout(
        title='Forecasted COVID-19 Cases (Zoomed In)',
        xaxis_title='Date',
        yaxis_title='Confirmed Cases'
    )
    
    return fig

@app.callback(
    dash.dependencies.Output('pca-graph', 'figure'),
    []
)
def update_pca_graph():
   
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=pca_df['PC1'], y=pca_df['PC2'], mode='markers', marker=dict(color='blue')))
    
    fig.update_layout(
        title='PCA Analysis',
        xaxis_title='Principal Component 1',
        yaxis_title='Principal Component 2'
    )
    
    return fig

@app.callback(
    dash.dependencies.Output('cluster-graph', 'figure'),
    []
)
def update_cluster_graph():

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=cluster_df['NewCases'], y=cluster_df['ConfirmedCases'], mode='markers', marker=dict(color=cluster_df['Cluster'], colorscale='Viridis')))
    
    fig.update_layout(
        title='Cluster Analysis',
        xaxis_title='New Cases',
        yaxis_title='Confirmed Cases'
    )
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
