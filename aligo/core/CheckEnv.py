def CheckEnv():
    try:
        from IPython import get_ipython
        ipy_str = str(type(get_ipython()))
        if 'zmqshell' in ipy_str:
            return 'jupyter'
        elif 'terminal' in ipy_str:
        #   return 'ipython'
            return 'terminal'
        elif 'colab' in ipy_str:
            return 'jupyter'
        else:
            return 'terminal'
    except:
            return 'terminal'
