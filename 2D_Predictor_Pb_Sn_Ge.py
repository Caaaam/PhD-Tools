import sys
import chart_studio.plotly as py
import plotly.graph_objects as go
import plotly as plty
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np

# Tolerance Factor Prediction for 2D Perovskites Pb/Sn/Ge Mixes
# From http://abulafia.mt.ic.ac.uk/shannon/ptable.php and https://pubs.acs.org/doi/pdf/10.1021/acs.chemmater.9b04472 https://pubs.rsc.org/en/content/articlepdf/2016/sc/c5sc04845a

Ra_list = {
        'PEA' : 4,
        'BA' : 3,
        'EA' : 2.74, 
        'FA' : 2.53, 
        'MA' : 2.16,
        'Cs' : 1.81}

Rb_list = {
        'Pb' : 1.19,
        'Sn' : 1.04,
        'Ge' : 0.73}

Rx_list = {
        'I' : 2.20,
        'Br' : 1.96,
        'Cl' : 1.81}

# Defines a np array for various values of Ra and Rx 
Ra_Range = np.linspace(Ra_list[min(Ra_list.keys(), key=(lambda k: Ra_list[k]))],Ra_list[max(Ra_list.keys(), key=(lambda k: Ra_list[k]))],10)
Rx_Range = np.linspace(Rx_list[min(Rx_list.keys(), key=(lambda k: Rx_list[k]))],Rx_list[max(Rx_list.keys(), key=(lambda k: Rx_list[k]))],10) 

for Rb in Rb_list: 
    ToleranceFactor = [] 
    # Calcs Tol Facs for Anything in original lists
    Scatter = {}
    Ra_Scatter = [] 
    Rb_Scatter = [] 
    Rx_Scatter = [] 
    for Ra in Ra_list:
        for Rx in Rx_list: 

            # Revised tol factor model (2016) https://pubs.rsc.org/en/content/articlepdf/2016/sc/c5sc04845a
            if Rb == 'Pb' and Rx == 'I':
                Rb_list[Rb] = 1.03
            elif Rb == 'Pb' and Rx == 'Br':
                Rb_list[Rb] = 0.98
            elif Rb == 'Pb' and Rx == 'Br':
                Rb_list[Rb] = 0.98
            elif Rb == 'Pb' and Rx == 'Cl':
                Rb_list[Rb] = 0.99
            elif Rb == 'Sn' and Rx == 'I':
                Rb_list[Rb] = 0.97
            elif Rb == 'Ge' and Rx == 'I':
                Rb_list[Rb] = 0.77

            # Updates the Scatter Plot Data with Correct Names for 2D, 1.06 suggested in https://pubs.rsc.org/en/content/articlepdf/2016/sc/c5sc04845a
            if (float(Ra_list[Ra])+float(Rx_list[Rx]))/(np.sqrt(2)*((float(Rb_list[Rb]))+float(Rx_list[Rx]))) > 1.06: 
                Scatter.update({str(Ra)+'2'+str(Rb)+str(Rx)+'4' : (float(Ra_list[Ra])+float(Rx_list[Rx]))/(np.sqrt(2)*((float(Rb_list[Rb]))+float(Rx_list[Rx])))})
            else: 
                Scatter.update({str(Ra)+str(Rb)+str(Rx)+'3' : (float(Ra_list[Ra])+float(Rx_list[Rx]))/(np.sqrt(2)*((float(Rb_list[Rb]))+float(Rx_list[Rx])))})

            # Appends to single list to be plotted on scatter3d
            Ra_Scatter.append(Ra_list[Ra])
            Rb_Scatter.append(Rb_list[Rb])
            Rx_Scatter.append(Rx_list[Rx])

    # Print
    for key in Scatter: 
        print(key+ ": {:.2f}".format(Scatter[key]))

    # Generating surface plot
    for Ra in Ra_Range:
        for Rx in Rx_Range: 
            ToleranceFactor.append((float(Ra)+float(Rx))/(np.sqrt(2)*((float(Rb_list[Rb]))+float(Rx))))
    
    # Reshape to Rx_Range x Ra_Range
    TolFacReshaped = np.array(ToleranceFactor).reshape((len(Ra_Range), len(Rx_Range)))

    fig = go.Figure()
    
    '''
    fig.add_trace(
        go.Surface(
            name = "Surface",
            x = Ra_Range,
            y = Rx_Range,
            z = TolFacReshaped,
            contours_z=dict(show=True, highlightcolor="limegreen", project_z=True)
        )
    )
    '''

    fig.add_trace(
        go.Scatter3d(
            name = "Scatter",
            x = Ra_Scatter,
            y = Rx_Scatter,
            z = list(Scatter.values()),
            text = list(Scatter.keys()),
            mode='markers+text'
        )
    )

    # Titles
    fig.update_layout(
                title = str(Rb)+' Tolerance Factor',
                scene = dict(
                    xaxis_title = "Ionic Radius of A site (Å)",
                    yaxis_title = "Ionic Radius of X site (Å)",
                    zaxis_title = 'Tolerance Factor'
                    )
                )

    # Range etc
    fig.update_layout(
        scene = dict(
            xaxis = dict(range=[0.98*min(Ra_Scatter),1.05*max(Ra_Scatter)],),
            yaxis = dict(range=[0.98*min(Rx_Scatter),1.02*max(Rx_Scatter)],),
            zaxis = dict(range=[0.98*min(list(Scatter.values())),1.02*max(list(Scatter.values()))],)))

    fig.show()
    filename = str(Rb)+'_TolerenceFactor.html'
    fig.write_html(filename)

