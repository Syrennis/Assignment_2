#Takes a list of MJO indices, ind, and a minimum criteria, min, and returns a vector with 
#the dates of all matches 
#
#Args
#ind      A list of indices from MJO filtered dataset 
#min      A numeric that is of a certain value and all values above will return
#
#Output
#A vector with the the dates and indicies of all matches
#
#Note: no error checking
#

find_active<-function(ind, min)

  data <- c()
  for(i in seq_along(ind)){
    data <- (ind >= min)
  }

