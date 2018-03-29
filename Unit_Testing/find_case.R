#Uses previous functions to determine from list of active events, case, which are the longest events in days, ocurmin, 
#and establish which ones are significant enough to further analyze as a case study.
#
#Args
#case        Numeric list of amount of days separate active events are occuring
#ocurmin     Amount of occurences to define a signficant MJO
#
#Output
#A vector with the case study events that reach the criteria
#
#Note: no error checking
#

find_case <- function(case, ocurmin)