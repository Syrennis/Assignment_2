#Takes a list of MJO indices, ind, and a minimum criteria, min, and returns a vector with 
#the dates of all matches 
#
#Args
#ind      A list of indices from MJO filtered dataset 
#min      A numeric that is of a certain value and all values above will return
#
#Output
#A vector with active MJO events
#
#Note: no error checking
#

find_active <- function(ind, min)

  {   
    # steps for function
    step1 <- c(ind)
    step2 <- ifelse(ind>=min, ind, 0)
    
    # save results and return
    final <- step3
    return(final)
  }