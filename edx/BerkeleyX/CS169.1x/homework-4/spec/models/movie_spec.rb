require 'spec_helper'

describe Movie do
  fixtures :movies

  describe 'find similar movies by director' do
    it 'should find movies with the same director as one given' do
      Movie.should_receive(:find_all_by_director)
      Movie.similar_to(Movie.find_by_director 'George Lucas')
    end
  end

  describe 'list movie ratings' do
    it 'should list all available movie ratings' do
      Movie.all_ratings.should == %w(G PG PG-13 NC-17 R)
    end
  end

end