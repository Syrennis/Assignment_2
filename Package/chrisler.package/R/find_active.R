#' Find Active Function
#'
#' Takes a list of MJO indices, ind, and a minimum criteria, min,
#' and returns a vector with the dates of all matches
#' @param ind A list of indices from MJO filtered dataset
#' @param min A numeric that is of a certain value and all values above will return
#' @export #A vector with active MJO events
#' @examples
#' find_active(data, 1)

find_active <- function(ind, min)

  {
    # steps for function
    step1 <- c(ind)
    step2 <- ifelse(ind>=min, ind, 0)

    # save results and return
    final <- step2
    return(final)
  }
