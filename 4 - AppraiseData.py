# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 12:11:51 2019

@author: graeme
"""
'''
Techniques for appraising Data include: checking data distribution via
box plots, plotting PDF and histograms. Identifying outliers. 
'''
#work out subplot size
def subplot_size(data):
    
    dfWidth = len(data.columns)
    large = int(plab.ceil(plab.sqrt(dfWidth)))
    small = int(plab.floor(plab.sqrt(dfWidth)))
    if large*small < dfWidth:
        small += 1
    return large,small

#plot bar graphs of nominal data
def plot_bars(data,wide):
    '''
    data = dataframe
    wide = boolean, True if subplots should be wide, false if they should be tall
    '''
    large,small = subplot_size(data)
    if wide:
        height = small
        width = large
    else:
        height = large
        width = small
    pos = 1
    for column in data:
        plab.figure(1)
        plab.subplot(height, \
                     width, \
                     pos,title=column)
        data[column].value_counts().plot.bar(rot=0)
        pos += 1
    plab.subplots_adjust(hspace=0.4)
    
#function to create combined boxplots and kde's
def box_kdes_advanced(data,wide):
    '''
    data = dataframe
    wide = boolean, True if subplots should be wide, False if they should be tall
    '''
    large,small = subplot_size(data)
    if wide:
        height = small
        width = large
    else:
        height = large
        width = small
    pos = 1
    for column in data:
        plab.figure(1)
        plab.subplot(height, \
                     width, \
                     pos,title=column)
        data[column].plot.kde()
        ymin,ymax = plab.ylim()
        yrange = ymax-ymin
        boxpos = yrange*0.1
        boxwidth = yrange*0.2

        data[column].plot.box(positions=[boxpos],manage_xticks=False,widths=boxwidth,vert=False,label=column)
        pos += 1
    plab.subplots_adjust(hspace=0.4)
        
def create_corrs(data,xrot,yrot,xsize,ysize):
    #Create Correlation Matrix
    plab.matshow(data.corr())
    #Include and Rotate labels
    plab.xticks(range(len(data.columns)), data.columns, rotation='vertical')
    plab.yticks(range(len(data.columns)), data.columns)
    
    corrMat = data.corr().as_matrix()
    #Create scatter matrix    
    ax = pd.plotting.scatter_matrix(data,diagonal='kde')
    for i, j in zip(*plab.np.triu_indices_from(ax, k=1)):
        ax[i, j].annotate("%.3f" %corrMat[i,j], (0.8, 0.8), xycoords='axes fraction', ha='center', va='center')
    
    #Rotate labels
    [plab.setp(item.xaxis.get_label(), 'rotation', xrot) for item in ax.ravel()]
    [plab.setp(item.yaxis.get_label(), 'rotation', yrot) for item in ax.ravel()]
    #Reduce y ticklabels size to unclutter
    [plab.setp(item.yaxis.get_majorticklabels(), 'size', ysize) for item in ax.ravel()]
    #Reduce x ticklabels size to unclutter
    [plab.setp(item.xaxis.get_majorticklabels(), 'size', xsize) for item in ax.ravel()]

def nominal_profit_kdehist(data,attribute,alpha):
    '''
    data = source dataframe
    attribute = str - single attribute from data
    alpha = transparency of histograms, float 0 to 1
    '''
    for nom in data[attribute].unique():
        if len(data[data[attribute]==nom]) > 1:
            data[data[attribute]==nom]['Profit'].plot.kde(label=nom)
            data[data[attribute]==nom]['Profit'].plot.hist(label=nom,alpha=alpha,normed=True)
    plab.title('Profit vs '+attribute)
    plab.xlabel('Profit (millions £)')
    plab.legend()
