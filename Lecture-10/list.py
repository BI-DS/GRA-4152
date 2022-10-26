########################################
### EXAMPLE: Buggy code to reverse a list
### Try to debug it! (fixes needed are explained below)
########################################
def rev_list_buggy(L):
    """
    input: L, a list
    Modifies L such that its elements are in reverse order
    returns: nothing
    """
    for i in range(len(L)):
        j = len(L) - i
        L[i] = temp
        L[i] = L[j]
        L[j] = L[i]

