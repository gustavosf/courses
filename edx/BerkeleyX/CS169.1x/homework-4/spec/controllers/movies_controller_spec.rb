require 'spec_helper'

describe MoviesController do
  fixtures :movies

  before :each do
    @similar = Movie.find_all_by_director Movie.find(1).director
  end

  describe 'similar movies' do
    it 'should call the model method that search for similar movies' do
      Movie.should_receive(:similar_to).and_return(@similar)
      get :similar, {:id => 1}
    end
    it 'should select the Find Similar template for rendering' do
      Movie.stub(:similar_to).and_return(@similar)
      get :similar, {:id => 1}
      response.should render_template('similar')
    end
    it 'should make similar movies available to that template' do
      Movie.stub(:similar_to).and_return(@similar)
      get :similar, {:id => 1}
      assigns(:movies).should == Movie.find_all_by_director('George Lucas')
    end
    it 'should return an error if movie director is undefined' do
      Movie.stub(:similar_to).and_return(@similar)
      get :similar, {:id => 3}
      response.should redirect_to(movies_path)
    end
  end

  describe 'delete movie' do
    it 'should select the movie to delete' do
      @movie = Movie.find(1)
      Movie.should_receive(:find).with('1').and_return(@movie)
      @movie.should_receive(:destroy)

      delete :destroy, :id => @movie
    end
  end

end