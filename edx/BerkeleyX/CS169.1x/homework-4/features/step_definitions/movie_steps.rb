# Add a declarative step here for populating the DB with movies.

Given /the following movies exist/ do |movies_table|
  movies_table.hashes.each do |movie|
    Movie.create!(movie)
  end
end

# Make sure that one string (regexp) occurs before or after another one
#   on the same page

Then /I should see "(.*)" before "(.*)"/ do |e1, e2|
  assert !page.body.match(/#{e1}.*#{e2}/m).nil?
end

# Make it easier to express checking or unchecking several boxes at once
#  "When I uncheck the following ratings: PG, G, R"
#  "When I check the following ratings: G"

When /I (uncheck|check) the following ratings: (.*)/ do |uncheck, rating_list|
  rating_list.split(/, ?/).each do |rating|
     steps %Q{When I #{uncheck} "ratings_#{rating}"}
  end
end

Then /I should see all of the movies/ do
  movie_rows = Movie.count
  page.should have_css("table tr", :count => movie_rows + 1)
end

Then /the director of "(.*)" should be "(.*)"/ do |movie, director|
  assert !page.body.match(/Director: #{director}/).nil?
end