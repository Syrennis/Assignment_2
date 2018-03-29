#Gives active MJO events from a list of indices, ind, and minimum amplitude, min, 
#and the length of days it occurs for each event, ocur
#
#Args
#ind      A list of indices from MJO filtered dataset 
#min      A numeric that is of a certain value and all values above will return
#ocur     Amount of occurences to define an active MJO
#
#Output
#A vector with the amount of days each event lasts
#
#Note: no error checking
#

find_ocur <- function(ind, min, ocur)