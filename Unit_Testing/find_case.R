#Uses previous functions to determine from list of active events, case, which are the long enough in days, ocurmin, 
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

find_case <- function(case, ocur)
  
{   
  # steps for function
  step1 <- c(case)
  step2 <- ifelse(case>=ocur, case, NaN)
  step3 <- na.omit(step2)
  
  # save results and return
  final <- step3
  return(final)
}