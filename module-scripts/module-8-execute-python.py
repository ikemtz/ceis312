def azureml_main(frame1):

    # import libraries
    import matplotlib
    matplotlib.use('agg')  # Set backend

    from pandas.tools.plotting import scatter_matrix
    import pandas.tools.rplot as rplot
    import matplotlib.pyplot as plt
    import numpy as np

# Create a pair-wise scatter plot
    Azure = True

    fig1 = plt.figure(1, figsize=(10, 10))
    ax = fig1.gca()
    sm = scatter_matrix(frame1, alpha=0.3,
                        diagonal='kde', ax=ax)
    [s.xaxis.label.set_rotation(45) for s in sm.reshape(-1)]
    [s.yaxis.label.set_rotation(45) for s in sm.reshape(-1)]

    plt.show()
    fig1.savefig('scatter1.png')
