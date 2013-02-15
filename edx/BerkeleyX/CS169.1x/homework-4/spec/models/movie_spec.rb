require 'spec_helper'

describe Movie do
  fixtures :movies
  describe 'find similar movies by director' do
    it 'should call find movie by director with movie director' do
      Movie.should_receive(:find_all_by_director)
      Movie.first.find_similar
    end
  end
end