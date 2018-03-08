import scrape_twitter
import back_end

job_seeker_culture = scrape_twitter.twitter_dataframe("kobebryant")
firstname = "Dennis"
lastname = "Tran"
street = "10592 Woodbury Road"
city = "Garden Grove"
state = "CA"
pred = back_end.lukes_function(firstname, lastname, street, city, state, job_seeker_culture)      

print(pred)