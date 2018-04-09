#Gives active MJO events from a list of indices find the length of days it occurs for each event.
#
#Args
#ind      A list of indices from MJO filtered dataset 
#
#Output
#A vector with the amount of days each event lasts
#
#Note: no error checking
#

find_ocur <- function(ind)

{   
  # transpose maindtrix and square the vector
  
  step1 <- c(ind)
  step2 <- diff(unique(cumsum(step1 >=1)[step1 <= 1]))
  step3 <- c(step2)
  
  # save both results in a list and return
  final <- step3
  return(final)
}