#***DAN: I did not understand until I read Tests.Rmd what this function was doing because I 
#do not know what MJO refers to.

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
    step1 <- c(ind) #***DAN: what is the purpose of this line? seems like none
    step2 <- ifelse(ind>=min, ind, 0) #***DAN: filling with 0s is often a bad idea unless it is impossible for MJOs (still don't know what those are) to be 0 naturally
    
    # save results and return
    final <- step2 
    return(final)
  }