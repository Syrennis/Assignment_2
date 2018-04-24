#' Find Case Study Function
#'
#' Uses previous functions to determine from list of active events, case, which are the long enough in days, ocurmin,
#' and establish which ones are significant enough to further analyze as a case study.
#' @param case Numeric list of amount of days separate active events are occuring
#' @param ocurmin Amount of occurences to define a signficant MJO
#' @export #A vector with the case study events that reach the criteria
#' @examples
#' find_active(data, 30)

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
