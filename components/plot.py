import plotly.express as px
import plotly.graph_objects as go


def sf_plot(x, shear):
    fig_sfd = go.Figure()
    fig_sfd.add_trace(go.Scatter(x=x, y=shear, mode='lines', name='Shear Force'))
    fig_sfd.update_layout(
        title='Shear Force Diagram',
        xaxis_title='Position (m)',
        yaxis_title='Shear Force (kN)',
        height=400
    )
    return fig_sfd



# Create BMD plot


def bmd_plot(x, moment):
    fig_bmd = go.Figure()
    fig_bmd.add_trace(go.Scatter(x=x, y=moment, mode='lines', name='Bending Moment'))
    fig_bmd.update_layout(
        title='Bending Moment Diagram',
        xaxis_title='Position (m)',
        yaxis_title='Bending Moment (kN·m)',
        height=400
    )
    return fig_bmd

